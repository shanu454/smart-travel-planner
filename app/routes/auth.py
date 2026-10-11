"""API Router for User Authentication, Registration, and Profiles."""
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, Header, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.services.auth import (
    create_user,
    authenticate_user,
    create_session,
    get_user_by_token,
    invalidate_session,
    format_user_payload,
    ensure_demo_user
)

router = APIRouter(prefix="/api/auth", tags=["Authentication & User Accounts"])


class RegisterRequest(BaseModel):
    email: str = Field(..., description="User email address")
    password: str = Field(..., min_length=6, description="Password (at least 6 characters)")
    full_name: str = Field(..., min_length=1, description="Full Name")
    phone: Optional[str] = ""
    preferred_currency: Optional[str] = "INR"


class LoginRequest(BaseModel):
    email: str = Field(..., description="User email address")
    password: str = Field(..., description="User password")


class ProfileUpdateRequest(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    preferred_currency: Optional[str] = None
    avatar_url: Optional[str] = None


def get_token_from_header(authorization: Optional[str] = Header(None)) -> Optional[str]:
    """Extract Bearer token from HTTP Authorization header."""
    if not authorization:
        return None
    parts = authorization.split()
    if len(parts) == 2 and parts[0].lower() == "bearer":
        return parts[1]
    return authorization


def require_current_user(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
) -> User:
    """Dependency that requires a valid authenticated user."""
    token = get_token_from_header(authorization)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token required"
        )
    user = get_user_by_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired session token"
        )
    return user


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(req: RegisterRequest, db: Session = Depends(get_db)):
    """Create a new user account and issue an authentication session token."""
    try:
        user = create_user(
            db=db,
            email=req.email,
            password=req.password,
            full_name=req.full_name,
            phone=req.phone or "",
            preferred_currency=req.preferred_currency or "INR"
        )
        token = create_session(db, user.id)
        return {
            "message": "Account created successfully! Welcome to TRAVEL PACE.",
            "token": token,
            "user": format_user_payload(user)
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/login")
def login(req: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate with email and password to receive an active session token."""
    user = authenticate_user(db, req.email, req.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password. Please try again or use Quick Demo Login."
        )

    token = create_session(db, user.id)
    return {
        "message": f"Welcome back, {user.full_name}!",
        "token": token,
        "user": format_user_payload(user)
    }


@router.post("/demo-login")
def demo_login(db: Session = Depends(get_db)):
    """1-Click Demo Login: Automatically logs into test account 'Sk Shanu'."""
    user, token = ensure_demo_user(db)
    return {
        "message": "Logged in as Sk Shanu (Demo Account)",
        "token": token,
        "user": format_user_payload(user)
    }


@router.get("/me")
def get_current_profile(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    """Retrieve currently authenticated user's profile from Bearer session token."""
    token = get_token_from_header(authorization)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing Authorization token"
        )

    user = get_user_by_token(db, token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Session has expired or is invalid. Please sign in again."
        )

    return {
        "authenticated": True,
        "user": format_user_payload(user)
    }


@router.post("/logout")
def logout(
    authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db)
):
    """Invalidate active session token on logout."""
    token = get_token_from_header(authorization)
    if token:
        invalidate_session(db, token)
    return {"message": "Logged out successfully", "authenticated": False}


@router.put("/profile")
def update_profile(
    req: ProfileUpdateRequest,
    current_user: User = Depends(require_current_user),
    db: Session = Depends(get_db)
):
    """Update profile information for the authenticated user."""
    if req.full_name is not None and req.full_name.strip():
        current_user.full_name = req.full_name.strip()
    if req.phone is not None:
        current_user.phone = req.phone.strip()
    if req.preferred_currency is not None:
        current_user.preferred_currency = req.preferred_currency.strip().upper()
    if req.avatar_url is not None:
        current_user.avatar_url = req.avatar_url.strip()

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profile updated successfully!",
        "user": format_user_payload(current_user)
    }

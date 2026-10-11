"""Authentication & User Security Service for TRAVEL PACE."""
import hashlib
import hmac
import secrets
from datetime import datetime, timedelta
from typing import Optional, Tuple, Dict, Any
from sqlalchemy.orm import Session

from app.models import User, UserSession


def hash_password(password: str, salt: Optional[str] = None) -> Tuple[str, str]:
    """Generate cryptographically secure PBKDF2-HMAC-SHA256 hash with salt."""
    if not salt:
        salt = secrets.token_hex(16)
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    )
    return key.hex(), salt


def verify_password(password: str, salt: str, hashed: str) -> bool:
    """Verify raw password against stored salt and hash using constant-time comparison."""
    test_hash, _ = hash_password(password, salt)
    return hmac.compare_digest(test_hash, hashed)


def create_user(
    db: Session,
    email: str,
    password: str,
    full_name: str,
    phone: str = "",
    preferred_currency: str = "INR"
) -> User:
    """Register a new user in the database."""
    clean_email = email.strip().lower()
    existing = db.query(User).filter(User.email == clean_email).first()
    if existing:
        raise ValueError("An account with this email already exists.")

    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters.")

    hashed, salt = hash_password(password)

    # Initial avatar initials or gravatar
    user = User(
        email=clean_email,
        full_name=full_name.strip() or "Traveler",
        hashed_password=hashed,
        salt=salt,
        phone=phone.strip(),
        preferred_currency=preferred_currency.upper(),
        is_active=True,
        avatar_url=""
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate_user(db: Session, email: str, password: str) -> Optional[User]:
    """Authenticate user credentials and return User instance if valid."""
    clean_email = email.strip().lower()
    user = db.query(User).filter(User.email == clean_email).first()
    if not user or not user.is_active:
        return None

    if not verify_password(password, user.salt, user.hashed_password):
        return None

    return user


def create_session(db: Session, user_id: int, duration_days: int = 30) -> str:
    """Issue a new session token for the user."""
    token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(days=duration_days)

    session_record = UserSession(
        user_id=user_id,
        token=token,
        expires_at=expires_at
    )
    db.add(session_record)
    db.commit()
    return token


def get_user_by_token(db: Session, token: str) -> Optional[User]:
    """Resolve active User from session token."""
    if not token:
        return None

    sess = db.query(UserSession).filter(UserSession.token == token).first()
    if not sess:
        return None

    if sess.expires_at and sess.expires_at < datetime.utcnow():
        db.delete(sess)
        db.commit()
        return None

    return sess.user if (sess.user and sess.user.is_active) else None


def invalidate_session(db: Session, token: str) -> bool:
    """Invalidate / delete user session on logout."""
    if not token:
        return False
    sess = db.query(UserSession).filter(UserSession.token == token).first()
    if sess:
        db.delete(sess)
        db.commit()
        return True
    return False


def format_user_payload(user: User) -> Dict[str, Any]:
    """Format user data for API responses without sensitive security details."""
    names = user.full_name.strip().split()
    first_name = names[0] if names else "Traveler"
    initials = ("".join([n[0] for n in names[:2]])).upper() if names else "TP"

    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "first_name": first_name,
        "initials": initials,
        "phone": user.phone or "",
        "preferred_currency": user.preferred_currency or "INR",
        "avatar_url": user.avatar_url or "",
        "member_since": user.created_at.strftime("%B %Y") if user.created_at else "Recent",
        "tier": "✨ Pro Traveler"
    }


def ensure_demo_user(db: Session) -> Tuple[User, str]:
    """Ensure demo user exists and issue an active session token for quick test login."""
    demo_email = "shanu48050@gmail.com"
    user = db.query(User).filter(User.email == demo_email).first()

    if not user:
        hashed, salt = hash_password("travelpace123")
        user = User(
            email=demo_email,
            full_name="Sk Shanu",
            hashed_password=hashed,
            salt=salt,
            phone="+91 98765 43210",
            preferred_currency="INR",
            is_active=True,
            avatar_url=""
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    token = create_session(db, user.id)
    return user, token

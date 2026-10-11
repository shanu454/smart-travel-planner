/**
 * Main Application Controller for WanderPulse Smart Travel Planner.
 * Featuring Curated Indian Destinations Discovery Grid & Transit Cost Engine.
 */

// Application State
const State = {
  trips: [],
  activeTrip: null,
  activeDay: 1,
  selectedCurrency: "INR",
  activeView: "explore", // "explore", "world", "stays", or "trip-detail"
  exploreFilter: "all",
  exploreSearch: "",
  // World Tour State
  worldGuides: [],
  worldFilterTag: "all",
  worldSearchQuery: "",
  activeWorldGuide: null,
  likedGuideIds: new Set(),
  // Stays State
  stays: [],
  staysFilterType: "all",
  staysFilterPrice: "all",
  staysFilterSort: "rating",
  staysSearchQuery: "",
  activeStayItem: null,
  latestBookingVoucher: null,
  // Local Travel Guides State
  guides: [],
  guidesFilterRegion: "all",
  guidesFilterDest: "all",
  guidesFilterLang: "all",
  guidesFilterSearch: "",
  guidesSortBy: "rating",
  activeChatGuide: null,
  activeBookingGuide: null,
  guideChatHistories: JSON.parse(localStorage.getItem("travelpace_guide_chats") || "{}"),
  // Auth State
  currentUser: null,
  authToken: localStorage.getItem("travelpace_auth_token") || null,
  pendingPostAuthAction: null
};

// DOM Elements
const Elements = {
  // Views & Navigation
  viewExplore: document.getElementById("view-explore"),
  viewWorld: document.getElementById("view-world"),
  viewStays: document.getElementById("view-stays"),
  viewGuides: document.getElementById("view-guides"),
  viewTripDetail: document.getElementById("view-trip-detail"),
  btnNavExplore: document.getElementById("btn-nav-explore"),
  btnNavWorld: document.getElementById("btn-nav-world"),
  btnNavStays: document.getElementById("btn-nav-stays"),
  btnNavGuides: document.getElementById("btn-nav-guides"),
  btnNavActiveTrip: document.getElementById("btn-nav-active-trip"),
  navActiveTripLabel: document.getElementById("nav-active-trip-label"),
  btnBackToExplore: document.getElementById("btn-back-to-explore"),
  backCrumbText: document.getElementById("back-crumb-text"),
  brandHome: document.getElementById("brand-home"),

  // Authentication & User Profile Elements
  btnOpenAuth: document.getElementById("btn-open-auth"),
  authNavWrap: document.getElementById("auth-nav-wrap"),
  userNavProfile: document.getElementById("user-nav-profile"),
  btnUserDropdownToggle: document.getElementById("btn-user-dropdown-toggle"),
  userDropdownMenu: document.getElementById("user-dropdown-menu"),
  navUserAvatar: document.getElementById("nav-user-avatar"),
  navUserName: document.getElementById("nav-user-name"),
  dropdownUserAvatar: document.getElementById("dropdown-user-avatar"),
  dropdownUserFullname: document.getElementById("dropdown-user-fullname"),
  dropdownUserEmail: document.getElementById("dropdown-user-email"),
  btnDropdownProfile: document.getElementById("btn-dropdown-profile"),
  btnDropdownStays: document.getElementById("btn-dropdown-stays"),
  btnDropdownTrips: document.getElementById("btn-dropdown-trips"),
  btnDropdownLogout: document.getElementById("btn-dropdown-logout"),

  // Auth Modal Elements
  modalAuth: document.getElementById("modal-auth"),
  btnAuthModalClose: document.getElementById("btn-auth-modal-close"),
  tabBtnSignin: document.getElementById("tab-btn-signin"),
  tabBtnSignup: document.getElementById("tab-btn-signup"),
  authPanelSignin: document.getElementById("auth-panel-signin"),
  authPanelSignup: document.getElementById("auth-panel-signup"),
  btnDemoLogin: document.getElementById("btn-demo-login"),
  formSignin: document.getElementById("form-signin"),
  signinEmail: document.getElementById("signin-email"),
  signinPassword: document.getElementById("signin-password"),
  btnPeekSigninPwd: document.getElementById("btn-peek-signin-pwd"),
  signinErrorBanner: document.getElementById("signin-error-banner"),
  linkSwitchToSignup: document.getElementById("link-switch-to-signup"),
  btnForgotPassword: document.getElementById("btn-forgot-password"),

  formSignup: document.getElementById("form-signup"),
  signupName: document.getElementById("signup-name"),
  signupEmail: document.getElementById("signup-email"),
  signupPassword: document.getElementById("signup-password"),
  btnPeekSignupPwd: document.getElementById("btn-peek-signup-pwd"),
  pwdStrengthContainer: document.getElementById("pwd-strength-container"),
  pwdStrengthBar: document.getElementById("pwd-strength-bar"),
  pwdStrengthLabel: document.getElementById("pwd-strength-label"),
  signupCurrency: document.getElementById("signup-currency"),
  signupPhone: document.getElementById("signup-phone"),
  signupErrorBanner: document.getElementById("signup-error-banner"),
  linkSwitchToSignin: document.getElementById("link-switch-to-signin"),

  // User Profile Modal Elements
  modalUserProfile: document.getElementById("modal-user-profile"),
  btnProfileModalClose: document.getElementById("btn-profile-modal-close"),
  profileAvatarLarge: document.getElementById("profile-avatar-large"),
  profileFullnameDisplay: document.getElementById("profile-fullname-display"),
  profileEmailDisplay: document.getElementById("profile-email-display"),
  profileMemberSince: document.getElementById("profile-member-since"),
  formEditProfile: document.getElementById("form-edit-profile"),
  editProfileName: document.getElementById("edit-profile-name"),
  editProfilePhone: document.getElementById("edit-profile-phone"),
  editProfileCurrency: document.getElementById("edit-profile-currency"),
  btnSaveProfile: document.getElementById("btn-save-profile"),
  btnProfileLogout: document.getElementById("btn-profile-logout"),
  btnProfileCancel: document.getElementById("btn-profile-cancel"),

  // Stays & Lodgings View Elements
  staysSearchInput: document.getElementById("stays-search-input"),
  btnClearStaysSearch: document.getElementById("btn-clear-stays-search"),
  staysCheckinDate: document.getElementById("stays-checkin-date"),
  staysCheckoutDate: document.getElementById("stays-checkout-date"),
  staysTravelersSelect: document.getElementById("stays-travelers-select"),
  btnSearchStays: document.getElementById("btn-search-stays"),
  staysTypeTabs: document.getElementById("stays-type-tabs"),
  staysPopularChips: document.getElementById("stays-popular-chips"),
  btnStaysManageBookings: document.getElementById("btn-stays-manage-bookings"),
  staysFilterTypePills: document.getElementById("stays-filter-type-pills"),
  staysPriceFilter: document.getElementById("stays-price-filter"),
  staysSortSelect: document.getElementById("stays-sort-select"),
  staysCountPill: document.getElementById("stays-count-pill"),
  staysCardsGrid: document.getElementById("stays-cards-grid"),

  // Stay Detail & Booking Modal Elements
  modalStayDetail: document.getElementById("modal-stay-detail"),
  btnSmodalClose: document.getElementById("btn-smodal-close"),
  btnSmodalCloseFoot: document.getElementById("btn-smodal-close-foot"),
  smodalCategory: document.getElementById("smodal-category"),
  smodalTitle: document.getElementById("smodal-title"),
  smodalLocation: document.getElementById("smodal-location"),
  smodalCoverImg: document.getElementById("smodal-cover-img"),
  smodalPriceDisplay: document.getElementById("smodal-price-display"),
  smodalRating: document.getElementById("smodal-rating"),
  smodalReviews: document.getElementById("smodal-reviews"),
  smodalSuperhost: document.getElementById("smodal-superhost"),
  smodalProximity: document.getElementById("smodal-proximity"),
  smodalOverview: document.getElementById("smodal-overview"),
  smodalRoomType: document.getElementById("smodal-room-type"),
  smodalMaxGuests: document.getElementById("smodal-max-guests"),
  smodalCancellation: document.getElementById("smodal-cancellation"),
  smodalAmenitiesList: document.getElementById("smodal-amenities-list"),
  smodalAddress: document.getElementById("smodal-address"),
  btnSmodalAddTrip: document.getElementById("btn-smodal-add-trip"),
  btnSmodalInstantBook: document.getElementById("btn-smodal-instant-book"),

  // Booking Voucher Modal Elements
  modalBookingVoucher: document.getElementById("modal-booking-voucher"),
  btnVoucherClose: document.getElementById("btn-voucher-close"),
  btnVoucherDone: document.getElementById("btn-voucher-done"),
  btnVoucherAddExpense: document.getElementById("btn-voucher-add-expense"),
  voucherCodeVal: document.getElementById("voucher-code-val"),
  voucherStayName: document.getElementById("voucher-stay-name"),
  voucherStayDest: document.getElementById("voucher-stay-dest"),
  voucherGuestName: document.getElementById("voucher-guest-name"),
  voucherGuestsCount: document.getElementById("voucher-guests-count"),
  voucherCheckin: document.getElementById("voucher-checkin"),
  voucherCheckout: document.getElementById("voucher-checkout"),
  voucherRateLabel: document.getElementById("voucher-rate-label"),
  voucherSubtotal: document.getElementById("voucher-subtotal"),
  voucherTaxes: document.getElementById("voucher-taxes"),
  voucherTotal: document.getElementById("voucher-total"),

  // World Tour View Elements
  worldSearchInput: document.getElementById("world-search-input"),
  btnClearWorldSearch: document.getElementById("btn-clear-world-search"),
  worldPopularChips: document.getElementById("world-popular-chips"),
  worldCardsGrid: document.getElementById("world-cards-grid"),
  worldCountPill: document.getElementById("world-count-pill"),
  worldActiveFilterWrap: document.getElementById("world-active-filter-wrap"),
  worldFilterName: document.getElementById("world-filter-name"),
  btnWorldClearFilter: document.getElementById("btn-world-clear-filter"),

  // World Guide Modal Elements
  modalWorldGuide: document.getElementById("modal-world-guide"),
  btnCloseWorldModal: document.getElementById("btn-close-world-modal"),
  btnWmodalCloseFoot: document.getElementById("btn-wmodal-close-foot"),
  wmodalTag: document.getElementById("wmodal-tag"),
  wmodalTitle: document.getElementById("wmodal-title"),
  wmodalCoverImg: document.getElementById("wmodal-cover-img"),
  wmodalDest: document.getElementById("wmodal-dest"),
  wmodalDays: document.getElementById("wmodal-days"),
  wmodalPace: document.getElementById("wmodal-pace"),
  wmodalStyle: document.getElementById("wmodal-style"),
  wmodalAuthorImg: document.getElementById("wmodal-author-img"),
  wmodalAuthorName: document.getElementById("wmodal-author-name"),
  wmodalAuthorHandle: document.getElementById("wmodal-author-handle"),
  btnWmodalLike: document.getElementById("btn-wmodal-like"),
  wmodalLikeIcon: document.getElementById("wmodal-like-icon"),
  wmodalLikesCount: document.getElementById("wmodal-likes-count"),
  wmodalViewsCount: document.getElementById("wmodal-views-count"),
  btnWmodalShare: document.getElementById("btn-wmodal-share"),
  wmodalDesc: document.getElementById("wmodal-desc"),
  wmodalBudgetDisplay: document.getElementById("wmodal-budget-display"),
  wmodalItineraryList: document.getElementById("wmodal-itinerary-list"),
  wmodalTransportsList: document.getElementById("wmodal-transports-list"),
  btnWmodalClone: document.getElementById("btn-wmodal-clone"),
  btnWmodalOpenPage: document.getElementById("btn-wmodal-open-page"),

  // Explore Front Page Grid
  exploreCardsGrid: document.getElementById("explore-cards-grid"),
  exploreSearchInput: document.getElementById("explore-search-input"),
  exploreFilterChips: document.getElementById("explore-filter-chips"),
  countAllTrips: document.getElementById("count-all-trips"),

  // Destination / Dham Calculator Elements
  dhamBudgetCalculator: document.getElementById("dham-budget-calculator"),
  btnNavDhamCalc: document.getElementById("btn-nav-dham-calc"),
  dhamSelect: document.getElementById("dham-select"),
  dhamCustomInputs: document.getElementById("dham-custom-inputs"),
  dhamCustomDest: document.getElementById("dham-custom-dest"),
  dhamCustomDays: document.getElementById("dham-custom-days"),
  dhamDaysPillBadge: document.getElementById("dham-days-pill-badge"),
  dhamQuickDays: document.getElementById("dham-quick-days"),
  dhamDate: document.getElementById("dham-date"),
  dhamTime: document.getElementById("dham-time"),
  dhamTier: document.getElementById("dham-tier"),
  dhamPilgrims: document.getElementById("dham-pilgrims"),
  dhamTotalBudget: document.getElementById("dham-total-budget"),
  dhamPerPerson: document.getElementById("dham-per-person"),
  dhamCostTransport: document.getElementById("dham-cost-transport"),
  dhamCostStay: document.getElementById("dham-cost-stay"),
  dhamCostPooja: document.getElementById("dham-cost-pooja"),
  dhamCostFood: document.getElementById("dham-cost-food"),
  btnGenerateDhamTrip: document.getElementById("btn-generate-dham-trip"),

  // Budget Tab Destination Cost Estimator Elements (Identical to Front Page)
  budgetSectionCalculator: document.getElementById("budget-section-calculator"),
  budgetCalcSelect: document.getElementById("budget-calc-select"),
  budgetCalcCustomInputs: document.getElementById("budget-calc-custom-inputs"),
  budgetCalcCustomDest: document.getElementById("budget-calc-custom-dest"),
  budgetCalcCustomDays: document.getElementById("budget-calc-custom-days"),
  budgetDaysPillBadge: document.getElementById("budget-days-pill-badge"),
  budgetQuickDays: document.getElementById("budget-quick-days"),
  budgetCalcDate: document.getElementById("budget-calc-date"),
  budgetCalcTime: document.getElementById("budget-calc-time"),
  budgetCalcTier: document.getElementById("budget-calc-tier"),
  budgetCalcTravelers: document.getElementById("budget-calc-travelers"),
  budgetCalcTotal: document.getElementById("budget-calc-total"),
  budgetCalcSub: document.getElementById("budget-calc-sub"),
  budgetCalcTransport: document.getElementById("budget-calc-transport"),
  budgetCalcStay: document.getElementById("budget-calc-stay"),
  budgetCalcActivities: document.getElementById("budget-calc-activities"),
  budgetCalcFood: document.getElementById("budget-calc-food"),
  btnApplyAsTripBudget: document.getElementById("btn-apply-as-trip-budget"),
  btnAddBreakdownAsExpenses: document.getElementById("btn-add-breakdown-as-expenses"),
  btnBudgetGenerateTrip: document.getElementById("btn-budget-generate-trip"),
  btnHeroCalcBudget: document.getElementById("btn-hero-calc-budget"),
  metricCardBudget: document.getElementById("metric-card-budget"),

  // Top Nav Controls
  tripSelect: document.getElementById("trip-select"),
  globalCurrencySelect: document.getElementById("global-currency-select"),

  // Trip Hero Banner
  heroBackdrop: document.getElementById("hero-backdrop"),
  heroTitle: document.getElementById("hero-title"),
  heroDestination: document.getElementById("hero-destination"),
  heroStyle: document.getElementById("hero-style"),
  heroPace: document.getElementById("hero-pace"),
  tripPaceSelect: document.getElementById("trip-pace-select"),
  heroDates: document.getElementById("hero-dates"),
  heroNotes: document.getElementById("hero-notes"),
  metricDuration: document.getElementById("metric-duration"),
  metricCountdown: document.getElementById("metric-countdown"),
  metricBudget: document.getElementById("metric-budget"),
  metricSpent: document.getElementById("metric-spent"),
  metricPacking: document.getElementById("metric-packing"),

  // Tab Navigation
  tabButtons: document.querySelectorAll(".tab-btn"),
  tabPanes: document.querySelectorAll(".tab-pane"),

  // Itinerary View Elements
  dayPillsWrap: document.getElementById("day-pills-wrap"),
  currentDayTitle: document.getElementById("current-day-title"),
  currentDayStats: document.getElementById("current-day-stats"),
  dayProgressText: document.getElementById("day-progress-text"),
  dayProgressFill: document.getElementById("day-progress-fill"),
  activitiesTimeline: document.getElementById("activities-timeline"),

  // Transport View Elements
  paneTransport: document.getElementById("pane-transport"),
  transportOptionsGrid: document.getElementById("transport-options-grid"),
  transportTotalCost: document.getElementById("transport-total-cost"),
  transportTotalCount: document.getElementById("transport-total-count"),
  transportBookedCost: document.getElementById("transport-booked-cost"),
  transportBookedCount: document.getElementById("transport-booked-count"),
  transportPendingCost: document.getElementById("transport-pending-cost"),
  transportPendingCount: document.getElementById("transport-pending-count"),
  btnOpenAddTransport: document.getElementById("btn-open-add-transport"),

  // Modals
  modalCreateTrip: document.getElementById("modal-create-trip"),
  createTripUserBadge: document.getElementById("create-trip-user-badge"),
  createTripUserName: document.getElementById("create-trip-user-name"),
  modalAddActivity: document.getElementById("modal-add-activity"),
  modalAddExpense: document.getElementById("modal-add-expense"),
  modalAddPacking: document.getElementById("modal-add-packing"),
  modalAddTransport: document.getElementById("modal-add-transport"),

  // Forms
  formCreateTrip: document.getElementById("form-create-trip"),
  formAddActivity: document.getElementById("form-add-activity"),
  formAddExpense: document.getElementById("form-add-expense"),
  formAddPacking: document.getElementById("form-add-packing"),
  formAddTransport: document.getElementById("form-add-transport"),

  // Autocomplete
  inputDestination: document.getElementById("input-destination"),
  destinationDropdown: document.getElementById("destination-dropdown"),

  // Packing
  packingCategoriesGrid: document.getElementById("packing-categories-grid"),
  packingProgressCount: document.getElementById("packing-progress-count"),
  packingProgressPercent: document.getElementById("packing-progress-percent"),
  packingProgressFill: document.getElementById("packing-progress-fill"),
  btnRegeneratePacking: document.getElementById("btn-regenerate-packing"),

  // AI Advisor
  aiQueryInput: document.getElementById("ai-query-input"),
  btnAskAi: document.getElementById("btn-ask-ai"),
  aiResponsePanel: document.getElementById("ai-response-panel"),
  aiResponseText: document.getElementById("ai-response-text"),
  aiEtiquetteList: document.getElementById("ai-etiquette-list"),
  aiHacksList: document.getElementById("ai-hacks-list"),
  aiDestinationIntro: document.getElementById("ai-destination-intro"),

  // Local Travel Guides Elements
  guidesCardsGrid: document.getElementById("guides-cards-grid"),
  guidesSearchInput: document.getElementById("guides-search-input"),
  btnClearGuidesSearch: document.getElementById("btn-clear-guides-search"),
  guidesLangSelect: document.getElementById("guides-lang-select"),
  guidesSortSelect: document.getElementById("guides-sort-select"),
  guidesCountPill: document.getElementById("guides-count-pill"),
  modalGuideChat: document.getElementById("modal-guide-chat"),
  modalGuideBooking: document.getElementById("modal-guide-booking"),
  modalGuideVoucher: document.getElementById("modal-guide-voucher"),
  tabBtnGuides: document.getElementById("tab-btn-guides"),
  paneGuides: document.getElementById("pane-guides"),
  workspaceGuidesGrid: document.getElementById("workspace-guides-grid"),

  // Contact Us Modal
  modalContactUs: document.getElementById("modal-contact-us")
};

// ---------------------------------------------------------------------------
// Initialization
// ---------------------------------------------------------------------------
document.addEventListener("DOMContentLoaded", async () => {
  initEventListeners();
  initTabNavigation();
  initModalLightDismiss();
  initDestinationAutocomplete();
  initDefaultDates();
  initStaysModule();
  initGuidesModule();
  initAuthModule();
  initGlobalFooter();
  initTripFeedbackModule();

  if (window.MapModule) {
    window.MapModule.initMap();
  }

  // Run URL and Hash routing
  handleUrlRouting();

  // Async data fetching with isolated error handlers
  loadTripsList().catch(e => console.error("loadTripsList error:", e));
  initDhamBudgetCalculator().catch(e => console.error("initDhamBudgetCalculator error:", e));
  initBudgetSectionCalculator().catch(e => console.error("initBudgetSectionCalculator error:", e));
});

// ---------------------------------------------------------------------------
// Universal URL & Hash Navigation Router
// ---------------------------------------------------------------------------
function handleUrlRouting() {
  const urlParams = new URLSearchParams(window.location.search);
  const hash = window.location.hash || "";

  // 1. Direct Trip Workspace navigation (?trip_id=... or ?view=workspace or #view-workspace)
  const tripIdParam = urlParams.get("trip_id") || urlParams.get("trip");
  if (tripIdParam) {
    const tId = parseInt(tripIdParam, 10);
    if (!isNaN(tId)) {
      showTripDetailView(tId);
      return;
    }
  }
  if (urlParams.get("view") === "workspace" || hash.includes("view-workspace") || hash.includes("trip-detail")) {
    const savedTripId = localStorage.getItem("active_trip_id");
    const tId = savedTripId ? parseInt(savedTripId, 10) : (State.activeTrip ? State.activeTrip.id : null);
    if (tId) {
      showTripDetailView(tId);
      return;
    }
  }

  // 2. World Tour view (?view=world or #view-world or ?guide=...)
  if (urlParams.get("view") === "world" || hash.includes("view-world") || urlParams.get("guide")) {
    showWorldView();
    const gId = urlParams.get("guide");
    if (gId) {
      setTimeout(async () => {
        if (!State.worldGuides || State.worldGuides.length === 0) await loadWorldGuides();
        const found = State.worldGuides.find(g => g.id === gId);
        if (found) openWorldGuideModal(found);
      }, 300);
    }
    return;
  }

  // 3. Hotels, Airbnbs & Stays view (?view=stays or #view-stays)
  if (urlParams.get("view") === "stays" || hash.includes("view-stays")) {
    showStaysView();
    let placeParam = urlParams.get("place");
    if (!placeParam && hash.includes("place=")) {
      const match = hash.match(/place=([^&]+)/);
      if (match) placeParam = decodeURIComponent(match[1]);
    }
    if (placeParam && Elements.staySearchInput) {
      Elements.staySearchInput.value = placeParam;
      if (typeof applyStaysFilters === "function") {
        applyStaysFilters();
      }
    }
    return;
  }

  // 4. Local Travel Guides view (?view=guides or #view-guides)
  if (urlParams.get("view") === "guides" || hash.includes("view-guides")) {
    showGuidesView();
    let destParam = urlParams.get("destination") || urlParams.get("dest") || urlParams.get("place");
    if (destParam && Elements.guidesSearchInput) {
      Elements.guidesSearchInput.value = destParam;
      State.guidesFilterSearch = destParam;
      loadGuidesList();
    }
    return;
  }

  // 5. Budget Calculator section anchor (#budget-section or #dham-budget)
  if (hash.includes("budget-section") || hash.includes("dham-budget")) {
    showExploreView();
    setTimeout(() => {
      const bSec = document.getElementById("budget-section") || document.getElementById("dham-budget-section");
      if (bSec) bSec.scrollIntoView({ behavior: "smooth" });
    }, 250);
    return;
  }

  // 6. Explore view (?view=explore or #view-explore)
  if (urlParams.get("view") === "explore" || hash.includes("view-explore")) {
    showExploreView();
    return;
  }
}

window.addEventListener("hashchange", handleUrlRouting);
window.addEventListener("popstate", handleUrlRouting);

// ---------------------------------------------------------------------------
// Login Guard for Trip Planning
// ---------------------------------------------------------------------------
function checkLoginBeforePlanning(actionCallback = null, contextMessage = "Please sign in or create an account to start planning your trip!") {
  if (!State.currentUser) {
    showToast(`🔒 ${contextMessage}`, "info");
    State.pendingPostAuthAction = actionCallback || null;
    openAuthModal("signin");
    return false;
  }
  return true;
}

function openCreateTripModal() {
  if (Elements.createTripUserBadge) {
    if (State.currentUser) {
      if (Elements.createTripUserName) {
        Elements.createTripUserName.textContent = State.currentUser.full_name || State.currentUser.first_name || "Traveler";
      }
      Elements.createTripUserBadge.style.display = "flex";
    } else {
      Elements.createTripUserBadge.style.display = "none";
    }
  }
  openModal(Elements.modalCreateTrip);
}

// ---------------------------------------------------------------------------
// Event Listeners Setup
// ---------------------------------------------------------------------------
function initEventListeners() {
  // Brand Home / Nav Click
  Elements.brandHome?.addEventListener("click", () => showExploreView());
  Elements.btnNavExplore?.addEventListener("click", () => showExploreView());
  Elements.btnNavWorld?.addEventListener("click", () => showWorldView());
  Elements.btnNavStays?.addEventListener("click", () => showStaysView());
  Elements.btnNavGuides?.addEventListener("click", () => showGuidesView());
  Elements.btnNavActiveTrip?.addEventListener("click", () => showTripDetailView());
  Elements.btnBackToExplore?.addEventListener("click", () => showExploreView());

  // World Tour View & Search Listeners
  Elements.worldSearchInput?.addEventListener("input", (e) => {
    State.worldSearchQuery = e.target.value.trim();
    if (Elements.btnClearWorldSearch) {
      Elements.btnClearWorldSearch.style.display = State.worldSearchQuery ? "block" : "none";
    }
    renderWorldGuides();
  });

  Elements.btnClearWorldSearch?.addEventListener("click", () => {
    if (Elements.worldSearchInput) Elements.worldSearchInput.value = "";
    State.worldSearchQuery = "";
    if (Elements.btnClearWorldSearch) Elements.btnClearWorldSearch.style.display = "none";
    renderWorldGuides();
  });

  Elements.btnWorldClearFilter?.addEventListener("click", () => {
    setWorldTagFilter("all");
  });

  // World Guide Modal Listeners
  Elements.btnCloseWorldModal?.addEventListener("click", () => closeModal(Elements.modalWorldGuide));
  Elements.btnWmodalCloseFoot?.addEventListener("click", () => closeModal(Elements.modalWorldGuide));
  Elements.btnWmodalLike?.addEventListener("click", () => {
    if (State.activeWorldGuide) handleToggleLikeGuide(State.activeWorldGuide.id);
  });
  Elements.btnWmodalShare?.addEventListener("click", () => {
    if (State.activeWorldGuide) handleShareGuide(State.activeWorldGuide);
  });
  Elements.btnWmodalClone?.addEventListener("click", () => {
    if (State.activeWorldGuide) handleCloneWorldGuide(State.activeWorldGuide.id);
  });

  // Destination & Dham Budget Calculator Nav Links
  Elements.btnNavDhamCalc?.addEventListener("click", () => {
    if (State.activeView === "trip-detail") {
      // If currently on other page (trip workspace), switch to budget tab and scroll to calculator
      const budgetTabBtn = document.getElementById("tab-btn-budget");
      budgetTabBtn?.click();
      setTimeout(() => {
        Elements.budgetSectionCalculator?.scrollIntoView({ behavior: "smooth", block: "start" });
        Elements.budgetCalcCustomDest?.focus();
      }, 100);
    } else {
      showExploreView();
      setTimeout(() => {
        Elements.dhamBudgetCalculator?.scrollIntoView({ behavior: "smooth", block: "center" });
        Elements.dhamCustomDest?.focus();
      }, 100);
    }
  });

  // Hero Banner Quick Budget Calculator Triggers
  Elements.btnHeroCalcBudget?.addEventListener("click", () => {
    const budgetTabBtn = document.getElementById("tab-btn-budget");
    budgetTabBtn?.click();
    setTimeout(() => {
      Elements.budgetSectionCalculator?.scrollIntoView({ behavior: "smooth", block: "start" });
      Elements.budgetCalcCustomDest?.focus();
    }, 100);
  });

  Elements.metricCardBudget?.addEventListener("click", () => {
    const budgetTabBtn = document.getElementById("tab-btn-budget");
    budgetTabBtn?.click();
    setTimeout(() => {
      Elements.budgetSectionCalculator?.scrollIntoView({ behavior: "smooth", block: "start" });
      Elements.budgetCalcCustomDest?.focus();
    }, 100);
  });

  // Trip Selection Dropdown
  Elements.tripSelect.addEventListener("change", (e) => {
    const tripId = parseInt(e.target.value);
    if (tripId) {
      loadTripDetails(tripId);
      showTripDetailView(tripId);
    }
  });

  // Explore Search Input
  Elements.exploreSearchInput?.addEventListener("input", (e) => {
    State.exploreSearch = e.target.value;
    renderExploreGrid(State.trips, State.exploreFilter, State.exploreSearch);
  });

  // Explore Filter Chips
  Elements.exploreFilterChips?.addEventListener("click", (e) => {
    const chip = e.target.closest(".chip");
    if (!chip) return;
    document.querySelectorAll(".explore-filter-chips .chip").forEach(c => c.classList.remove("active"));
    chip.classList.add("active");
    State.exploreFilter = chip.dataset.filter || "all";
    renderExploreGrid(State.trips, State.exploreFilter, State.exploreSearch);
  });

  // Global Currency Switcher
  Elements.globalCurrencySelect.addEventListener("change", (e) => {
    State.selectedCurrency = e.target.value;
    if (State.activeTrip) {
      updateHeroMetrics(State.activeTrip);
      if (window.BudgetModule && State.activeTrip.budget_summary) {
        window.BudgetModule.renderBudgetSummary(
          State.activeTrip.budget_summary,
          State.selectedCurrency,
          State.activeTrip.days_count
        );
      }
      renderTransportSection(State.activeTrip.transport_options, State.selectedCurrency);
    }
    if (State.stays && State.stays.length > 0) {
      filterAndRenderStays();
    }
  });

  // Quick Travel Pace Switcher
  Elements.tripPaceSelect?.addEventListener("change", async (e) => {
    const newPace = e.target.value;
    if (!State.activeTrip) return;
    try {
      showToast(`Adjusting travel pace to ${newPace}...`, "info");
      const res = await fetch(`/api/trips/${State.activeTrip.id}/pace`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ travel_pace: newPace })
      });
      if (!res.ok) throw new Error("Failed to update travel pace");
      const updatedTrip = await res.json();
      State.activeTrip = updatedTrip;
      renderHeroBanner(updatedTrip);
      renderDayActivities(State.activeDay);
      showToast(`✨ Travel pace changed to ${newPace}! Daily activities re-optimized.`, "success");
    } catch (err) {
      console.error("Pace update error:", err);
      showToast("Could not update travel pace", "error");
    }
  });

  // Modal Open Buttons
  document.getElementById("btn-open-create")?.addEventListener("click", () => {
    if (!checkLoginBeforePlanning(() => openCreateTripModal(), "Please sign in or create an account to start planning your trip!")) {
      return;
    }
    openCreateTripModal();
  });

  document.getElementById("btn-open-add-activity")?.addEventListener("click", () => {
    prepareAddActivityModal();
    openModal(Elements.modalAddActivity);
  });

  document.getElementById("btn-open-add-expense")?.addEventListener("click", () => {
    prepareAddExpenseModal();
    openModal(Elements.modalAddExpense);
  });

  document.getElementById("btn-open-add-packing")?.addEventListener("click", () => {
    openModal(Elements.modalAddPacking);
  });

  Elements.btnOpenAddTransport?.addEventListener("click", () => {
    openModal(Elements.modalAddTransport);
  });

  // Modal Close Buttons
  document.getElementById("btn-close-create")?.addEventListener("click", () => closeModal(Elements.modalCreateTrip));
  document.getElementById("btn-cancel-create")?.addEventListener("click", () => closeModal(Elements.modalCreateTrip));

  document.getElementById("btn-close-activity")?.addEventListener("click", () => closeModal(Elements.modalAddActivity));
  document.getElementById("btn-cancel-activity")?.addEventListener("click", () => closeModal(Elements.modalAddActivity));

  document.getElementById("btn-close-expense")?.addEventListener("click", () => closeModal(Elements.modalAddExpense));
  document.getElementById("btn-cancel-expense")?.addEventListener("click", () => closeModal(Elements.modalAddExpense));

  document.getElementById("btn-close-packing")?.addEventListener("click", () => closeModal(Elements.modalAddPacking));
  document.getElementById("btn-cancel-packing")?.addEventListener("click", () => closeModal(Elements.modalAddPacking));

  document.getElementById("btn-close-transport")?.addEventListener("click", () => closeModal(Elements.modalAddTransport));
  document.getElementById("btn-cancel-transport")?.addEventListener("click", () => closeModal(Elements.modalAddTransport));

  // Form Submissions
  Elements.formCreateTrip.addEventListener("submit", handleCreateTripSubmit);
  Elements.formAddActivity.addEventListener("submit", handleAddActivitySubmit);
  Elements.formAddExpense.addEventListener("submit", handleAddExpenseSubmit);
  Elements.formAddPacking.addEventListener("submit", handleAddPackingSubmit);
  Elements.formAddTransport?.addEventListener("submit", handleAddTransportSubmit);

  // Packing Regenerate
  Elements.btnRegeneratePacking?.addEventListener("click", handleRegeneratePacking);

  // AI Advisor
  Elements.btnAskAi?.addEventListener("click", handleAskAi);
  Elements.aiQueryInput?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") handleAskAi();
  });
}

// ---------------------------------------------------------------------------
// View Switcher (Indian Journeys vs World Tour vs Stays vs Guides vs Active Trip Workspace)
// ---------------------------------------------------------------------------
function showExploreView() {
  State.activeView = "explore";
  Elements.viewExplore.style.display = "block";
  Elements.viewExplore?.classList.add("active");
  if (Elements.viewWorld) {
    Elements.viewWorld.style.display = "none";
    Elements.viewWorld.classList.remove("active");
  }
  if (Elements.viewStays) {
    Elements.viewStays.style.display = "none";
    Elements.viewStays.classList.remove("active");
  }
  if (Elements.viewGuides) {
    Elements.viewGuides.style.display = "none";
    Elements.viewGuides.classList.remove("active");
  }
  Elements.viewTripDetail.style.display = "none";
  Elements.btnNavExplore?.classList.add("active");
  Elements.btnNavWorld?.classList.remove("active");
  Elements.btnNavStays?.classList.remove("active");
  Elements.btnNavGuides?.classList.remove("active");
  Elements.btnNavActiveTrip?.classList.remove("active");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showWorldView() {
  State.activeView = "world";
  Elements.viewExplore.style.display = "none";
  Elements.viewExplore?.classList.remove("active");
  if (Elements.viewWorld) {
    Elements.viewWorld.style.display = "block";
    Elements.viewWorld.classList.add("active");
  }
  if (Elements.viewStays) {
    Elements.viewStays.style.display = "none";
    Elements.viewStays.classList.remove("active");
  }
  if (Elements.viewGuides) {
    Elements.viewGuides.style.display = "none";
    Elements.viewGuides.classList.remove("active");
  }
  Elements.viewTripDetail.style.display = "none";
  Elements.btnNavExplore?.classList.remove("active");
  Elements.btnNavWorld?.classList.add("active");
  Elements.btnNavStays?.classList.remove("active");
  Elements.btnNavGuides?.classList.remove("active");
  Elements.btnNavActiveTrip?.classList.remove("active");

  if (!State.worldGuides || State.worldGuides.length === 0) {
    loadWorldGuides();
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showStaysView() {
  State.activeView = "stays";
  Elements.viewExplore.style.display = "none";
  Elements.viewExplore?.classList.remove("active");
  if (Elements.viewWorld) {
    Elements.viewWorld.style.display = "none";
    Elements.viewWorld.classList.remove("active");
  }
  if (Elements.viewStays) {
    Elements.viewStays.style.display = "block";
    Elements.viewStays.classList.add("active");
  }
  if (Elements.viewGuides) {
    Elements.viewGuides.style.display = "none";
    Elements.viewGuides.classList.remove("active");
  }
  Elements.viewTripDetail.style.display = "none";
  Elements.btnNavExplore?.classList.remove("active");
  Elements.btnNavWorld?.classList.remove("active");
  Elements.btnNavStays?.classList.add("active");
  Elements.btnNavGuides?.classList.remove("active");
  Elements.btnNavActiveTrip?.classList.remove("active");

  if (!State.stays || State.stays.length === 0) {
    loadStays();
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showGuidesView() {
  State.activeView = "guides";
  Elements.viewExplore.style.display = "none";
  Elements.viewExplore?.classList.remove("active");
  if (Elements.viewWorld) {
    Elements.viewWorld.style.display = "none";
    Elements.viewWorld.classList.remove("active");
  }
  if (Elements.viewStays) {
    Elements.viewStays.style.display = "none";
    Elements.viewStays.classList.remove("active");
  }
  if (Elements.viewGuides) {
    Elements.viewGuides.style.display = "block";
    Elements.viewGuides.classList.add("active");
  }
  Elements.viewTripDetail.style.display = "none";
  Elements.btnNavExplore?.classList.remove("active");
  Elements.btnNavWorld?.classList.remove("active");
  Elements.btnNavStays?.classList.remove("active");
  Elements.btnNavGuides?.classList.add("active");
  Elements.btnNavActiveTrip?.classList.remove("active");

  if (!State.guides || State.guides.length === 0) {
    loadGuidesList();
  }
  window.scrollTo({ top: 0, behavior: "smooth" });
}

function showTripDetailView(tripId = null) {
  State.activeView = "trip-detail";
  Elements.viewExplore.style.display = "none";
  Elements.viewExplore?.classList.remove("active");
  if (Elements.viewWorld) {
    Elements.viewWorld.style.display = "none";
    Elements.viewWorld.classList.remove("active");
  }
  if (Elements.viewStays) {
    Elements.viewStays.style.display = "none";
    Elements.viewStays.classList.remove("active");
  }
  if (Elements.viewGuides) {
    Elements.viewGuides.style.display = "none";
    Elements.viewGuides.classList.remove("active");
  }
  Elements.viewTripDetail.style.display = "block";
  Elements.btnNavExplore?.classList.remove("active");
  Elements.btnNavWorld?.classList.remove("active");
  Elements.btnNavStays?.classList.remove("active");
  Elements.btnNavGuides?.classList.remove("active");
  Elements.btnNavActiveTrip?.classList.add("active");

  if (tripId && (!State.activeTrip || State.activeTrip.id !== tripId)) {
    loadTripDetails(tripId);
  } else if (State.activeTrip) {
    if (Elements.backCrumbText) {
      Elements.backCrumbText.textContent = `${State.activeTrip.destination}`;
    }
  }

  // Trigger leaflet resize if on itinerary tab
  setTimeout(() => {
    if (window.MapModule && State.activeTrip) {
      renderMapForDay(State.activeDay);
    }
  }, 150);

  window.scrollTo({ top: 0, behavior: "smooth" });
}

// ---------------------------------------------------------------------------
// Tabs Handling
// ---------------------------------------------------------------------------
function initTabNavigation() {
  Elements.tabButtons.forEach(btn => {
    btn.addEventListener("click", () => {
      const targetTab = btn.dataset.tab;
      Elements.tabButtons.forEach(b => b.classList.remove("active"));
      Elements.tabPanes.forEach(p => p.classList.remove("active"));

      btn.classList.add("active");
      const targetPane = document.getElementById(`pane-${targetTab}`);
      if (targetPane) targetPane.classList.add("active");

      // Invalidate Leaflet map size if switching back to itinerary
      if (targetTab === "itinerary" && window.MapModule) {
        setTimeout(() => {
          if (State.activeTrip) renderMapForDay(State.activeDay);
        }, 200);
      }

      // Update feedback UI when switching to feedback tab
      if (targetTab === "feedback" && State.activeTrip) {
        updateTripCompletionUI(State.activeTrip);
      }

      // Load recommended guides when switching to guides tab
      if (targetTab === "guides" && State.activeTrip) {
        loadWorkspaceGuides(State.activeTrip.destination);
      }
    });
  });
}

// ---------------------------------------------------------------------------
// Native <dialog> Modal Handling with Light Dismiss
// ---------------------------------------------------------------------------
function openModal(dialog) {
  if (!dialog) return;
  dialog.showModal();
}

function closeModal(dialog) {
  if (!dialog) return;
  dialog.close();
}

function initModalLightDismiss() {
  [
    Elements.modalCreateTrip,
    Elements.modalAddActivity,
    Elements.modalAddExpense,
    Elements.modalAddPacking,
    Elements.modalAddTransport,
    Elements.modalWorldGuide,
    Elements.modalStayDetail,
    Elements.modalBookingVoucher,
    Elements.modalGuideChat,
    Elements.modalGuideBooking,
    Elements.modalGuideVoucher,
    Elements.modalContactUs
  ].forEach(dialog => {
    if (!dialog) return;
    dialog.addEventListener("click", (e) => {
      const rect = dialog.getBoundingClientRect();
      const isInDialog = (
        rect.top <= e.clientY &&
        e.clientY <= rect.top + rect.height &&
        rect.left <= e.clientX &&
        e.clientX <= rect.left + rect.width
      );
      if (!isInDialog) {
        closeModal(dialog);
      }
    });
  });
}

// ---------------------------------------------------------------------------
// Trips Data Loading
// ---------------------------------------------------------------------------
async function loadTripsList() {
  try {
    const res = await fetch("/api/trips?country=India");
    if (!res.ok) throw new Error("Failed to fetch trips");
    const trips = await res.json();
    State.trips = trips;

    // Render Front Page Discovery Grid (Strictly Indian destinations)
    renderExploreGrid(trips, State.exploreFilter, State.exploreSearch);

    // Populate Top Nav Dropdown
    Elements.tripSelect.innerHTML = "";
    if (trips.length === 0) {
      Elements.tripSelect.innerHTML = `<option value="">No trips found. Create one!</option>`;
      return;
    }

    trips.forEach(t => {
      const opt = document.createElement("option");
      opt.value = t.id;
      opt.textContent = `${t.destination} (${t.days_count} Days) – ${t.title}`;
      Elements.tripSelect.appendChild(opt);
    });

    // Auto-select first trip in background
    if (trips.length > 0) {
      await loadTripDetails(trips[0].id);
    }
  } catch (err) {
    console.error("Trips list error:", err);
    showToast("Error loading travel itineraries", "error");
  }
}

// ---------------------------------------------------------------------------
// Curated Authentic Destination Image Registry for Indian Places
// ---------------------------------------------------------------------------
const INDIAN_DESTINATION_IMAGES = {
  // Sacred Circuits & Temples
  "kedarnath": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
  "badrinath": "https://images.unsplash.com/photo-1605649487212-47bdab064df7?auto=format&fit=crop&w=1200&q=80",
  "char dham": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
  "yamunotri": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
  "gangotri": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
  "vaishno": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
  "katra": "https://images.unsplash.com/photo-1598091383021-15ddea10925d?auto=format&fit=crop&w=1200&q=80",
  "tirupati": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?auto=format&fit=crop&w=1200&q=80",
  "balaji": "https://images.unsplash.com/photo-1590077428593-a55bb07c4665?auto=format&fit=crop&w=1200&q=80",
  "ayodhya": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
  "varanasi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
  "kashi": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
  "banaras": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
  "puri": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
  "konark": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
  "jagannath": "https://images.unsplash.com/photo-1609137144813-7d9921338f24?auto=format&fit=crop&w=1200&q=80",
  "dwarka": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
  "somnath": "https://images.unsplash.com/photo-1590050752117-238cb0fb12b1?auto=format&fit=crop&w=1200&q=80",
  "ujjain": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
  "omkareshwar": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
  "mahakal": "https://images.unsplash.com/photo-1627894483216-2138af692e32?auto=format&fit=crop&w=1200&q=80",
  "rameswaram": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
  "madurai": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
  "meenakshi": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
  "amritsar": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",
  "golden temple": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",
  "harmandir": "https://images.unsplash.com/photo-1514222134-b57cbb8ce073?auto=format&fit=crop&w=1200&q=80",

  // Popular Holiday Destinations, Palaces, Beaches, Mountains & Cities
  "jaipur": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
  "hawa mahal": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
  "amer": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
  "udaipur": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
  "pichola": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
  "lake palace": "https://images.unsplash.com/photo-1615836245337-f5b9b2303f10?auto=format&fit=crop&w=1200&q=80",
  "goa": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
  "calangute": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
  "baga": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
  "manali": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
  "solang": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
  "kullu": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
  "atal tunnel": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?auto=format&fit=crop&w=1200&q=80",
  "leh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
  "ladakh": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
  "pangong": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
  "nubra": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
  "munnar": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
  "alleppey": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
  "kerala": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
  "kochi": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
  "rishikesh": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
  "haridwar": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
  "ganga": "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
  "ooty": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
  "nilgiri": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
  "coonoor": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?auto=format&fit=crop&w=1200&q=80",
  "mussoorie": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
  "mussorie": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
  "shimla": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=1200&q=80",
  "kufri": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=1200&q=80",
  "darjeeling": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
  "sikkim": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
  "gangtok": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
  "agra": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
  "taj mahal": "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=1200&q=80",
  "delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
  "new delhi": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
  "mohali": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
  "chandigarh": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
  "punjab": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
  "mumbai": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
  "bombay": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
  "kolkata": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1200&q=80",
  "calcutta": "https://images.unsplash.com/photo-1558431382-27e303142255?auto=format&fit=crop&w=1200&q=80",
  "chennai": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
  "madras": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
  "bangalore": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
  "bengaluru": "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=1200&q=80",
  "hyderabad": "https://images.unsplash.com/photo-1605281317010-fe5ffe798166?auto=format&fit=crop&w=1200&q=80",
  "kashmir": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80",
  "srinagar": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80",
  "dal lake": "https://images.unsplash.com/photo-1566837945700-30057527ade0?auto=format&fit=crop&w=1200&q=80"
};

function getIndianDestinationImage(destination, currentImage) {
  const d = (destination || "").toLowerCase();

  // If currentImage is an old duplicated generic fallback (e.g. Hawa Mahal on Dwarka/Udaipur or Taj Mahal on mountains), override it
  const isGenericTajMahal = currentImage && currentImage.includes("photo-1524492412937-b28074a5d7da") && !d.includes("agra");
  const isGenericHawaMahal = currentImage && currentImage.includes("photo-1599661046289-e31897846e41") && !d.includes("jaipur");
  const isGenericVaranasi = currentImage && currentImage.includes("photo-1561361513-2d000a50f0dc") && !d.includes("varanasi") && !d.includes("ayodhya") && !d.includes("kashi");
  const isGenericKedarnath = currentImage && currentImage.includes("photo-1626714485844-93b5847e9559");
  const isGenericTirupati = currentImage && currentImage.includes("photo-1590077428593-a55bb07c4665") && !d.includes("tirupati") && !d.includes("balaji");
  const isGenericRishikesh = currentImage && currentImage.includes("photo-1506461883276-594a12b11cf3") && !d.includes("rishikesh") && !d.includes("haridwar") && !d.includes("ganga");

  if (currentImage && !isGenericTajMahal && !isGenericHawaMahal && !isGenericVaranasi && !isGenericKedarnath && !isGenericTirupati && !isGenericRishikesh) {
    return currentImage;
  }

  // Look for match in registry
  for (const [key, img] of Object.entries(INDIAN_DESTINATION_IMAGES)) {
    if (d.includes(key)) {
      return img;
    }
  }

  if (currentImage && !isGenericTajMahal && !isGenericHawaMahal) return currentImage;
  return "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80";
}

// ---------------------------------------------------------------------------
// Front Page Explore Grid (Matches user reference image layout exactly)
// ---------------------------------------------------------------------------
function renderExploreGrid(trips, filter = "all", searchQuery = "") {
  const grid = Elements.exploreCardsGrid;
  if (!grid) return;
  grid.innerHTML = "";

  // Strictly filter Indian destinations so world destinations never leak into Indian explore grid
  const indianTrips = (trips || []).filter(t => (t.country || "").toLowerCase().includes("india"));

  const q = searchQuery.toLowerCase().trim();
  let filtered = indianTrips.filter(t => {
    if (q) {
      const matchDest = (t.destination || "").toLowerCase().includes(q);
      const matchTitle = (t.title || "").toLowerCase().includes(q);
      const matchStyle = (t.travel_style || "").toLowerCase().includes(q);
      const matchNotes = (t.notes || "").toLowerCase().includes(q);
      if (!matchDest && !matchTitle && !matchStyle && !matchNotes) return false;
    }

    if (filter === "all") return true;
    if (filter === "Spiritual & Pilgrimage") {
      return (t.travel_style || "").includes("Spiritual") ||
             (t.title || "").includes("Dham") ||
             (t.destination || "").includes("Kedarnath") ||
             (t.destination || "").includes("Badrinath") ||
             (t.destination || "").includes("Dham") ||
             (t.destination || "").includes("Vaishno") ||
             (t.destination || "").includes("Tirupati") ||
             (t.destination || "").includes("Ayodhya") ||
             (t.destination || "").includes("Puri") ||
             (t.destination || "").includes("Dwarka") ||
             (t.destination || "").includes("Somnath") ||
             (t.destination || "").includes("Ujjain") ||
             (t.destination || "").includes("Varanasi") ||
             (t.destination || "").includes("Rameswaram");
    }
    if (filter.startsWith("pace-")) {
      const paceVal = filter.replace("pace-", "");
      return t.travel_pace === paceVal;
    }
    return (t.travel_style || "").toLowerCase().includes(filter.toLowerCase());
  });

  if (Elements.countAllTrips) {
    Elements.countAllTrips.textContent = indianTrips.length;
  }

  const countPill = document.getElementById("explore-count-pill");
  if (countPill) {
    countPill.textContent = `Showing ${filtered.length} of ${indianTrips.length} journeys`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="explore-empty">
        <div class="explore-empty-icon">🔍</div>
        <h3>No journeys match your search</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">Try adjusting your keywords or clearing the filter chip.</p>
        <button class="btn btn-secondary btn-sm" style="margin-top: 1rem;" onclick="resetExploreFilters()">Reset Filters</button>
      </div>
    `;
    return;
  }

  filtered.forEach(trip => {
    const card = document.createElement("div");
    card.className = "explore-card";
    card.dataset.tripId = trip.id;

    let paceIcon = "⚖️";
    if (trip.travel_pace === "Relaxed") paceIcon = "🧘";
    if (trip.travel_pace === "Fast-Paced") paceIcon = "⚡";

    const daysCount = trip.days_count || 1;
    const cover = getIndianDestinationImage(trip.destination, trip.cover_image);

    card.innerHTML = `
      <div class="explore-card-img-wrap">
        <img src="${escapeHtml(cover)}" alt="${escapeHtml(trip.destination)}" class="explore-card-img" loading="lazy" />
        <div class="explore-card-pace-badge">${paceIcon} ${escapeHtml(trip.travel_pace || "Moderate")}</div>
      </div>
      <div class="explore-card-body">
        <h3 class="explore-card-title">${escapeHtml(trip.title)}</h3>
        <div class="explore-card-pills">
          <span class="explore-pill pill-duration">${daysCount} days</span>
          <span class="explore-pill pill-destination">${escapeHtml(trip.destination)}</span>
          <span class="explore-pill pill-budget">₹${(trip.total_budget || 0).toLocaleString('en-IN')}</span>
        </div>
        <div class="explore-card-footer">
          <span>View Itinerary & Transport</span>
          <span>→</span>
        </div>
      </div>
    `;

    card.addEventListener("click", () => {
      showTripDetailView(trip.id);
    });

    grid.appendChild(card);
  });
}

function resetExploreFilters() {
  State.exploreFilter = "all";
  State.exploreSearch = "";
  if (Elements.exploreSearchInput) Elements.exploreSearchInput.value = "";
  document.querySelectorAll(".explore-filter-chips .chip").forEach(c => {
    c.classList.toggle("active", c.dataset.filter === "all");
  });
  renderExploreGrid(State.trips, "all", "");
}
window.resetExploreFilters = resetExploreFilters;

async function loadTripDetails(tripId) {
  try {
    const res = await fetch(`/api/trips/${tripId}`);
    if (!res.ok) throw new Error("Failed to fetch trip details");
    const trip = await res.json();
    State.activeTrip = trip;
    State.selectedCurrency = trip.currency || "INR";
    if (Elements.globalCurrencySelect) Elements.globalCurrencySelect.value = State.selectedCurrency;

    // Ensure trip is present in dropdown options
    if (Elements.tripSelect) {
      let existingOpt = Elements.tripSelect.querySelector(`option[value="${trip.id}"]`);
      if (!existingOpt) {
        const opt = document.createElement("option");
        opt.value = trip.id;
        opt.textContent = `${trip.destination} (${trip.days_count} Days) – ${trip.title}`;
        Elements.tripSelect.appendChild(opt);
      }
      Elements.tripSelect.value = trip.id;
    }

    if (Elements.navActiveTripLabel) {
      Elements.navActiveTripLabel.textContent = trip.destination;
    }
    if (Elements.backCrumbText) {
      Elements.backCrumbText.textContent = trip.country ? `${trip.destination}, ${trip.country}` : `${trip.destination}`;
    }

    // Render components
    renderHeroBanner(trip);
    renderDayPills(trip);
    renderDayActivities(1);

    // Transport & Commute Section
    renderTransportSection(trip.transport_options, trip.currency);

    // Weather
    if (window.WeatherModule) {
      window.WeatherModule.fetchAndRenderWeather(trip.latitude, trip.longitude, trip.destination);
    }

    // Budget
    if (window.BudgetModule) {
      window.BudgetModule.renderBudgetSummary(trip.budget_summary, trip.currency, trip.days_count);
      window.BudgetModule.renderExpenseTable(trip.expenses, trip.currency, handleDeleteExpense);
      window.BudgetModule.initCurrencyConverter(trip.currency, trip.currency === "INR" ? "USD" : "INR");
    }
    updateBudgetSectionCalculator(trip);

    // Packing
    renderPackingList(trip.packing_summary);

    // AI Advisor
    renderAiAdvisor(trip);

  } catch (err) {
    console.error("Trip details error:", err);
    showToast("Error loading trip information", "error");
  }
}

// ---------------------------------------------------------------------------
// Hero Banner & Metrics
// ---------------------------------------------------------------------------
function renderHeroBanner(trip) {
  const sym = window.BudgetModule ? window.BudgetModule.getCurrencySymbol(trip.currency) : "₹";

  // Cover Image
  const coverImg = getIndianDestinationImage(trip.destination, trip.cover_image);
  Elements.heroBackdrop.style.backgroundImage = `url('${coverImg}')`;

  Elements.heroTitle.textContent = trip.title;
  Elements.heroDestination.textContent = `${trip.destination}${trip.country ? ', ' + trip.country : ''}`;
  Elements.heroStyle.textContent = trip.travel_style;

  // Travel Pace Display
  const pace = trip.travel_pace || "Moderate";
  if (Elements.heroPace) {
    if (pace === "Fast-Paced") Elements.heroPace.textContent = "⚡ Fast-Paced (5 acts/day)";
    else if (pace === "Relaxed") Elements.heroPace.textContent = "🧘 Relaxed (2 acts/day)";
    else Elements.heroPace.textContent = "⚖️ Moderate (3 acts/day)";
  }
  if (Elements.tripPaceSelect) {
    Elements.tripPaceSelect.value = pace;
  }

  // Format Dates
  const sDate = new Date(trip.start_date + "T00:00:00");
  const eDate = new Date(trip.end_date + "T00:00:00");
  const dateStr = `${sDate.toLocaleDateString("en-US", { month: "short", day: "numeric" })} – ${eDate.toLocaleDateString("en-US", { month: "short", day: "numeric", year: "numeric" })}`;
  Elements.heroDates.textContent = dateStr;

  Elements.heroNotes.textContent = trip.notes || `Your personalized smart travel itinerary for ${trip.destination}.`;

  updateHeroMetrics(trip);
  updateTripCompletionUI(trip);
}

function updateHeroMetrics(trip) {
  const sym = window.BudgetModule ? window.BudgetModule.getCurrencySymbol(State.selectedCurrency) : "₹";

  Elements.metricDuration.textContent = `${trip.days_count} ${trip.days_count === 1 ? 'Day' : 'Days'}`;

  // Countdown
  const today = new Date();
  today.setHours(0, 0, 0, 0);
  const start = new Date(trip.start_date + "T00:00:00");
  const diffDays = Math.ceil((start - today) / (1000 * 60 * 60 * 24));

  if (diffDays > 0) {
    Elements.metricCountdown.textContent = `In ${diffDays} days`;
  } else if (diffDays === 0) {
    Elements.metricCountdown.textContent = "Today!";
  } else {
    Elements.metricCountdown.textContent = `${Math.abs(diffDays)}d ago`;
  }

  // Budget
  Elements.metricBudget.textContent = `${sym}${(trip.total_budget || 0).toLocaleString('en-IN')}`;

  const spent = trip.total_spent || 0;
  const pct = trip.total_budget > 0 ? Math.round((spent / trip.total_budget) * 100) : 0;
  Elements.metricSpent.textContent = `${sym}${spent.toLocaleString('en-IN')} (${pct}%)`;

  // Packing
  const packPct = trip.packing_summary ? trip.packing_summary.percent_packed : 0;
  Elements.metricPacking.textContent = `${packPct}%`;
}

// ---------------------------------------------------------------------------
// TRANSPORT & COMMUTE SECTION (WITH COSTS)
// ---------------------------------------------------------------------------
function getTransportModeIcon(mode) {
  const map = {
    Train: "🚆",
    Flight: "✈️",
    "Cab/Taxi": "🚕",
    "Auto-Rickshaw": "🛺",
    Scooter: "🛵",
    Bus: "🚌",
    Ferry: "⛴️",
    Boat: "🛶",
    Metro: "🚇"
  };
  return map[mode] || "🚗";
}

function renderTransportSection(transportOptions = [], currency = "INR") {
  const grid = Elements.transportOptionsGrid;
  if (!grid) return;
  grid.innerHTML = "";

  const sym = window.BudgetModule ? window.BudgetModule.getCurrencySymbol(currency) : "₹";

  const totalCost = transportOptions.reduce((acc, t) => acc + (t.estimated_cost || 0), 0);
  const bookedOptions = transportOptions.filter(t => t.is_booked);
  const bookedCost = bookedOptions.reduce((acc, t) => acc + (t.estimated_cost || 0), 0);
  const pendingOptions = transportOptions.filter(t => !t.is_booked);
  const pendingCost = pendingOptions.reduce((acc, t) => acc + (t.estimated_cost || 0), 0);

  // Update Summary Stats
  if (Elements.transportTotalCost) Elements.transportTotalCost.textContent = `${sym}${totalCost.toLocaleString('en-IN')}`;
  if (Elements.transportTotalCount) Elements.transportTotalCount.textContent = `${transportOptions.length} routes configured`;
  if (Elements.transportBookedCost) Elements.transportBookedCost.textContent = `${sym}${bookedCost.toLocaleString('en-IN')}`;
  if (Elements.transportBookedCount) Elements.transportBookedCount.textContent = `${bookedOptions.length} of ${transportOptions.length} booked`;
  if (Elements.transportPendingCost) Elements.transportPendingCost.textContent = `${sym}${pendingCost.toLocaleString('en-IN')}`;
  if (Elements.transportPendingCount) Elements.transportPendingCount.textContent = `${pendingOptions.length} items remaining`;

  if (!transportOptions || transportOptions.length === 0) {
    grid.innerHTML = `
      <div class="transport-empty">
        <div class="transport-empty-icon">🚗</div>
        <h3>No transit options configured yet</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">Add Vande Bharat trains, domestic flights, cabs, or scooter rentals with estimated Indian Rupee costs.</p>
        <button class="btn btn-primary" style="margin-top: 1rem;" onclick="openModal(Elements.modalAddTransport)">+ Add First Transport Option</button>
      </div>
    `;
    return;
  }

  transportOptions.forEach(opt => {
    const card = document.createElement("div");
    card.className = `transport-card ${opt.is_booked ? 'is-booked' : ''}`;
    card.dataset.transportId = opt.id;

    const modeIcon = getTransportModeIcon(opt.mode);
    const costFormatted = `${sym}${(opt.estimated_cost || 0).toLocaleString('en-IN')}`;

    card.innerHTML = `
      <div class="transport-card-top">
        <span class="transport-mode-pill">${modeIcon} ${escapeHtml(opt.mode)}</span>
        <div class="transport-cost-badge">
          <span class="cost-figure">${costFormatted}</span>
          <span class="cost-label">Est. Cost</span>
        </div>
      </div>
      <h3 class="transport-title">${escapeHtml(opt.title)}</h3>
      ${opt.route ? `
        <div class="transport-route">
          <span class="transport-route-icon">📍</span>
          <span>${escapeHtml(opt.route)}</span>
        </div>
      ` : ''}
      ${opt.booking_tips ? `
        <div class="transport-tips">
          <strong>💡 Booking Tips & Hacks:</strong> ${escapeHtml(opt.booking_tips)}
        </div>
      ` : ''}
      <div class="transport-actions-row">
        <button class="btn-toggle-booked ${opt.is_booked ? 'booked' : ''}" data-id="${opt.id}" title="Toggle booking confirmation">
          <span>${opt.is_booked ? '✓ Confirmed / Booked' : '○ Mark as Booked'}</span>
        </button>
        <div style="display: flex; align-items: center; gap: 0.4rem;">
          <button class="btn-to-expense" data-id="${opt.id}" title="Log this commute directly into trip expenses">
            <span>+ Add to Expenses</span>
          </button>
          <button class="btn-delete-trans" data-id="${opt.id}" title="Delete option">
            <span>🗑️</span>
          </button>
        </div>
      </div>
    `;

    // Toggle booked
    card.querySelector(".btn-toggle-booked").addEventListener("click", async (e) => {
      e.stopPropagation();
      await handleToggleTransportBooked(opt.id);
    });

    // Convert to expense
    card.querySelector(".btn-to-expense").addEventListener("click", async (e) => {
      e.stopPropagation();
      await handleConvertTransportToExpense(opt.id);
    });

    // Delete transport
    card.querySelector(".btn-delete-trans").addEventListener("click", async (e) => {
      e.stopPropagation();
      await handleDeleteTransport(opt.id);
    });

    grid.appendChild(card);
  });
}

async function handleToggleTransportBooked(transportId) {
  try {
    const res = await fetch(`/api/transport/${transportId}/toggle`, {
      method: "PATCH"
    });
    if (!res.ok) throw new Error("Failed to toggle transport status");
    const updated = await res.json();
    showToast(`Transit marked as ${updated.is_booked ? 'Confirmed / Booked' : 'Pending'}!`, "success");

    if (State.activeTrip) {
      const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
      if (tripRes.ok) {
        State.activeTrip = await tripRes.json();
        renderTransportSection(State.activeTrip.transport_options, State.activeTrip.currency);
      }
    }
  } catch (err) {
    console.error("Toggle transport error:", err);
    showToast("Could not update transport status", "error");
  }
}

async function handleConvertTransportToExpense(transportId) {
  try {
    const res = await fetch(`/api/transport/${transportId}/to-expense`, {
      method: "POST"
    });
    if (!res.ok) throw new Error("Failed to convert transport to expense");
    const exp = await res.json();
    showToast(`🎉 Transport cost ₹${(exp.amount || 0).toLocaleString('en-IN')} logged into expenses!`, "success");

    if (State.activeTrip) {
      await loadTripDetails(State.activeTrip.id);
    }
  } catch (err) {
    console.error("Convert transport error:", err);
    showToast("Could not convert to expense", "error");
  }
}

async function handleDeleteTransport(transportId) {
  if (!confirm("Are you sure you want to delete this transport option?")) return;
  try {
    const res = await fetch(`/api/transport/${transportId}`, {
      method: "DELETE"
    });
    if (!res.ok) throw new Error("Failed to delete transport option");
    showToast("Transport option removed", "info");

    if (State.activeTrip) {
      const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
      if (tripRes.ok) {
        State.activeTrip = await tripRes.json();
        renderTransportSection(State.activeTrip.transport_options, State.activeTrip.currency);
      }
    }
  } catch (err) {
    console.error("Delete transport error:", err);
    showToast("Could not delete transport option", "error");
  }
}

async function handleAddTransportSubmit(e) {
  e.preventDefault();
  if (!State.activeTrip) return;

  const mode = document.getElementById("transport-mode-select").value;
  const cost = parseFloat(document.getElementById("transport-cost-input").value) || 0;
  const title = document.getElementById("transport-title-input").value.trim();
  const route = document.getElementById("transport-route-input").value.trim();
  const tips = document.getElementById("transport-tips-input").value.trim();

  try {
    const res = await fetch(`/api/trips/${State.activeTrip.id}/transport`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        mode,
        title,
        route,
        estimated_cost: cost,
        currency: "INR",
        booking_tips: tips,
        is_booked: false
      })
    });

    if (!res.ok) throw new Error("Failed to add transport option");
    closeModal(Elements.modalAddTransport);
    Elements.formAddTransport.reset();
    showToast("✨ Transport option added successfully!", "success");

    const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
    if (tripRes.ok) {
      State.activeTrip = await tripRes.json();
      renderTransportSection(State.activeTrip.transport_options, State.activeTrip.currency);
    }
  } catch (err) {
    console.error("Add transport error:", err);
    showToast("Could not save transport option", "error");
  }
}

// ---------------------------------------------------------------------------
// Day Pills & Day Activities Handling
// ---------------------------------------------------------------------------
function renderDayPills(trip) {
  Elements.dayPillsWrap.innerHTML = "";
  const days = trip.days_count || 1;

  for (let i = 1; i <= days; i++) {
    const btn = document.createElement("button");
    btn.className = `day-pill-btn ${i === 1 ? 'active' : ''}`;
    btn.dataset.day = i;

    // Calculate actual date for this day
    const sDate = new Date(trip.start_date + "T00:00:00");
    const thisDate = new Date(sDate.getTime() + (i - 1) * 24 * 60 * 60 * 1000);
    const dayName = thisDate.toLocaleDateString("en-US", { weekday: "short" });
    const dayNum = thisDate.getDate();

    btn.innerHTML = `
      <span class="day-pill-name">Day ${i}</span>
      <span class="day-pill-date">${dayName}, ${dayNum}</span>
    `;

    btn.addEventListener("click", () => {
      document.querySelectorAll(".day-pill-btn").forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      State.activeDay = i;
      renderDayActivities(i);
      renderMapForDay(i);
    });

    Elements.dayPillsWrap.appendChild(btn);
  }
}

function renderDayActivities(dayNum) {
  if (!State.activeTrip) return;
  const items = (State.activeTrip.itinerary_items || []).filter(item => item.day_number === dayNum);

  // Update Day Header Card
  Elements.currentDayTitle.textContent = `Day ${dayNum}: Planned Activities & Schedule`;

  const totalCost = items.reduce((sum, it) => sum + (it.estimated_cost || 0), 0);
  const sym = window.BudgetModule ? window.BudgetModule.getCurrencySymbol(State.activeTrip.currency) : "₹";
  Elements.currentDayStats.textContent = `${items.length} activities • Est. cost ${sym}${totalCost.toLocaleString('en-IN')}`;

  const completed = items.filter(it => it.is_completed).length;
  const pct = items.length > 0 ? Math.round((completed / items.length) * 100) : 0;
  Elements.dayProgressText.textContent = `${completed} of ${items.length} done (${pct}%)`;
  Elements.dayProgressFill.style.width = `${pct}%`;

  // Render Timeline
  Elements.activitiesTimeline.innerHTML = "";

  if (items.length === 0) {
    Elements.activitiesTimeline.innerHTML = `
      <div class="timeline-empty">
        <span class="empty-icon">🏖️</span>
        <p>No scheduled activities for Day ${dayNum}. Click "+ Add Activity" above to schedule a visit!</p>
      </div>
    `;
    return;
  }

  // Sort by order_index
  items.sort((a, b) => a.order_index - b.order_index);

  items.forEach(item => {
    const card = document.createElement("div");
    card.className = `activity-card ${item.is_completed ? 'completed' : ''}`;
    card.dataset.itemId = item.id;

    const slotClass = item.time_slot ? item.time_slot.toLowerCase().replace(/[^a-z0-9]/g, '-') : 'morning';
    const catIcon = getCategoryIcon(item.category);

    card.innerHTML = `
      <div class="activity-time-badge slot-${slotClass}">
        <span>${escapeHtml(item.time_slot || 'All Day')}</span>
      </div>
      <div class="activity-main">
        <div class="activity-header">
          <span class="activity-cat-icon">${catIcon}</span>
          <h4 class="activity-name">${escapeHtml(item.title)}</h4>
          ${item.estimated_cost > 0 ? `<span class="activity-cost">${sym}${item.estimated_cost.toLocaleString('en-IN')}</span>` : ''}
        </div>
        ${item.location ? `<p class="activity-location">📍 ${escapeHtml(item.location)}</p>` : ''}
        ${item.description ? `<p class="activity-desc">${escapeHtml(item.description)}</p>` : ''}
      </div>
      <div class="activity-actions">
        <button class="btn-check-activity ${item.is_completed ? 'checked' : ''}" data-id="${item.id}" title="Toggle completed">
          <span>${item.is_completed ? '✓' : '○'}</span>
        </button>
        <button class="btn-delete-activity" data-id="${item.id}" title="Delete activity">
          <span>🗑️</span>
        </button>
      </div>
    `;

    // Toggle completed
    card.querySelector(".btn-check-activity").addEventListener("click", (e) => {
      e.stopPropagation();
      handleToggleActivity(item.id);
    });

    // Delete activity
    card.querySelector(".btn-delete-activity").addEventListener("click", (e) => {
      e.stopPropagation();
      handleDeleteActivity(item.id);
    });

    Elements.activitiesTimeline.appendChild(card);
  });
}

function renderMapForDay(dayNum) {
  if (!window.MapModule || !State.activeTrip) return;
  const items = (State.activeTrip.itinerary_items || []).filter(item => item.day_number === dayNum);
  window.MapModule.renderDayMarkers(items, State.activeTrip.latitude, State.activeTrip.longitude);
}

// ---------------------------------------------------------------------------
// Activity Actions (Toggle, Delete, Add)
// ---------------------------------------------------------------------------
async function handleToggleActivity(itemId) {
  try {
    const res = await fetch(`/api/itinerary/${itemId}/toggle`, {
      method: "PATCH"
    });
    if (!res.ok) throw new Error("Failed to toggle activity");
    const updatedItem = await res.json();

    // Update in state
    const target = State.activeTrip.itinerary_items.find(i => i.id === itemId);
    if (target) target.is_completed = updatedItem.is_completed;

    renderDayActivities(State.activeDay);
  } catch (err) {
    console.error("Toggle activity error:", err);
    showToast("Error updating activity status", "error");
  }
}

async function handleDeleteActivity(itemId) {
  if (!confirm("Are you sure you want to remove this activity?")) return;

  try {
    const res = await fetch(`/api/itinerary/${itemId}`, {
      method: "DELETE"
    });
    if (!res.ok) throw new Error("Failed to delete activity");

    // Remove from state
    State.activeTrip.itinerary_items = State.activeTrip.itinerary_items.filter(i => i.id !== itemId);
    renderDayActivities(State.activeDay);
    renderMapForDay(State.activeDay);
    showToast("Activity removed from itinerary", "info");
  } catch (err) {
    console.error("Delete activity error:", err);
    showToast("Error removing activity", "error");
  }
}

function prepareAddActivityModal() {
  const select = document.getElementById("activity-day-select");
  if (!select || !State.activeTrip) return;

  select.innerHTML = "";
  for (let i = 1; i <= State.activeTrip.days_count; i++) {
    const opt = document.createElement("option");
    opt.value = i;
    opt.textContent = `Day ${i}`;
    if (i === State.activeDay) opt.selected = true;
    select.appendChild(opt);
  }
}

async function handleAddActivitySubmit(e) {
  e.preventDefault();
  if (!State.activeTrip) return;

  const dayNum = parseInt(document.getElementById("activity-day-select").value);
  const timeSlot = document.getElementById("activity-slot-select").value;
  const title = document.getElementById("activity-title").value.trim();
  const cat = document.getElementById("activity-category").value;
  const cost = parseFloat(document.getElementById("activity-cost").value) || 0;
  const loc = document.getElementById("activity-location").value.trim();
  const desc = document.getElementById("activity-desc").value.trim();

  try {
    const payload = {
      day_number: dayNum,
      time_slot: timeSlot,
      title: title,
      category: cat,
      estimated_cost: cost,
      location: loc,
      description: desc,
      order_index: 99
    };

    const res = await fetch(`/api/trips/${State.activeTrip.id}/itinerary`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed to add activity");
    const createdItem = await res.json();

    State.activeTrip.itinerary_items.push(createdItem);
    closeModal(Elements.modalAddActivity);
    Elements.formAddActivity.reset();

    renderDayActivities(State.activeDay);
    renderMapForDay(State.activeDay);
    showToast("✨ Activity added to itinerary!", "success");
  } catch (err) {
    console.error("Add activity error:", err);
    showToast("Error creating activity", "error");
  }
}

// ---------------------------------------------------------------------------
// Expense Actions
// ---------------------------------------------------------------------------
function prepareAddExpenseModal() {
  const dateInput = document.getElementById("expense-date");
  if (dateInput) {
    dateInput.value = new Date().toISOString().split("T")[0];
  }
}

async function handleAddExpenseSubmit(e) {
  e.preventDefault();
  if (!State.activeTrip) return;

  const title = document.getElementById("expense-title").value.trim();
  const amount = parseFloat(document.getElementById("expense-amount").value) || 0;
  const category = document.getElementById("expense-category").value;
  const dateStr = document.getElementById("expense-date").value;
  const notes = document.getElementById("expense-notes").value.trim();

  try {
    const payload = {
      title,
      amount,
      category,
      date: dateStr,
      notes,
      currency: State.activeTrip.currency || "INR"
    };

    const res = await fetch(`/api/trips/${State.activeTrip.id}/expenses`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed to log expense");

    closeModal(Elements.modalAddExpense);
    Elements.formAddExpense.reset();

    // Reload trip details to update budget calculations
    await loadTripDetails(State.activeTrip.id);
    showToast("💰 Expense logged successfully!", "success");
  } catch (err) {
    console.error("Add expense error:", err);
    showToast("Error recording expense", "error");
  }
}

async function handleDeleteExpense(expenseId) {
  if (!confirm("Remove this logged expense?")) return;

  try {
    const res = await fetch(`/api/expenses/${expenseId}`, {
      method: "DELETE"
    });
    if (!res.ok) throw new Error("Failed to delete expense");

    await loadTripDetails(State.activeTrip.id);
    showToast("Expense removed", "info");
  } catch (err) {
    console.error("Delete expense error:", err);
    showToast("Error removing expense", "error");
  }
}

// ---------------------------------------------------------------------------
// Smart Packing List
// ---------------------------------------------------------------------------
function renderPackingList(packingSummary) {
  const grid = Elements.packingCategoriesGrid;
  if (!grid || !packingSummary) return;

  grid.innerHTML = "";

  // Update progress bar
  Elements.packingProgressCount.textContent = `${packingSummary.packed_items} of ${packingSummary.total_items} items packed`;
  Elements.packingProgressPercent.textContent = `${packingSummary.percent_packed}%`;
  Elements.packingProgressFill.style.width = `${packingSummary.percent_packed}%`;

  const byCat = packingSummary.by_category || {};
  const catNames = Object.keys(byCat);

  if (catNames.length === 0) {
    grid.innerHTML = `<div class="timeline-empty"><p>No packing items generated yet.</p></div>`;
    return;
  }

  catNames.forEach(cat => {
    const items = byCat[cat];
    const catCard = document.createElement("div");
    catCard.className = "packing-category-card glass-panel";

    const catIconMap = {
      Clothing: "👕",
      Documents: "🛂",
      Electronics: "🔌",
      Toiletries: "🧴",
      Health: "💊",
      Gear: "🎒"
    };
    const catIcon = catIconMap[cat] || "📦";

    catCard.innerHTML = `
      <div class="category-header">
        <h4>${catIcon} ${escapeHtml(cat)}</h4>
        <span class="cat-count">${items.filter(i => i.is_packed).length}/${items.length}</span>
      </div>
      <ul class="packing-items-list" id="packing-cat-${cat}">
        ${items.map(it => `
          <li class="packing-item-row ${it.is_packed ? 'packed' : ''}" data-id="${it.id}">
            <label class="packing-checkbox-wrap">
              <input type="checkbox" class="packing-checkbox" ${it.is_packed ? 'checked' : ''} data-id="${it.id}" />
              <span class="packing-name">${escapeHtml(it.item_name)}</span>
            </label>
            <button class="btn-delete-packing" data-id="${it.id}" title="Remove item">&times;</button>
          </li>
        `).join('')}
      </ul>
    `;

    // Checkbox toggle listener
    catCard.querySelectorAll(".packing-checkbox").forEach(chk => {
      chk.addEventListener("change", async (e) => {
        const itemId = parseInt(e.target.dataset.id);
        await handleTogglePacking(itemId);
      });
    });

    // Delete item listener
    catCard.querySelectorAll(".btn-delete-packing").forEach(btn => {
      btn.addEventListener("click", async (e) => {
        const itemId = parseInt(e.target.dataset.id);
        await handleDeletePacking(itemId);
      });
    });

    grid.appendChild(catCard);
  });
}

async function handleTogglePacking(itemId) {
  try {
    const res = await fetch(`/api/packing/${itemId}/toggle`, {
      method: "PATCH"
    });
    if (!res.ok) throw new Error("Failed to toggle packing item");
    const updated = await res.json();

    // Reload trip details
    const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
    if (tripRes.ok) {
      State.activeTrip = await tripRes.json();
      renderPackingList(State.activeTrip.packing_summary);
      updateHeroMetrics(State.activeTrip);
    }
  } catch (err) {
    console.error("Toggle packing error:", err);
    showToast("Error updating packing checklist", "error");
  }
}

async function handleDeletePacking(itemId) {
  try {
    const res = await fetch(`/api/packing/${itemId}`, {
      method: "DELETE"
    });
    if (!res.ok) throw new Error("Failed to delete packing item");

    const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
    if (tripRes.ok) {
      State.activeTrip = await tripRes.json();
      renderPackingList(State.activeTrip.packing_summary);
      updateHeroMetrics(State.activeTrip);
    }
  } catch (err) {
    console.error("Delete packing error:", err);
    showToast("Error deleting item", "error");
  }
}

async function handleAddPackingSubmit(e) {
  e.preventDefault();
  if (!State.activeTrip) return;

  const itemName = document.getElementById("packing-item-name").value.trim();
  const category = document.getElementById("packing-category-select").value;

  try {
    const payload = {
      item_name: itemName,
      category: category,
      is_packed: false
    };

    const res = await fetch(`/api/trips/${State.activeTrip.id}/packing`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed to add packing item");

    closeModal(Elements.modalAddPacking);
    Elements.formAddPacking.reset();

    const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
    if (tripRes.ok) {
      State.activeTrip = await tripRes.json();
      renderPackingList(State.activeTrip.packing_summary);
    }
    showToast("Item added to packing list!", "success");
  } catch (err) {
    console.error("Add packing error:", err);
    showToast("Could not add item", "error");
  }
}

async function handleRegeneratePacking() {
  if (!State.activeTrip) return;
  try {
    showToast("Synchronizing packing checklist with live forecasts...", "info");
    const res = await fetch(`/api/trips/${State.activeTrip.id}/packing/regenerate`, {
      method: "POST"
    });
    if (!res.ok) throw new Error("Failed to regenerate packing");

    const tripRes = await fetch(`/api/trips/${State.activeTrip.id}`);
    if (tripRes.ok) {
      State.activeTrip = await tripRes.json();
      renderPackingList(State.activeTrip.packing_summary);
      updateHeroMetrics(State.activeTrip);
    }
    showToast("✨ Packing list synchronized with live weather!", "success");
  } catch (err) {
    console.error("Regenerate packing error:", err);
    showToast("Error updating packing checklist", "error");
  }
}

// ---------------------------------------------------------------------------
// AI Travel Guide & Cultural Etiquette
// ---------------------------------------------------------------------------
function renderAiAdvisor(trip) {
  Elements.aiDestinationIntro.textContent = `Instant local insights, transportation hacks, etiquette customs, and personalized recommendations for ${trip.destination}, India.`;

  const dest = trip.destination || "";
  const etiquetteMap = {
    Jaipur: [
      "Dress modestly when entering heritage temples and royal premises; remove footwear at sacred shrines.",
      "Always negotiate taxi and auto-rickshaw fares beforehand or insist on official meter / prepaid counter tickets.",
      "Opt for authorized Rajasthan Tourism Development Corporation (RTDC) licensed guides at Amer and City Palace.",
      "Greet shopkeepers with a respectful 'Namaste' with hands folded; it breaks barriers and helps during bazaar bargaining."
    ],
    Goa: [
      "Swim only in designated safety zones marked by lifeguard flags; avoid swimming after dusk or during monsoons.",
      "Always wear an ISI-approved helmet when riding rented Activas/bikes; traffic police actively check tourist licenses.",
      "Keep Goa clean: littering on public beaches attracts strict fines by coastal authorities.",
      "Respect historic Portuguese church dress codes in Old Goa; cover shoulders and knees at Basilica of Bom Jesus."
    ],
    Varanasi: [
      "Photography is strictly prohibited at Manikarnika Ghat out of respect for traditional cremation ceremonies.",
      "Arrive at Dashashwamedh Ghat by 5:45 PM to secure a front-row boat or ghat steps seat for the Grand Ganga Aarti.",
      "Beware of unsolicited touts near temple alleyways offering 'priority darshan' at inflated prices; use the official Kashi Vishwanath portal.",
      "Always remove leather belts, shoes, and electronic gadgets before passing through security gates into the main sanctum."
    ]
  };

  const hacksMap = {
    Jaipur: [
      "Purchase the Composite Monument Ticket at Amer Fort for ₹1,000 to enter Hawa Mahal, Jantar Mantar, and Nahargarh for 2 full days.",
      "Catch breathtaking golden hour views and dinner at Padao Open-Air Restaurant atop Nahargarh Fort overlooking the entire illuminated city.",
      "Take an electric e-rickshaw through Sireh Deori Bazaar for the smoothest commute through congested old gates."
    ],
    Goa: [
      "Download the 'GoaMiles' mobile app for government-regulated fixed-rate taxi bookings to avoid beach cab surges.",
      "Rent a scooter for ~₹450/day from registered vendors in Calangute or Panaji for the highest flexibility across beaches.",
      "Visit Fontainhas Latin Quarter early at 8:00 AM for undisturbed photography before cafes open."
    ],
    Varanasi: [
      "Hire a hand-rowed wooden boat instead of a noisy motorboat at 5:15 AM from Assi Ghat to observe morning prayers and ghat life in silence.",
      "Sample authentic hot Malaiyo and Tamatar Chaat at Kashi Chaat Bhandar near Godowlia Chowk in the late afternoon.",
      "Use shared e-rickshaws (₹10-20 per seat) between Cantt Railway Station and Godowlia crossing."
    ]
  };

  const etiquetteList = etiquetteMap[dest] || [
    "Dress modestly when entering religious landmarks; remove footwear before stepping inside sanctuaries.",
    "Carry small currency notes (₹10, ₹20, ₹50, ₹100) or use UPI scanning (Google Pay/PhonePe/Paytm) which is accepted everywhere.",
    "Bargaining is customary in traditional street markets; maintain a polite, smiling demeanor."
  ];

  const hacksList = hacksMap[dest] || [
    "Book Indian Railways Vande Bharat & Shatabdi train tickets up to 120 days early on IRCTC or via the Tatkal quota.",
    "Drink bottled or filtered RO water from reputed brands, and enjoy piping hot freshly prepared street food from crowded stalls.",
    "Prepaid taxi counters at airport arrival terminals offer the safest and most transparent fares without hidden surcharges."
  ];

  Elements.aiEtiquetteList.innerHTML = etiquetteList.map(t => `<li><span>🙏</span><span>${escapeHtml(t)}</span></li>`).join('');
  Elements.aiHacksList.innerHTML = hacksList.map(h => `<li><span>💡</span><span>${escapeHtml(h)}</span></li>`).join('');
}

async function handleAskAi() {
  const query = Elements.aiQueryInput.value.trim();
  if (!query) return;

  Elements.btnAskAi.disabled = true;
  Elements.btnAskAi.innerHTML = `<span>Thinking...</span>`;
  Elements.aiResponsePanel.style.display = "block";
  Elements.aiResponseText.textContent = "Analyzing query and local travel intelligence...";

  try {
    const dest = State.activeTrip ? State.activeTrip.destination : "India";
    const prompt = `Provide practical, concise local advice for a traveler in ${dest}, India regarding: "${query}". Include transportation, cost estimates, safety tips, and timing recommendations where relevant.`;

    const res = await fetch(`/api/advisor/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        destination: dest,
        query: query
      })
    });

    if (res.ok) {
      const data = await res.json();
      Elements.aiResponseText.textContent = data.answer || "Advisor response received.";
    } else {
      // Local simulated response fallback
      setTimeout(() => {
        Elements.aiResponseText.textContent = `For "${query}" in ${dest}: The best time to visit is early morning to avoid crowds and peak heat. Pre-book transportation using official apps or prepaid booths, expect average commute costs around ₹200-₹500 for local distances, and carry UPI or cash for small vendors.`;
      }, 600);
    }
  } catch (err) {
    console.error("AI Advisor error:", err);
    Elements.aiResponseText.textContent = "Advisor connection failed. Please try again.";
  } finally {
    Elements.btnAskAi.disabled = false;
    Elements.btnAskAi.innerHTML = `<span>Ask Advisor</span>`;
  }
}

// ---------------------------------------------------------------------------
// Destination Autocomplete with Open-Meteo Geocoding
// ---------------------------------------------------------------------------
let autocompleteTimer = null;

function initDestinationAutocomplete() {
  const input = Elements.inputDestination;
  const dropdown = Elements.destinationDropdown;

  input.addEventListener("input", () => {
    clearTimeout(autocompleteTimer);
    const val = input.value.trim();
    if (val.length < 2) {
      dropdown.style.display = "none";
      return;
    }

    autocompleteTimer = setTimeout(async () => {
      try {
        const res = await fetch(`/api/places/search?q=${encodeURIComponent(val)}`);
        if (res.ok) {
          const places = await res.json();
          renderAutocomplete(places);
        }
      } catch (err) {
        console.error("Autocomplete search error:", err);
      }
    }, 300);
  });

  // Hide dropdown on blur
  document.addEventListener("click", (e) => {
    if (!input.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.style.display = "none";
    }
  });
}

function renderAutocomplete(places) {
  const dropdown = Elements.destinationDropdown;
  dropdown.innerHTML = "";

  if (!places || places.length === 0) {
    dropdown.style.display = "none";
    return;
  }

  places.forEach(p => {
    const item = document.createElement("div");
    item.className = "autocomplete-item";
    item.innerHTML = `
      <span class="auto-city">${escapeHtml(p.name)}</span>
      <span class="auto-country">${p.admin1 ? escapeHtml(p.admin1) + ', ' : ''}${escapeHtml(p.country)}</span>
    `;

    item.addEventListener("click", () => {
      Elements.inputDestination.value = p.name;
      Elements.inputDestination.dataset.country = p.country;
      Elements.inputDestination.dataset.lat = p.latitude;
      Elements.inputDestination.dataset.lon = p.longitude;
      dropdown.style.display = "none";
    });

    dropdown.appendChild(item);
  });

  dropdown.style.display = "block";
}

// ---------------------------------------------------------------------------
// Create Smart Trip Submission
// ---------------------------------------------------------------------------
async function handleCreateTripSubmit(e) {
  e.preventDefault();

  if (!checkLoginBeforePlanning(null, "Please sign in or create an account to start planning your trip!")) {
    return;
  }

  const dest = Elements.inputDestination.value.trim();
  const country = Elements.inputDestination.dataset.country || "India";
  const startDate = document.getElementById("input-start-date").value;
  const endDate = document.getElementById("input-end-date").value;
  const style = document.getElementById("select-travel-style").value;
  const pace = document.getElementById("select-pace").value;
  const budget = parseFloat(document.getElementById("input-budget").value) || 25000;
  const currency = document.getElementById("select-currency").value || "INR";

  if (new Date(endDate) < new Date(startDate)) {
    showToast("End date must be after start date", "error");
    return;
  }

  const submitBtn = document.getElementById("btn-submit-create");
  submitBtn.disabled = true;
  submitBtn.innerHTML = `<span>⏳ Synthesizing Smart Journey...</span>`;

  showToast(`Generating custom itinerary for ${dest}...`, "info");

  try {
    const payload = {
      destination: dest,
      country: country,
      start_date: startDate,
      end_date: endDate,
      travel_style: style,
      travel_pace: pace,
      total_budget: budget,
      currency: currency
    };

    const res = await fetch("/api/trips/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Trip generation failed");
    const createdTrip = await res.json();

    closeModal(Elements.modalCreateTrip);
    Elements.formCreateTrip.reset();

    showToast(`✨ Journey to ${dest} generated successfully!`, "success");

    // Reload trips list and switch to newly created trip
    await loadTripsList();
    await loadTripDetails(createdTrip.id);
    showTripDetailView(createdTrip.id);

  } catch (err) {
    console.error("Trip creation error:", err);
    showToast("Failed to generate trip. Please try again.", "error");
  } finally {
    submitBtn.disabled = false;
    submitBtn.innerHTML = `<span>Generate Smart Itinerary</span>`;
  }
}

// ---------------------------------------------------------------------------
// Utilities & Helpers
// ---------------------------------------------------------------------------
function initDefaultDates() {
  const startInput = document.getElementById("input-start-date");
  const endInput = document.getElementById("input-end-date");
  if (!startInput || !endInput) return;

  const today = new Date();
  const s = new Date(today.getTime() + 14 * 24 * 60 * 60 * 1000);
  const e = new Date(today.getTime() + 20 * 24 * 60 * 60 * 1000);

  startInput.value = s.toISOString().split("T")[0];
  endInput.value = e.toISOString().split("T")[0];
}

function getCategoryIcon(cat) {
  const map = {
    Attraction: "🏛️",
    Food: "🍜",
    Transport: "🚇",
    Leisure: "🌿",
    Lodging: "🏨"
  };
  return map[cat] || "📍";
}

function escapeHtml(str) {
  return String(str || "").replace(/[&<>"']/g, m => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
}

function showToast(message, type = "info") {
  const container = document.getElementById("toast-container");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;

  const icon = type === "success" ? "✅" : (type === "error" ? "⚠️" : "ℹ️");
  toast.innerHTML = `<span>${icon}</span><span>${escapeHtml(message)}</span>`;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateX(20px)";
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ---------------------------------------------------------------------------
// Circuit Defaults Metadata for Instant Two-Way Sync
// ---------------------------------------------------------------------------
const CIRCUIT_DEFAULTS = {
  "do-dham-kedarnath-badrinath": { name: "Kedarnath & Badrinath" },
  "char-dham-uttarakhand": { name: "Char Dham (Uttarakhand)" },
  "vaishno-devi-shiv-khori": { name: "Vaishno Devi (Katra)" },
  "tirupati-balaji": { name: "Tirupati Balaji" },
  "ayodhya-kashi": { name: "Ayodhya & Kashi" },
  "jagannath-puri": { name: "Jagannath Puri" },
  "dwarka-somnath": { name: "Dwarka & Somnath" },
  "ujjain-omkareshwar": { name: "Ujjain & Omkareshwar" },
  "rameswaram-madurai": { name: "Rameswaram & Madurai" },
  "amritsar-golden-temple": { name: "Amritsar" },
  "jaipur-pink-city": { name: "Jaipur" },
  "udaipur-city-of-lakes": { name: "Udaipur" },
  "goa-sun-sand": { name: "Goa" },
  "manali-solang-snow": { name: "Manali" },
  "leh-ladakh-high-passes": { name: "Leh Ladakh" },
  "munnar-alleppey-kerala": { name: "Munnar & Alleppey" }
};

function updateDhamDaysUI(days) {
  const badge = document.getElementById("dham-days-pill-badge");
  if (badge) {
    badge.textContent = `${days} Day${days > 1 ? "s" : ""}`;
  }
  const chips = document.querySelectorAll("#dham-quick-days .chip");
  chips.forEach(c => {
    if (parseInt(c.dataset.days) === days) {
      c.classList.add("active");
    } else {
      c.classList.remove("active");
    }
  });
}

// ---------------------------------------------------------------------------
// 1. Front Page Instant Destination & Dham Budget Calculator
// ---------------------------------------------------------------------------
async function initDhamBudgetCalculator() {
  const dateInput = Elements.dhamDate;
  if (dateInput && !dateInput.value) {
    const d = new Date();
    d.setDate(d.getDate() + 10);
    dateInput.value = d.toISOString().split("T")[0];
  }

  let dhamCalcDebounceTimer = null;

  // Typable destination input with debounced calculation and circuit matching
  Elements.dhamCustomDest?.addEventListener("input", () => {
    const val = Elements.dhamCustomDest.value.trim();

    // Try matching typed text with known circuits in select
    let matchedCircuit = "";
    if (Elements.dhamSelect) {
      for (const opt of Elements.dhamSelect.options) {
        if (opt.value && (opt.text.toLowerCase().includes(val.toLowerCase()) || val.toLowerCase().includes(opt.text.toLowerCase()))) {
          matchedCircuit = opt.value;
          break;
        }
      }
      Elements.dhamSelect.value = matchedCircuit;
    }

    // Highlight matching chip if any
    document.querySelectorAll("#dham-quick-dest-chips .chip").forEach(c => {
      if (c.dataset.dest && (c.dataset.dest.toLowerCase().includes(val.toLowerCase()) || val.toLowerCase().includes(c.dataset.dest.toLowerCase()))) {
        c.classList.add("active");
      } else {
        c.classList.remove("active");
      }
    });

    clearTimeout(dhamCalcDebounceTimer);
    dhamCalcDebounceTimer = setTimeout(recalculateDhamBudget, 250);
  });

  // Combo select picks curated circuit and copies directly into typable input
  Elements.dhamSelect?.addEventListener("change", () => {
    const selectVal = Elements.dhamSelect.value;
    if (selectVal) {
      const opt = Elements.dhamSelect.options[Elements.dhamSelect.selectedIndex];
      const name = CIRCUIT_DEFAULTS[selectVal]?.name || opt.text.replace(/^[^\w]+/, "").trim();
      if (Elements.dhamCustomDest) {
        Elements.dhamCustomDest.value = name;
      }
      // Update quick chips
      document.querySelectorAll("#dham-quick-dest-chips .chip").forEach(c => {
        if (c.dataset.dest && (c.dataset.dest.toLowerCase().includes(name.toLowerCase()) || name.toLowerCase().includes(c.dataset.dest.toLowerCase()))) {
          c.classList.add("active");
        } else {
          c.classList.remove("active");
        }
      });
      recalculateDhamBudget();
    }
  });

  // Quick Destination Chips click handler
  const dhamDestChips = document.getElementById("dham-quick-dest-chips");
  if (dhamDestChips) {
    dhamDestChips.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip || !chip.dataset.dest) return;
      document.querySelectorAll("#dham-quick-dest-chips .chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      if (Elements.dhamCustomDest) {
        Elements.dhamCustomDest.value = chip.dataset.dest;
      }
      if (Elements.dhamSelect) {
        let matched = "";
        for (const opt of Elements.dhamSelect.options) {
          if (opt.value && opt.text.toLowerCase().includes(chip.dataset.dest.toLowerCase())) {
            matched = opt.value;
            break;
          }
        }
        Elements.dhamSelect.value = matched;
      }
      recalculateDhamBudget();
    });
  }

  // Changing duration days keeps the chosen destination selected (never switches to custom)
  Elements.dhamCustomDays?.addEventListener("input", () => {
    const days = parseInt(Elements.dhamCustomDays.value) || 1;
    updateDhamDaysUI(days);
    recalculateDhamBudget();
  });

  // Quick Days Chips click handler
  const dhamChipsContainer = document.getElementById("dham-quick-days");
  if (dhamChipsContainer) {
    dhamChipsContainer.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip) return;
      const days = parseInt(chip.dataset.days);
      if (days && Elements.dhamCustomDays) {
        Elements.dhamCustomDays.value = days;
        updateDhamDaysUI(days);
        recalculateDhamBudget();
      }
    });
  }

  // Event listeners for real-time recalculation on all fields
  const triggerInputs = [
    Elements.dhamDate,
    Elements.dhamTime,
    Elements.dhamTier,
    Elements.dhamPilgrims
  ];

  triggerInputs.forEach(input => {
    input?.addEventListener("change", recalculateDhamBudget);
    input?.addEventListener("input", recalculateDhamBudget);
  });

  // 1-Click Generate Button
  Elements.btnGenerateDhamTrip?.addEventListener("click", handleGenerateDhamTrip);

  // Initial calculation
  if (Elements.dhamCustomDays) {
    updateDhamDaysUI(parseInt(Elements.dhamCustomDays.value) || 6);
  }
  await recalculateDhamBudget();
}

async function recalculateDhamBudget() {
  if (!Elements.dhamSelect) return;

  const selectVal = Elements.dhamSelect.value;
  const isCustom = selectVal === "custom";
  const date = Elements.dhamDate?.value;
  const time = Elements.dhamTime?.value || "06:30 AM";
  const tier = Elements.dhamTier?.value || "Standard";
  const numTravelers = parseInt(Elements.dhamPilgrims?.value) || 1;
  const destName = Elements.dhamCustomDest?.value?.trim() || "Kedarnath & Badrinath";
  const daysCount = parseInt(Elements.dhamCustomDays?.value) || 6;

  let payload = {
    date: date,
    departure_time: time,
    travel_tier: tier,
    num_travelers: numTravelers,
    destination: destName,
    days: daysCount
  };

  if (!isCustom && selectVal) {
    payload.circuit_id = selectVal;
  }

  try {
    const res = await fetch("/api/pilgrimage/estimate-budget", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      const data = await res.json();
      renderDhamBudgetResults(data);
    }
  } catch (err) {
    console.error("Destination budget calculation error:", err);
  }
}

function renderDhamBudgetResults(data) {
  if (Elements.dhamTotalBudget) {
    Elements.dhamTotalBudget.textContent = `₹${(data.total_budget || 0).toLocaleString('en-IN')}`;
  }
  if (Elements.dhamPerPerson) {
    const days = data.recommended_days || parseInt(Elements.dhamCustomDays?.value) || 1;
    Elements.dhamPerPerson.textContent = `₹${(data.per_person_budget || 0).toLocaleString('en-IN')} per person • ${days} Day${days > 1 ? 's' : ''} (${data.tier || 'Standard'} Tier)`;
  }

  const b = data.breakdown || {};
  if (Elements.dhamCostTransport) Elements.dhamCostTransport.textContent = `₹${(b.transport || 0).toLocaleString('en-IN')}`;
  if (Elements.dhamCostStay) Elements.dhamCostStay.textContent = `₹${(b.stay || 0).toLocaleString('en-IN')}`;
  if (Elements.dhamCostPooja) Elements.dhamCostPooja.textContent = `₹${(b.activities_entry || b.darshan_pooja || 0).toLocaleString('en-IN')}`;
  if (Elements.dhamCostFood) Elements.dhamCostFood.textContent = `₹${(b.food_dining || b.food_prasad || 0).toLocaleString('en-IN')}`;
}

async function handleGenerateDhamTrip() {
  if (!checkLoginBeforePlanning(() => handleGenerateDhamTrip(), "Please sign in or create an account to start planning your pilgrimage journey!")) {
    return;
  }

  const btn = Elements.btnGenerateDhamTrip;
  if (!btn) return;

  const selectVal = Elements.dhamSelect?.value || "do-dham-kedarnath-badrinath";
  const isCustom = selectVal === "custom";
  const date = Elements.dhamDate?.value;
  const time = Elements.dhamTime?.value || "06:30 AM";
  const tier = Elements.dhamTier?.value || "Standard";
  const numTravelers = parseInt(Elements.dhamPilgrims?.value) || 1;
  const destName = Elements.dhamCustomDest?.value?.trim() || "Kedarnath & Badrinath";
  const daysCount = parseInt(Elements.dhamCustomDays?.value) || 6;

  let payload = {
    start_date: date,
    departure_time: time,
    travel_tier: tier,
    num_travelers: numTravelers,
    destination: destName,
    days: daysCount
  };

  if (!isCustom && selectVal) {
    payload.circuit_id = selectVal;
  }

  btn.disabled = true;
  btn.innerHTML = `<span>⏳ Synthesizing Trip & Itinerary...</span>`;
  showToast("Synthesizing multi-day itinerary, transport tickets & realistic budget...", "info");

  try {
    const res = await fetch("/api/pilgrimage/generate-trip", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed to generate trip");
    const createdTrip = await res.json();

    showToast(`✨ ${createdTrip.title} created with calculated budget!`, "success");

    // Refresh trips list
    await loadTripsList();

    // Directly load the created trip details and open workspace
    await loadTripDetails(createdTrip.id);
    showTripDetailView(createdTrip.id);

  } catch (err) {
    console.error("Trip generation error:", err);
    showToast("Could not generate trip. Please try again.", "error");
  } finally {
    btn.disabled = false;
    btn.innerHTML = `
      <span class="btn-icon">✨</span>
      <span>Generate Trip with This Budget</span>
    `;
  }
}

// ---------------------------------------------------------------------------
// 2. Integrated Destination & Dham Budget Calculator (Budget Tab #pane-budget)
// ---------------------------------------------------------------------------
let lastBudgetPaneEstimate = null;

function updateBudgetDaysUI(days) {
  const badge = document.getElementById("budget-days-pill-badge");
  if (badge) {
    badge.textContent = `${days} Day${days > 1 ? "s" : ""}`;
  }
  const chips = document.querySelectorAll("#budget-quick-days .chip");
  chips.forEach(c => {
    if (parseInt(c.dataset.days) === days) {
      c.classList.add("active");
    } else {
      c.classList.remove("active");
    }
  });
}

async function initBudgetSectionCalculator() {
  if (!Elements.budgetSectionCalculator) return;

  const dateInput = Elements.budgetCalcDate;
  if (dateInput && !dateInput.value) {
    const d = new Date();
    d.setDate(d.getDate() + 10);
    dateInput.value = d.toISOString().split("T")[0];
  }

  let budgetCalcDebounceTimer = null;

  // Typable destination input with debounced calculation
  Elements.budgetCalcCustomDest?.addEventListener("input", () => {
    const val = Elements.budgetCalcCustomDest.value.trim();

    let matchedCircuit = "";
    if (Elements.budgetCalcSelect) {
      for (const opt of Elements.budgetCalcSelect.options) {
        if (opt.value && (opt.text.toLowerCase().includes(val.toLowerCase()) || val.toLowerCase().includes(opt.text.toLowerCase()))) {
          matchedCircuit = opt.value;
          break;
        }
      }
      Elements.budgetCalcSelect.value = matchedCircuit;
    }

    document.querySelectorAll("#budget-quick-dest-chips .chip").forEach(c => {
      if (c.dataset.dest && (c.dataset.dest.toLowerCase().includes(val.toLowerCase()) || val.toLowerCase().includes(c.dataset.dest.toLowerCase()))) {
        c.classList.add("active");
      } else {
        c.classList.remove("active");
      }
    });

    clearTimeout(budgetCalcDebounceTimer);
    budgetCalcDebounceTimer = setTimeout(recalculateBudgetSectionBudget, 250);
  });

  // Combo select picks curated circuit
  Elements.budgetCalcSelect?.addEventListener("change", () => {
    const selectVal = Elements.budgetCalcSelect.value;
    if (selectVal === "current-trip") {
      if (Elements.budgetCalcCustomDest) Elements.budgetCalcCustomDest.value = State.activeTrip?.destination || "Jaipur, India";
      if (Elements.budgetCalcCustomDays && State.activeTrip?.days_count) {
        Elements.budgetCalcCustomDays.value = State.activeTrip.days_count;
        updateBudgetDaysUI(State.activeTrip.days_count);
      }
    } else if (selectVal) {
      const opt = Elements.budgetCalcSelect.options[Elements.budgetCalcSelect.selectedIndex];
      const name = CIRCUIT_DEFAULTS[selectVal]?.name || opt.text.replace(/^[^\w]+/, "").trim();
      if (Elements.budgetCalcCustomDest) {
        Elements.budgetCalcCustomDest.value = name;
      }
      document.querySelectorAll("#budget-quick-dest-chips .chip").forEach(c => {
        if (c.dataset.dest && (c.dataset.dest.toLowerCase().includes(name.toLowerCase()) || name.toLowerCase().includes(c.dataset.dest.toLowerCase()))) {
          c.classList.add("active");
        } else {
          c.classList.remove("active");
        }
      });
    }
    recalculateBudgetSectionBudget();
  });

  // Quick Destination Chips in Budget section
  const budgetDestChips = document.getElementById("budget-quick-dest-chips");
  if (budgetDestChips) {
    budgetDestChips.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip || !chip.dataset.dest) return;
      document.querySelectorAll("#budget-quick-dest-chips .chip").forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
      if (Elements.budgetCalcCustomDest) {
        Elements.budgetCalcCustomDest.value = chip.dataset.dest;
      }
      recalculateBudgetSectionBudget();
    });
  }

  // Changing duration days keeps the chosen destination selected (never switches to custom)
  Elements.budgetCalcCustomDays?.addEventListener("input", () => {
    const days = parseInt(Elements.budgetCalcCustomDays.value) || 1;
    updateBudgetDaysUI(days);
    recalculateBudgetSectionBudget();
  });

  // Quick Days Chips click handler
  const budgetChipsContainer = document.getElementById("budget-quick-days");
  if (budgetChipsContainer) {
    budgetChipsContainer.addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip) return;
      const days = parseInt(chip.dataset.days);
      if (days && Elements.budgetCalcCustomDays) {
        Elements.budgetCalcCustomDays.value = days;
        updateBudgetDaysUI(days);
        recalculateBudgetSectionBudget();
      }
    });
  }

  // Real-time recalculation on any input field
  const triggerInputs = [
    Elements.budgetCalcDate,
    Elements.budgetCalcTime,
    Elements.budgetCalcTier,
    Elements.budgetCalcTravelers
  ];

  triggerInputs.forEach(input => {
    input?.addEventListener("change", recalculateBudgetSectionBudget);
    input?.addEventListener("input", recalculateBudgetSectionBudget);
  });

  // Action Buttons
  Elements.btnApplyAsTripBudget?.addEventListener("click", handleApplyAsTripBudget);
  Elements.btnAddBreakdownAsExpenses?.addEventListener("click", handleAddBreakdownAsExpenses);
  Elements.btnBudgetGenerateTrip?.addEventListener("click", handleGenerateBudgetSectionTrip);

  // Initial calculation
  if (Elements.budgetCalcCustomDays) {
    updateBudgetDaysUI(parseInt(Elements.budgetCalcCustomDays.value) || 5);
  }
  await recalculateBudgetSectionBudget();
}

function updateBudgetSectionCalculator(trip) {
  if (!trip || !Elements.budgetCalcSelect) return;

  // Update current trip optgroup label
  const currentOpt = Elements.budgetCalcSelect.querySelector("option[value='current-trip']");
  if (currentOpt) {
    currentOpt.textContent = `📍 Active Trip: ${trip.destination} (${trip.days_count || 1} Days)`;
  }

  // Pre-fill active trip values if current trip is selected
  if (Elements.budgetCalcSelect.value === "current-trip") {
    if (Elements.budgetCalcCustomDest) Elements.budgetCalcCustomDest.value = trip.destination;
    if (Elements.budgetCalcCustomDays) {
      Elements.budgetCalcCustomDays.value = trip.days_count || 5;
      updateBudgetDaysUI(trip.days_count || 5);
    }
    if (Elements.budgetCalcDate && trip.start_date) Elements.budgetCalcDate.value = trip.start_date;
  }

  // Recalculate
  recalculateBudgetSectionBudget();
}

async function recalculateBudgetSectionBudget() {
  if (!Elements.budgetCalcSelect) return;

  const selectVal = Elements.budgetCalcSelect.value;
  const isCustom = selectVal === "custom";
  const tier = Elements.budgetCalcTier?.value || "Standard";
  const numTravelers = parseInt(Elements.budgetCalcTravelers?.value) || 1;
  const date = Elements.budgetCalcDate?.value;
  const time = Elements.budgetCalcTime?.value || "06:30 AM";
  const destName = Elements.budgetCalcCustomDest?.value?.trim() || (State.activeTrip?.destination || "Jaipur, India");
  const daysCount = parseInt(Elements.budgetCalcCustomDays?.value) || (State.activeTrip?.days_count || 5);

  let payload = {
    date: date,
    departure_time: time,
    travel_tier: tier,
    num_travelers: numTravelers,
    destination: destName,
    days: daysCount
  };

  if (selectVal !== "current-trip" && !isCustom && selectVal) {
    payload.circuit_id = selectVal;
  }

  try {
    const res = await fetch("/api/pilgrimage/estimate-budget", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      const data = await res.json();
      lastBudgetPaneEstimate = data;
      renderBudgetSectionResults(data);
    }
  } catch (err) {
    console.error("Budget pane estimation error:", err);
  }
}

function renderBudgetSectionResults(data) {
  if (Elements.budgetCalcTotal) {
    Elements.budgetCalcTotal.textContent = `₹${(data.total_budget || 0).toLocaleString('en-IN')}`;
  }
  if (Elements.budgetCalcSub) {
    const days = data.recommended_days || parseInt(Elements.budgetCalcCustomDays?.value) || 1;
    Elements.budgetCalcSub.textContent = `₹${(data.per_person_budget || 0).toLocaleString('en-IN')} per person • ${days} Day${days > 1 ? 's' : ''} (${data.tier || 'Standard'} Tier)`;
  }

  const b = data.breakdown || {};
  if (Elements.budgetCalcTransport) Elements.budgetCalcTransport.textContent = `₹${(b.transport || 0).toLocaleString('en-IN')}`;
  if (Elements.budgetCalcStay) Elements.budgetCalcStay.textContent = `₹${(b.stay || 0).toLocaleString('en-IN')}`;
  if (Elements.budgetCalcActivities) Elements.budgetCalcActivities.textContent = `₹${(b.activities_entry || b.darshan_pooja || 0).toLocaleString('en-IN')}`;
  if (Elements.budgetCalcFood) Elements.budgetCalcFood.textContent = `₹${(b.food_dining || b.food_prasad || 0).toLocaleString('en-IN')}`;
}

async function handleApplyAsTripBudget() {
  if (!State.activeTrip || !lastBudgetPaneEstimate) {
    showToast("No active trip or calculated estimate available", "error");
    return;
  }

  const newTotal = lastBudgetPaneEstimate.total_budget;
  const btn = Elements.btnApplyAsTripBudget;

  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<span>⏳ Applying...</span>`;
  }

  try {
    const res = await fetch(`/api/trips/${State.activeTrip.id}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ total_budget: newTotal })
    });

    if (!res.ok) throw new Error("Failed to update trip budget");
    const updatedTrip = await res.json();

    State.activeTrip = updatedTrip;
    showToast(`🎯 Allocated trip budget updated to ₹${newTotal.toLocaleString('en-IN')}!`, "success");

    // Re-render hero budget metric & summary cards
    renderHeroBanner(updatedTrip);
    if (window.BudgetModule) {
      window.BudgetModule.renderBudgetSummary(updatedTrip.budget_summary, updatedTrip.currency, updatedTrip.days_count);
    }

  } catch (err) {
    console.error("Apply budget error:", err);
    showToast("Could not update trip budget", "error");
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `<span class="btn-icon">🎯</span><span>Apply as Trip Budget</span>`;
    }
  }
}

async function handleAddBreakdownAsExpenses() {
  if (!State.activeTrip || !lastBudgetPaneEstimate) {
    showToast("No active trip or calculated estimate available", "error");
    return;
  }

  const b = lastBudgetPaneEstimate.breakdown || {};
  const btn = Elements.btnAddBreakdownAsExpenses;

  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<span>⏳ Adding Expenses...</span>`;
  }

  const itemsToAdd = [
    {
      title: `Transit & Commute (${lastBudgetPaneEstimate.tier} Tier)`,
      amount: b.transport || 0,
      category: "Transport",
      date: State.activeTrip.start_date,
      notes: "Estimated transit fare from budget planner"
    },
    {
      title: `Accommodation Advance / Deposit (${lastBudgetPaneEstimate.tier})`,
      amount: roundNumber((b.stay || 0) * 0.5),
      category: "Accommodation",
      date: State.activeTrip.start_date,
      notes: "Hotel / stay deposit estimate"
    },
    {
      title: `Sightseeing & Activities Passes`,
      amount: b.activities_entry || b.darshan_pooja || 0,
      category: "Activities",
      date: State.activeTrip.start_date,
      notes: "Guided tours & attraction passes"
    },
    {
      title: `Food & Dining Allowance`,
      amount: roundNumber((b.food_dining || 0) * 0.5),
      category: "Food",
      date: State.activeTrip.start_date,
      notes: "Initial meal and dining budget"
    }
  ].filter(it => it.amount > 0);

  try {
    for (const item of itemsToAdd) {
      await fetch(`/api/trips/${State.activeTrip.id}/expenses`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(item)
      });
    }

    showToast(`📋 Added ${itemsToAdd.length} estimated itemized expenses to trip!`, "success");
    await loadTripDetails(State.activeTrip.id);

  } catch (err) {
    console.error("Add expenses error:", err);
    showToast("Error adding breakdown expenses", "error");
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `<span class="btn-icon">📋</span><span>Add Itemized Expenses</span>`;
    }
  }
}

async function handleGenerateBudgetSectionTrip() {
  if (!checkLoginBeforePlanning(() => handleGenerateBudgetSectionTrip(), "Please sign in or create an account to generate a new trip with this budget!")) {
    return;
  }

  const btn = Elements.btnBudgetGenerateTrip;
  if (!btn) return;

  const selectVal = Elements.budgetCalcSelect?.value || "current-trip";
  const isCustom = selectVal === "custom";
  const date = Elements.budgetCalcDate?.value;
  const time = Elements.budgetCalcTime?.value || "06:30 AM";
  const tier = Elements.budgetCalcTier?.value || "Standard";
  const numTravelers = parseInt(Elements.budgetCalcTravelers?.value) || 1;
  const destName = Elements.budgetCalcCustomDest?.value?.trim() || "Jaipur, India";
  const daysCount = parseInt(Elements.budgetCalcCustomDays?.value) || 5;

  let payload = {
    start_date: date,
    departure_time: time,
    travel_tier: tier,
    num_travelers: numTravelers,
    destination: destName,
    days: daysCount
  };

  if (selectVal !== "current-trip" && !isCustom && selectVal) {
    payload.circuit_id = selectVal;
  }

  btn.disabled = true;
  btn.innerHTML = `<span>⏳ Synthesizing Trip & Itinerary...</span>`;
  showToast("Synthesizing multi-day itinerary, transport tickets & realistic budget...", "info");

  try {
    const res = await fetch("/api/pilgrimage/generate-trip", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    if (!res.ok) throw new Error("Failed to generate trip");
    const createdTrip = await res.json();

    showToast(`✨ ${createdTrip.title} created with calculated budget!`, "success");

    // Refresh trips list
    await loadTripsList();

    // Directly load the created trip details and open workspace
    await loadTripDetails(createdTrip.id);
    showTripDetailView(createdTrip.id);

  } catch (err) {
    console.error("Trip generation error from budget tab:", err);
    showToast("Could not generate trip. Please try again.", "error");
  } finally {
    btn.disabled = false;
    btn.innerHTML = `
      <span class="btn-icon">✨</span>
      <span>Generate Trip with This Budget</span>
    `;
  }
}

function roundNumber(num) {
  return Math.round((num + Number.EPSILON) * 100) / 100;
}

// ===========================================================================
// WORLD DESTINATIONS TOUR CONTROLLER
// Explore global cities & country itineraries (Replicating user's reference)
// ===========================================================================

async function loadWorldGuides() {
  try {
    // 1. Fetch Popular Tags
    loadPopularWorldTags();

    // 2. Fetch Catalog of World Guides
    const res = await fetch("/api/world-guides");
    if (!res.ok) throw new Error("Failed to load world guides");
    const guides = await res.json();
    State.worldGuides = guides;

    renderWorldGuides();
  } catch (err) {
    console.error("Error loading world guides:", err);
    if (Elements.worldCardsGrid) {
      Elements.worldCardsGrid.innerHTML = `
        <div class="world-empty">
          <div class="world-empty-icon">⚠️</div>
          <h3 class="world-empty-title">Could not load world destination guides</h3>
          <p class="world-empty-sub">Please verify your server connection and try again.</p>
          <button class="btn btn-secondary btn-sm" onclick="loadWorldGuides()">Retry</button>
        </div>
      `;
    }
  }
}

async function loadPopularWorldTags() {
  if (!Elements.worldPopularChips) return;
  try {
    const res = await fetch("/api/world-guides/popular-tags");
    if (!res.ok) return;
    const tags = await res.json();

    let html = `
      <button class="world-chip ${State.worldFilterTag === 'all' ? 'active' : ''}" data-tag="all">
        All Destinations
      </button>
    `;

    tags.forEach(t => {
      const isActive = State.worldFilterTag.toLowerCase() === t.name.toLowerCase();
      html += `
        <button class="world-chip ${isActive ? 'active' : ''}" data-tag="${escapeHtml(t.name)}">
          ${escapeHtml(t.name)}
        </button>
      `;
    });

    Elements.worldPopularChips.innerHTML = html;

    // Attach click listener to each chip
    Elements.worldPopularChips.querySelectorAll(".world-chip").forEach(chip => {
      chip.addEventListener("click", () => {
        const tag = chip.dataset.tag;
        setWorldTagFilter(tag);
      });
    });
  } catch (err) {
    console.warn("Could not load popular tags:", err);
  }
}

function setWorldTagFilter(tag) {
  State.worldFilterTag = tag;

  if (Elements.worldPopularChips) {
    Elements.worldPopularChips.querySelectorAll(".world-chip").forEach(c => {
      const isMatch = (tag === "all" && c.dataset.tag === "all") || (c.dataset.tag.toLowerCase() === tag.toLowerCase());
      c.classList.toggle("active", isMatch);
    });
  }

  renderWorldGuides();
}
window.setWorldTagFilter = setWorldTagFilter;

function renderWorldGuides() {
  const grid = Elements.worldCardsGrid;
  if (!grid) return;

  const tag = State.worldFilterTag.toLowerCase();
  const q = State.worldSearchQuery.toLowerCase();

  const filtered = State.worldGuides.filter(guide => {
    // Tag match
    if (tag !== "all") {
      const matchesCountry = guide.country && guide.country.toLowerCase().includes(tag);
      const matchesCity = guide.city && guide.city.toLowerCase().includes(tag);
      const matchesDest = guide.destination && guide.destination.toLowerCase().includes(tag);
      const matchesTags = guide.tags && guide.tags.some(t => t.toLowerCase().includes(tag));
      if (!matchesCountry && !matchesCity && !matchesDest && !matchesTags) {
        return false;
      }
    }

    // Query match
    if (q) {
      const inTitle = guide.title && guide.title.toLowerCase().includes(q);
      const inDest = guide.destination && guide.destination.toLowerCase().includes(q);
      const inCity = guide.city && guide.city.toLowerCase().includes(q);
      const inCountry = guide.country && guide.country.toLowerCase().includes(q);
      const inExcerpt = guide.excerpt && guide.excerpt.toLowerCase().includes(q);
      const inTags = guide.tags && guide.tags.some(t => t.toLowerCase().includes(q));
      if (!inTitle && !inDest && !inCity && !inCountry && !inExcerpt && !inTags) {
        return false;
      }
    }

    return true;
  });

  // Update header count pill
  if (Elements.worldCountPill) {
    Elements.worldCountPill.textContent = `Showing ${filtered.length} ${filtered.length === 1 ? 'guide' : 'guides'}`;
  }

  // Update active tag filter indicator
  if (Elements.worldActiveFilterWrap) {
    if (State.worldFilterTag !== "all") {
      Elements.worldActiveFilterWrap.style.display = "block";
      if (Elements.worldFilterName) Elements.worldFilterName.textContent = State.worldFilterTag;
    } else {
      Elements.worldActiveFilterWrap.style.display = "none";
    }
  }

  // Handle empty search / filter state
  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="world-empty">
        <div class="world-empty-icon">🌍</div>
        <h3 class="world-empty-title">No world destination guides found</h3>
        <p class="world-empty-sub">We couldn't find any guides matching "${escapeHtml(State.worldSearchQuery || State.worldFilterTag)}". Try searching for cities like Tokyo, Paris, New York, Seoul, Chicago or Bali.</p>
        <button class="btn btn-secondary btn-sm" onclick="resetWorldFilters()">Clear Search & Filters</button>
      </div>
    `;
    return;
  }

  grid.innerHTML = "";

  filtered.forEach(guide => {
    const card = document.createElement("div");
    card.className = "world-guide-card";
    card.dataset.guideId = guide.id;

    const isLiked = State.likedGuideIds.has(guide.id);
    const likesCount = (guide.likes || 0) + (isLiked ? 1 : 0);
    const viewsCount = guide.views || 1000;
    const authorName = guide.author?.name || "Traveler";
    const authorAvatar = guide.author?.avatar;
    const coverImg = guide.cover_image || "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80";
    const locationTag = guide.city || guide.country || guide.destination;
    const guidePageUrl = `/world-guide?id=${encodeURIComponent(guide.id)}`;

    const avatarHtml = authorAvatar
      ? `<img src="${escapeHtml(authorAvatar)}" alt="${escapeHtml(authorName)}" class="world-author-avatar" loading="lazy" />`
      : `<div class="world-author-avatar-fallback">${escapeHtml(authorName.charAt(0).toUpperCase())}</div>`;

    const touristPlaces = guide.tourist_places || [];
    const placesNames = touristPlaces.slice(0, 3).map(p => p.name).join(", ");
    const placesExtra = touristPlaces.length > 3 ? ` +${touristPlaces.length - 3} more` : "";
    const placesHtml = placesNames ? `
      <div class="world-card-places-row" title="Key tourist places: ${escapeHtml(touristPlaces.map(p => p.name).join(', '))}">
        <span class="world-places-badge">🏛️ Sights:</span>
        <span class="world-places-text">${escapeHtml(placesNames)}${placesExtra}</span>
      </div>
    ` : "";

    card.innerHTML = `
      <div class="world-card-thumb-wrap">
        <img src="${escapeHtml(coverImg)}" alt="${escapeHtml(guide.title)}" class="world-card-img" loading="lazy" />
        <span class="world-card-tag-pill">📍 ${escapeHtml(locationTag)}</span>
        <div class="world-card-floating-actions">
          <button class="world-card-share-btn" data-share-id="${guide.id}" title="Share guide">
            <span style="font-size: 0.85rem;">🔗</span> Share
          </button>
          <button class="world-card-dots-btn" data-dots-id="${guide.id}" title="Quick preview modal">•••</button>
        </div>
      </div>

      <div class="world-card-body">
        <div class="world-card-title-row">
          <a href="${guidePageUrl}" target="_blank" class="world-card-title-link" title="Open complete guide in new page">
            <h3 class="world-card-title">${escapeHtml(guide.title)}</h3>
          </a>
          <span class="verified-badge-red" title="Verified Travel Guide">✓</span>
        </div>

        <p class="world-card-excerpt">${escapeHtml(guide.excerpt || guide.description || '')}</p>

        ${placesHtml}

        <div class="world-card-action-bar">
          <a href="${guidePageUrl}" target="_blank" class="world-card-open-page-btn" title="Open complete guide in new page">
            <span>Explore in New Page</span>
            <span class="open-icon">↗</span>
          </a>
        </div>

        <div class="world-card-footer">
          <div class="world-card-author">
            ${avatarHtml}
            <span class="world-author-name">${escapeHtml(authorName)}</span>
          </div>

          <div class="world-card-metrics">
            <button class="world-metric-btn ${isLiked ? 'liked' : ''}" data-like-id="${guide.id}" title="Like this guide">
              <span class="metric-heart-icon">${isLiked ? '❤️' : '🤍'}</span>
              <span class="metric-likes-val">${likesCount.toLocaleString()}</span>
            </button>
            <div class="world-metric-item" title="Guide Views">
              <span>👁️</span>
              <span>${viewsCount.toLocaleString()}</span>
            </div>
          </div>
        </div>
      </div>
    `;

    // Click on main card opens guide in a NEW PAGE (per user request)
    card.addEventListener("click", (e) => {
      // Avoid opening page if clicked on share or like buttons specifically
      if (e.target.closest(".world-card-share-btn") || e.target.closest(".world-metric-btn")) {
        return;
      }
      // If user specifically clicked dots button, open quick preview modal
      if (e.target.closest(".world-card-dots-btn")) {
        e.stopPropagation();
        openWorldGuideModal(guide);
        return;
      }
      // If clicked title link or action button, native <a> will navigate to new page.
      // If clicked elsewhere on the card, programmatically open in new tab
      if (!e.target.closest("a")) {
        window.open(guidePageUrl, "_blank");
      }
    });

    // Share button click
    const shareBtn = card.querySelector(".world-card-share-btn");
    shareBtn?.addEventListener("click", (e) => {
      e.stopPropagation();
      handleShareGuide(guide);
    });

    // Dots button click (Quick preview modal)
    const dotsBtn = card.querySelector(".world-card-dots-btn");
    dotsBtn?.addEventListener("click", (e) => {
      e.stopPropagation();
      openWorldGuideModal(guide);
    });

    // Like button click
    const likeBtn = card.querySelector(".world-metric-btn");
    likeBtn?.addEventListener("click", (e) => {
      e.stopPropagation();
      handleToggleLikeGuide(guide.id, likeBtn);
    });

    grid.appendChild(card);
  });
}

function resetWorldFilters() {
  State.worldFilterTag = "all";
  State.worldSearchQuery = "";
  if (Elements.worldSearchInput) Elements.worldSearchInput.value = "";
  if (Elements.btnClearWorldSearch) Elements.btnClearWorldSearch.style.display = "none";
  setWorldTagFilter("all");
}
window.resetWorldFilters = resetWorldFilters;

function formatWorldBudgetCurrency(amountInInr) {
  const sym = window.BudgetModule ? window.BudgetModule.getCurrencySymbol(State.selectedCurrency) : "₹";
  // If user selected USD or EUR, approximate conversion
  let converted = amountInInr;
  if (State.selectedCurrency === "USD") converted = amountInInr / 84;
  else if (State.selectedCurrency === "EUR") converted = amountInInr / 92;
  else if (State.selectedCurrency === "GBP") converted = amountInInr / 108;
  else if (State.selectedCurrency === "JPY") converted = amountInInr * 1.8;
  else if (State.selectedCurrency === "AUD") converted = amountInInr / 55;
  else if (State.selectedCurrency === "CAD") converted = amountInInr / 61;

  return `${sym}${Math.round(converted).toLocaleString()}`;
}

function openWorldGuideModal(guide) {
  State.activeWorldGuide = guide;

  if (Elements.wmodalTag) {
    Elements.wmodalTag.textContent = `${guide.country} • ${guide.travel_style || 'Global Tour'}`;
  }
  if (Elements.wmodalTitle) {
    Elements.wmodalTitle.textContent = guide.title;
  }
  if (Elements.wmodalCoverImg) {
    Elements.wmodalCoverImg.src = guide.cover_image;
    Elements.wmodalCoverImg.alt = guide.title;
  }
  if (Elements.wmodalDest) {
    Elements.wmodalDest.textContent = guide.destination;
  }
  if (Elements.wmodalDays) {
    Elements.wmodalDays.textContent = `${guide.recommended_days || 5} Days`;
  }
  if (Elements.wmodalPace) {
    const paceIcon = guide.travel_pace === "Relaxed" ? "🧘" : (guide.travel_pace === "Fast-Paced" ? "⚡" : "⚖️");
    Elements.wmodalPace.textContent = `${paceIcon} ${guide.travel_pace || 'Moderate'} Pace`;
  }
  if (Elements.wmodalStyle) {
    Elements.wmodalStyle.textContent = guide.travel_style || "World Tour";
  }

  // Author profile
  if (Elements.wmodalAuthorImg) {
    Elements.wmodalAuthorImg.src = guide.author?.avatar || "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=160&q=80";
  }
  if (Elements.wmodalAuthorName) {
    Elements.wmodalAuthorName.textContent = guide.author?.name || "Verified Traveler";
  }
  if (Elements.wmodalAuthorHandle) {
    Elements.wmodalAuthorHandle.textContent = `${guide.author?.handle || '@explorer'} • Verified Guide Curator`;
  }

  // Likes & Views
  const isLiked = State.likedGuideIds.has(guide.id);
  const likesCount = (guide.likes || 0) + (isLiked ? 1 : 0);
  if (Elements.wmodalLikeIcon) {
    Elements.wmodalLikeIcon.textContent = isLiked ? "❤️" : "🤍";
  }
  if (Elements.wmodalLikesCount) {
    Elements.wmodalLikesCount.textContent = likesCount.toLocaleString();
  }
  if (Elements.wmodalViewsCount) {
    Elements.wmodalViewsCount.textContent = (guide.views || 1000).toLocaleString();
  }

  // Description
  if (Elements.wmodalDesc) {
    Elements.wmodalDesc.textContent = guide.description || guide.excerpt;
  }

  // Estimated budget formatted in selected display currency
  if (Elements.wmodalBudgetDisplay) {
    Elements.wmodalBudgetDisplay.textContent = `Est. Total Budget: ${formatWorldBudgetCurrency(guide.total_budget || 100000)}`;
  }

  // Itinerary Highlights list
  if (Elements.wmodalItineraryList) {
    const highlights = guide.itinerary_highlights || [];
    if (highlights.length === 0) {
      Elements.wmodalItineraryList.innerHTML = `<p style="color: var(--text-muted); font-size: 0.85rem;">Daily highlights are ready to be synthesized in your workspace.</p>`;
    } else {
      Elements.wmodalItineraryList.innerHTML = highlights.map(item => {
        const [dayNum, slot, title, loc, lat, lon, cost, cat, notes] = item;
        const costStr = cost > 0 ? ` • ${formatWorldBudgetCurrency(cost)}` : "";
        return `
          <div class="wmodal-day-item">
            <span class="wmodal-day-pill">Day ${dayNum} (${slot})</span>
            <div class="wmodal-day-content">
              <div class="wmodal-day-title">${escapeHtml(title)}${costStr}</div>
              <div class="wmodal-day-notes">📍 ${escapeHtml(loc || '')} — ${escapeHtml(notes || '')}</div>
            </div>
          </div>
        `;
      }).join("");
    }
  }

  // Curated Transports list
  if (Elements.wmodalTransportsList) {
    const transports = guide.transports || [];
    if (transports.length === 0) {
      Elements.wmodalTransportsList.innerHTML = `<p style="color: var(--text-muted); font-size: 0.85rem;">Standard transit & flight options available in trip workspace.</p>`;
    } else {
      Elements.wmodalTransportsList.innerHTML = transports.map(t => {
        const [mode, title, route, fare, notes] = t;
        let modeIcon = "🚗";
        if (mode.toLowerCase().includes("train") || mode.toLowerCase().includes("shinkansen")) modeIcon = "🚆";
        if (mode.toLowerCase().includes("flight") || mode.toLowerCase().includes("air")) modeIcon = "✈️";
        if (mode.toLowerCase().includes("metro") || mode.toLowerCase().includes("subway")) modeIcon = "🚇";
        if (mode.toLowerCase().includes("ferry") || mode.toLowerCase().includes("boat")) modeIcon = "⛴️";

        return `
          <div class="wmodal-trans-item">
            <div class="wmodal-trans-info">
              <span class="wmodal-trans-icon">${modeIcon}</span>
              <div>
                <div class="wmodal-trans-title">${escapeHtml(title)}</div>
                <div class="wmodal-trans-route">Route: ${escapeHtml(route)}</div>
              </div>
            </div>
            <div class="wmodal-trans-cost">${formatWorldBudgetCurrency(fare || 0)}</div>
          </div>
        `;
      }).join("");
    }
  }

  // Link to dedicated full page
  if (Elements.btnWmodalOpenPage) {
    Elements.btnWmodalOpenPage.href = `/world-guide?id=${encodeURIComponent(guide.id)}`;
  }

  openModal(Elements.modalWorldGuide);
}

function handleShareGuide(guide) {
  const shareText = `Check out this amazing guide: ${guide.title} on TRAVEL PACE!`;
  const shareUrl = `${window.location.origin}/?guide=${guide.id}`;

  if (navigator.clipboard) {
    navigator.clipboard.writeText(`${shareText}\n${shareUrl}`).then(() => {
      showToast(`🔗 Guide link copied to clipboard!`, "success");
    }).catch(() => {
      showToast(`Link: ${shareUrl}`, "info");
    });
  } else {
    showToast(`Link: ${shareUrl}`, "info");
  }
}

async function handleToggleLikeGuide(guideId, btnElement = null) {
  try {
    const res = await fetch(`/api/world-guides/${guideId}/like`, { method: "POST" });
    if (!res.ok) throw new Error("Could not register like");
    const data = await res.json();

    State.likedGuideIds.add(guideId);

    // Update in memory guide
    const g = State.worldGuides.find(x => x.id === guideId);
    if (g) g.likes = data.likes;

    // Update modal if open
    if (State.activeWorldGuide && State.activeWorldGuide.id === guideId) {
      if (Elements.wmodalLikeIcon) Elements.wmodalLikeIcon.textContent = "❤️";
      if (Elements.wmodalLikesCount) Elements.wmodalLikesCount.textContent = data.likes.toLocaleString();
    }

    // Update specific card button if provided
    if (btnElement) {
      btnElement.classList.add("liked");
      const icon = btnElement.querySelector(".metric-heart-icon");
      const val = btnElement.querySelector(".metric-likes-val");
      if (icon) icon.textContent = "❤️";
      if (val) val.textContent = data.likes.toLocaleString();
    } else {
      renderWorldGuides();
    }

    showToast(`❤️ Added like to ${g ? g.title : 'guide'}!`, "success");
  } catch (err) {
    console.warn("Like failed:", err);
  }
}

async function handleCloneWorldGuide(guideId) {
  if (!checkLoginBeforePlanning(() => handleCloneWorldGuide(guideId), "Please sign in or create an account to clone this world journey to your trip workspace!")) {
    return;
  }

  const btn = Elements.btnWmodalClone;
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<span class="btn-icon">⏳</span><span>Synthesizing Trip Workspace...</span>`;
  }

  try {
    const res = await fetch(`/api/world-guides/${guideId}/clone`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({})
    });

    if (!res.ok) {
      const errData = await res.json().catch(() => ({}));
      throw new Error(errData.detail || "Failed to clone world guide");
    }

    const clonedTrip = await res.json();

    closeModal(Elements.modalWorldGuide);
    showToast(`🎉 Cloned "${clonedTrip.title}" into your workspace!`, "success");

    // Refresh trips list
    await loadTripsList();

    // Select the cloned trip in top nav and open workspace
    if (Elements.tripSelect) {
      Elements.tripSelect.value = clonedTrip.id;
    }
    await loadTripDetails(clonedTrip.id);
    showTripDetailView(clonedTrip.id);

  } catch (err) {
    console.error("Clone world guide error:", err);
    showToast(`Could not clone trip: ${err.message}`, "error");
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `<span class="btn-icon">🚀</span><span>Clone & Open in Trip Workspace</span>`;
    }
  }
}

// ===========================================================================
// HOTELS, AIRBNB & HOSTELS MODULE
// ===========================================================================

async function loadStays() {
  try {
    const res = await fetch("/api/stays");
    if (!res.ok) throw new Error("Failed to load stays");
    const data = await res.json();
    State.stays = data;
    initStaysPopularChips();
    filterAndRenderStays();
  } catch (err) {
    console.error("Error loading stays catalog:", err);
    showToast("Could not load hotel & Airbnb listings", "error");
  }
}

async function initStaysPopularChips() {
  const container = Elements.staysPopularChips;
  if (!container || container.children.length > 0) return;

  try {
    const res = await fetch("/api/stays/popular-destinations");
    if (!res.ok) return;
    const chips = await res.json();

    container.innerHTML = "";

    // Add "All Destinations" chip first
    const allBtn = document.createElement("button");
    allBtn.type = "button";
    allBtn.className = "stay-pop-chip active";
    allBtn.textContent = "✨ All Destinations";
    allBtn.addEventListener("click", () => {
      document.querySelectorAll(".stay-pop-chip").forEach(c => c.classList.remove("active"));
      allBtn.classList.add("active");
      if (Elements.staysSearchInput) Elements.staysSearchInput.value = "";
      if (Elements.btnClearStaysSearch) Elements.btnClearStaysSearch.style.display = "none";
      State.staysSearchQuery = "";
      filterAndRenderStays();
    });
    container.appendChild(allBtn);

    chips.forEach(chip => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "stay-pop-chip";
      btn.textContent = chip.label;
      btn.addEventListener("click", () => {
        document.querySelectorAll(".stay-pop-chip").forEach(c => c.classList.remove("active"));
        btn.classList.add("active");
        if (Elements.staysSearchInput) Elements.staysSearchInput.value = chip.name;
        if (Elements.btnClearStaysSearch) Elements.btnClearStaysSearch.style.display = "block";
        State.staysSearchQuery = chip.name;
        filterAndRenderStays();
      });
      container.appendChild(btn);
    });
  } catch (err) {
    console.warn("Could not load popular stay destinations:", err);
  }
}

function filterAndRenderStays() {
  let list = State.stays || [];
  const q = (State.staysSearchQuery || "").toLowerCase().trim();
  const typeFilter = State.staysFilterType || "all";
  const priceFilter = State.staysFilterPrice || "all";
  const sortBy = State.staysFilterSort || "rating";

  // 1. Text Search Filter
  if (q) {
    list = list.filter(s =>
      (s.title || "").toLowerCase().includes(q) ||
      (s.destination || "").toLowerCase().includes(q) ||
      (s.city || "").toLowerCase().includes(q) ||
      (s.country || "").toLowerCase().includes(q) ||
      (s.proximity || "").toLowerCase().includes(q) ||
      (s.amenities || []).some(a => a.toLowerCase().includes(q))
    );
  }

  // 2. Type Filter (hotel, airbnb, hostel)
  if (typeFilter !== "all") {
    list = list.filter(s => (s.type || "").toLowerCase() === typeFilter.toLowerCase());
  }

  // 3. Price Filter
  if (priceFilter === "budget") {
    list = list.filter(s => s.price_per_night_inr < 1500);
  } else if (priceFilter === "mid") {
    list = list.filter(s => s.price_per_night_inr >= 1500 && s.price_per_night_inr <= 6000);
  } else if (priceFilter === "premium") {
    list = list.filter(s => s.price_per_night_inr > 6000 && s.price_per_night_inr <= 15000);
  } else if (priceFilter === "luxury") {
    list = list.filter(s => s.price_per_night_inr > 15000);
  }

  // 4. Sort
  if (sortBy === "rating") {
    list.sort((a, b) => (b.rating || 0) - (a.rating || 0));
  } else if (sortBy === "price_asc") {
    list.sort((a, b) => a.price_per_night_inr - b.price_per_night_inr);
  } else if (sortBy === "price_desc") {
    list.sort((a, b) => b.price_per_night_inr - a.price_per_night_inr);
  } else if (sortBy === "reviews") {
    list.sort((a, b) => (b.reviews_count || 0) - (a.reviews_count || 0));
  }

  renderStaysCardsGrid(list);

  if (Elements.staysCountPill) {
    Elements.staysCountPill.textContent = `Showing ${list.length} stay${list.length === 1 ? '' : 's'}`;
  }
}

function renderStaysCardsGrid(stays) {
  const grid = Elements.staysCardsGrid;
  if (!grid) return;
  grid.innerHTML = "";

  if (!stays || stays.length === 0) {
    grid.innerHTML = `
      <div class="explore-empty" style="grid-column: 1 / -1; padding: 4rem 2rem;">
        <div class="explore-empty-icon">🏨</div>
        <h3>No lodging stays match your search</h3>
        <p style="color: var(--text-muted); margin-top: 0.5rem;">Try relaxing your filters or typing another city (e.g. Goa, Jaipur, Rishikesh, Tokyo, Paris).</p>
        <button class="btn btn-secondary btn-sm" style="margin-top: 1rem;" onclick="resetStaysFilters()">Reset Stay Filters</button>
      </div>
    `;
    return;
  }

  stays.forEach(stay => {
    const card = document.createElement("div");
    card.className = "stay-card";
    card.dataset.stayId = stay.id;

    let typeBadgeClass = "badge-type-hotel";
    let typeIcon = "🏨";
    let typeLabel = "Hotel";
    if (stay.type === "airbnb") {
      typeBadgeClass = "badge-type-airbnb";
      typeIcon = "🏡";
      typeLabel = "Airbnb Villa";
    } else if (stay.type === "hostel") {
      typeBadgeClass = "badge-type-hostel";
      typeIcon = "🎒";
      typeLabel = "Hostel / Pods";
    }

    const formattedPrice = formatWorldBudgetCurrency(stay.price_per_night_inr);

    const topAmenities = (stay.amenities || []).slice(0, 3).map(a => `<span class="stay-amenity-tag">${a}</span>`).join("");

    card.innerHTML = `
      <div class="stay-card-thumb-wrap" style="cursor: pointer;">
        <img src="${stay.image}" alt="${stay.title}" class="stay-card-thumb" loading="lazy" />
        <span class="stay-card-type-badge ${typeBadgeClass}">
          ${typeIcon} ${typeLabel}
        </span>
        ${stay.is_superhost ? `<span class="stay-card-superhost-badge">🏆 Superhost</span>` : ''}
      </div>
      <div class="stay-card-body">
        <div class="stay-card-meta-row">
          <div class="stay-rating">
            <span>★</span>
            <span>${stay.rating.toFixed(2)}</span>
            <span class="stay-review-count">(${stay.reviews_count.toLocaleString()})</span>
          </div>
          <span class="stay-location-tag">${stay.city}, ${stay.country}</span>
        </div>
        <h3 class="stay-card-title" title="${stay.title}">${stay.title}</h3>
        <p class="stay-card-proximity" title="${stay.proximity}">${stay.proximity}</p>
        <div class="stay-amenities-tags">
          ${topAmenities}
        </div>
        <div class="stay-card-footer">
          <div class="stay-price-wrap">
            <span class="stay-price-figure">${formattedPrice}</span>
            <span class="stay-price-unit">per night</span>
          </div>
          <div class="stay-card-actions">
            <button type="button" class="btn-stay-details" data-action="details">Details</button>
            <button type="button" class="btn-stay-reserve" data-action="reserve">Reserve</button>
          </div>
        </div>
      </div>
    `;

    card.querySelector('[data-action="details"]')?.addEventListener("click", () => openStayDetailModal(stay));
    card.querySelector('[data-action="reserve"]')?.addEventListener("click", () => openStayDetailModal(stay));
    card.querySelector(".stay-card-thumb-wrap")?.addEventListener("click", () => openStayDetailModal(stay));

    grid.appendChild(card);
  });
}

function openStayDetailModal(stay) {
  State.activeStayItem = stay;

  if (Elements.smodalCategory) Elements.smodalCategory.textContent = stay.category_label || stay.type;
  if (Elements.smodalTitle) Elements.smodalTitle.textContent = stay.title;
  if (Elements.smodalLocation) Elements.smodalLocation.textContent = `📍 ${stay.destination} • ${stay.country}`;
  if (Elements.smodalCoverImg) Elements.smodalCoverImg.src = stay.image;
  if (Elements.smodalPriceDisplay) Elements.smodalPriceDisplay.textContent = formatWorldBudgetCurrency(stay.price_per_night_inr);
  if (Elements.smodalRating) Elements.smodalRating.textContent = stay.rating.toFixed(2);
  if (Elements.smodalReviews) Elements.smodalReviews.textContent = `(${stay.reviews_count.toLocaleString()} reviews)`;
  if (Elements.smodalSuperhost) Elements.smodalSuperhost.style.display = stay.is_superhost ? "inline-block" : "none";
  if (Elements.smodalProximity) Elements.smodalProximity.textContent = stay.proximity;
  if (Elements.smodalOverview) Elements.smodalOverview.textContent = stay.overview;
  if (Elements.smodalRoomType) Elements.smodalRoomType.textContent = stay.room_type || "Deluxe Suite";
  if (Elements.smodalMaxGuests) Elements.smodalMaxGuests.textContent = `Up to ${stay.max_guests || 2} Guests`;
  if (Elements.smodalCancellation) Elements.smodalCancellation.textContent = stay.cancellation_policy || "Flexible cancellation";
  if (Elements.smodalAddress) Elements.smodalAddress.textContent = stay.address;

  if (Elements.smodalAmenitiesList) {
    Elements.smodalAmenitiesList.innerHTML = (stay.amenities || [])
      .map(a => `<div class="smodal-amenity-item">${a}</div>`)
      .join("");
  }

  openModal(Elements.modalStayDetail);
}

function resetStaysFilters() {
  State.staysSearchQuery = "";
  State.staysFilterType = "all";
  State.staysFilterPrice = "all";
  State.staysFilterSort = "rating";

  if (Elements.staysSearchInput) Elements.staysSearchInput.value = "";
  if (Elements.btnClearStaysSearch) Elements.btnClearStaysSearch.style.display = "none";
  if (Elements.staysPriceFilter) Elements.staysPriceFilter.value = "all";
  if (Elements.staysSortSelect) Elements.staysSortSelect.value = "rating";

  document.querySelectorAll(".stays-type-tab").forEach(t => {
    if (t.dataset.type === "all") t.classList.add("active");
    else t.classList.remove("active");
  });

  document.querySelectorAll("#stays-filter-type-pills .chip").forEach(p => {
    if (p.dataset.filterType === "all") p.classList.add("active");
    else p.classList.remove("active");
  });

  document.querySelectorAll(".stay-pop-chip").forEach((c, idx) => {
    if (idx === 0) c.classList.add("active");
    else c.classList.remove("active");
  });

  filterAndRenderStays();
}
window.resetStaysFilters = resetStaysFilters;

async function handleInstantBookStay(stay) {
  if (!stay) stay = State.activeStayItem;
  if (!stay) return;

  const btn = Elements.btnSmodalInstantBook;
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = `<span class="btn-icon">⏳</span><span>Confirming Reservation...</span>`;
  }

  const ci = Elements.staysCheckinDate?.value || (new Date(Date.now() + 7 * 86400000)).toISOString().split("T")[0];
  const co = Elements.staysCheckoutDate?.value || (new Date(Date.now() + 9 * 86400000)).toISOString().split("T")[0];

  try {
    const res = await fetch(`/api/stays/${stay.id}/book`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        guest_name: State.currentUser ? State.currentUser.full_name : "Valued Traveler",
        guest_email: State.currentUser ? State.currentUser.email : "traveler@example.com",
        check_in: ci,
        check_out: co,
        guests_count: 2,
        rooms_count: 1
      })
    });

    if (!res.ok) throw new Error("Booking failed");
    const voucher = await res.json();
    State.latestBookingVoucher = voucher;

    closeModal(Elements.modalStayDetail);
    openBookingVoucherModal(voucher);
    showToast(`🎉 Reservation confirmed for ${stay.title}!`, "success");

  } catch (err) {
    console.error("Instant booking error:", err);
    showToast("Could not complete reservation. Please try again.", "error");
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = `<span class="btn-icon">⚡</span><span>Instant Reserve</span>`;
    }
  }
}

function openBookingVoucherModal(voucher) {
  if (!voucher) return;

  if (Elements.voucherCodeVal) Elements.voucherCodeVal.textContent = voucher.voucher_code;
  if (Elements.voucherStayName) Elements.voucherStayName.textContent = voucher.stay_title;
  if (Elements.voucherStayDest) Elements.voucherStayDest.textContent = `${voucher.destination} • ${voucher.category_label}`;
  if (Elements.voucherGuestName) Elements.voucherGuestName.textContent = voucher.guest_name;
  if (Elements.voucherGuestsCount) Elements.voucherGuestsCount.textContent = `${voucher.guests_count} Guests (${voucher.rooms_count} Room)`;
  if (Elements.voucherCheckin) Elements.voucherCheckin.textContent = `${voucher.check_in} (02:00 PM)`;
  if (Elements.voucherCheckout) Elements.voucherCheckout.textContent = `${voucher.check_out} (11:00 AM)`;
  if (Elements.voucherRateLabel) Elements.voucherRateLabel.textContent = `₹${voucher.price_per_night.toLocaleString()} × ${voucher.nights} night${voucher.nights > 1 ? 's' : ''}`;
  if (Elements.voucherSubtotal) Elements.voucherSubtotal.textContent = `₹${voucher.subtotal.toLocaleString()}`;
  if (Elements.voucherTaxes) Elements.voucherTaxes.textContent = `₹${voucher.taxes.toLocaleString()}`;
  if (Elements.voucherTotal) Elements.voucherTotal.textContent = `₹${voucher.total_amount.toLocaleString()}`;

  openModal(Elements.modalBookingVoucher);
}

async function handleAddStayToActiveTrip(stay) {
  if (!stay) stay = State.activeStayItem;
  if (!stay) return;

  if (!State.activeTrip) {
    showToast("Please select an active trip first to attach this stay", "warning");
    return;
  }

  const ci = Elements.staysCheckinDate?.value || State.activeTrip.start_date;
  const co = Elements.staysCheckoutDate?.value || State.activeTrip.end_date;

  try {
    const res = await fetch(`/api/stays/${stay.id}/add-to-trip`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        trip_id: State.activeTrip.id,
        check_in: ci,
        check_out: co,
        guests_count: 2
      })
    });

    if (!res.ok) throw new Error("Failed to attach stay");
    const result = await res.json();

    closeModal(Elements.modalStayDetail);
    closeModal(Elements.modalBookingVoucher);

    showToast(`🏨 Added ${stay.title} (₹${result.total_cost.toLocaleString()}) to ${State.activeTrip.title}!`, "success");

    // Refresh active trip to reflect updated expense
    await loadTripDetails(State.activeTrip.id);

  } catch (err) {
    console.error("Add stay to trip error:", err);
    showToast("Could not attach stay to active trip", "error");
  }
}

function initStaysModule() {
  // Set default dates if empty: Checkin = 14 days ahead, Checkout = 16 days ahead
  if (Elements.staysCheckinDate && !Elements.staysCheckinDate.value) {
    const d1 = new Date();
    d1.setDate(d1.getDate() + 14);
    Elements.staysCheckinDate.value = d1.toISOString().split("T")[0];
  }
  if (Elements.staysCheckoutDate && !Elements.staysCheckoutDate.value) {
    const d2 = new Date();
    d2.setDate(d2.getDate() + 16);
    Elements.staysCheckoutDate.value = d2.toISOString().split("T")[0];
  }

  // Type Selector Tabs (Hero)
  Elements.staysTypeTabs?.addEventListener("click", (e) => {
    const tab = e.target.closest(".stays-type-tab");
    if (!tab) return;
    const type = tab.dataset.type;
    State.staysFilterType = type;

    document.querySelectorAll(".stays-type-tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");

    // Sync toolbar pills
    document.querySelectorAll("#stays-filter-type-pills .chip").forEach(p => {
      if (p.dataset.filterType === type) p.classList.add("active");
      else p.classList.remove("active");
    });

    filterAndRenderStays();
  });

  // Type Filter Pills (Toolbar)
  Elements.staysFilterTypePills?.addEventListener("click", (e) => {
    const pill = e.target.closest(".chip");
    if (!pill) return;
    const type = pill.dataset.filterType;
    State.staysFilterType = type;

    document.querySelectorAll("#stays-filter-type-pills .chip").forEach(p => p.classList.remove("active"));
    pill.classList.add("active");

    // Sync hero tabs
    document.querySelectorAll(".stays-type-tab").forEach(t => {
      if (t.dataset.type === type) t.classList.add("active");
      else t.classList.remove("active");
    });

    filterAndRenderStays();
  });

  // Search input & clear button
  Elements.staysSearchInput?.addEventListener("input", (e) => {
    State.staysSearchQuery = e.target.value.trim();
    if (Elements.btnClearStaysSearch) {
      Elements.btnClearStaysSearch.style.display = State.staysSearchQuery ? "block" : "none";
    }
    filterAndRenderStays();
  });

  Elements.btnClearStaysSearch?.addEventListener("click", () => {
    if (Elements.staysSearchInput) Elements.staysSearchInput.value = "";
    Elements.btnClearStaysSearch.style.display = "none";
    State.staysSearchQuery = "";
    filterAndRenderStays();
  });

  // Search button
  Elements.btnSearchStays?.addEventListener("click", () => {
    if (Elements.staysSearchInput) {
      State.staysSearchQuery = Elements.staysSearchInput.value.trim();
    }
    filterAndRenderStays();
    const toolbar = document.querySelector(".stays-toolbar-wrap");
    if (toolbar) toolbar.scrollIntoView({ behavior: "smooth" });
  });

  // Manage Bookings link -> jump to active trip or explore
  Elements.btnStaysManageBookings?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView(State.activeTrip.id);
      // Switch to budget tab
      const budgetTabBtn = document.querySelector('.tab-button[data-tab="budget"]');
      budgetTabBtn?.click();
    } else {
      showToast("Select or create a trip to manage your bookings", "info");
    }
  });

  // Price and Sort filters
  Elements.staysPriceFilter?.addEventListener("change", (e) => {
    State.staysFilterPrice = e.target.value;
    filterAndRenderStays();
  });

  Elements.staysSortSelect?.addEventListener("change", (e) => {
    State.staysFilterSort = e.target.value;
    filterAndRenderStays();
  });

  // Modal actions
  Elements.btnSmodalClose?.addEventListener("click", () => closeModal(Elements.modalStayDetail));
  Elements.btnSmodalCloseFoot?.addEventListener("click", () => closeModal(Elements.modalStayDetail));
  Elements.btnSmodalInstantBook?.addEventListener("click", () => handleInstantBookStay(State.activeStayItem));
  Elements.btnSmodalAddTrip?.addEventListener("click", () => handleAddStayToActiveTrip(State.activeStayItem));

  Elements.btnVoucherClose?.addEventListener("click", () => closeModal(Elements.modalBookingVoucher));
  Elements.btnVoucherDone?.addEventListener("click", () => closeModal(Elements.modalBookingVoucher));
  Elements.btnVoucherAddExpense?.addEventListener("click", () => handleAddStayToActiveTrip(State.activeStayItem));

  // Preload stays catalog in background
  loadStays();
}

// ===========================================================================
// AUTHENTICATION & USER PROFILE MODULE
// ===========================================================================

function initAuthModule() {
  // Trigger auth modal
  Elements.btnOpenAuth?.addEventListener("click", () => openAuthModal("signin"));

  // Tab switching
  Elements.tabBtnSignin?.addEventListener("click", () => switchAuthTab("signin"));
  Elements.tabBtnSignup?.addEventListener("click", () => switchAuthTab("signup"));
  Elements.linkSwitchToSignup?.addEventListener("click", () => switchAuthTab("signup"));
  Elements.linkSwitchToSignin?.addEventListener("click", () => switchAuthTab("signin"));

  // Close buttons
  Elements.btnAuthModalClose?.addEventListener("click", () => closeModal(Elements.modalAuth));
  Elements.btnProfileModalClose?.addEventListener("click", () => closeModal(Elements.modalUserProfile));
  Elements.btnProfileCancel?.addEventListener("click", () => closeModal(Elements.modalUserProfile));

  // Password visibility peeks
  Elements.btnPeekSigninPwd?.addEventListener("click", () => {
    togglePasswordPeek(Elements.signinPassword, Elements.btnPeekSigninPwd);
  });
  Elements.btnPeekSignupPwd?.addEventListener("click", () => {
    togglePasswordPeek(Elements.signupPassword, Elements.btnPeekSignupPwd);
  });

  // Real-time password strength meter
  Elements.signupPassword?.addEventListener("input", (e) => {
    updatePasswordStrength(e.target.value);
  });

  // 1-Click Demo Login
  Elements.btnDemoLogin?.addEventListener("click", handleDemoLogin);

  // Form submits
  Elements.formSignin?.addEventListener("submit", handleSignIn);
  Elements.formSignup?.addEventListener("submit", handleSignUp);
  Elements.formEditProfile?.addEventListener("submit", handleSaveProfile);

  // Forgot password tip
  Elements.btnForgotPassword?.addEventListener("click", () => {
    showToast("Password reset instructions have been sent to your email.", "info");
  });

  // User Dropdown toggle in nav
  Elements.btnUserDropdownToggle?.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleUserDropdown();
  });

  // Close dropdown when clicking outside
  document.addEventListener("click", (e) => {
    if (Elements.userDropdownMenu && Elements.userDropdownMenu.style.display !== "none") {
      if (!Elements.userNavProfile?.contains(e.target)) {
        Elements.userDropdownMenu.style.display = "none";
      }
    }
  });

  // Dropdown options
  Elements.btnDropdownProfile?.addEventListener("click", () => {
    if (Elements.userDropdownMenu) Elements.userDropdownMenu.style.display = "none";
    openUserProfileModal();
  });

  Elements.btnDropdownStays?.addEventListener("click", () => {
    if (Elements.userDropdownMenu) Elements.userDropdownMenu.style.display = "none";
    showStaysView();
  });

  Elements.btnDropdownTrips?.addEventListener("click", () => {
    if (Elements.userDropdownMenu) Elements.userDropdownMenu.style.display = "none";
    showExploreView();
  });

  Elements.btnDropdownLogout?.addEventListener("click", () => {
    if (Elements.userDropdownMenu) Elements.userDropdownMenu.style.display = "none";
    handleLogout();
  });

  Elements.btnProfileLogout?.addEventListener("click", () => {
    closeModal(Elements.modalUserProfile);
    handleLogout();
  });

  // Validate existing session from localStorage
  checkAuthSession();
}

function openAuthModal(defaultTab = "signin") {
  switchAuthTab(defaultTab);
  clearAuthErrors();
  openModal(Elements.modalAuth);
}

function switchAuthTab(tab) {
  clearAuthErrors();
  if (tab === "signin") {
    Elements.tabBtnSignin?.classList.add("active");
    Elements.tabBtnSignin?.setAttribute("aria-selected", "true");
    Elements.tabBtnSignup?.classList.remove("active");
    Elements.tabBtnSignup?.setAttribute("aria-selected", "false");
    if (Elements.authPanelSignin) Elements.authPanelSignin.style.display = "block";
    if (Elements.authPanelSignup) Elements.authPanelSignup.style.display = "none";
  } else {
    Elements.tabBtnSignup?.classList.add("active");
    Elements.tabBtnSignup?.setAttribute("aria-selected", "true");
    Elements.tabBtnSignin?.classList.remove("active");
    Elements.tabBtnSignin?.setAttribute("aria-selected", "false");
    if (Elements.authPanelSignup) Elements.authPanelSignup.style.display = "block";
    if (Elements.authPanelSignin) Elements.authPanelSignin.style.display = "none";
  }
}

function togglePasswordPeek(inputElem, btnElem) {
  if (!inputElem) return;
  if (inputElem.type === "password") {
    inputElem.type = "text";
    if (btnElem) btnElem.textContent = "🙈";
  } else {
    inputElem.type = "password";
    if (btnElem) btnElem.textContent = "👁️";
  }
}

function updatePasswordStrength(pwd) {
  const container = Elements.pwdStrengthContainer;
  const bar = Elements.pwdStrengthBar;
  const label = Elements.pwdStrengthLabel;
  if (!container || !bar || !label) return;

  if (!pwd) {
    container.style.display = "none";
    bar.className = "pwd-strength-bar";
    return;
  }

  container.style.display = "flex";
  let score = 0;
  if (pwd.length >= 6) score++;
  if (pwd.length >= 9) score++;
  if (/[0-9]/.test(pwd)) score++;
  if (/[^A-Za-z0-9]/.test(pwd)) score++;

  if (score <= 1) {
    bar.className = "pwd-strength-bar weak";
    label.textContent = "Weak";
    label.style.color = "#ef4444";
  } else if (score <= 2) {
    bar.className = "pwd-strength-bar medium";
    label.textContent = "Good";
    label.style.color = "#f59e0b";
  } else {
    bar.className = "pwd-strength-bar strong";
    label.textContent = "Strong";
    label.style.color = "#10b981";
  }
}

function clearAuthErrors() {
  if (Elements.signinErrorBanner) {
    Elements.signinErrorBanner.style.display = "none";
    Elements.signinErrorBanner.textContent = "";
  }
  if (Elements.signupErrorBanner) {
    Elements.signupErrorBanner.style.display = "none";
    Elements.signupErrorBanner.textContent = "";
  }
}

function showAuthError(bannerElem, msg) {
  if (!bannerElem) return;
  bannerElem.textContent = msg;
  bannerElem.style.display = "block";
}

async function handleSignIn(e) {
  e.preventDefault();
  clearAuthErrors();

  const email = Elements.signinEmail?.value.trim();
  const password = Elements.signinPassword?.value;

  if (!email || !password) {
    showAuthError(Elements.signinErrorBanner, "Please provide your email address and password.");
    return;
  }

  const submitBtn = Elements.formSignin?.querySelector("button[type='submit']");
  const origHtml = submitBtn ? submitBtn.innerHTML : "";
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = "<span>Signing In...</span>";
  }

  try {
    const res = await fetch("/api/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Incorrect email or password");
    }

    setAuthSession(data.token, data.user);
    closeModal(Elements.modalAuth);
    showToast(`Welcome back, ${data.user.full_name}! 👋`, "success");
  } catch (err) {
    showAuthError(Elements.signinErrorBanner, err.message);
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = origHtml;
    }
  }
}

async function handleSignUp(e) {
  e.preventDefault();
  clearAuthErrors();

  const full_name = Elements.signupName?.value.trim();
  const email = Elements.signupEmail?.value.trim();
  const password = Elements.signupPassword?.value;
  const currency = Elements.signupCurrency?.value || "INR";
  const phone = Elements.signupPhone?.value.trim() || "";

  if (!full_name || !email || !password) {
    showAuthError(Elements.signupErrorBanner, "Please fill in all required fields.");
    return;
  }

  if (password.length < 6) {
    showAuthError(Elements.signupErrorBanner, "Password must be at least 6 characters.");
    return;
  }

  const submitBtn = Elements.formSignup?.querySelector("button[type='submit']");
  const origHtml = submitBtn ? submitBtn.innerHTML : "";
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerHTML = "<span>Creating Account...</span>";
  }

  try {
    const res = await fetch("/api/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        full_name,
        email,
        password,
        preferred_currency: currency,
        phone
      })
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Registration failed");
    }

    setAuthSession(data.token, data.user);
    closeModal(Elements.modalAuth);
    showToast(`Account created! Welcome to TRAVEL PACE, ${data.user.first_name}! 🎉`, "success");
  } catch (err) {
    showAuthError(Elements.signupErrorBanner, err.message);
  } finally {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerHTML = origHtml;
    }
  }
}

async function handleDemoLogin() {
  const btn = Elements.btnDemoLogin;
  const origHtml = btn ? btn.innerHTML : "";
  if (btn) {
    btn.disabled = true;
    btn.innerHTML = "<span>Logging in...</span>";
  }

  try {
    const res = await fetch("/api/auth/demo-login", {
      method: "POST",
      headers: { "Content-Type": "application/json" }
    });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.detail || "Demo login failed");
    }

    setAuthSession(data.token, data.user);
    closeModal(Elements.modalAuth);
    showToast(`Signed in as demo traveler ${data.user.full_name}! 🚀`, "success");
  } catch (err) {
    showToast(err.message, "error");
  } finally {
    if (btn) {
      btn.disabled = false;
      btn.innerHTML = origHtml;
    }
  }
}

function setAuthSession(token, user) {
  State.authToken = token;
  State.currentUser = user;
  localStorage.setItem("travelpace_auth_token", token);
  localStorage.setItem("travelpace_user", JSON.stringify(user));
  updateAuthNavUI();

  // If user has a preferred currency, sync it
  if (user.preferred_currency && Elements.globalCurrencySelect) {
    Elements.globalCurrencySelect.value = user.preferred_currency;
    State.selectedCurrency = user.preferred_currency;
  }

  // Execute any pending trip planning action queued before login
  if (State.pendingPostAuthAction) {
    const action = State.pendingPostAuthAction;
    State.pendingPostAuthAction = null;
    setTimeout(() => {
      try {
        action();
      } catch (err) {
        console.error("Post-auth action error:", err);
      }
    }, 450);
  }
}

async function checkAuthSession() {
  const token = State.authToken;
  if (!token) {
    updateAuthNavUI();
    return;
  }

  try {
    const res = await fetch("/api/auth/me", {
      headers: { "Authorization": `Bearer ${token}` }
    });
    if (res.ok) {
      const data = await res.json();
      State.currentUser = data.user;
      localStorage.setItem("travelpace_user", JSON.stringify(data.user));
    } else {
      clearAuthSession();
    }
  } catch (err) {
    console.warn("Auth check network error:", err);
  }
  updateAuthNavUI();
}

async function handleLogout() {
  const token = State.authToken;
  if (token) {
    try {
      await fetch("/api/auth/logout", {
        method: "POST",
        headers: { "Authorization": `Bearer ${token}` }
      });
    } catch (e) {}
  }
  clearAuthSession();
  showToast("You have been signed out.", "info");
}

function clearAuthSession() {
  State.authToken = null;
  State.currentUser = null;
  localStorage.removeItem("travelpace_auth_token");
  localStorage.removeItem("travelpace_user");
  updateAuthNavUI();
}

function updateAuthNavUI() {
  const isAuth = !!State.currentUser;
  if (isAuth) {
    if (Elements.btnOpenAuth) Elements.btnOpenAuth.style.display = "none";
    if (Elements.userNavProfile) Elements.userNavProfile.style.display = "block";

    const user = State.currentUser;
    if (Elements.navUserAvatar) Elements.navUserAvatar.textContent = user.initials || "TP";
    if (Elements.navUserName) Elements.navUserName.textContent = user.first_name || user.full_name || "Traveler";
    if (Elements.dropdownUserAvatar) Elements.dropdownUserAvatar.textContent = user.initials || "TP";
    if (Elements.dropdownUserFullname) Elements.dropdownUserFullname.textContent = user.full_name;
    if (Elements.dropdownUserEmail) Elements.dropdownUserEmail.textContent = user.email;
  } else {
    if (Elements.btnOpenAuth) Elements.btnOpenAuth.style.display = "inline-flex";
    if (Elements.userNavProfile) Elements.userNavProfile.style.display = "none";
    if (Elements.userDropdownMenu) Elements.userDropdownMenu.style.display = "none";
  }
}

function toggleUserDropdown() {
  if (!Elements.userDropdownMenu) return;
  const isShown = Elements.userDropdownMenu.style.display === "block";
  Elements.userDropdownMenu.style.display = isShown ? "none" : "block";
}

function openUserProfileModal() {
  const user = State.currentUser;
  if (!user) {
    openAuthModal("signin");
    return;
  }

  if (Elements.profileAvatarLarge) Elements.profileAvatarLarge.textContent = user.initials || "TP";
  if (Elements.profileFullnameDisplay) Elements.profileFullnameDisplay.textContent = user.full_name;
  if (Elements.profileEmailDisplay) Elements.profileEmailDisplay.textContent = user.email;
  if (Elements.profileMemberSince) Elements.profileMemberSince.textContent = `Member since ${user.member_since || 'Sept 2026'}`;
  if (Elements.editProfileName) Elements.editProfileName.value = user.full_name;
  if (Elements.editProfilePhone) Elements.editProfilePhone.value = user.phone || "";
  if (Elements.editProfileCurrency) Elements.editProfileCurrency.value = user.preferred_currency || "INR";

  openModal(Elements.modalUserProfile);
}

async function handleSaveProfile(e) {
  e.preventDefault();
  const token = State.authToken;
  if (!token) return;

  const full_name = Elements.editProfileName?.value.trim();
  const phone = Elements.editProfilePhone?.value.trim();
  const currency = Elements.editProfileCurrency?.value;

  const saveBtn = Elements.btnSaveProfile;
  if (saveBtn) {
    saveBtn.disabled = true;
    saveBtn.textContent = "Saving...";
  }

  try {
    const res = await fetch("/api/auth/profile", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      },
      body: JSON.stringify({
        full_name,
        phone,
        preferred_currency: currency
      })
    });
    const data = await res.json();
    if (!res.ok) throw new Error(data.detail || "Could not update profile");

    State.currentUser = data.user;
    localStorage.setItem("travelpace_user", JSON.stringify(data.user));
    updateAuthNavUI();
    closeModal(Elements.modalUserProfile);
    showToast("Profile settings saved successfully! ✨", "success");
  } catch (err) {
    showToast(err.message, "error");
  } finally {
    if (saveBtn) {
      saveBtn.disabled = false;
      saveBtn.textContent = "Save Changes";
    }
  }
}

// ===========================================================================
// GLOBAL FOOTER (Available on Every Page & View)
// ===========================================================================
function initGlobalFooter() {
  const btnChangeLang = document.getElementById("btn-change-language");
  const modalLang = document.getElementById("modal-language-select");
  const btnCloseLang = document.getElementById("btn-close-language");
  const langOptions = document.querySelectorAll(".lang-option-row");
  const currentLangLabel = document.getElementById("current-lang-label");

  btnChangeLang?.addEventListener("click", () => {
    openModal(modalLang);
  });

  btnCloseLang?.addEventListener("click", () => {
    closeModal(modalLang);
  });

  // Saved language preference
  const savedLang = localStorage.getItem("travelpace_lang") || "en";
  const langMap = {
    en: "English",
    hi: "हिन्दी (Hindi)",
    es: "Español",
    fr: "Français",
    de: "Deutsch"
  };
  if (currentLangLabel && langMap[savedLang]) {
    currentLangLabel.textContent = langMap[savedLang];
  }

  langOptions.forEach(row => {
    const lang = row.dataset.lang;
    const check = row.querySelector(".lang-check");
    if (lang === savedLang) {
      row.classList.add("active");
      if (check) check.style.display = "inline";
    } else {
      row.classList.remove("active");
      if (check) check.style.display = "none";
    }

    row.addEventListener("click", () => {
      langOptions.forEach(r => {
        r.classList.remove("active");
        const c = r.querySelector(".lang-check");
        if (c) c.style.display = "none";
      });
      row.classList.add("active");
      const c = row.querySelector(".lang-check");
      if (c) c.style.display = "inline";

      const selected = row.dataset.lang;
      localStorage.setItem("travelpace_lang", selected);
      if (currentLangLabel && langMap[selected]) {
        currentLangLabel.textContent = langMap[selected];
      }
      closeModal(modalLang);
      showToast(`Display language updated to ${langMap[selected]}! 🌐`, "success");
    });
  });

  // Footer Navigation Links - Strictly Tailored to Travel Pace Features
  document.getElementById("fl-stays")?.addEventListener("click", () => showStaysView());
  document.getElementById("fl-guides")?.addEventListener("click", () => showGuidesView());
  document.getElementById("fl-hire-guide")?.addEventListener("click", () => showGuidesView());
  document.getElementById("fl-dhams")?.addEventListener("click", () => {
    showExploreView();
    const dhamChip = document.querySelector('.explore-filter-chips button[data-filter="Spiritual & Pilgrimage"]');
    if (dhamChip) dhamChip.click();
  });
  document.getElementById("fl-explore")?.addEventListener("click", () => {
    showExploreView();
    const allChip = document.querySelector('.explore-filter-chips button[data-filter="all"]');
    if (allChip) allChip.click();
  });
  document.getElementById("fl-world")?.addEventListener("click", () => showWorldView());
  document.getElementById("fl-budget-calc")?.addEventListener("click", () => {
    showExploreView();
    const calc = document.getElementById("dham-budget-calculator");
    if (calc) calc.scrollIntoView({ behavior: "smooth", block: "center" });
  });
  document.getElementById("fl-transit")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-transport")?.click();
    } else {
      showExploreView();
      showToast("Select any journey above to explore live transit intelligence!", "info");
    }
  });
  document.getElementById("fl-packing")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-packing")?.click();
    } else {
      showExploreView();
      showToast("Select any journey to view its smart packing checklist & live weather!", "info");
    }
  });
  document.getElementById("fl-pace")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("trip-pace-select")?.focus();
    } else {
      showExploreView();
      showToast("Customize travel pace (Relaxed, Moderate, Fast-Paced) inside any journey!", "info");
    }
  });
  document.getElementById("fl-profile")?.addEventListener("click", () => {
    if (State.currentUser) {
      openModal(Elements.modalUserProfile);
    } else {
      openModal(Elements.modalAuth);
    }
  });
  document.getElementById("fl-terms")?.addEventListener("click", () => {
    showToast("Travel Pace: Terms of Service & Privacy Policy are fully encrypted and verified.", "info");
  });

  // Guides & Resources Links
  document.getElementById("fl-planners")?.addEventListener("click", () => {
    if (!checkLoginBeforePlanning(() => openCreateTripModal(), "Please sign in or create an account to start planning your trip!")) {
      return;
    }
    openCreateTripModal();
  });
  document.getElementById("fl-dham-guides")?.addEventListener("click", () => {
    showExploreView();
    const dhamChip = document.querySelector('.explore-filter-chips button[data-filter="Spiritual & Pilgrimage"]');
    if (dhamChip) dhamChip.click();
  });
  document.getElementById("fl-world-guides")?.addEventListener("click", () => showWorldView());
  document.getElementById("fl-weather-guide")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-weather")?.click();
    } else {
      showExploreView();
      showToast("Pick any destination to view real-time weather forecasts!", "info");
    }
  });
  document.getElementById("fl-cost-tracking")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-budget")?.click();
    } else {
      showExploreView();
      const calc = document.getElementById("dham-budget-calculator");
      if (calc) calc.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  });
  document.getElementById("fl-interactive-maps")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-itinerary")?.click();
    } else {
      showExploreView();
      showToast("Open any journey to explore interactive Leaflet route maps!", "info");
    }
  });
  document.getElementById("fl-hacks")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-ai")?.click();
    } else {
      showExploreView();
      showToast("Explore AI Transit & Money Hacks inside any trip itinerary!", "info");
    }
  });
  document.getElementById("fl-darshan")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-ai")?.click();
    } else {
      showExploreView();
      const dhamChip = document.querySelector('.explore-filter-chips button[data-filter="Spiritual & Pilgrimage"]');
      if (dhamChip) dhamChip.click();
    }
  });
  document.getElementById("fl-reviews")?.addEventListener("click", () => {
    if (State.activeTrip) {
      showTripDetailView();
      document.getElementById("tab-btn-feedback")?.click();
    } else {
      showExploreView();
      showToast("Select any trip to view verified traveler reviews and leave feedback!", "info");
    }
  });

  // App Store / Google Play buttons
  document.getElementById("btn-app-store")?.addEventListener("click", () => {
    showToast("📱 Travel Pace iOS app is launching soon on the App Store! Enjoy our responsive Web App right now.", "info");
  });
  document.getElementById("btn-google-play")?.addEventListener("click", () => {
    showToast("📱 Travel Pace Android app is launching soon on Google Play! Enjoy our responsive Web App right now.", "info");
  });

  // Contact Us Modal & Email Copy Handlers
  document.getElementById("fl-contact-us")?.addEventListener("click", () => {
    openModal(Elements.modalContactUs);
  });
  document.getElementById("btn-close-contact-modal")?.addEventListener("click", () => {
    closeModal(Elements.modalContactUs);
  });

  const handleCopyContactEmail = async () => {
    try {
      await navigator.clipboard.writeText("shanu48050@gmail.com");
      showToast("📋 Email copied to clipboard: shanu48050@gmail.com", "success");
    } catch (e) {
      showToast("✉️ Contact email: shanu48050@gmail.com", "info");
    }
  };

  document.getElementById("btn-copy-footer-email")?.addEventListener("click", handleCopyContactEmail);
  document.getElementById("btn-copy-modal-email")?.addEventListener("click", handleCopyContactEmail);

  // Quick inquiry draft form submission in modal
  document.getElementById("form-quick-contact")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const subj = encodeURIComponent(document.getElementById("contact-subject")?.value.trim() || "Travel Pace Inquiry");
    const msg = encodeURIComponent(document.getElementById("contact-body")?.value.trim() || "");
    window.location.href = `mailto:shanu48050@gmail.com?subject=${subj}&body=${msg}`;
    closeModal(Elements.modalContactUs);
    showToast("📨 Launching your email client with your message...", "info");
  });
}

// ===========================================================================
// TRIP COMPLETION & TRAVELER FEEDBACK MODULE
// ===========================================================================
function initTripFeedbackModule() {
  const btnHeroComplete = document.getElementById("btn-hero-complete-trip");
  const btnHeroFeedback = document.getElementById("btn-hero-open-feedback");
  const tabBtnFeedback = document.getElementById("tab-btn-feedback");
  const btnToggleComplete = document.getElementById("btn-toggle-trip-complete-state");
  const formFeedback = document.getElementById("form-trip-feedback");
  const btnEditFeedback = document.getElementById("btn-edit-existing-feedback");
  const btnReopenTrip = document.getElementById("btn-reopen-trip");

  // Open feedback tab
  btnHeroFeedback?.addEventListener("click", () => {
    showTripDetailView();
    tabBtnFeedback?.click();
  });

  // Hero complete toggle
  btnHeroComplete?.addEventListener("click", async () => {
    if (!State.activeTrip) return;
    await toggleTripCompletion(State.activeTrip.id);
  });

  // Toggle complete button in feedback banner
  btnToggleComplete?.addEventListener("click", async () => {
    if (!State.activeTrip) return;
    await toggleTripCompletion(State.activeTrip.id);
  });

  // Reopen trip from verified feedback card
  btnReopenTrip?.addEventListener("click", async () => {
    if (!State.activeTrip) return;
    await toggleTripCompletion(State.activeTrip.id);
  });

  // Edit review
  btnEditFeedback?.addEventListener("click", () => {
    const cardForm = document.getElementById("card-feedback-form");
    const cardDisplay = document.getElementById("card-feedback-display");
    if (cardForm) cardForm.style.display = "block";
    if (cardDisplay) cardDisplay.style.display = "none";
  });

  // 1. Overall Star Rating Widget
  const overallGroup = document.getElementById("rating-group-overall");
  const overallStars = overallGroup?.querySelectorAll(".star-btn");
  const textOverall = document.getElementById("text-rating-overall");
  const ratingCaptions = {
    1: "⭐ Poor (1 / 5)",
    2: "⭐⭐ Fair (2 / 5)",
    3: "⭐⭐⭐ Good (3 / 5)",
    4: "⭐⭐⭐⭐ Very Good (4 / 5)",
    5: "⭐⭐⭐⭐⭐ Exceptional (5 / 5)"
  };

  overallStars?.forEach(btn => {
    const val = parseInt(btn.dataset.val, 10);
    btn.addEventListener("mouseenter", () => {
      overallStars.forEach(b => {
        b.classList.toggle("hover", parseInt(b.dataset.val, 10) <= val);
      });
    });
    btn.addEventListener("mouseleave", () => {
      overallStars.forEach(b => b.classList.remove("hover"));
    });
    btn.addEventListener("click", () => {
      if (overallGroup) overallGroup.dataset.value = val;
      overallStars.forEach(b => {
        b.classList.toggle("active", parseInt(b.dataset.val, 10) <= val);
      });
      if (textOverall) textOverall.textContent = ratingCaptions[val] || `${val}/5`;
    });
  });

  // 2. Category Mini Stars Setup
  ["transit", "stays", "activities", "budget"].forEach(cat => {
    const group = document.getElementById(`rating-group-${cat}`);
    const scoreText = document.getElementById(`score-text-${cat}`);
    const stars = group?.querySelectorAll(".mini-star");
    stars?.forEach(star => {
      const val = parseInt(star.dataset.val, 10);
      star.addEventListener("mouseenter", () => {
        stars.forEach(s => s.classList.toggle("hover", parseInt(s.dataset.val, 10) <= val));
      });
      star.addEventListener("mouseleave", () => {
        stars.forEach(s => s.classList.remove("hover"));
      });
      star.addEventListener("click", () => {
        if (group) group.dataset.value = val;
        stars.forEach(s => s.classList.toggle("active", parseInt(s.dataset.val, 10) <= val));
        if (scoreText) scoreText.textContent = `${val}/5`;
      });
    });
  });

  // 3. Recommendation Chips
  const recChips = document.querySelectorAll(".recommend-chip");
  recChips.forEach(chip => {
    chip.addEventListener("click", () => {
      recChips.forEach(c => c.classList.remove("active"));
      chip.classList.add("active");
    });
  });

  // 4. Highlight Chips toggle
  const hlChips = document.querySelectorAll("#fb-highlights-wrap .chip");
  hlChips.forEach(chip => {
    chip.addEventListener("click", () => {
      chip.classList.toggle("active");
    });
  });

  // 5. Submit Feedback Form
  formFeedback?.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!State.activeTrip) {
      showToast("No active trip selected.", "error");
      return;
    }

    const overallRating = parseInt(overallGroup?.dataset.value || "5", 10);
    const transitRating = parseInt(document.getElementById("rating-group-transit")?.dataset.value || "5", 10);
    const staysRating = parseInt(document.getElementById("rating-group-stays")?.dataset.value || "5", 10);
    const activitiesRating = parseInt(document.getElementById("rating-group-activities")?.dataset.value || "5", 10);
    const budgetRating = parseInt(document.getElementById("rating-group-budget")?.dataset.value || "5", 10);

    const activeRec = document.querySelector(".recommend-chip.active");
    const recommend = activeRec ? activeRec.dataset.recommend : "Highly Recommend";

    const selectedHighlights = Array.from(document.querySelectorAll("#fb-highlights-wrap .chip.active"))
      .map(c => c.dataset.highlight || c.textContent.trim())
      .join(", ");

    const comments = document.getElementById("fb-comments-input")?.value.trim() || "";
    const tips = document.getElementById("fb-tips-input")?.value.trim() || "";
    const travelerName = document.getElementById("fb-traveler-name")?.value.trim() ||
      (State.currentUser ? State.currentUser.full_name : "Sk Shanu");

    const submitBtn = document.getElementById("btn-submit-feedback");
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = "Submitting Review...";
    }

    try {
      const res = await fetch(`/api/trips/${State.activeTrip.id}/feedback`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          rating_overall: overallRating,
          rating_transit: transitRating,
          rating_stays: staysRating,
          rating_activities: activitiesRating,
          rating_budget: budgetRating,
          recommend: recommend,
          best_highlights: selectedHighlights,
          comments: comments,
          tips_for_others: tips,
          traveler_name: travelerName
        })
      });

      if (!res.ok) throw new Error("Failed to submit feedback");
      const feedback = await res.json();

      // Update State activeTrip
      State.activeTrip.is_completed = true;
      State.activeTrip.feedback = feedback;

      // Update UI components
      updateTripCompletionUI(State.activeTrip);
      renderVerifiedFeedbackCard(feedback);

      showToast("🎉 Trip completed and review saved successfully!", "success");
    } catch (err) {
      showToast(err.message, "error");
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<span class="btn-icon">🚀</span><span>Submit Review & Complete Trip</span>';
      }
    }
  });
}

// ---------------------------------------------------------------------------
// Toggle Trip Completion State (Active <-> Completed)
// ---------------------------------------------------------------------------
async function toggleTripCompletion(tripId) {
  try {
    const res = await fetch(`/api/trips/${tripId}/complete`, { method: "POST" });
    if (!res.ok) throw new Error("Could not update trip completion status");
    const updatedTrip = await res.json();

    State.activeTrip = updatedTrip;
    updateTripCompletionUI(updatedTrip);

    if (updatedTrip.is_completed) {
      showToast("🎉 Journey marked as Completed! Please take a moment to leave your feedback.", "success");
      document.getElementById("tab-btn-feedback")?.click();
    } else {
      showToast("🟢 Journey reopened and set to Active.", "info");
    }
  } catch (err) {
    showToast(err.message, "error");
  }
}

// ---------------------------------------------------------------------------
// Update Trip Completion UI Elements
// ---------------------------------------------------------------------------
function updateTripCompletionUI(trip) {
  if (!trip) return;

  const heroStatus = document.getElementById("hero-trip-status");
  const heroCompleteLabel = document.getElementById("btn-hero-complete-label");
  const btnToggleCompleteText = document.getElementById("btn-toggle-complete-text");
  const feedbackHeroBanner = document.getElementById("feedback-hero-banner");
  const fbStatusPill = document.getElementById("fb-status-pill");
  const fbTitleDest = document.getElementById("fb-title-dest");
  const fbTravelerName = document.getElementById("fb-traveler-name");

  if (fbTitleDest) fbTitleDest.textContent = trip.destination || "Destination";
  if (fbTravelerName && !fbTravelerName.value) {
    fbTravelerName.value = State.currentUser ? State.currentUser.full_name : "Sk Shanu";
  }

  const isDone = Boolean(trip.is_completed);

  // Hero Status Badge
  if (heroStatus) {
    if (isDone) {
      heroStatus.className = "badge badge-trip-status badge-status-completed";
      heroStatus.innerHTML = '<span class="status-dot"></span> 🎉 Trip Completed';
    } else {
      heroStatus.className = "badge badge-trip-status badge-status-active";
      heroStatus.innerHTML = '<span class="status-dot"></span> 🟢 Active Journey';
    }
  }

  // Hero Action Button Label
  if (heroCompleteLabel) {
    heroCompleteLabel.textContent = isDone ? "Completed" : "Mark Completed";
  }

  // Banner Action Button Text
  if (btnToggleCompleteText) {
    btnToggleCompleteText.textContent = isDone ? "Reopen Trip (Ongoing)" : "Mark Trip as Completed";
  }

  // Feedback Banner Theme
  if (feedbackHeroBanner) {
    if (isDone) {
      feedbackHeroBanner.className = "feedback-hero-banner trip-completed-celebration";
      if (fbStatusPill) fbStatusPill.textContent = "🎉 Journey Completed";
    } else {
      feedbackHeroBanner.className = "feedback-hero-banner";
      if (fbStatusPill) fbStatusPill.textContent = "Active Journey Review";
    }
  }

  // Feedback Display vs Form Card
  const cardForm = document.getElementById("card-feedback-form");
  const cardDisplay = document.getElementById("card-feedback-display");

  if (trip.feedback) {
    if (cardForm) cardForm.style.display = "none";
    if (cardDisplay) cardDisplay.style.display = "flex";
    renderVerifiedFeedbackCard(trip.feedback);
  } else {
    if (cardForm) cardForm.style.display = "block";
    if (cardDisplay) cardDisplay.style.display = "none";
  }
}

// ---------------------------------------------------------------------------
// Render Verified Traveler Review Card
// ---------------------------------------------------------------------------
function renderVerifiedFeedbackCard(fb) {
  if (!fb) return;

  const cardDisplay = document.getElementById("card-feedback-display");
  if (!cardDisplay) return;

  const dispAvatar = document.getElementById("disp-avatar");
  const dispName = document.getElementById("disp-traveler-name");
  const dispScore = document.getElementById("disp-overall-score");
  const dispStars = document.getElementById("disp-overall-stars");
  const dispRecText = document.getElementById("disp-recommend-text");
  const dispRatingsStrip = document.getElementById("disp-ratings-strip");
  const dispHighlightsTags = document.getElementById("disp-highlights-tags");
  const dispReviewComments = document.getElementById("disp-review-comments");
  const dispReviewTips = document.getElementById("disp-review-tips");
  const dispTipsWrap = document.getElementById("disp-tips-wrap");

  const name = fb.traveler_name || "Traveler";
  if (dispName) dispName.textContent = name;
  if (dispAvatar) {
    const parts = name.split(" ");
    dispAvatar.textContent = parts.length > 1 ? (parts[0][0] + parts[1][0]).toUpperCase() : name.substring(0, 2).toUpperCase();
  }

  const score = fb.rating_overall || 5;
  if (dispScore) dispScore.textContent = `${score}.0`;
  if (dispStars) dispStars.textContent = "★".repeat(score) + "☆".repeat(Math.max(0, 5 - score));

  if (dispRecText) {
    dispRecText.textContent = `${fb.recommend || 'Highly Recommended'} by Traveler`;
  }

  // Category breakdown strip
  if (dispRatingsStrip) {
    dispRatingsStrip.innerHTML = `
      <div class="disp-cat-pill">
        <span>🚆 Transit & Commute</span>
        <span class="disp-cat-score">${fb.rating_transit || 5}/5 ★</span>
      </div>
      <div class="disp-cat-pill">
        <span>🏨 Stays & Accommodation</span>
        <span class="disp-cat-score">${fb.rating_stays || 5}/5 ★</span>
      </div>
      <div class="disp-cat-pill">
        <span>🛕 Sightseeing & Activities</span>
        <span class="disp-cat-score">${fb.rating_activities || 5}/5 ★</span>
      </div>
      <div class="disp-cat-pill">
        <span>💰 Budget & Value</span>
        <span class="disp-cat-score">${fb.rating_budget || 5}/5 ★</span>
      </div>
    `;
  }

  // Highlights tags
  if (dispHighlightsTags) {
    if (fb.best_highlights) {
      const tags = fb.best_highlights.split(",").map(t => t.trim()).filter(Boolean);
      dispHighlightsTags.innerHTML = tags.map(t => `<span class="chip chip-sm active">${t}</span>`).join("");
      document.getElementById("disp-highlights-box")?.style.setProperty("display", "block");
    } else {
      document.getElementById("disp-highlights-box")?.style.setProperty("display", "none");
    }
  }

  // Review comments
  if (dispReviewComments) {
    dispReviewComments.textContent = fb.comments || "No written comments provided.";
  }

  // Tips for others
  if (dispTipsWrap && dispReviewTips) {
    if (fb.tips_for_others) {
      dispReviewTips.textContent = fb.tips_for_others;
      dispTipsWrap.style.display = "block";
    } else {
      dispTipsWrap.style.display = "none";
    }
  }
}

// ---------------------------------------------------------------------------
// Load Trip Feedback from Server (if not loaded)
// ---------------------------------------------------------------------------
async function loadAndRenderTripFeedback(tripId) {
  if (!tripId) return;
  try {
    const res = await fetch(`/api/trips/${tripId}/feedback`);
    if (res.ok) {
      const fb = await res.json();
      if (State.activeTrip) State.activeTrip.feedback = fb;
      updateTripCompletionUI(State.activeTrip);
    }
  } catch (e) {
    // Feedback may not yet exist
  }
}

// ---------------------------------------------------------------------------
// Currency Formatter with Live Multi-Currency Conversion
// ---------------------------------------------------------------------------
function formatConvertedCurrency(amountInInr) {
  if (amountInInr === null || amountInInr === undefined || isNaN(amountInInr)) return "₹0";
  const cur = State.selectedCurrency || "INR";
  let sym = "₹";
  if (window.BudgetModule && typeof window.BudgetModule.getCurrencySymbol === "function") {
    sym = window.BudgetModule.getCurrencySymbol(cur);
  } else {
    const symMap = { INR: "₹", USD: "$", EUR: "€", GBP: "£", JPY: "¥", AUD: "A$", CAD: "C$" };
    sym = symMap[cur] || "₹";
  }

  let converted = Number(amountInInr);
  if (cur === "USD") converted = amountInInr / 84;
  else if (cur === "EUR") converted = amountInInr / 92;
  else if (cur === "GBP") converted = amountInInr / 108;
  else if (cur === "JPY") converted = amountInInr * 1.8;
  else if (cur === "AUD") converted = amountInInr / 55;
  else if (cur === "CAD") converted = amountInInr / 61;

  return `${sym}${Math.round(converted).toLocaleString()}`;
}

// ===========================================================================
// LOCAL TRAVEL GUIDES & DIRECT CONNECTION MODULE
// ===========================================================================

function initGuidesModule() {
  // 1. Specialty / Category Tabs
  const typeTabs = document.getElementById("guides-type-tabs");
  typeTabs?.addEventListener("click", (e) => {
    const tab = e.target.closest(".guides-type-tab");
    if (!tab) return;
    const region = tab.dataset.region;
    State.guidesFilterRegion = region;

    typeTabs.querySelectorAll(".guides-type-tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");

    loadGuidesList();
  });

  // 2. Search Input & Clear Button
  let searchTimer = null;
  Elements.guidesSearchInput?.addEventListener("input", (e) => {
    const val = e.target.value.trim();
    State.guidesFilterSearch = val;
    if (Elements.btnClearGuidesSearch) {
      Elements.btnClearGuidesSearch.style.display = val ? "block" : "none";
    }
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      loadGuidesList();
    }, 280);
  });

  Elements.btnClearGuidesSearch?.addEventListener("click", () => {
    if (Elements.guidesSearchInput) Elements.guidesSearchInput.value = "";
    State.guidesFilterSearch = "";
    if (Elements.btnClearGuidesSearch) Elements.btnClearGuidesSearch.style.display = "none";
    loadGuidesList();
  });

  document.getElementById("btn-search-guides")?.addEventListener("click", () => {
    loadGuidesList();
  });

  // 3. Language Filter
  Elements.guidesLangSelect?.addEventListener("change", (e) => {
    State.guidesFilterLang = e.target.value;
    loadGuidesList();
  });

  // 4. Sort Filter
  Elements.guidesSortSelect?.addEventListener("change", (e) => {
    State.guidesSortBy = e.target.value;
    loadGuidesList();
  });

  // 5. Popular Destination Chips
  const popularChips = document.getElementById("guides-popular-chips");
  popularChips?.addEventListener("click", (e) => {
    const chip = e.target.closest(".chip");
    if (!chip) return;
    const dest = chip.dataset.dest;
    State.guidesFilterDest = dest;

    popularChips.querySelectorAll(".chip").forEach(c => c.classList.remove("active"));
    chip.classList.add("active");

    if (dest !== "all" && Elements.guidesSearchInput) {
      Elements.guidesSearchInput.value = "";
      State.guidesFilterSearch = "";
      if (Elements.btnClearGuidesSearch) Elements.btnClearGuidesSearch.style.display = "none";
    }
    loadGuidesList();
  });

  // 6. Dialog Close Buttons
  document.getElementById("btn-close-guide-chat")?.addEventListener("click", () => {
    closeModal(Elements.modalGuideChat);
  });

  document.getElementById("btn-close-guide-booking")?.addEventListener("click", () => {
    closeModal(Elements.modalGuideBooking);
  });

  document.getElementById("btn-close-voucher")?.addEventListener("click", () => {
    closeModal(Elements.modalGuideVoucher);
  });

  // 7. Direct Chat Form Submission
  document.getElementById("form-guide-chat")?.addEventListener("submit", (e) => {
    e.preventDefault();
    const input = document.getElementById("input-guide-chat-msg");
    const msg = input?.value.trim();
    if (!msg) return;
    input.value = "";
    sendGuideChatMessage(msg);
  });

  // 8. Quick Chat Prompt Chips
  document.getElementById("guide-chat-prompts")?.addEventListener("click", (e) => {
    const chip = e.target.closest(".chat-prompt-chip");
    if (!chip) return;
    const promptText = chip.dataset.prompt;
    if (promptText) {
      sendGuideChatMessage(promptText);
    }
  });

  // 9. Booking Form Submission & Live Calculation
  const formBooking = document.getElementById("form-guide-booking");
  formBooking?.addEventListener("submit", handleGuideInquirySubmit);

  const durationSelect = document.getElementById("booking-duration-type");
  const groupSelect = document.getElementById("booking-group-size");
  [durationSelect, groupSelect].forEach(sel => {
    sel?.addEventListener("change", updateBookingEstimateDisplay);
  });

  // 10. Workspace browse all guides button
  document.getElementById("btn-workspace-browse-all-guides")?.addEventListener("click", () => {
    showGuidesView();
  });
}

// ---------------------------------------------------------------------------
// Fetch & Load Guides List
// ---------------------------------------------------------------------------
async function loadGuidesList() {
  const grid = Elements.guidesCardsGrid;
  if (!grid) return;

  grid.innerHTML = `
    <div style="grid-column: 1/-1; text-align: center; padding: 3rem 1rem; color: #94a3b8;">
      <div class="loading-spinner" style="margin: 0 auto 1rem;"></div>
      <p>Loading verified local guides...</p>
    </div>
  `;

  try {
    const params = new URLSearchParams();
    if (State.guidesFilterSearch) params.set("q", State.guidesFilterSearch);
    if (State.guidesFilterDest && State.guidesFilterDest !== "all") params.set("destination", State.guidesFilterDest);
    if (State.guidesFilterRegion && State.guidesFilterRegion !== "all") params.set("region", State.guidesFilterRegion);
    if (State.guidesFilterLang && State.guidesFilterLang !== "all") params.set("language", State.guidesFilterLang);
    if (State.guidesSortBy) params.set("sort_by", State.guidesSortBy);

    const res = await fetch(`/api/guides?${params.toString()}`);
    if (!res.ok) throw new Error("Failed to load guides directory");
    const guides = await res.json();
    State.guides = guides;

    if (Elements.guidesCountPill) {
      Elements.guidesCountPill.textContent = `Showing ${guides.length} verified guide${guides.length === 1 ? "" : "s"}`;
    }

    renderGuidesGrid(guides);
  } catch (err) {
    console.error("Guides loading error:", err);
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem 1rem; color: #ef4444;">
        <p>⚠️ Unable to load local guides. Please refresh or try again.</p>
      </div>
    `;
  }
}

// ---------------------------------------------------------------------------
// Render Guides Cards Grid
// ---------------------------------------------------------------------------
function renderGuidesGrid(guides) {
  const grid = Elements.guidesCardsGrid;
  if (!grid) return;

  if (!guides || guides.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 4rem 1.5rem; background: rgba(17,24,39,0.5); border: 1px dashed rgba(255,255,255,0.1); border-radius: 16px;">
        <div style="font-size: 2.8rem; margin-bottom: 0.75rem;">🔍</div>
        <h3 style="color: #ffffff; margin-bottom: 0.35rem;">No local guides match your search</h3>
        <p style="color: #94a3b8; max-width: 480px; margin: 0 auto 1.25rem;">Try clearing search keywords or choosing "All Guides" to explore certified experts across all destinations.</p>
        <button type="button" class="btn btn-secondary btn-sm" onclick="resetGuidesFilters()">Reset All Filters</button>
      </div>
    `;
    return;
  }

  grid.innerHTML = "";

  guides.forEach(g => {
    const card = document.createElement("div");
    card.className = "guide-card";
    card.dataset.guideId = g.id;

    // Currency conversion for day rate
    const convertedDay = formatConvertedCurrency(g.rate_per_day);
    const convertedHour = formatConvertedCurrency(g.rate_per_hour);

    const languagesHtml = (g.languages || []).map(l => `<span class="guide-spec-chip">🗣️ ${escapeHtml(l)}</span>`).join("");
    const specialtiesHtml = (g.specialties || []).slice(0, 3).map(s => `<span class="guide-spec-chip">✦ ${escapeHtml(s)}</span>`).join("");

    const waClean = (g.direct_whatsapp || "").replace("+", "").replace(/\s+/g, "");

    card.innerHTML = `
      <div class="guide-card-cover" style="background-image: url('${escapeHtml(g.cover_image || g.avatar)}');">
        <div class="guide-card-cover-overlay"></div>
        <span class="guide-card-dest-badge">📍 ${escapeHtml(g.destination)}</span>
        <span class="guide-card-badge-tag">${escapeHtml(g.badge || "Verified Guide")}</span>
      </div>

      <div class="guide-card-profile-header">
        <div class="guide-card-avatar-wrap">
          <img src="${escapeHtml(g.avatar)}" alt="${escapeHtml(g.name)}" class="guide-card-avatar" loading="lazy" />
          <span class="guide-card-online-dot" title="Online now"></span>
        </div>
        <div class="guide-card-identity">
          <h3 class="guide-card-name">${escapeHtml(g.name)}</h3>
          <div class="guide-card-title">${escapeHtml(g.title)}</div>
        </div>
      </div>

      <div class="guide-card-body">
        <div class="guide-card-rating-row">
          <div class="guide-rating-score">
            <span>⭐</span>
            <strong>${g.rating ? g.rating.toFixed(2) : "4.95"}</strong>
            <span class="guide-reviews-cnt">(${g.reviews_count || 120} reviews)</span>
          </div>
          <span class="guide-exp-pill">${g.experience_years || 10}+ Years Exp</span>
        </div>

        <div class="guide-card-accreditation">
          <span>🛡️</span>
          <span>${escapeHtml(g.accreditation)}</span>
        </div>

        <div class="guide-card-specialties-wrap">
          ${specialtiesHtml}
        </div>

        <div class="guide-card-languages">
          ${languagesHtml}
        </div>

        <p class="guide-card-bio">${escapeHtml(g.bio)}</p>

        <div class="guide-card-pricing-row">
          <div class="guide-price-day">${convertedDay} <span>/ full day</span></div>
          <div class="guide-price-hour">${convertedHour} / hr</div>
        </div>
      </div>

      <div class="guide-card-actions">
        <button type="button" class="btn-guide-chat" data-id="${g.id}" title="Direct live chat with ${escapeHtml(g.name)}">
          <span>💬</span>
          <span>Chat</span>
        </button>
        <a href="https://wa.me/${waClean}?text=Hello%20${encodeURIComponent(g.name)},%20I%20found%20your%20profile%20on%20Travel%20Pace%20for%20${encodeURIComponent(g.destination)}.%20Are%20you%20available%20for%20a%20guided%20tour?" target="_blank" rel="noopener noreferrer" class="btn-guide-connect" title="Connect on WhatsApp">
          <span>📱</span>
          <span>WhatsApp</span>
        </a>
        <button type="button" class="btn-guide-hire" data-id="${g.id}" title="Hire ${escapeHtml(g.name)} for your journey">
          <span>📅</span>
          <span>Hire</span>
        </button>
      </div>
    `;

    // Bind action buttons
    card.querySelector(".btn-guide-chat")?.addEventListener("click", () => {
      openGuideChatModal(g.id);
    });

    card.querySelector(".btn-guide-hire")?.addEventListener("click", () => {
      openGuideBookingModal(g.id);
    });

    grid.appendChild(card);
  });
}

function resetGuidesFilters() {
  State.guidesFilterSearch = "";
  State.guidesFilterDest = "all";
  State.guidesFilterRegion = "all";
  State.guidesFilterLang = "all";
  State.guidesSortBy = "rating";

  if (Elements.guidesSearchInput) Elements.guidesSearchInput.value = "";
  if (Elements.guidesLangSelect) Elements.guidesLangSelect.value = "all";
  if (Elements.guidesSortSelect) Elements.guidesSortSelect.value = "rating";

  document.querySelectorAll("#guides-type-tabs .guides-type-tab").forEach((t, i) => {
    if (i === 0) t.classList.add("active");
    else t.classList.remove("active");
  });

  document.querySelectorAll("#guides-popular-chips .chip").forEach((c, i) => {
    if (i === 0) c.classList.add("active");
    else c.classList.remove("active");
  });

  loadGuidesList();
}

// ---------------------------------------------------------------------------
// Direct Interactive Live Chat Modal
// ---------------------------------------------------------------------------
async function openGuideChatModal(guideId) {
  // Login check guard
  if (!checkLoginBeforePlanning(() => openGuideChatModal(guideId), "Please sign in or create an account to chat directly with this local guide!")) {
    return;
  }

  let guide = (State.guides || []).find(g => g.id === guideId) ||
              (State.workspaceGuides || []).find(g => g.id === guideId);

  if (!guide) {
    try {
      const res = await fetch(`/api/guides/${encodeURIComponent(guideId)}`);
      if (res.ok) {
        guide = await res.json();
        if (!State.guides) State.guides = [];
        State.guides.push(guide);
      }
    } catch (e) {
      console.error("Could not load guide details:", e);
    }
  }

  if (!guide) {
    showToast("Guide profile not found", "error");
    return;
  }

  State.activeChatGuide = guide;

  // Header Elements
  const avatar = document.getElementById("chat-guide-avatar");
  const name = document.getElementById("chat-guide-name");
  const badge = document.getElementById("chat-guide-badge");
  const sub = document.getElementById("chat-guide-sub");
  const destBanner = document.getElementById("chat-guide-dest-banner");
  const btnWa = document.getElementById("btn-chat-header-whatsapp");

  if (avatar) avatar.src = guide.avatar;
  if (name) name.textContent = guide.name;
  if (badge) badge.textContent = guide.badge || "Verified Guide";
  if (sub) sub.textContent = `Usually replies within 5 minutes • ${guide.accreditation}`;
  if (destBanner) destBanner.textContent = `Connecting regarding: ${guide.destination} (${guide.country})`;

  if (btnWa) {
    const waClean = (guide.direct_whatsapp || "").replace("+", "").replace(/\s+/g, "");
    btnWa.href = `https://wa.me/${waClean}?text=Hello%20${encodeURIComponent(guide.name)},%20I%20am%20chatting%20with%20you%20via%20Travel%20Pace%20regarding%20${encodeURIComponent(guide.destination)}!`;
  }

  // Restore or initialize chat history
  if (!State.guideChatHistories[guideId] || State.guideChatHistories[guideId].length === 0) {
    const clientName = State.currentUser?.full_name || State.currentUser?.first_name || "Traveler";
    State.guideChatHistories[guideId] = [
      {
        sender: "guide",
        text: `Namaste & Hello ${clientName}! I am ${guide.name}, your verified local guide for ${guide.destination}. How can I assist you in planning your visit?`,
        time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" })
      }
    ];
    saveGuideChatHistories();
  }

  renderGuideChatMessages();
  openModal(Elements.modalGuideChat);

  // Focus input
  setTimeout(() => {
    document.getElementById("input-guide-chat-msg")?.focus();
  }, 150);
}

function renderGuideChatMessages() {
  const thread = document.getElementById("guide-chat-thread");
  if (!thread || !State.activeChatGuide) return;

  const guide = State.activeChatGuide;
  const messages = State.guideChatHistories[guide.id] || [];

  thread.innerHTML = "";

  messages.forEach(m => {
    const row = document.createElement("div");
    row.className = m.sender === "guide" ? "msg-row msg-row-guide" : "msg-row msg-row-client";

    const bubble = document.createElement("div");
    bubble.className = m.sender === "guide" ? "msg-bubble msg-bubble-guide" : "msg-bubble msg-bubble-client";
    bubble.textContent = m.text;

    const time = document.createElement("span");
    time.className = "msg-time";
    time.textContent = m.time || "";

    row.appendChild(bubble);
    row.appendChild(time);
    thread.appendChild(row);
  });

  thread.scrollTop = thread.scrollHeight;
}

async function sendGuideChatMessage(msgText) {
  if (!State.activeChatGuide || !msgText) return;

  const guide = State.activeChatGuide;
  const thread = document.getElementById("guide-chat-thread");
  const nowTime = new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });

  // 1. Append client message
  if (!State.guideChatHistories[guide.id]) State.guideChatHistories[guide.id] = [];
  State.guideChatHistories[guide.id].push({
    sender: "client",
    text: msgText,
    time: nowTime
  });
  saveGuideChatHistories();
  renderGuideChatMessages();

  // 2. Add typing indicator
  const typingIndicator = document.createElement("div");
  typingIndicator.className = "msg-row msg-row-guide";
  typingIndicator.id = "chat-typing-indicator";
  typingIndicator.innerHTML = `
    <div class="msg-bubble msg-bubble-guide" style="font-style: italic; opacity: 0.8; display: flex; align-items: center; gap: 0.5rem;">
      <span class="loading-spinner" style="width: 14px; height: 14px; border-width: 2px;"></span>
      <span>${escapeHtml(guide.name)} is typing...</span>
    </div>
  `;
  thread.appendChild(typingIndicator);
  thread.scrollTop = thread.scrollHeight;

  try {
    const clientName = State.currentUser?.full_name || State.currentUser?.first_name || "Traveler";
    const res = await fetch(`/api/guides/${guide.id}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: msgText,
        traveler_name: clientName
      })
    });

    const typingEl = document.getElementById("chat-typing-indicator");
    if (typingEl) typingEl.remove();

    if (!res.ok) throw new Error("Failed to get response from guide");
    const data = await res.json();

    State.guideChatHistories[guide.id].push({
      sender: "guide",
      text: data.reply,
      time: data.timestamp || nowTime
    });
    saveGuideChatHistories();
    renderGuideChatMessages();
  } catch (err) {
    const typingEl = document.getElementById("chat-typing-indicator");
    State.guideChatHistories[guide.id].push({
      sender: "guide",
      text: `Thank you for your message! You can also connect with me directly on WhatsApp at ${guide.direct_phone} so we can coordinate your tour dates without delay.`,
      time: nowTime
    });
    saveGuideChatHistories();
    renderGuideChatMessages();
  }
}

function saveGuideChatHistories() {
  try {
    localStorage.setItem("travelpace_guide_chats", JSON.stringify(State.guideChatHistories));
  } catch (e) {
    console.error("Storage error:", e);
  }
}

// ---------------------------------------------------------------------------
// Direct Guide Booking & Inquiry Modal
// ---------------------------------------------------------------------------
async function openGuideBookingModal(guideId) {
  // Login check guard
  if (!checkLoginBeforePlanning(() => openGuideBookingModal(guideId), "Please sign in or create an account to book or hire this local guide!")) {
    return;
  }

  let guide = (State.guides || []).find(g => g.id === guideId) ||
              (State.workspaceGuides || []).find(g => g.id === guideId);

  if (!guide) {
    try {
      const res = await fetch(`/api/guides/${encodeURIComponent(guideId)}`);
      if (res.ok) {
        guide = await res.json();
        if (!State.guides) State.guides = [];
        State.guides.push(guide);
      }
    } catch (e) {
      console.error("Could not load guide details:", e);
    }
  }

  if (!guide) {
    showToast("Guide profile not found", "error");
    return;
  }

  State.activeBookingGuide = guide;

  // Populate Guide Card Summary
  const avatar = document.getElementById("booking-guide-avatar");
  const name = document.getElementById("booking-guide-name");
  const dest = document.getElementById("booking-guide-dest");
  const title = document.getElementById("booking-guide-title");
  const rate = document.getElementById("booking-guide-rate");
  const guideIdInput = document.getElementById("booking-guide-id");

  if (avatar) avatar.src = guide.avatar;
  if (name) name.textContent = guide.name;
  if (dest) dest.textContent = guide.destination;
  if (title) title.textContent = `${guide.title} • ${guide.accreditation}`;
  if (rate) rate.textContent = `${formatConvertedCurrency(guide.rate_per_day)} / day`;
  if (guideIdInput) guideIdInput.value = guide.id;

  // Pre-fill user info
  const clientPhone = document.getElementById("booking-client-phone");
  if (clientPhone && State.currentUser?.phone) {
    clientPhone.value = State.currentUser.phone;
  }

  // Pre-fill default tour date (tomorrow or active trip start date)
  const dateInput = document.getElementById("booking-tour-date");
  if (dateInput) {
    if (State.activeTrip?.start_date) {
      dateInput.value = State.activeTrip.start_date;
    } else {
      const tomorrow = new Date();
      tomorrow.setDate(tomorrow.getDate() + 1);
      dateInput.value = tomorrow.toISOString().split("T")[0];
    }
  }

  // Direct 1-Click Action Buttons
  const btnWa = document.getElementById("btn-guide-whatsapp-direct");
  const btnPhone = document.getElementById("btn-guide-phone-direct");

  const waClean = (guide.direct_whatsapp || "").replace("+", "").replace(/\s+/g, "");
  const phoneClean = (guide.direct_phone || "").replace(/\s+/g, "");

  if (btnWa) {
    btnWa.href = `https://wa.me/${waClean}?text=Hello%20${encodeURIComponent(guide.name)},%20I%20am%20interested%20in%20hiring%20you%20as%20my%20local%20guide%20in%20${encodeURIComponent(guide.destination)}%20via%20Travel%20Pace.`;
  }
  if (btnPhone) {
    btnPhone.href = `tel:${phoneClean}`;
  }

  updateBookingEstimateDisplay();
  openModal(Elements.modalGuideBooking);
}

function updateBookingEstimateDisplay() {
  const guide = State.activeBookingGuide;
  if (!guide) return;

  const durationType = document.getElementById("booking-duration-type")?.value || "full_day";
  const groupSize = parseInt(document.getElementById("booking-group-size")?.value || "1", 10);

  let baseRate = durationType === "full_day" ? guide.rate_per_day : Math.round(guide.rate_per_day * 0.6);
  if (groupSize > 4) baseRate += Math.round(baseRate * 0.25);

  const estEl = document.getElementById("booking-estimated-fee");
  if (estEl) {
    estEl.textContent = formatConvertedCurrency(baseRate);
  }
}

async function handleGuideInquirySubmit(e) {
  e.preventDefault();

  const guide = State.activeBookingGuide;
  if (!guide) return;

  const tourDate = document.getElementById("booking-tour-date")?.value;
  const durationType = document.getElementById("booking-duration-type")?.value || "full_day";
  const groupSize = parseInt(document.getElementById("booking-group-size")?.value || "1", 10);
  const clientPhone = document.getElementById("booking-client-phone")?.value.trim();
  const specialNotes = document.getElementById("booking-client-notes")?.value.trim();

  if (!tourDate) {
    showToast("Please select a tour date", "error");
    return;
  }

  const btnSubmit = document.getElementById("btn-submit-guide-booking");
  const origText = btnSubmit ? btnSubmit.innerHTML : "";
  if (btnSubmit) {
    btnSubmit.disabled = true;
    btnSubmit.innerHTML = `<span class="loading-spinner" style="width: 16px; height: 16px;"></span> Dispatching Inquiry...`;
  }

  try {
    const clientName = State.currentUser?.full_name || State.currentUser?.first_name || "Valued Traveler";
    const clientEmail = State.currentUser?.email || "traveler@example.com";

    const res = await fetch(`/api/guides/${guide.id}/inquire`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        client_name: clientName,
        client_email: clientEmail,
        client_phone: clientPhone,
        tour_date: tourDate,
        group_size: groupSize,
        duration_type: durationType,
        special_notes: specialNotes
      })
    });

    if (!res.ok) {
      const errData = await res.json();
      throw new Error(errData.detail || "Failed to submit booking inquiry");
    }

    const voucher = await res.json();

    // Close booking modal
    closeModal(Elements.modalGuideBooking);

    // Populate Voucher Modal
    const vCode = document.getElementById("disp-voucher-code");
    const vGuide = document.getElementById("disp-voucher-guide-name");
    const vDest = document.getElementById("disp-voucher-dest");
    const vDate = document.getElementById("disp-voucher-date");
    const vGroup = document.getElementById("disp-voucher-group");
    const vPhone = document.getElementById("disp-voucher-phone");
    const vFee = document.getElementById("disp-voucher-fee");
    const btnWa = document.getElementById("btn-voucher-open-whatsapp");

    if (vCode) vCode.textContent = voucher.voucher_id;
    if (vGuide) vGuide.textContent = voucher.guide?.name || guide.name;
    if (vDest) vDest.textContent = voucher.guide?.destination || guide.destination;
    if (vDate) vDate.textContent = voucher.booking_details?.tour_date || tourDate;
    if (vGroup) vGroup.textContent = `${voucher.booking_details?.duration_type || 'Full Day'} • ${voucher.booking_details?.group_size || groupSize} Traveler(s)`;
    if (vPhone) vPhone.textContent = voucher.guide?.direct_phone || guide.direct_phone;
    if (vFee) vFee.textContent = formatConvertedCurrency(voucher.booking_details?.estimated_fee || guide.rate_per_day);

    if (btnWa && voucher.direct_connect?.whatsapp_url) {
      btnWa.href = voucher.direct_connect.whatsapp_url;
    }

    // Open Voucher Modal
    openModal(Elements.modalGuideVoucher);
    showToast(`🎉 Guide inquiry voucher ${voucher.voucher_id} generated! Connect with ${guide.name} now.`, "success");
  } catch (err) {
    console.error("Booking error:", err);
    showToast(err.message, "error");
  } finally {
    if (btnSubmit) {
      btnSubmit.disabled = false;
      btnSubmit.innerHTML = origText;
    }
  }
}

// ---------------------------------------------------------------------------
// Load Recommended Guides for Active Trip Workspace
// ---------------------------------------------------------------------------
async function loadWorkspaceGuides(destination) {
  const grid = Elements.workspaceGuidesGrid;
  const destBadge = document.getElementById("workspace-guide-dest-badge");
  const sub = document.getElementById("workspace-guides-sub");

  if (!grid) return;

  const destClean = destination || (State.activeTrip ? State.activeTrip.destination : "India");
  if (destBadge) destBadge.textContent = `Recommended for: ${destClean}`;
  if (sub) sub.textContent = `Connect directly with verified local scholars, temple guides, and historians for ${destClean}.`;

  grid.innerHTML = `
    <div style="grid-column: 1/-1; text-align: center; padding: 2.5rem 1rem; color: #94a3b8;">
      <div class="loading-spinner" style="margin: 0 auto 0.75rem;"></div>
      <p>Finding verified local guides for ${escapeHtml(destClean)}...</p>
    </div>
  `;

  try {
    const res = await fetch(`/api/guides/destination/${encodeURIComponent(destClean)}?limit=4`);
    if (!res.ok) throw new Error("Failed to load guides for destination");
    const guides = await res.json();
    State.workspaceGuides = guides;

    if (!guides || guides.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 2rem; background: rgba(0,0,0,0.25); border-radius: 12px; color: #94a3b8;">
          <p>No dedicated guide found specifically for ${escapeHtml(destClean)}. Browse all guides to find cross-regional specialists.</p>
          <button type="button" class="btn btn-secondary btn-sm" onclick="showGuidesView()">Browse All Guides</button>
        </div>
      `;
      return;
    }

    grid.innerHTML = "";
    guides.forEach(g => {
      const card = document.createElement("div");
      card.className = "guide-card";

      const waClean = (g.direct_whatsapp || "").replace("+", "").replace(/\s+/g, "");

      card.innerHTML = `
        <div class="guide-card-cover" style="height: 90px; background-image: url('${escapeHtml(g.cover_image || g.avatar)}');">
          <div class="guide-card-cover-overlay"></div>
          <span class="guide-card-dest-badge">📍 ${escapeHtml(g.destination)}</span>
          <span class="guide-card-badge-tag">${escapeHtml(g.badge || "Verified Guide")}</span>
        </div>

        <div class="guide-card-profile-header" style="margin-top: -34px;">
          <div class="guide-card-avatar-wrap" style="width: 62px; height: 62px;">
            <img src="${escapeHtml(g.avatar)}" alt="${escapeHtml(g.name)}" class="guide-card-avatar" />
            <span class="guide-card-online-dot"></span>
          </div>
          <div class="guide-card-identity">
            <h4 class="guide-card-name" style="font-size: 1.05rem;">${escapeHtml(g.name)}</h4>
            <div class="guide-card-title">${escapeHtml(g.title)}</div>
          </div>
        </div>

        <div class="guide-card-body" style="padding: 0.85rem 1rem;">
          <div class="guide-card-rating-row" style="padding: 0.4rem 0.65rem;">
            <div class="guide-rating-score">
              <span>⭐</span>
              <strong>${g.rating.toFixed(2)}</strong>
              <span class="guide-reviews-cnt">(${g.reviews_count} reviews)</span>
            </div>
            <span class="guide-exp-pill">${g.experience_years} yrs exp</span>
          </div>

          <div class="guide-card-accreditation" style="font-size: 0.72rem;">
            <span>🛡️</span>
            <span>${escapeHtml(g.accreditation)}</span>
          </div>

          <div class="guide-card-pricing-row" style="padding-top: 0.5rem; margin-top: 0.5rem;">
            <div class="guide-price-day" style="font-size: 1rem;">${formatConvertedCurrency(g.rate_per_day)} <span>/ day</span></div>
            <div class="guide-price-hour">${formatConvertedCurrency(g.rate_per_hour)}/hr</div>
          </div>
        </div>

        <div class="guide-card-actions" style="padding: 0 1rem 1rem;">
          <button type="button" class="btn-guide-chat" data-id="${g.id}">
            <span>💬</span> Chat
          </button>
          <a href="https://wa.me/${waClean}?text=Hello%20${encodeURIComponent(g.name)},%20I%20am%20planning%20my%20trip%20to%20${encodeURIComponent(destClean)}%20on%20Travel%20Pace!" target="_blank" rel="noopener noreferrer" class="btn-guide-connect">
            <span>📱</span> WhatsApp
          </a>
          <button type="button" class="btn-guide-hire" data-id="${g.id}">
            <span>📅</span> Hire
          </button>
        </div>
      `;

      card.querySelector(".btn-guide-chat")?.addEventListener("click", () => {
        openGuideChatModal(g.id);
      });

      card.querySelector(".btn-guide-hire")?.addEventListener("click", () => {
        openGuideBookingModal(g.id);
      });

      grid.appendChild(card);
    });
  } catch (err) {
    console.error("Workspace guides error:", err);
  }
}

// Expose functions globally on window for inline handlers & external modules
window.formatConvertedCurrency = formatConvertedCurrency;
window.resetGuidesFilters = resetGuidesFilters;
window.showGuidesView = showGuidesView;
window.openGuideChatModal = openGuideChatModal;
window.openGuideBookingModal = openGuideBookingModal;
window.loadGuidesList = loadGuidesList;

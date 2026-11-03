import streamlit as st
from datetime import date
import random

# ---------------------------------------------------------
# WaterBuddy - Daily Hydration Companion
# Built for the CRS Python Programming Formative Assessment
# ---------------------------------------------------------

st.set_page_config(
    page_title="WaterBuddy | Hydration Companion",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Suggested targets are taken from the assignment examples.
# They are general project defaults, not personalised medical advice.
AGE_GOALS = {
    "6–12 years (Kids)": 1600,
    "13–18 years (Teens)": 2000,
    "19–50 years (Adults)": 2500,
    "65+ years (Seniors)": 1800,
}

TIPS = [
    "Keep a reusable water bottle where you can easily see it.",
    "Try having a glass of water with your regular meals.",
    "Take a few sips during study or screen breaks.",
    "Refill your bottle when you return to your desk.",
    "Listen to your body's thirst signals throughout the day.",
    "Make water easy to reach when you are travelling.",
]

MESSAGES = [
    (0, "Let's get started! Take your first sip. 🌱", "🙂"),
    (25, "Nice start! You're building a good habit. 💧", "😊"),
    (50, "Great work! You've reached halfway. 🎉", "😄"),
    (75, "Amazing progress! You're getting closer. ⭐", "🤩"),
    (100, "Daily goal reached! Fantastic effort! 🏆", "🐢"),
]


def get_feedback(progress):
    """Return a friendly message and mascot based on goal progress."""
    selected = MESSAGES[0]
    for milestone in MESSAGES:
        if progress >= milestone[0]:
            selected = milestone
    return selected[1], selected[2]


def calculate_progress(total_ml, goal_ml):
    """Calculate remaining intake and percentage of the daily goal."""
    percentage = (total_ml / goal_ml) * 100 if goal_ml > 0 else 0
    remaining = max(goal_ml - total_ml, 0)
    return remaining, percentage


def initialise_state():
    """Set up session values and automatically start a fresh day when needed."""
    today = date.today().isoformat()
    if "tracking_date" not in st.session_state:
        st.session_state.tracking_date = today
    if st.session_state.tracking_date != today:
        st.session_state.tracking_date = today
        st.session_state.total_intake = 0
    if "total_intake" not in st.session_state:
        st.session_state.total_intake = 0
    if "age_group" not in st.session_state:
        st.session_state.age_group = list(AGE_GOALS.keys())[1]
    if "daily_goal" not in st.session_state:
        st.session_state.daily_goal = AGE_GOALS[st.session_state.age_group]
    if "show_reset_confirmation" not in st.session_state:
        st.session_state.show_reset_confirmation = False
    if "custom_amount" not in st.session_state:
        st.session_state.custom_amount = 250


def reset_day():
    st.session_state.total_intake = 0
    st.session_state.show_reset_confirmation = False
    st.toast("Your daily tracker has been reset.", icon="🔄")


initialise_state()

# ----------------------------- Styling -----------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
    html, body, [class*="css"] { font-family: 'Nunito', sans-serif; }
    .stApp {
        background: linear-gradient(145deg, #effcff 0%, #f7fbff 48%, #eaf8ff 100%);
        color: #173b55;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #dff7ff 0%, #eefaff 100%);
    }
    .hero {
        padding: 1.5rem 1.7rem;
        border-radius: 24px;
        background: linear-gradient(115deg, #087eaa, #35b8c9);
        color: white;
        box-shadow: 0 10px 28px rgba(20, 126, 170, .16);
        margin-bottom: 1rem;
    }
    .hero h1 { color: white; margin: 0; font-size: 2.4rem; font-weight: 900; }
    .hero p { color: #e8fbff; margin: .35rem 0 0 0; font-size: 1.05rem; }
    .metric-card {
        background: white; border: 1px solid #d8edf5; border-radius: 18px;
        padding: 1rem 1.15rem; min-height: 112px;
        box-shadow: 0 5px 18px rgba(30, 105, 135, .06);
    }
    .metric-label { color: #648398; font-size: .9rem; font-weight: 700; }
    .metric-value { color: #087eaa; font-size: 1.8rem; font-weight: 900; }
    .mascot-card {
        background: #ffffff; border: 1px solid #d8edf5; border-radius: 20px;
        text-align: center; padding: 1.2rem; height: 100%;
    }
    .mascot { font-size: 4.2rem; line-height: 1.2; }
    .small-note { color: #648398; font-size: .85rem; }
    div.stButton > button {
        border-radius: 12px; border: 0; font-weight: 800;
        background: #0b91b8; color: white; min-height: 2.7rem;
    }
    div.stButton > button:hover { background: #087eaa; color: white; }
    h2, h3 { color: #15506d; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------- Header -----------------------------
st.markdown(
    """
    <div class="hero">
      <h1>💧 WaterBuddy</h1>
      <p>Your friendly daily hydration companion. Small sips, great habits!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------- Sidebar -----------------------------
with st.sidebar:
    st.header("⚙️ Your Settings")
    selected_age = st.selectbox(
        "Select your age group",
        list(AGE_GOALS.keys()),
        index=list(AGE_GOALS.keys()).index(st.session_state.age_group),
        help="Choose the age group that best describes the user.",
    )
    if selected_age != st.session_state.age_group:
        st.session_state.age_group = selected_age
        st.session_state.daily_goal = AGE_GOALS[selected_age]

    standard_goal = AGE_GOALS[selected_age]
    st.caption(f"Suggested target for this project: **{standard_goal:,} ml/day**")
    st.session_state.daily_goal = st.number_input(
        "Your daily goal (ml)",
        min_value=250,
        max_value=6000,
        value=int(st.session_state.daily_goal),
        step=50,
        help="You can adjust the suggested target.",
    )
    st.divider()
    st.subheader("🌿 A little hydration tip")
    st.info(random.choice(TIPS))
    st.caption("WaterBuddy does not require an account. Your tracker runs in this browser session.")

# ----------------------------- Calculations -----------------------------
total = int(st.session_state.total_intake)
goal = int(st.session_state.daily_goal)
remaining, percentage = calculate_progress(total, goal)
progress_for_bar = min(percentage / 100, 1.0)
message, mascot = get_feedback(percentage)

# ----------------------------- Main dashboard -----------------------------
st.subheader("Your Daily Dashboard")
metric1, metric2, metric3 = st.columns(3)
with metric1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">💧 Total water logged</div>'
        f'<div class="metric-value">{total:,} ml</div></div>',
        unsafe_allow_html=True,
    )
with metric2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">🎯 Daily goal</div>'
        f'<div class="metric-value">{goal:,} ml</div></div>',
        unsafe_allow_html=True,
    )
with metric3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">🌊 Still to go</div>'
        f'<div class="metric-value">{remaining:,} ml</div></div>',
        unsafe_allow_html=True,
    )

st.write("")
left, right = st.columns([1.65, 1], gap="large")

with left:
    st.markdown("### 📈 Your progress")
    st.progress(progress_for_bar)
    st.markdown(f"**{percentage:.1f}%** of your selected daily goal")
    if percentage >= 100:
        st.success("You've reached your selected daily goal. Well done!")
    elif percentage >= 75:
        st.success("You're very close. Keep listening to your body!")
    elif percentage >= 50:
        st.info("Halfway there — great progress!")
    elif percentage >= 25:
        st.info("A good start. Keep your water nearby.")
    else:
        st.caption("Your progress will appear here as you log water.")

    st.markdown("### ➕ Log your water")
    quick_cols = st.columns(4)
    for col, amount in zip(quick_cols, [150, 250, 350, 500]):
        with col:
            if st.button(f"+{amount} ml", key=f"quick_{amount}", use_container_width=True):
                st.session_state.total_intake += amount
                st.rerun()

    with st.form("custom_water_form", clear_on_submit=True):
        custom_amount = st.number_input(
            "Or enter another amount (ml)",
            min_value=1,
            max_value=2000,
            value=250,
            step=50,
        )
        submitted = st.form_submit_button("Add water", use_container_width=True)
        if submitted:
            st.session_state.total_intake += int(custom_amount)
            st.toast(f"{int(custom_amount)} ml added!", icon="💧")
            st.rerun()

with right:
    st.markdown("### 🐢 WaterBuddy mascot")
    st.markdown(
        f'<div class="mascot-card"><div class="mascot">{mascot}</div>'
        f'<h3>WaterBuddy says...</h3><p>{message}</p>'
        f'<div class="small-note">Your mascot reacts as your progress changes.</div></div>',
        unsafe_allow_html=True,
    )

# ----------------------------- Optional converter -----------------------------
st.divider()
st.subheader("🥤 Quick Cup Converter")
converter_col1, converter_col2 = st.columns([1, 2])
with converter_col1:
    cups = st.number_input("Number of cups", min_value=0.0, max_value=30.0, value=1.0, step=0.5)
with converter_col2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Approximate water amount (1 cup = 250 ml)</div>'
        f'<div class="metric-value">{cups * 250:,.0f} ml</div></div>',
        unsafe_allow_html=True,
    )

# ----------------------------- Reset -----------------------------
st.divider()
st.subheader("🔄 Start a new day")
st.write("Reset your logged water intake when you want to begin a fresh daily tracker.")
if not st.session_state.show_reset_confirmation:
    if st.button("Reset today's progress", type="secondary"):
        st.session_state.show_reset_confirmation = True
        st.rerun()
else:
    st.warning("Are you sure you want to clear today's water total?")
    confirm_col, cancel_col = st.columns(2)
    with confirm_col:
        if st.button("Yes, reset my day", type="primary", use_container_width=True):
            reset_day()
            st.rerun()
    with cancel_col:
        if st.button("No, keep my progress", use_container_width=True):
            st.session_state.show_reset_confirmation = False
            st.rerun()

st.caption(
    f"Tracking date: {date.today().strftime('%d %B %Y')} · "
    "Suggested goals are classroom project defaults, not medical prescriptions."
)
st.caption("Remember: hydration needs vary. Follow appropriate guidance from a qualified health professional.")

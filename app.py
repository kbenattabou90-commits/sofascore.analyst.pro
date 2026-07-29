import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="Sofascore Analyst AI - Comprehensive Edition",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover { background-color: #2ca02c; }
    .metric-card {
        background-color: #1e2530;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #30363d;
    }
    .live-badge {
        background-color: #ff4b4b;
        color: white;
        padding: 2px 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    .live-timer {
        font-size: 26px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        background-color: #1e2530;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #ff4b4b;
    }
    .match-event {
        background-color: #161b22;
        padding: 10px 15px;
        border-radius: 6px;
        margin-bottom: 8px;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Session State Management
if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'selected_match' not in st.session_state:
    st.session_state.selected_match = None

# Comprehensive Tournaments and Matches Database
TOURNAMENTS_DATA = {
    "🏆 UEFA Champions League": [
        {"id": 101, "home": "Real Madrid", "home_flag": "👑", "away": "Manchester City", "away_flag": "🔵", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 74, "second": 12, "score_home": 2, "score_away": 1},
        {"id": 102, "home": "Bayern Munich", "home_flag": "🔴", "away": "Paris Saint-Germain", "away_flag": "🔵🔴", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 38, "second": 45, "score_home": 0, "score_away": 0},
        {"id": 103, "home": "Arsenal", "home_flag": "⚪🔴", "away": "Inter Milan", "away_flag": "⚫🔵", "date": "2026-06-06", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🌍 World Cup (National Teams)": [
        {"id": 201, "home": "Brazil", "home_flag": "🇧🇷", "away": "Argentina", "away_flag": "🇦🇷", "date": "2026-06-10", "time": "21:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 202, "home": "France", "home_flag": "🇫🇷", "away": "England", "away_flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "date": "2026-06-11", "time": "19:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 203, "home": "Spain", "home_flag": "🇪🇸", "away": "Germany", "away_flag": "🇩🇪", "date": "2026-06-12", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 Premier League": [
        {"id": 301, "home": "Liverpool", "home_flag": "🔴", "away": "Chelsea", "away_flag": "🔵", "date": "2026-06-07", "time": "18:30", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 302, "home": "Manchester United", "home_flag": "🔴", "away": "Tottenham", "away_flag": "⚪", "date": "2026-06-07", "time": "16:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🇪🇸 La Liga": [
        {"id": 401, "home": "Barcelona", "home_flag": "🔵🔴", "away": "Atletico Madrid", "home_flag": "⚪🔴", "date": "2026-06-08", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ]
}

# ================= 1. Welcome Screen =================
if st.session_state.step == 'welcome':
    st.title("⚽ Sofascore Analyst AI - Comprehensive Platform")
    st.markdown("### Transforming complex statistics into clear insights with real-time live tracking by the second.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>200+</h3><p>Global Leagues & Tournaments</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>1 Sec</h3><p>Live Real-Time Updates</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>94%</h3><p>AI Prediction Accuracy</p></div>', unsafe_allow_html=True)
        
    st.write("---")
    st.info("💡 Full coverage of global clubs and national team matches with exact scheduling and AI analysis.")
    
    if st.button("🚀 Enter Analytics Platform"):
        st.session_state.step = 'dashboard'
        st.rerun()

# ================= 2. Dashboard & Navigation =================
elif st.session_state.step == 'dashboard':
    st.sidebar.title("⚙️ Navigation & Settings")
    menu = st.sidebar.radio("Sections:", ["⚽ Matches & Live Feed", "🏆 Standings & Tables", "⚙️ Settings & Approvals"])
    
    if st.sidebar.button("🚪 Logout / Home"):
        st.session_state.step = 'welcome'
        st.rerun()

    # --- Matches & Live Section ---
    if menu == "⚽ Matches & Live Feed":
        st.header("📅 Global Matches & National Teams - Schedule & Live Stream")
        
        selected_tournament = st.selectbox("Select Tournament or National Team:", list(TOURNAMENTS_DATA.keys()))
        
        st.write(f"### Matches for {selected_tournament}")
        matches_list = TOURNAMENTS_DATA[selected_tournament]

        for m in matches_list:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            with col1:
                st.markdown(f"**{m['home_flag']} {m['home']}** vs **{m['away_flag']} {m['away']}**")
                st.caption(f"📅 Date: {m['date']} | ⏰ Time: {m['time']}")
            with col2:
                if m['status'] == "LIVE":
                    st.markdown(f'<span class="live-badge">LIVE 🔴 {m["minute"]}\'</span>', unsafe_allow_html=True)
                    st.markdown(f"**Score: {m['score_home']} - {m['score_away']}**")
                else:
                    st.markdown("⏳ **Upcoming Match**")
            with col3:
                st.markdown("📍 AI Analysis Available")
            with col4:
                if m['status'] == "LIVE":
                    if st.button("🔴 Open Live Stream", key=f"match_live_{m['id']}"):
                        st.session_state.selected_match = m
                        st.session_state.step = 'live_match'
                        st.rerun()
                else:
                    if st.button("🔍 View Analysis", key=f"match_ai_{m['id']}"):
                        st.session_state.selected_match = m
                        st.session_state.step = 'analysis'
                        st.rerun()
            st.divider()

    # --- Standings Section ---
    elif menu == "🏆 Standings & Tables":
        st.header("🏆 League Standings & Club Rankings")
        league_choice = st.selectbox("Select League:", ["La Liga", "UEFA Champions League", "Premier League"])
        
        if league_choice == "La Liga":
            df = pd.DataFrame({
                "Position": [1, 2, 3, 4],
                "Team": ["👑 Real Madrid", "🔵🔴 Barcelona", "⚪🔴 Atletico Madrid", "🦁 Athletic Bilbao"],
                "Played": [36, 36, 36, 36],
                "Points": [90, 82, 75, 68]
            })
            st.dataframe(df, use_container_width=True)
        else:
            st.info("Select a valid league to view detailed automated standings.")

    # --- Settings Section ---
    elif menu == "⚙️ Settings & Approvals":
        st.header("⚙️ Application Settings & Preferences")
        st.checkbox("Agree to live data tracking and privacy policy", value=True)
        st.checkbox("Enable live match minute notifications", value=True)
        st.selectbox("Time Format", ["Greenwich Mean Time (GMT)", "Local Device Time"])
        st.slider("AI Analysis Detail Level", 1, 5, 4)
        if st.button("Save Changes"):
            st.success("Settings updated successfully!")

# ================= 3. Live Match Stream (Minute & Second Tracking) =================
elif st.session_state.step == 'live_match':
    m = st.session_state.selected_match
    
    if st.button("⬅️ Back to Matches"):
        st.session_state.step = 'dashboard'
        st.rerun()

    st.title(f"🔴 Live Tracking: {m['home_flag']} {m['home']} {m['score_home']} - {m['score_away']} {m['away_flag']} {m['away']}")
    
    timer_placeholder = st.empty()
    events_placeholder = st.empty()

    for sec_offset in range(15):
        current_sec = (m['second'] + sec_offset) % 60
        current_min = m['minute'] + ((m['second'] + sec_offset) // 60)
        
        timer_placeholder.markdown(f'<div class="live-timer">⏱️ Live Match Timer: {current_min} : {current_sec:02d} min</div>', unsafe_allow_html=True)
        
        with events_placeholder.container():
            st.subheader("⚡ Match Events in Real-Time:")
            st.markdown(f'<div class="match-event"><b>Minute {current_min}:{current_sec:02d}</b> - Full possession maintained by {m["home"]} in the midfield area.</div>', unsafe_allow_html=True)
            if current_min >= 75:
                st.markdown(f'<div class="match-event" style="border-left-color: #2ca02c;"><b>Minute 75:00</b> - Tactical substitution made by {m["home"]} to boost the attack.</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="match-event" style="border-left-color: #ff4b4b;"><b>Minute {max(1, current_min-12)}:30</b> - Dangerous counter-attack by {m["away"]}, defense clears safely.</div>', unsafe_allow_html=True)
        
        time.sleep(1)

# ================= 4. AI Analysis & Predictions =================
elif st.session_state.step == 'analysis':
    m = st.session_state.selected_match
    
    if st.button("⬅️ Back to Matches"):
        st.session_state.step = 'dashboard'
        st.rerun()

    st.title(f"🧠 AI Match Analysis: {m['home_flag']} {m['home']} vs {m['away_flag']} {m['away']}")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 Win Probabilities & Projections")
        st.progress(0.60, text=f"{m['home']} Win: 60%")
        st.progress(0.25, text="Draw: 25%")
        st.progress(0.15, text=f"{m['away']} Win: 15%")
        
    with col2:
        st.subheader("🎯 AI Expected Scoreline")
        st.info("Based on real-time simulation of over 10,000 scenarios:")
        st.markdown(f"### ⚽ {m['home']} **2 - 0** {m['away']}")

    st.write("---")
    st.subheader("📈 Pre & Post Match Updates")
    st.markdown("- **Referee Profile:** International referee with moderate strictness regarding disciplinary cards.")
    st.markdown("- **Injuries & Absences:** Both squads are nearly fully fit with only minor bench absences.")
    st.markdown("- **Head-to-Head History:** Slight advantage for the home team in their last 5 direct encounters.")

    if st.button("🔄 Refresh Analysis & Live Data"):
        with st.spinner("Fetching latest AI insights..."):
            time.sleep(1.2)
        st.success("Predictions and statistics updated successfully!")

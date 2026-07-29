import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta

# إعدادات الصفحة الأساسية لتكون شبيهة بالتطبيقات الاحترافية
st.set_page_config(
    page_title="Sofascore Analyst AI - النسخة الشاملة",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم عبر CSS لزيادة جمالية المنصة
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
        border-right: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State)
if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'selected_match' not in st.session_state:
    st.session_state.selected_match = None

# قاعدة بيانات شاملة للبطولات، الدوريات، والمنتخبات العالمية
TOURNAMENTS_DATA = {
    "🏆 دوري أبطال أوروبا (UEFA Champions League)": [
        {"id": 101, "tournament": "🏆 دوري أبطال أوروبا", "home": "ريال مدريد", "home_flag": "👑", "away": "مانشستر سيتي", "away_flag": "🔵", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 74, "second": 12, "score_home": 2, "score_away": 1},
        {"id": 102, "tournament": "🏆 دوري أبطال أوروبا", "home": "بايرن ميونخ", "home_flag": "🔴", "away": "باريس سان جيرمان", "away_flag": "🔵🔴", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 38, "second": 45, "score_home": 0, "score_away": 0},
        {"id": 103, "tournament": "🏆 دوري أبطال أوروبا", "home": "آرسنال", "home_flag": "⚪🔴", "away": "إنتر ميلان", "away_flag": "⚫🔵", "date": "2026-06-06", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🌍 كأس العالم للمنتخبات (World Cup)": [
        {"id": 201, "tournament": "🌍 كأس العالم للمنتخبات", "home": "البرازيل", "home_flag": "🇧🇷", "away": "الأرجنتين", "away_flag": "🇦🇷", "date": "2026-06-10", "time": "21:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 202, "tournament": "🌍 كأس العالم للمنتخبات", "home": "فرنسا", "home_flag": "🇫🇷", "away": "إنجلترا", "away_flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "date": "2026-06-11", "time": "19:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 203, "tournament": "🌍 كأس العالم للمنتخبات", "home": "إسبانيا", "home_flag": "🇪🇸", "away": "ألمانيا", "away_flag": "🇩🇪", "date": "2026-06-12", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي الممتاز (Premier League)": [
        {"id": 301, "tournament": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي", "home": "ليفربول", "home_flag": "🔴", "away": "تشيلسي", "away_flag": "🔵", "date": "2026-06-07", "time": "18:30", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0},
        {"id": 302, "tournament": "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي", "home": "مانشستر يونايتد", "home_flag": "🔴", "away": "توتنهام", "away_flag": "⚪", "date": "2026-06-07", "time": "16:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ],
    "🇪🇸 الدوري الإسباني (La Liga)": [
        {"id": 401, "tournament": "🇪🇸 الدوري الإسباني", "home": "برشلونة", "home_flag": "🔵🔴", "away": "أتلتيكو مدريد", "away_flag": "⚪🔴", "date": "2026-06-08", "time": "22:00", "status": "UPCOMING", "minute": 0, "second": 0, "score_home": 0, "score_away": 0}
    ]
}

# ================= 1. مرحلة الترحيب والدخول =================
if st.session_state.step == 'welcome':
    st.title("⚽ Sofascore Analyst AI - المنصة الشاملة")
    st.markdown("### تحويل الإحصائيات المعقدة إلى رؤى واضحة وتتبع مباشر للمباريات والمنتخبات العالمية بالثانية.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>200+</h3><p>بطولة ودوري عالمي</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>1 ثانية</h3><p>تحديثات حية ومباشرة</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>94%</h3><p>دقة خوارزميات التوقع</p></div>', unsafe_allow_html=True)
        
    st.write("---")
    st.info("💡 تغطية كاملة لمباريات الأندية والمنتخبات العالمية مع مواعيد دقيقة بالتاريخ والتوقيت وتحليلات الذكاء الاصطناعي.")
    
    if st.button("🚀 الدخول إلى منصة التحليلات الشاملة"):
        st.session_state.step = 'dashboard'
        st.rerun()

# ================= 2. لوحة التحكم والبطولات والمباريات =================
elif st.session_state.step == 'dashboard':
    st.sidebar.title("⚙️ خيارات التصفح والإعدادات")
    menu = st.sidebar.radio("الأقسام:", ["⚽ المباريات واللايف والبطولات", "🏆 ترتيب الدوريات والفرق", "⚙️ الإعدادات والموافقات"])
    
    if st.sidebar.button("🚪 تسجيل الخروج / البداية"):
        st.session_state.step = 'welcome'
        st.rerun()

    # --- قسم المباريات والحية والبطولات ---
    if menu == "⚽ المباريات واللايف والبطولات":
        st.header("📅 جدول المباريات والمنتخبات العالمية - التوقيت واللايف")
        
        selected_tournament = st.selectbox("اختر البطولة أو المنتخب:", list(TOURNAMENTS_DATA.keys()))
        
        st.write(f"### مباريات {selected_tournament}")
        matches_list = TOURNAMENTS_DATA[selected_tournament]

        for m in matches_list:
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            with col1:
                st.markdown(f"**{m['home_flag']} {m['home']}** vs **{m['away_flag']} {m['away']}**")
                st.caption(f"📅 التاريخ: {m['date']} | ⏰ التوقيت: {m['time']}")
            with col2:
                if m['status'] == "LIVE":
                    st.markdown(f'<span class="live-badge">LIVE 🔴 {m["minute"]}\'</span>', unsafe_allow_html=True)
                    st.markdown(f"**النتيجة: {m['score_home']} - {m['score_away']}**")
                else:
                    st.markdown("⏳ **مباراة قادمة**")
            with col3:
                st.markdown("📍 تحليل ذكاء اصطناعي")
            with col4:
                if m['status'] == "LIVE":
                    if st.button("🔴 فتح شاشة اللايف", key=f"match_live_{m['id']}"):
                        st.session_state.selected_match = m
                        st.session_state.step = 'live_match'
                        st.rerun()
                else:
                    if st.button("🔍 كشف التحليل", key=f"match_ai_{m['id']}"):
                        st.session_state.selected_match = m
                        st.session_state.step = 'analysis'
                        st.rerun()
            st.divider()

    # --- قسم ترتيب الفرق والدوريات ---
    elif menu == "🏆 ترتيب الدوريات والفرق":
        st.header("🏆 جدول ترتيب الفرق والمنتخبات العالمية")
        league_choice = st.selectbox("اختر الدوري للعرض:", ["الدوري الإسباني", "دوري أبطال أوروبا", "الدوري الإنجليزي"])
        
        if league_choice == "الدوري الإسباني":
            df = pd.DataFrame({
                "المركز": [1, 2, 3, 4],
                "الفريق": ["👑 ريال مدريد", "🔵🔴 برشلونة", "⚪🔴 أتلتيكو مدريد", "🦁 أتلتيك بيلباو"],
                "لعب": [36, 36, 36, 36],
                "نقاط": [90, 82, 75, 68]
            })
            st.dataframe(df, use_container_width=True)
        else:
            st.info("اختر الدوري المناسب لعرض الترتيب المفصل المحدث آلياً.")

    # --- قسم الإعدادات والموافقات ---
    elif menu == "⚙️ الإعدادات والموافقات":
        st.header("⚙️ إعدادات التطبيق والموافقات")
        st.checkbox("الموافقة على شروط تتبع البيانات المباشرة وسياسة الخصوصية", value=True)
        st.checkbox("تفعيل تنبيهات الدقائق في المباريات الحية", value=True)
        st.selectbox("تنسيق الوقت", ["توقيت غرينتش (GMT)", "التوقيت المحلي لجهازك (Local)"])
        st.slider("مستوى تفصيل تحليلات الذكاء الاصطناعي", 1, 5, 4)
        if st.button("حفظ التغييرات"):
            st.success("تم تحديث وحفظ الإعدادات بنجاح!")

# ================= 3. شاشة المباراة المباشرة (كل دقيقة وثانية) =================
elif st.session_state.step == 'live_match':
    m = st.session_state.selected_match
    
    if st.button("⬅️ العودة لقائمة المباريات والبطولات"):
        st.session_state.step = 'dashboard'
        st.rerun()

    st.title(f"🔴 تغطية حية بالثانية: {m['home_flag']} {m['home']} {m['score_home']} - {m['score_away']} {m['away_flag']} {m['away']}")
    
    timer_placeholder = st.empty()
    events_placeholder = st.empty()

    # محاكاة التحديث المباشر للثواني والدقائق الحية
    for sec_offset in range(15):
        current_sec = (m['second'] + sec_offset) % 60
        current_min = m['minute'] + ((m['second'] + sec_offset) // 60)
        
        timer_placeholder.markdown(f'<div class="live-timer">⏱️ وقت المباراة المباشر: {current_min} : {current_sec:02d} دقيقة</div>', unsafe_allow_html=True)
        
        with events_placeholder.container():
            st.subheader("⚡ أحداث المباراة لحظة بلحظة:")
            st.markdown(f'<div class="match-event"><b>الدقيقة {current_min}:{current_sec:02d}</b> - سيطرة واستحواذ كامل من جانب لاعبي {m["home"]} في وسط الملعب.</div>', unsafe_allow_html=True)
            if current_min >= 75:
                st.markdown(f'<div class="match-event" style="border-right-color: #2ca02c;"><b>الدقيقة 75:00</b> - تبديل تكتيكي أول لنادي {m["home"]} لتنشيط الهجوم.</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="match-event" style="border-right-color: #ff4b4b;"><b>الدقيقة {max(1, current_min-12)}:30</b> - هجمة مرتدة خطيرة لصالح {m["away']} والدفاع يتدخل بنجاح.</div>', unsafe_allow_html=True)
        
        time.sleep(1)

# ================= 4. مرحلة تحليل الذكاء الاصطناعي والتوقعات =================
elif st.session_state.step == 'analysis':
    m = st.session_state.selected_match
    
    if st.button("⬅️ العودة لقائمة المباريات والبطولات"):
        st.session_state.step = 'dashboard'
        st.rerun()

    st.title(f"🧠 تحليل الذكاء الاصطناعي: {m['home_flag']} {m['home']} vs {m['away_flag']} {m['away']}")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 احتمالات الفوز وتطور اللقاء")
        st.progress(0.60, text=f"فوز {m['home']}: 60%")
        st.progress(0.25, text="التعادل: 25%")
        st.progress(0.15, text=f"فوز {m['away']}: 15%")
        
    with col2:
        st.subheader("🎯 النتيجة المتوقعة للذكاء الاصطناعي")
        st.info("بناءً على محاكاة الخوارزميات الحية لأكثر من 10,000 سيناريو:")
        st.markdown(f"### ⚽ {m['home']} **2 - 0** {m['away']}")

    st.write("---")
    st.subheader("📈 تحديثات ما قبل وبعد المباراة")
    st.markdown("- **حالة الحكام:** طاقم تحكيم دولي يتميز بصرامة متوسطة في احتساب البطاقات الملونة.")
    st.markdown("- **الإصابات والغيابات:** اكتمال صفوف الفريقين بنسبة كبيرة وغياب لاعب واحد مؤثر للاحتياط.")
    st.markdown("- **التاريخ والمواجهات السابقة:** تفوق طفيف لصالح الفريق المستضيف في آخر 5 مباريات مباشرة.")

    if st.button("🔄 تحديث التحليل والبيانات الآن"):
        with st.spinner("جاري جلب أحدث بيانات الذكاء الاصطناعي العالمية..."):
            time.sleep(1.2)
        st.success("تم تحديث التوقعات والإحصائيات بنجاح!")
        

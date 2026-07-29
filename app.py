import streamlit as st
import random
import time

# إعدادات الصفحة لتكون شبيهة بالتطبيقات الاحترافية
st.set_page_config(
    page_title="Sofascore Analyst AI",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم عبر CSS لزيادة الجمالية وسهولة الاستخدام
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
    .stButton>button:hover {
        background-color: #2ca02c;
    }
    .metric-card {
        background-color: #1e2530;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (المراحل المختلفة)
if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'selected_match' not in st.session_state:
    st.session_state.selected_match = None

# ================= مرحلة الترحيب والدخول =================
if st.session_state.step == 'welcome':
    st.title("⚽ Sofascore Analyst AI")
    st.markdown("### تحويل الإحصائيات المعقدة إلى رؤى واضحة باستخدام خوارزميات الذكاء الاصطناعي.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>43%</h3><p>دقة توقعات الفوز</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>22%</h3><p>توقع التعادل</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>35%</h3><p>توقع الأهداف المتقدمة</p></div>', unsafe_allow_html=True)
        
    st.write("---")
    st.info("💡 **ميزات التطبيق:** تغطية أكثر من 200 بطولة عالمية، تحديثات ما قبل وأثناء المباريات، وتحليل متقدم للأداء والإصابات.")
    
    if st.button("🚀 الدخول إلى منصة التحليلات"):
        st.session_state.step = 'dashboard'
        st.rerun()

# ================= لوحة التحكم الرئيسية (Dashboard) =================
elif st.session_state.step == 'dashboard':
    st.sidebar.title("⚙️ الإعدادات والقائمة")
    menu = st.sidebar.radio("اختر القسم:", ["🏠 المباريات الحية والجدول", "📊 ترتيب الفرق", "⚙️ الإعدادات والموافقات"])
    
    if st.sidebar.button("🚪 تسجيل الخروج / البداية"):
        st.session_state.step = 'welcome'
        st.rerun()

    # --- قسم المباريات والجدول ---
    if menu == "🏠 المباريات الحية والجدول":
        st.header("📅 جدول المباريات والتوقيت والتحليلات الذكية")
        st.write("اختر مباراة لعرض رؤى الخبراء وتحليل الذكاء الاصطناعي:")

        # قائمة مباريات وهمية مع الصور والأيقونات
        matches = [
            {"id": 1, "home": "ريال مدريد", "away": "برشلونة", "home_img": "👑", "away_img": "🔵🔴", "time": "21:00 - اليوم", "status": "مباشر  LIVE ⏱️ 65'"},
            {"id": 2, "home": "مانشستر سيتي", "away": "آرسنال", "home_img": "⚽", "away_img": "🔴 الأبيض", "time": "19:30 - غداً", "status": "قادم ⏳"},
            {"id": 3, "home": "بايرن ميونخ", "away": "بوروسيا دورتموند", "home_img": "🔴", "away_img": "🟡", "time": "22:00 - بعد غد", "status": "قادم ⏳"}
        ]

        for m in matches:
            col1, col2, col3 = st.columns([3, 2, 2])
            with col1:
                st.markdown(f"**{m['home_img']} {m['home']}** VS **{m['away_img']} {m['away']}**")
                st.caption(f"التوقيت: {m['time']} | الحالة: {m['status']}")
            with col2:
                st.markdown(f"📍 بطولة الدوري العالمي")
            with col3:
                if st.button(f"🔍 كشف التحليل", key=f"match_{m['id']}"):
                    st.session_state.selected_match = m
                    st.session_state.step = 'analysis'
                    st.rerun()
            st.divider()

    # --- قسم ترتيب الفرق ---
    elif menu == "📊 ترتيب الفرق":
        st.header("🏆 جدول ترتيب الفرق والاندية حول العالم")
        
        import pandas as pd
        data = {
            "المركز": [1, 2, 3, 4],
            "الفريق": ["👑 ريال مدريد", "🔵🔴 برشلونة", "⚽ مانشستر سيتي", "🔴 بايرن ميونخ"],
            "لعب": [20, 20, 20, 20],
            "نقاط": [52, 49, 48, 45]
        }
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)

    # --- قسم الإعدادات والموافقات ---
    elif menu == "⚙️ الإعدادات والموافقات":
        st.header("⚙️ إعدادات التطبيق والموافقات")
        st.checkbox("الموافقة على سياسة استخدام بيانات الذكاء الاصطناعي", value=True)
        st.checkbox("تفعيل التنبيهات الفورية للمباريات الحية", value=True)
        st.selectbox("اختر اللغة المفضلة", ["العربية", "English", "Español"])
        st.slider("مستوى تفصيل التحليلات", 1, 5, 4)
        if st.button("حفظ الإعدادات"):
            st.success("تم حفظ الإعدادات بنجاح!")

# ================= مرحلة كشف وتحليل الفريق والذكاء الاصطناعي =================
elif st.session_state.step == 'analysis':
    m = st.session_state.selected_match
    st.title(f"🧠 تحليل الذكاء الاصطناعي: {m['home_img']} {m['home']} vs {m['away_img']} {m['away']}")
    
    if st.button("⬅️ العودة إلى قائمة المباريات"):
        st.session_state.step = 'dashboard'
        st.rerun()

    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 احتمالات الفوز (AI Model)")
        st.progress(0.55, text=f"فوز {m['home']}: 55%")
        st.progress(0.25, text="التعادل: 25%")
        st.progress(0.20, text=f"فوز {m['away']}: 20%")
        
    with col2:
        st.subheader("🎯 النتيجة المتوقعة")
        st.info("بناءً على محاكاة المباراة آلاف المرات، النتيجة الأكثر احتمالاً هي:")
        st.markdown(f"### ⚽ {m['home']} **2 - 1** {m['away']}")

    st.write("---")
    st.subheader("📈 تحديثات ما قبل وأثناء المباراة")
    st.write("- **حالة الحكام وأنماط الإنذارات:** الحكم يعتاد إخراج 4 بطاقات صفراء في المتوسط.")
    st.write("- **الإصابات المؤثرة:** لا توجد غيابات مؤثرة في صفوف الفريقين.")
    st.write("- **تحليل الشوط الأول:** أظهرت أول 45 دقيقة سيطرة واضحة بنسبة 58% لصاحب الأرض.")

    if st.button("🔄 تحديث التحليل لايف"):
        with st.spinner("جاري جلب أحدث بيانات الذكاء الاصطناعي..."):
            time.sleep(1.5)
     
st.success("تم تحديث التوقعات بناءً على أحداث اللحظة!")
                        
import streamlit as st
import random
import time
from datetime import datetime, timedelta

# إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="Sofascore Analyst AI - الدوريات والمنتخبات العالمية",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص التصميم عبر CSS
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
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق
if 'step' not in st.session_state:
    st.session_state.step = 'welcome'
if 'selected_match' not in st.session_state:
    st.session_state.selected_match = None

# قاعدة بيانات واسعة تشمل الدوريات العالمية والمنتخبات
TOURNAMENTS_DATA = {
    "🏆 دوري أبطال أوروبا (UEFA Champions League)": [
        {"id": 101, "home": "ريال مدريد", "home_flag": "👑", "away": "مانشستر سيتي", "away_flag": "🔵", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 74, "score": "2 - 1"},
        {"id": 102, "home": "بايرن ميونخ", "home_flag": "🔴", "away": "باريس سان جيرمان", "away_flag": "🔵🔴", "date": "2026-06-05", "time": "22:00", "status": "LIVE", "minute": 38, "score": "0 - 0"},
        {"id": 103, "home": "آرسنال", "home_flag": "⚪🔴", "away": "إنتر ميلان", "away_flag": "⚫🔵", "date": "2026-06-06", "time": "22:00", "status": "UPCOMING", "minute": 0, "score": "vs"}
    ],
    "🌍 كأس العالم للمنتخبات (World Cup)": [
        {"id": 201, "home": "البرازيل", "home_flag": "🇧🇷", "away": "الأرجنتين", "away_flag": "🇦🇷", "date": "2026-06-10", "time": "21:00", "status": "UPCOMING", "minute": 0, "score": "vs"},
        {"id": 202, "home": "فرنسا", "home_flag": "🇫🇷", "away": "إنجلترا", "away_flag": "🏴󠁧󠁢󠁥󠁮󠁧󠁿", "date": "2026-06-11", "time": "19:00", "status": "UPCOMING", "minute": 0, "score": "vs"},
        {"id": 203, "home": "إسبانيا", "home_flag": "🇪🇸", "away": "ألمانيا", "away_flag": "🇩🇪", "date": "2026-06-12", "time": "22:00", "status": "UPCOMING", "minute": 0, "score": "vs"}
    ],
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 الدوري الإنجليزي الممتاز (Premier League)": [
        {"id": 301, "home": "ليفربول", "home_flag": "🔴", "away": "تشيلسي", "away_flag": "🔵", "date": "2026-06-07", "time": "18:30", "status": "UPCOMING", "minute": 0, "score": "vs"},
        {"id": 302, "home": "مانشستر يونايتد", "home_flag": "🔴", "away": "توتنهام", "away_flag": "⚪", "date": "2026-06-07", "time": "16:00", "status": "UPCOMING", "minute": 0, "score": "vs"}
    ],
    "🇪🇸 الدوري الإسباني (La Liga)": [
        {"id": 401, "home": "برشلونة", "home_flag": "🔵🔴", "away": "أتلتيكو مدريد", "home_flag": "⚪🔴", "date": "2026-06-08", "time": "22:00", "status": "UPCOMING", "minute": 0, "score": "vs"}
    ]
}

# ================= 1. مرحلة الترحيب والدخول =================
if st.session_state.step == 'welcome':
    st.title("⚽ Sofascore Analyst AI - الشامل للمباريات والمنتخبات")
    st.markdown("### رؤى الخبراء، التوقيتات الدقيقة، واللايف بالدقيقة لجميع دوريات ومنتخبات العالم عبر الذكاء الاصطناعي.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>200+</h3><p>بطولة ودوري عالمي</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>1 دقيقة</h3><p>تحديثات حية ومباشرة</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>94%</h3><p>دقة خوارزميات التوقع</p></div>', unsafe_allow_html=True)
        
    st.write("---")
    st.info("💡 تغطية كاملة لمباريات الأندية والمنتخبات العالمية مع مواعيد دقيقة بالتاريخ والتوقيت المحلي.")
    
    if st.button("🚀 الدخول إلى منصة التحليلات الشاملة"):
        st.session_state.step = 'dashboard'
        st.rerun()

# ================= 2. لوحة التحكم والبطولات والمباريات =================
elif st.session_state.step == 'dashboard':
    st.sidebar.title("⚙️ خيارات التصفح")
    menu = st.sidebar.radio("الأقسام:", ["⚽ المباريات واللايف (حسب البطولة)", "🏆 ترتيب الدوريات والفرق", "⚙️ الإعدادات والموافقات"])
    
    if st.sidebar.button("🚪 العودة للبداية"):
        st.session_state.step = 'welcome'
        st.rerun()

    # --- قسم المباريات الحية والجدول والبطولات ---
    if menu == "⚽ المباريات واللايف (حسب البطولة)":
        st.header("📅 جدول المباريات والمنتخبات العالمية - التوقيت واللايف")
        
        # اختيار البطولة أو الدوري
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
                    st.markdown(f"**النتيجة: {m['score']}**")
                else:
                    st.markdown(f"⏳ **مباراة قادمة**")
            with col3:
                st.markdown(f"📍 تغطية شاملة بالذكاء الاصطناعي")
            with col4:
                if st.button(f"🔍 كشف التحليل", key=f"match_{m['id']}"):
                    st.session_state.selected_match = m
                    st.session_state.step = 'analysis'
                    st.rerun()
            st.divider()

    # --- قسم ترتيب الفرق والدوريات ---
    elif menu == "🏆 ترتيب الدوريات والفرق":
        st.header("🏆 جدول ترتيب الفرق والمنتخبات")
        import pandas as pd
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

    # --- قسم الإعدادات ---
    elif menu == "⚙️ الإعدادات والموافقات":
        st.header("⚙️ الإعدادات وتفضيلات التطبيق")
        st.checkbox("الموافقة على شروط تتبع البيانات المباشرة (Live Data)", value=True)
        st.checkbox("تفعيل تنبيهات الدقائق في المباريات الحية", value=True)
        st.selectbox("تنسيق الوقت", ["توقيت غرينتش (GMT)", "التوقيت المحلي لجهازك (Local)"])
        if st.button("حفظ التغييرات"):
            st.success("تم تحديث الإعدادات بنجاح!")

# ================= 3. مرحلة تفاصيل وتحليل المباراة بالذكاء الاصطناعي =================
elif st.session_state.step == 'analysis':
    m = st.session_state.selected_match
    st.title(f"🧠 تحليل الذكاء الاصطناعي: {m['home_flag']} {m['home']} vs {m['away_flag']} {m['away']}")
    
    if st.button("⬅️ العودة لقائمة المباريات والبطولات"):
        st.session_state.step = 'dashboard'
        st.rerun()

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
    st.subheader(f"⏱️ تفاصيل الدقيقة بالدقيقة (تحديث مباشر)")
    if m['status'] == "LIVE":
        st.success(f"المباراة جارية الآن في الدقيقة **{m['minute']}'** والسيطرة تميل لصالح أصحاب الأرض بنسبة 62%.")
        st.markdown("- **الدقيقة 12:** هدف مبكر ملغي بعد العودة لتقنية الـ VAR.")
        st.markdown("- **الدقيقة 45+2:** نهاية الشوط الأول بتقدم مستحق.")
        st.markdown(f"- **الدقيقة {m['minute']}:** استمرار الضغط الهجومي وتسديدة قريبة على مرمى {m['away']}.")
    else:
        st.info("المباراة لم تنطلق بعد. تبدأ في الموعد المحدد بالتاريخ والتوقيت المذكور أعلاه.")

    if st.button("🔄 تحديث البيانات الحية الآن"):
        with st.spinner("جاري جلب آخر دقيقة من الملاعب العالمية..."):
            time.sleep(1.2)
        st.success("تم جلب أحدث إحصائيات الدقيقة الحالية بنجاح!")
        

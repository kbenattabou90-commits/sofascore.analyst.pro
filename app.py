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
                        

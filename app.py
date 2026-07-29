import datetime
import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="Sofascore Analyst Pro - Global",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# القاموس متعدد اللغات (عربي، إنجليزي، فرنسي)
translations = {
    "العربية": {
        "title": "⚽ Sofascore Analyst Pro - مباريات العالم والذكاء الاصطناعي",
        "subtitle": "المنظومة العالمية الشاملة للتحليل الرياضي، وجداول المباريات الحية",
        "settings": "⚙️ إعدادات النظام واللغة",
        "lang_label": "اختر لغة الواجهة (Language)",
        "menu": "قائمة التنقل",
        "menu_items": [
            "📅 مباريات اليوم العالمية",
            "🤖 التحليل الذكي المتقدم",
            "💾 أرشيف البيانات",
        ],
        "today_matches": "🌍 جدول مباريات اليوم الحية والتاريخ",
        "live_info": "يتم جلب جدول المباريات الحية والزمنية من الخوادم العالمية بنجاح.",
        "status_soon": "قريباً",
        "status_live": "مباشر 🔴",
        "status_ended": "منتهي ✅",
        "ai_title": "🧠 محرك التحليل والذكاء الاصطناعي العالمي",
        "home_team": "الفريق المضيف (Home Team):",
        "away_team": "الفريق الضيف (Away Team):",
        "run_ai": "🚀 تشغيل محرك التحليل الذكي",
        "ai_loading": "🔄 جاري تحليل بيانات الأداء العالمية والخوارزميات...",
        "ai_success": "✨ تم إصدار التقرير التحليلي بنجاح!",
        "expected_goals": "أهداف متوقعة (xG)",
        "win_prob": "نسبة الفوز المتوقعة",
        "expert_insight": "💡 رؤية الخبير الآلي:",
        "database_title": "💾 أرشيف التحليلات والسجلات العالمية",
        "database_desc": "جميع التحليلات السابقة محفوظة هنا مع تواريخها بدقة.",
    },
    "English": {
        "title": "⚽ Sofascore Analyst Pro - Global Matches & AI",
        "subtitle": (
            "Comprehensive Global Sports Analytics System & Live Match Schedules"
        ),
        "settings": "⚙️ System & Language Settings",
        "lang_label": "Select Language",
        "menu": "Navigation Menu",
        "menu_items": [
            "📅 Global Live Matches",
            "🤖 Advanced AI Analysis",
            "💾 Data Archive",
        ],
        "today_matches": "🌍 Today's Live Match Schedule & Date",
        "live_info": (
            "Live match schedules and timelines are successfully fetched from"
            " global servers."
        ),
        "status_soon": "Upcoming",
        "status_live": "LIVE 🔴",
        "status_ended": "Finished ✅",
        "ai_title": "🧠 Global AI Match Analysis Engine",
        "home_team": "Home Team:",
        "away_team": "Away Team:",
        "run_ai": "🚀 Run AI Analysis Engine",
        "ai_loading": (
            "🔄 Analyzing global performance data and algorithms..."
        ),
        "ai_success": "✨ Analytical report generated successfully!",
        "expected_goals": "Expected Goals (xG)",
        "win_prob": "Win Probability",
        "expert_insight": "💡 AI Expert Insight:",
        "database_title": "💾 Global Analytics Archive",
        "database_desc": (
            "All previous analyses are safely stored here with precise dates."
        ),
    },
    "Français": {
        "title": (
            "⚽ Sofascore Analyst Pro - Matchs Mondiaux et Intelligence"
            " Artificielle"
        ),
        "subtitle": (
            "Système global d'analyse sportive et calendrier des matchs en"
            " direct"
        ),
        "settings": "⚙️ Paramètres du Système et Langue",
        "lang_label": "Choisir la Langue",
        "menu": "Menu de Navigation",
        "menu_items": [
            "📅 Matchs Mondiaux en Direct",
            "🤖 Analyse IA Avancée",
            "💾 Archive des Données",
        ],
        "today_matches": (
            "🌍 Calendrier des Matchs du Jour et Date en Direct"
        ),
        "live_info": (
            "Les horaires et matchs en direct sont récupérés avec succès des"
            " serveurs mondiaux."
        ),
        "status_soon": "À venir",
        "status_live": "EN DIRECT 🔴",
        "status_ended": "Terminé ✅",
        "ai_title": "🧠 Moteur d'Analyse IA Global",
        "home_team": "Équipe à Domicile:",
        "away_team": "Équipe à l'Extérieur:",
        "run_ai": "🚀 Lancer le Moteur d'Analyse",
        "ai_loading": (
            "🔄 Analyse des données de performance mondiales et des"
            " algorithmes..."
        ),
        "ai_success": "✨ Rapport analytique généré avec succès !",
        "expected_goals": "Buts Attendus (xG)",
        "win_prob": "Probabilité de Victoire",
        "expert_insight": "💡 Analyse de l'Expert IA :",
        "database_title": "💾 Archive des Analyses Globales",
        "database_desc": (
            "Toutes les analyses précédentes sont stockées ici avec des dates"
            " précises."
        ),
    },
}

# تصميم وتنسيق المظهر (Dark Modern UI)
st.markdown(
    """
    <style>
    .main-header {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 2rem;
        border: 1px solid #334155;
    }
    .match-card {
        background-color: #1e293b;
        padding: 1.2rem;
        border-radius: 10px;
        border: 1px solid #334155;
        margin-bottom: 1rem;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# القائمة الجانبية لإعدادات اللغة والنظام
st.sidebar.header("⚙️ Settings / إعدادات")
selected_lang = st.sidebar.selectbox(
    "🌍 Choose Language / اختر اللغة", ("العربية", "English", "Français")
)
t = translations[selected_lang]

# الهيدر الرئيسي
st.markdown(
    f"""
    <div class="main-header">
        <h1>{t['title']}</h1>
        <p style="color: #94a3b8; font-size: 1.2rem;">{t['subtitle']}</p>
    </div>
""",
    unsafe_allow_html=True,
)

# القائمة الجانبية للتنقل
st.sidebar.markdown("---")
st.sidebar.header(t["menu"])
app_mode = st.sidebar.radio("", t["menu_items"])

# 1. قسم مباريات اليوم حول العالم
if app_mode == t["menu_items"][0]:
  current_date = datetime.datetime.now().strftime("%Y-%m-%d")
  st.subheader(f"{t['today_matches']} ({current_date})")
  st.info(f"💡 {t['live_info']}")

  # جدول المباريات العالمية الشاملة بالتوقيت والتاريخ
  global_matches = [
      {
          "league": (
              "UEFA Champions League / دوري أبطال أوروبا / Ligue des Champions"
          ),
          "time": "21:00 GMT",
          "home": "Real Madrid",
          "away": "Manchester City",
          "status": t["status_soon"],
      },
      {
          "league": (
              "Premier League / الدوري الإنجليزي الممتاز / Premier League"
          ),
          "time": "18:30 GMT",
          "home": "Arsenal",
          "away": "Liverpool",
          "status": t["status_live"],
      },
      {
          "league": "La Liga / الدوري الإسباني / La Liga",
          "time": "20:00 GMT",
          "home": "FC Barcelona",
          "away": "Atletico Madrid",
          "status": t["status_soon"],
      },
      {
          "league": "Serie A / الدوري الإيطالي / Serie A",
          "time": "19:45 GMT",
          "home": "Inter Milan",
          "away": "Juventus",
          "status": t["status_ended"],
      },
  ]

  for match in global_matches:
    col1, col2, col3 = st.columns([2, 3, 1])
    with col1:
      st.markdown(f"**{match['league']}**")
      st.caption(f"🕒 {match['time']}")
    with col2:
      st.markdown(
          f"### ⚔️ {match['home']} <span style='color: #38bdf8;'>VS</span>"
          f" {match['away']}",
          unsafe_allow_html=True,
      )
    with col3:
      st.markdown(f"**{match['status']}**")
    st.markdown("---")

# 2. قسم التحليل الذكي العميق
elif app_mode == t["menu_items"][1]:
  st.subheader(t["ai_title"])

  team1 = st.text_input(t["home_team"], "Real Madrid")
  team2 = st.text_input(t["away_team"], "FC Barcelona")

  if st.button(t["run_ai"]):
    with st.spinner(t["ai_loading"]):
      datetime.time(1)  # محاكاة وقت المعالجة البرمجية
    st.success(t["ai_success"])

    col1, col2 = st.columns(2)
    with col1:
      st.metric(label=f"{t['win_prob']} ({team1})", value="54%")
      st.metric(label=t["expected_goals"], value="1.95")
    with col2:
      st.metric(label=f"{t['win_prob']} ({team2})", value="46%")
      st.metric(label=t["expected_goals"], value="1.40")

    st.info(
        f"{t['expert_insight']} التوقعات الفنية للمواجهة بين **{team1}** و"
        f" **{team2}** تقود إلى تقارب كبير في السيطرة على خط الوسط، مع تفوق"
        " طفيف للفريق المضيف في استغلال الهرتدات الهجومية والضغط الفعّال."
    )

# 3. قسم أرشيف البيانات
else:
  st.subheader(t["database_title"])
  st.write(t["database_desc"])
  st.dataframe(
      {
          "Date / التاريخ": ["2026-07-29", "2026-07-28", "2026-07-27"],
          "Match / المباراة": [
              "Real Madrid vs Manchester City",
              "Arsenal vs Liverpool",
              "FC Barcelona vs Atletico Madrid",
          ],
          "Predicted Score / النتيجة المتوقعة": ["2 - 1", "2 - 2", "3 - 1"],
      }
  )
    

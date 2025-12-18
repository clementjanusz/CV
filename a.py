import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Clément JANUSZ | Data Analyst BI",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4B5563;
        font-style: italic;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1E3A8A;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .highlight {
        color: #1E3A8A;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://ui-avatars.com/api/?name=Clement+Janusz&background=1E3A8A&color=fff&size=200", width=150)
    st.markdown("## Contact Info")
    st.write("📧 Clement.janusz@outlook.com")
    st.write("📍 Paris, France")
    st.write("🔗 [LinkedIn Profile](#)")
    
    st.markdown("---")
    st.markdown("## 🗣️ Languages")
    st.write("🇫🇷 **Français:** Natif")
    st.write("🇬🇧 **Anglais:** B2 (European Section)")
    st.write("🇪🇸 **Espagnol:** B1")
    
    st.markdown("---")
    st.markdown("## ♟️ Interests")
    st.write(f"• Chess (ELO 1500)")
    st.write("• Lecture")
    st.write("• Course à pied")
    st.write("• Rhétorique")
    
    st.markdown("---")
    # Download button (optional): the app runs even if the PDF isn't present.
    pdf_path = Path(__file__).with_name("Clement_JANUSZ_CV.pdf")
    if pdf_path.exists():
        pdf_bytes = pdf_path.read_bytes()
        st.download_button(
            label="📄 Download Full CV (PDF)",
            data=pdf_bytes,
            file_name=pdf_path.name,
            mime="application/pdf",
        )
    else:
        st.caption("📄 CV PDF non requis pour exécuter l'app (fichier absent).")

# --- MAIN CONTENT ---

# Header Section
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="main-header">Clément JANUSZ</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Alternance Data Analyst BI</div>', unsafe_allow_html=True)
    st.info("📅 **Disponible à partir du 1er septembre 2025**")
    st.markdown("""
    Passionate about data manipulation, visualization, and machine learning. 
    Currently seeking a work-study opportunity to apply skills in SQL, Python, and BI tools.
    """)

# Skills Visualization (Radar Chart)
with col2:
    st.markdown("### 🛠️ Technical Arsenal")
    skills_data = pd.DataFrame({
        'Skill': ['Python', 'SQL/NoSQL', 'Azure Cloud', 'Power BI/Tableau', 'Excel', 'Databricks'],
        'Level': [5, 5, 5, 3, 5, 3]  # 5=Advanced, 3=Intermediate based on CV
    })
    
    fig = px.line_polar(skills_data, r='Level', theta='Skill', line_close=True)
    fig.update_traces(fill='toself', line_color='#1E3A8A')
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
        margin=dict(t=20, b=20, l=20, r=20),
        height=250
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

# --- EXPERIENCE & PROJECTS ---
st.markdown("## 🚀 Key Projects & Experience")

# Row 1: AI & Finance
col_proj1, col_proj2 = st.columns(2)

with col_proj1:
    st.markdown("### 🤖 [Scrape.AI (Textual AI)](http://localhost:3000/)")
    st.caption("2023 - 2025")
    st.markdown("""
    Development of a conversational AI using MCP and specialized tools for file analysis.
    * **Tech Stack:** BERT, Levenshtein, MCP.
    """)
    st.metric(label="Request Time Reduction", value="-70%", delta="Optimization")

with col_proj2:
    st.markdown("### 📈 ESG Financial Analysis")
    st.caption("Sector Analysis")
    st.markdown("""
    Optimization of a theoretical ESG portfolio and critical study of responsible finance evolution.
    * **Focus:** Risk management, Volatility control.
    """)
    st.metric(label="Benchmark Outperformance", value="+3.2%", delta="Annualized (5 yrs)")

# Row 2: Prediction Models
col_proj3, col_proj4 = st.columns(2)

with col_proj3:
    st.markdown("### 🏥 Diabetes Prediction Model")
    st.caption("Medical Data Classification")
    st.markdown("""
    Implementation of a decision tree algorithm trained on medical datasets with cross-validation.
    * **Tech:** Decision Trees, Hyperparameter optimization.
    """)
    st.metric(label="Model Precision", value="90%")

with col_proj4:
    st.markdown("### 🎮 Competitive Match Analytics")
    st.caption("Data Viz & Regression")
    st.markdown("""
    Statistical analysis and interactive visualization of pro player performance.
    * **Tech:** Linear Regression, Data Viz.
    """)
    st.metric(label="Prediction Reliability", value="80%")

st.divider()

# --- EDUCATION ---
st.markdown("## 🎓 Education")

tab1, tab2 = st.tabs(["Current Degree", "International Exchange"])

with tab1:
    st.markdown("### 🇫🇷 Bachelor Grade Licence | EFREI Paris")
    st.markdown("**09/2023 - Present**")
    st.write("Formation focused on data: Database manipulation (SQL, NoSQL), Data Visualization, Big Data, Cloud Computing, Machine Learning, and ETL pipelines.")

with tab2:
    st.markdown("### 🇪🇪 University Exchange | TalTech (Tallinn, Estonia)")
    st.markdown("**2025 (2 Months)**")
    st.write("Specialization in Supervised AI, Neural Networks, NLP, and Data Analysis. Participated in international collaborative projects.")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: grey;">
    Built with Streamlit • Based on the CV of Clément JANUSZ
</div>
""", unsafe_allow_html=True)

st.markdown(
        """
<div style="
        background: rgba(0, 24, 0, 0.65);
        border-left: 6px solid #22C55E;
        padding: 16px 18px;
        border-radius: 10px;
        margin-top: 14px;
">
    <div style="color: black; font-size: 0.95rem; line-height: 1.4;">
        Dashboard interactif réalisé sous la supervision pédagogique de : <b>Mano Joseph Matthew</b>
    </div>
    <div style="margin-top: 6px; color: black; font-size: 0.95rem; line-height: 1.4;">
        Profil LinkedIn :
        <a href="https://www.linkedin.com/in/manojosephmatthew/" target="_blank" rel="noopener noreferrer">
            https://www.linkedin.com/in/manojosephmatthew/
        </a>
    </div>
</div>
""",
        unsafe_allow_html=True,
)

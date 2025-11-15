# streamlit_app.py
import streamlit as st
from PIL import Image
import pandas as pd
import time
import os

# ---- Page Config ----
st.set_page_config(
    page_title="Shervin Dale Tabernero | Portfolio",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Custom Styling (Professional Blue Theme) ----
st.markdown(
    """
    <style>

    /* ❗ Force Light Mode (Fixes black background issue on Streamlit Cloud) */
    @media (prefers-color-scheme: dark) {
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F5F8FB !important;
            color: #2B2B2B !important;
        }
    }

    /* App Background */
    [data-testid="stAppViewContainer"] {
        background-color: #F5F8FB !important;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #4D7EAF, #3B6B99) !important;
        color: white !important;
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* Headings */
    .big-title {
        font-size: 36px;
        font-weight: 700;
        color: #2E4965;
    }
    .subtitle {
        color: #4D7EAF;
        font-size: 18px;
        margin-bottom: 16px;
    }

    /* Project Cards */
    .project-card {
        background: linear-gradient(180deg, #FFFFFF, #F0F6FB);
        border: 1px solid #D3E0EC;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        transition: 0.25s ease;
    }
    .project-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
    }

    /* Buttons */
    .stButton button, .stDownloadButton button, .stFormSubmitButton button {
        background-color: #4D7EAF !important;
        color: white !important;
        border-radius: 6px !important;
        border: none !important;
    }
    .stButton button:hover,
    .stDownloadButton button:hover,
    .stFormSubmitButton button:hover {
        background-color: #3B6B99 !important;
    }

    /* Forms */
    .stForm {
        background-color: #FFFFFF !important;
        padding: 20px !important;
        border-radius: 12px !important;
        border: 1px solid #D3E0EC !important;
    }
    .stForm label {
        color: #2E4965 !important;
    }

    /* Progress Bars */
    .stProgress > div > div > div > div {
        background-color: #4D7EAF !important;
    }

    /* DataFrame Table */
    .stDataFrame table {
        background-color: #FFFFFF !important;
    }
    .stDataFrame thead tr th {
        background-color: #E9F1FA !important;
        color: #2E4965 !important;
    }
    .stDataFrame tbody tr td {
        background-color: #FFFFFF !important;
        color: #2E4965 !important;
    }

    /* Fix expander background */
    .streamlit-expanderHeader {
        color: #2E4965 !important;
    }
    .streamlit-expanderContent {
        background-color: #F7FAFC !important;
    }

    /* Links */
    a {
        color: #4D7EAF;
        text-decoration: none;
    }
    a:hover {
        color: #2E4965;
        text-decoration: underline;
    }

    /* Custom card container fix */
    .light-card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 12px;
        border: 1px solid #D3E0EC;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---- Sidebar ----
with st.sidebar:
    # Safe profile image loading
    profile_path = "images/profile.png"
    if os.path.exists(profile_path):
        st.image(profile_path, use_container_width=True)
    else:
        st.image(
            "https://placehold.co/300x300/4D7EAF/FFFFFF?text=Profile+Image",
            use_container_width=True,
        )

    st.title("Shervin Dale M. Tabernero")
    st.write("Frontend • Backend • Designer")
    st.markdown("---")
    st.header("Quick Links")
    st.markdown("- [About](#about)")
    st.markdown("- [Projects](#projects)")
    st.markdown("- [Contact](#contact)")
    st.markdown("---")
    st.write("📄 **Download my resume**")

    resume_path = "files/resume.pdf"
    if os.path.exists(resume_path):
        try:
            with open(resume_path, "rb") as f:
                resume_bytes = f.read()
            st.download_button(
                label="Download Resume",
                data=resume_bytes,
                file_name="Tabernero_Resume.pdf",
                mime="application/pdf",
            )
        except Exception as e:
            st.error(f"Could not load resume file: {e}")
    else:
        st.info("Resume file not found on server. (Make sure files/resume.pdf is in the repo.)")

# ---- Header / Hero ----
col1, col2 = st.columns([2, 3])
with col1:
    st.markdown('<div class="big-title">Hi — I’m Shervin Dale 👋</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Computer Science Student • Web & App Developer • UI/UX Enthusiast</div>', unsafe_allow_html=True)
    st.write("""
    I’m Shervin Dale M. Tabernero, a Computer Science student passionate about building digital experiences that blend functionality and aesthetics.
    From developing full-stack systems to crafting clean user interfaces, I aim to create solutions that are intuitive and impactful.
    """)
    if st.button("Say Hello"):
        st.success("Thanks for visiting — send a message in the Contact section below!")

with col2:
    uploaded = st.file_uploader("Upload a custom profile picture (optional)", type=["png", "jpg", "jpeg"])
    if uploaded:
        img = Image.open(uploaded)
        st.image(img, caption="Profile Photo", use_container_width=True)
    else:
        st.image("https://placehold.co/600x350/4D7EAF/FFFFFF?text=Your+Cover+Image", caption="Cover", use_container_width=True)

st.markdown("---")

# ---- About Section ----
st.header("About")
left, right = st.columns([1, 2])
with left:
    st.subheader("Bio")
    st.write("""
    - **Name:** Shervin Dale M. Tabernero  
    - **Age / Year:** 22 / 3rd Year CS  
    - **Location:** Mandaue City, Philippines  
    - **Interests:** Web dev, mobile apps, UI/UX, databases
    """)
    st.subheader("Skills")
    st.write("HTML / CSS / JS / ReactJs")
    st.progress(80)
    st.write("Python")
    st.progress(85)
    st.write("Java / Kotlin / C / C++ / C#")
    st.progress(90)
    st.write("Databases")
    st.progress(85)

with right:
    st.subheader("Short Autobiography")
    st.write("""
    Hi! I’m Shervin Dale, a Computer Science student passionate about technology and creative design.
    I enjoy developing software that combines functionality with elegant design — from web and mobile applications to interactive dashboards and simulations.
    Over the years, I’ve built projects using Java, Kotlin, PHP, and Python, with a strong focus on user experience and system efficiency.
    Outside of coding, I explore new design tools, learn emerging technologies, and collaborate on projects that make a difference.
    """)

st.markdown("---")

# ---- Projects ----
st.header("Projects")
proj_col1, proj_col2, proj_col3 = st.columns(3)

def render_project(col, project):
    with col:
        # Safe project image loading
        img_path = project["image"]

        if os.path.exists(img_path):
            # If image exists locally (e.g., images/project1.png)
            st.image(img_path, use_container_width=True)
        else:
            # If local file does not exist, treat 'image' as URL
            st.image(
                img_path if img_path.startswith("http") else
                "https://placehold.co/600x400/4D7EAF/FFFFFF?text=Image+Not+Found",
                use_container_width=True
            )

        # Project title
        st.markdown(f"### {project['title']}")

        # Short description
        st.write(project["short"])

        # Expandable details section
        with st.expander("Read more"):
            st.write(project["details"])
            st.write(f"🔗 [View on GitHub]({project['link']})")

        st.markdown("</div>", unsafe_allow_html=True)

projects = [
    {
        "title": "Inventory System - Web-based",
        "short": "PHP + Chart.js Inventory System",
        "details": "Developed an interactive System using HTML, CSS, PHP, MySQL, and Chart.js with owner and supplier views.",
        "image": "images/StoreStock_logo.png",
        "link": "https://github.com/Bossdale/StoreStock.git"
    },
    {
        "title": "Android E-commerce App",
        "short": "Kotlin + RecyclerView App",
        "details": "E-commerce app with archive/restore features, RecyclerView lists, and persistent local storage.",
        "image": "images/wildcats_prototype.png",
        "link": "https://github.com/Tong-nvk/Wildcat-FreshFinds.git"
    },
    {
        "title": "Cooking Simulation Game",
        "short": "Java FXGL Game",
        "details": "Cooking simulation with custom entities, drag-and-drop mechanics, and interactive gameplay.",
        "image": "images/cooking_ina.png",
        "link": "https://github.com/ero-s/Cooking-Ina-Ang-Sarap-.git"
    }
]

for col, project in zip([proj_col1, proj_col2, proj_col3], projects):
    render_project(col, project)

st.markdown("---")

# ---- Filterable Project List ----
st.markdown(
    """
    <div style="background-color:#E9F1FA; padding:5px; border-radius:12px; border:1px solid #D3E0EC; margin-bottom: 20px">
        <h3 style="color:#2E4965; margin-bottom:0px;">Filterable Project List</h3>
    """,
    unsafe_allow_html=True
)

projects_df = pd.DataFrame([
    {"name": "Inventory System", "year": 2025, "tech": "PHP"},
    {"name": "E-commerce Android App", "year": 2025, "tech": "Kotlin"},
    {"name": "Cooking Sim", "year": 2025, "tech": "Java"}
])

cols = st.columns([2, 1, 1])
with cols[0]:
    q = st.text_input(" Search by name", placeholder="Type project name...")
with cols[1]:
    sel_year = st.selectbox("📅 Year", options=[2025, 2024, 2023])
with cols[2]:
    tech = st.selectbox("💻 Tech", options=["All", "PHP", "Kotlin", "Java"])

filtered = projects_df[projects_df['name'].str.contains(q or "", case=False)]
if tech != "All":
    filtered = filtered[filtered['tech'] == tech]
filtered = filtered[filtered['year'] == sel_year]

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)

st.markdown("</div>", unsafe_allow_html=True)

# ---- Contact Section ----
st.header("Contact")
st.write("Send me a message — I usually reply within a few days.")

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    attach = st.file_uploader("Attach a file (optional)", type=["pdf", "png", "jpg", "txt"])
    submitted = st.form_submit_button("Send Message")

    if submitted:
        if "messages" not in st.session_state:
            st.session_state.messages = []
        st.session_state.messages.append({"name": name, "email": email, "message": message})
        st.success("✅ Message sent successfully!")
        if attach:
            st.info(f"Received attachment: {attach.name} ({attach.type})")

if "messages" in st.session_state and st.session_state.messages:
    with st.expander("Submitted Messages (Demo)"):
        for m in st.session_state.messages:
            st.write(f"**{m['name']}** ({m['email']}) — {m['message']}")

st.markdown("---")

# ---- Footer ----
st.write("🌐 Made with ❤️ using Streamlit — Designed by **Shervin Dale Tabernero**")

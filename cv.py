from pathlib import Path
import streamlit as st
from PIL import Image

# Path setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
profile_pic = current_dir / "assests" / "nav_pic.jpeg"

# General Setting
PAGE_TITLE = "Digital CV | Arnav Singh Rana"
PAGE_ICON = "random"
NAME = "Arnav Singh Rana"
DESCRIPTION = """
I'm excited about the idea of applying my operational background to make sense of data for smarter decision-making. I'm actively looking for opportunities in Data Science, where I can learn, grow, and contribute to making data work for the success of the organization.
"""
EMAIL = "arnavsinghrana74@gmail.com"
SOCIAL_MEDIA = {
    "LinkdIn": "www.linkedin.com/in/arnav-singh-rana-a76508263",
    "GitHub": "https://github.com/ArnavSinghRana01",
}

PROJECTS = {
    "**🏆 PBL Metrics Graphical Visualization in Wells (Python, Streamlit, Pyplotly)**":
        (
        "The 'PBL Metrics Graphical Visualization in Wells' project focused on implementing graphical visualization for "
        "Project-Based Learning (PBL) metrics at Wells Fargo. It leveraged Python for scripting and data processing, "
        "Streamlit for creating interactive web applications, and Pyplotly for crafting engaging charts. Excel served as the "
        "primary data source for PBL metrics."
    ),
    "**🏆 My Digital CV (Python, Streamlit)**": (
        "My Digital CV is a standout project that represents my professional journey in a modern and "
        "interactive way. Developed with Python and the Streamlit framework, this digital CV offers a dynamic platform for "
        "showcasing my skills, work experience, and contact information. The user-friendly interface ensures a seamless "
        "experience for anyone exploring my professional background. With the ability to customize the content and layout, "
        "this digital CV is a visually appealing and efficient tool for presenting my qualifications. It serves as a testament to "
        "my expertise and provides an engaging overview of my career achievements."
    ),
}



# Set wide layout
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# Custom CSS for background color and image border
st.markdown(
    """<style>
    body {
        background-color: #e6f7ff;  /* Light blue background */
    }
    img {
        border-radius: 50%;
        border: 5px solid #008080;  /* Teal border */
        box-shadow: 0 0 10px rgba(0, 128, 128, 0.3);  /* Light teal shadow */
    }
    </style>""",
    unsafe_allow_html=True,
)

# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230, caption="Data Scientist")

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)

# SOCIAL LINKS
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# EXPERIENCE & QUALIFICATIONS
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 1 Year experience as a System Operations Associate
- ✔️ Strong hands-on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player with a strong sense of initiative on tasks
"""
)

# EDUCATION
st.write("\n")
st.subheader("Education")
st.write(
    """
- 🎓 Bachelor of Business Administration (BBA) -  Hemvati Nandan Bahuguna Garhwal University, Srinagar, Uttarakhand, 2022
- 🎓 Diploma in Computer Application - Hilton Calc, Rishikesh, 2019
"""
)

# CERTIFICATIONS
st.write("\n")
st.subheader("Certifications")
st.write(
    """
- 📜 Google Data Analytics - Google
- 📜 Microsoft Certified: Azure Fundamentals - Microsoft
"""
)

# SKILLS
st.write("\n")
st.subheader("Skills")
# Hard Skills
st.write("Hard Skills:")
st.write(
    """
- 👩‍💻 Programming: Python (Numpy, Streamlit, Pandas), SQL
- 📊 Data Visualization: Tableau, MS Excel, Plotly
- 🗄️ Databases: MySQL
"""
)
# Soft Skills
st.write("Soft Skills:")
st.write(
    """
- 🤝 Team Collaboration
- 💡 Problem Solving
- 📚 Continuous Learning
- 🗣 Communication
- ⏰ Time Management
- 📚 Quick Learner
- ⏰ Punctual
"""
)

# LANGUAGES
st.write("\n")
st.subheader("Languages")
st.write(
    """
- 🌐 English (Proficient)
- 🌐 Hindi (Native)
"""
)

# WORK HISTORY
st.write("\n")
st.subheader("Work History")
st.write("---")
# JOB 1
st.write("🔧", "**System Operations Associate | Wells Fargo**")
st.write("Dec 2022 - Present | Bengaluru, Karnataka, India")
st.write(
    """
- Proactively monitored and enhanced vital application performance for a seamless user experience.
- Collaborated on Autosys job scheduling, optimizing task execution for efficiency.
- Contributed to Linux server administration, covering configuration, maintenance, and troubleshooting.
- Executed server restart procedures, minimizing downtime for enhanced reliability.
- Contributed to incident response activities, actively identifying and resolving issues promptly.
- Collaborated with development teams for application performance optimization and efficiency changes.
- Executed DML queries, ensuring effective data manipulation, and utilized AMA for database performance optimization.
- Assisted the development team with deployment activities, ensuring a smooth and efficient process.
- Maintained comprehensive documentation and fostered collaboration with development teams.
- Drove efficiency through the implementation of automation scripts and tools.
- Actively participated in on-call rotations, responding to critical incidents outside regular hours.

**Skills:** Linux System Administration, Unix, Az-900, Troubleshooting, Microsoft Azure, Grafana, Autosys, Oracle Database, Microsoft SQL Server, Python (Programming Language)
"""
)

# VOLUNTEERING EXPERIENCE
st.write("\n")
st.subheader("Volunteering Experience")
st.write(
    """
- 🌈 Pride Scavenger Hunt - Wells Fargo
  - Organized and facilitated a clue-based scavenger hunt focused on LGBTQ history.
  - Designed questions and challenges that educated participants on important LGBTQ milestones.
  - Fostered a sense of inclusivity and community engagement within the organization.
"""
)

# PROJECTS & ACCOMPLISHMENTS
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, description in PROJECTS.items():
    st.write(f"{project}: {description}")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
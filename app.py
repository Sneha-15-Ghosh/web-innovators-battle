import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Sneha's Portfolio", layout="wide", page_icon="🌐")

# ---- STYLES ----


# ---- HEADER SECTION ----
st.title("🌐 Welcome to My Personal Portfolio")
st.markdown("### Hi, I'm Sneha Ghosh! 👋 This is my website for web Innovators Battle.")


# ---- SIDEBAR MENU ----
menu = st.sidebar.radio(
    "Explore the Website",
    ["Home", "About Me", "Educational Background", "Experience", 
      "Awards and Achievements", 
     "Projects",
     "Events (Organized/Attended)", "Poster/Paper Presentation", 
     "Courses Completed", "Contact"]
)

# ---- HOME SECTION ----
if menu == "Home":
    st.header("Welcome to My Personal Portfolio!")
    st.write("Feel free to explore my website to know more about me, my achievements, projects.")
    st.balloons()

# ---- ABOUT ME SECTION ----
elif menu == "About Me":
    st.header("About Me")
    st.write("""
    I am Sneha Ghosh, a first-year BTECH student in ECE at Institute of Engineering & Management.
    I love exploring the latest technologies, contributing to open-source, and building meaningful projects.
    """)

# ---- EDUCATIONAL BACKGROUND ----
elif menu == "Educational Background":
    st.header("Educational Background")
    st.write("**B.Tech - Electrical Communication Engineering** | Institute of Engineering & Management (2024-2028)")
    st.write("Completed my 10th Boards from St.Agnes under the ICSE curriculum and then attended BNR Execellence Academy under CBSE curriculum.")


# ---- EXPERIENCE SECTION ----
elif menu == "Experience":
    st.header("Experience")
    st.write("- THEATRIX member (singer)")
    st.write("- IRIS member (photographer)")


# ---- AWARDS AND ACHIEVEMENTS ----
elif menu == "Awards and Achievements":
    st.header("Awards and Achievements")
    st.write("- UEMCOS 2024 Certificate of participation.")
    

# ---- PROJECTS SECTION ----
elif menu == "Projects":
    st.header("Projects")
    st.write("### 1000 Rupee Challenge")
    st.write("- An economics project,where we aimed to make 5 times profit with a value of Rs 1000")
    



# ---- EVENTS ORGANIZED/ATTENDED ----
elif menu == "Events (Organized/Attended)":
    st.header("List of Events")
    st.write("- **Attended**: 6th International Conference on Sensors and Transducers (UEMCOS 2024)")

# ---- POSTER/PAPER PRESENTATION ----
elif menu == "Poster/Paper Presentation":
    st.header("Poster/Paper Presentation")
    st.write("- Presented *“Application of Artificial Intelligence In Drug Discovery”* at UEMK 2024.")

# ---- COURSES COMPLETED ----
elif menu == "Courses Completed":
    st.header("Courses Completed (NPTEL)")
    st.write("NPTEL online course")
    

# ---- CONTACT SECTION ----
elif menu == "Contact":
    st.header("Contact Address")
    st.write("📍 **Location**: Kharagpur, West Bengal, India")
    st.write("📧 **Email**: ghoshsneha1506@gmail.com")
    

# ---- FOOTER ----
st.sidebar.write("Developed by Sneha Ghosh")

from locale import currency
from tokenize import Name
import requests
from PIL import Image  #pillow function for images
from streamlit_lottie import st_lottie  #Animation module - for this you have to install pip streamlit-lottie and pip requests
from turtle import left, right, width
import streamlit as st
from pathlib import Path


#---Path Setting----

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "image" / "CV.pdf"
profile_pic = current_dir / "image" / "profile-pic.png"


#---General Seetings---

st.set_page_config(page_title="Resume-Akshay Thakare", page_icon=":tada:")

Name = "Akshay Thakare"
Description ="""
    A Computer Engineer currently pursuing for Masters in Computer Science
"""
Email = "akshay.n.thakare@gmail.com"

Social_Media = {
    
    "LinkedIn":"https://linkedin.com",
    "Instagram":"https://instagram.com",
    "Youtube":"https://youtube.com",
    "Blog":"https://akshaynthakare.wixsite.com/trackshay",
    
}

Certifications = {
    "🏆 AWS Solution Architecture" : "https://www.credly.com/badges/23854aa1-2379-4f25-8b04-fea689b22d8e/public_url",
    # "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    # "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    # "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}



#----load CSS, PDF & Profile Pic ----

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#---profile---

c1, c2 = st.columns((2,3), gap="small")

with c1:
        st.image(profile_pic, width=230)

with c2:
        st.title(Name)
        st.write(Description)
        st.download_button(
        
        label="Download Resume",
        data =PDFbyte,
        file_name=resume_file.name,
        mime="application/octtet-stream",
    )            
        st.write("😀",Email)
    
#----Social links-----
st.write("#")
cols = st.columns(len(Social_Media))
for index, (platform, link) in enumerate(Social_Media.items()):
    cols[index].write(f"[{platform}]({link})")    
    

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 1.3 Years expereince in System Administration snd ETL process
- ✔️ Strong hands on experience and knowledge in Python, Web Development and AWS
- ✔️ Certified AWS Solution Architecture
- ✔️ Graduated as a Computer Engineer (2017) from Mumbai University - CGPA 6.79
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
    
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), C, java
- 📊 Cloud: Amazon Web Services Cloud Platform
- 📚 Web Development: HTML, CSS, Python + Straemlit Module 
 
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Associate System Admin | Tata Consultancy Services**")
st.write("07/2017 - 10/2018")
st.write(
 
"""
-System Admin in TCS-GE AuditWorks
- ► Provided 24*7 support to Application Back-end and front-end as well as user's queries
- ► Server's Maintenance, Monitoring, Up-gradation, Debugging Issue in Peak Period
- ► Worked on Remote Server Handling, Maintenance and Support
- ► Worked on ETL(Extract-Transaction-Load) Process
- ► Worked on SQL Database, New Relic Monitoring Interface
"""
)

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in Certifications.items():
    st.write(f"[{project}]({link})")
import streamlit as st
from PIL import Image

# Set page title and favicon
st.set_page_config(page_title="Hammayl's Portfolio", page_icon="🎯", layout="wide")


# Sidebar with Image and Details
with st.sidebar:
    st.title("Hammayal Ramzan")
    profile_image = Image.open("hammayal.jpeg")
    st.image(profile_image, width=200, caption="Hammayal Ramzan")
    st.subheader("AI Enthusiast | Developer | Programmer | Freelancer")
    st.write("I'm dedicated to acquiring AI skills that will help me make a meaningful impact in the field.  Open to new opportunities!")
    st.markdown("**📧 Email:** [Copy Email](hammayalramzan@gmail.com)")
    st.markdown("**🔗 LinkedIn:** [linkedin.com/in/hammayal_ramzan](https://www.linkedin.com/in/hammayal-ramzan-a9b722313/)")
    st.markdown("**📍 Instagram:** [instagram.com/hammayal_ramzan](https://www.instagram.com/hammayal_ramzan/)")
    st.markdown("**👨‍💻 GitHub:** [github.com/hammayal_ramzan](https://github.com/HammayalRamzan)")
    
    # Hire Me Button
    st.markdown("""
    <a href="hammayalramzan@gmail.com" target="_blank">
        <button style="background-color:#4CAF50; color:white; padding:10px 20px; font-size:16px; border:none; cursor:pointer; width:100%;">
            🚀 Hire Me - Open to Work
        </button>
    </a>
    """, unsafe_allow_html=True)

# Main Content
st.header("Welcome to My Portfolio!")
st.write("""
Hi! I'm Hammayl, Welcome to my personal portfolio! 
    This project showcases my journey and skills in artificial intelligence
    and web development using Streamlit. Here, you will find interactive applications 
    and projects that reflect my proficiency in Python, and machine learning. 
    Each project highlights my passion for creating innovative solutions and my commitment to 
    continuous learning in the AI field. Feel free to explore and connect! Let's collaborate!
"""
)

# Skills Section
st.subheader("⚡ Skills")
st.write("""
- 🧠 AI & Machine Learning
- 🔗 LangChain & CrewAI
- 🖥️ Python 
- 🌐 Chainlit & Streamlit
- 🤖 Generative AI & RAG
- 💼 Freelancing with AI
"""
)

# Projects Section
st.subheader("🚀 Projects")
st.write("""
- **[Code Cracker](https://codecracker-project.streamlit.app/)** - Enter an encrypted message, choose a cipher, and crack the code instantly!
- **[Research Agent](https://github.com/HammayalRamzan/Research_agent00)** - An AI-powered assistant that automates research, extracts insights, verifies data, and delivers structured reports for efficient decision-making.
- **[AI Rehman Clothing Website](https://clothing-website.streamlit.app/)** - Clothing brand website built with Streamlit.
- **[Karate Website](#)** -Coming Soon.
"""
)

# Contact Section
st.subheader("📬 Get in Touch")
st.write("""I welcome the opportunity to connect for collaborations, 
"project inquiries, or any questions you may have. Don't hesitate to reach out!""")
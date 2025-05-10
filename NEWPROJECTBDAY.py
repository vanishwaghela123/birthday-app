import streamlit as st
from dotenv import dotenv_values

# Load credentials from .env file
creds = dotenv_values(".env")
USERNAME = creds.get("USERNAME")
PASSWORD = creds.get("PASSWORD")

# 🎨 Custom CSS styling
def add_custom_css():
    st.markdown("""
    <style>
    body {
        animation: gradientShift 15s ease infinite;
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #ffdde1, #fbc2eb);
        background-size: 400% 400%;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .main {
        background-color: rgba(255, 255, 255, 0.92);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 4px 30px rgba(255, 105, 180, 0.5);
        max-width: 900px;
        margin: auto;
        margin-top: 5vh;
        border: 2px dashed #ff69b4;
    }

    h1, h2, p {
        text-align: center;
        color: #d63384;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }

    .glow-header {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #fff;
        text-shadow: 0 0 10px #ff69b4, 0 0 20px #ff69b4, 0 0 30px #ff1493;
        margin-top: 30px;
        font-family: cursive;
        padding: 10px 0;
        background-color: rgba(255, 105, 180, 0.6);
        border-radius: 15px;
        animation: rotateText 10s linear infinite;
    }

    @keyframes rotateText {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    .login-box {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .stTextInput>div>div>input {
        text-align: center;
        font-size: 16px;
    }

    .stButton>button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-size: 16px;
    }

    .message-box {
        font-size: 18px;
        color: #d63384;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        padding: 20px;
        margin-top: 30px;
    }

    /* Custom styling for video */
    .video-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
    }

    .video-container iframe {
        width: 80%;
        height: 400px; /* Makes the video appear square */
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    }

    /* Styling the message under the video */
    .message-under-video {
        font-size: 20px;
        color: #d63384;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        margin-top: 30px;
        font-weight: bold;
    }

    /* Decorative line */
    .line {
        border-top: 2px solid #ff69b4;
        width: 60%;
        margin: 20px auto;
    }
    </style>
    """, unsafe_allow_html=True)

# 🎥 Embed YouTube video with autoplay and audio
def embed_youtube_video(video_id):
    st.markdown(f"""
        <div class="video-container">
            <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&mute=0&modestbranding=1&showinfo=0&controls=0" 
            frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
            </iframe>
        </div>
    """, unsafe_allow_html=True)

# 🚪 Login page
def login():
    st.markdown("<div class='main login-box'>", unsafe_allow_html=True)
    st.markdown("<div class='glow-header'>💖 Welcome Birthday Girl 💖</div>", unsafe_allow_html=True)
    st.title("🔐 Birthday Card Login")
    st.write("Only Anju can unlock this celebration! 🎁")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username.strip().lower() == "anju" and password == "happy10May":
            st.session_state.logged_in = True
            st.success("Access granted! 🎉")
            st.rerun()
        else:
            st.error("Incorrect username or password. Try again!")

    st.markdown("</div>", unsafe_allow_html=True)

# 🎂 Birthday card page
def birthday_card():
    st.markdown("<div class='main'>", unsafe_allow_html=True)

    st.markdown("<div class='glow-header'>🎉 Birthday Special 🎉</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="message-box">
        <h2>Dear Anju ❤️🎂,</h2>
        <p>Today is your special day — full of love, joy, cake, and magic! 🎉</p>
        <p>You bring so much light and laughter to those around you. ✨</p>
        <p>We’re so lucky to celebrate YOU today. 🎈🎁</p>
        <p><strong>Wishing you a life filled with sparkles, happiness, and endless dreams! 💖</strong></p>
        <h2 style='margin-top: 30px;'>🎂 Happy Birthday Anju! 🎂</h2>
        <p>💖 🎉 🎂 🧁 🎈 🎁 💖</p>
    </div>
    """, unsafe_allow_html=True)

    # Embed YouTube video without emojis
    embed_youtube_video("n6M8ELkdPOM")  # Your YouTube video ID

    # Decorative line
    st.markdown('<div class="line"></div>', unsafe_allow_html=True)

    # Message under the video
    st.markdown("<div class='message-under-video'>Enjoy the celebrations, Anju! 🎉 Let’s make this day unforgettable! 🎂💖</div>", unsafe_allow_html=True)

    st.balloons()

    st.markdown("</div>", unsafe_allow_html=True)

# 🔑 Session state to manage login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# 🚀 Run app
add_custom_css()
if not st.session_state.logged_in:
    login()
else:
    birthday_card()

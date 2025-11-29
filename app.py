import os
from dotenv import load_dotenv
load_dotenv()


import streamlit as st
from openai import OpenAI


# ---------------- OPENAI CLIENT ----------------

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --------------------------------------------------
st.set_page_config(page_title="Social Media Agent", layout="wide")

# ------------------- CSS -------------------
st.markdown("""
<style>
body, .stApp { background-color: #ffffff !important; }

.stButton > button {
    background-color: #1E88E5 !important;
    color: white !important;
    padding: 10px 20px !important;
    border-radius: 8px !important;
    font-size: 16px !important;
    border: none;
}

.big-box {
    background-color: #E3F2FD;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    font-size: 20px;
    font-weight: 700;
    cursor: pointer;
    border: 2px solid #90CAF9;
    transition: 0.3s;
}

.big-box:hover {
    background-color: #BBDEFB;
}

.output-box {
    border: 2px solid #1E88E5;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    background-color: #F0F7FF;
}
</style>
""", unsafe_allow_html=True)


# ----------------- SESSION ----------------------
if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "user" not in st.session_state:
    st.session_state.user = None

if "passwd" not in st.session_state:
    st.session_state.passwd = None


# --------------------------------------------------
# PAGE 0 — WELCOME PAGE
# --------------------------------------------------
if st.session_state.page == "welcome":

    top_left, top_center, top_right = st.columns([6, 2, 1])
    with top_right:
        login_btn = st.button("Login")

    if login_btn:
        st.session_state.page = "login"
        st.rerun()

    st.markdown("""
        <h1 style="
            text-align:center; 
            color:#1E88E5; 
            margin-top:20px; 
            font-weight:800;
        ">
            WELCOME TO AI SOCIAL MEDIA AGENT
        </h1>
    """, unsafe_allow_html=True)

    left, right = st.columns([1, 1])

    with left:
        st.markdown("""
            <div style="padding: 20px;">
                <h3 style="color:#1E88E5;">How to Use This Website</h3>
                <ul style="font-size:18px; line-height:1.7;">
                    <li>Create an account or login</li>
                    <li>Select your social media platform</li>
                    <li>Enter brand name & choose a niche</li>
                    <li>Select tone style & add notes</li>
                    <li>Get captions, hashtags & ideas instantly</li>
                    <li>Use them for Instagram, Facebook, YouTube</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with right:
        st.video("how_to_use.mp4")
        register_btn = st.button("Register", use_container_width=True)

        if register_btn:
            st.session_state.page = "register"
            st.rerun()


# --------------------------------------------------
# PAGE 1 — REGISTER
# --------------------------------------------------
if st.session_state.page == "register":

    st.markdown("""
        <div style="text-align:center; margin-top:40px;">
            <h2 style="color:#1E88E5; font-weight:700;">
                Create Your Account
            </h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            width: 400px;
            margin: auto;
            padding: 25px;
            border: 2px solid #64B5F6;
            border-radius: 12px;
            background-color: #ffffff;
            text-align: center;
        ">
        """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    register_btn = st.button("Register", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if register_btn:
        if username.strip() == "" or password.strip() == "":
            st.error("Please enter both username and password.")
        else:
            with open("users.txt", "w") as f:
                f.write(username + "," + password)

            st.success("Account created successfully! Please login now.")
            st.session_state.page = "login"
            st.rerun()


# --------------------------------------------------
# PAGE 2 — LOGIN
# --------------------------------------------------
elif st.session_state.page == "login":

    st.markdown("""
        <div style="text-align:center; margin-top:40px;">
            <h2 style="color:#1E88E5; font-weight:700;">
                Login
            </h2>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="
            width: 400px;
            margin: auto;
            padding: 25px;
            border: 2px solid #64B5F6;
            border-radius: 12px;
            background-color: #ffffff;
            text-align: center;
        ">
        """, unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login", use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    if login_btn:

        try:
            with open("users.txt", "r") as f:
                stored_user, stored_pass = f.read().split(",")
        except:
            stored_user = None
            stored_pass = None

        if stored_user is None:
            st.error("No account found. Please register first.")

        elif username.strip() == "" or password.strip() == "":
            st.error("Please enter both username and password.")

        elif username == stored_user and password == stored_pass:
            st.session_state.page = "platform"
            st.rerun()

        else:
            st.error("Wrong username or password.")


# --------------------------------------------------
# PAGE 3 — PLATFORM SELECT
# --------------------------------------------------
elif st.session_state.page == "platform":

    st.markdown("""
        <div style="display:flex; justify-content:center; margin-top:30px;">
            <h2 style="color:#1E88E5; font-weight:700;">
                Select Your Platform
            </h2>
        </div>
    """, unsafe_allow_html=True)

    center = st.columns([1, 1, 1])[1]

    with center:
        insta = st.button("📸 Instagram")
        fb = st.button("📘 Facebook")
        yt = st.button("▶ YouTube")

    if insta:
        st.session_state.platform = "Instagram"
        st.session_state.page = "details"
        st.rerun()

    if fb:
        st.session_state.platform = "Facebook"
        st.session_state.page = "details"
        st.rerun()

    if yt:
        st.session_state.platform = "YouTube"
        st.session_state.page = "details"
        st.rerun()


# --------------------------------------------------
# PAGE 4 — DETAILS INPUT
# --------------------------------------------------
elif st.session_state.page == "details":

    st.title(f"{st.session_state.platform} Content Details")

    brand = st.text_input("Brand Name")

    niche = st.selectbox(
        "Select Niche",
        ["Skincare", "Clothing", "Food", "Fitness", "Makeup",
         "Jewelry", "Travel", "Education", "Tech", "Lifestyle"]
    )

    tone = st.selectbox("Tone Style", ["Friendly", "Professional", "Emotional", "Fun"])
    notes = st.text_area("Special Notes (Optional)")

    if st.button("Generate Content"):
        st.session_state.brand = brand
        st.session_state.niche = niche
        st.session_state.tone = tone
        st.session_state.notes = notes
        st.session_state.page = "output"
        st.rerun()


# --------------------------------------------------
# PAGE 5 — AI OUTPUT PAGE
# --------------------------------------------------
elif st.session_state.page == "output":

    st.title("Your AI Generated Content")

    brand = st.session_state.brand
    niche = st.session_state.niche
    tone = st.session_state.tone
    notes = st.session_state.notes

    st.info("⏳ Generating using AI... Please wait 3-5 seconds.")

    prompt = f"""
    You are a professional social media content writer.
    Generate the following for:

    Brand: {brand}
    Niche: {niche}
    Tone: {tone}
    Notes: {notes}

    Provide:
    - 8 short captions
    - 8 hashtag sets
    - 8 content ideas
    - an 8-day content creation plan

    Format with clear section headings:
    CAPTIONS:
    1...
    HASHTAGS:
    1...
    IDEAS:
    1...
    PLAN:
    1...
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    output = response.choices[0].message.content

    st.markdown(output)

    if st.button("Start Over"):
        st.session_state.page = "platform"
        st.rerun()
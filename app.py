import streamlit as st
import time
from chatbot import get_answer
import pandas as pd
from datetime import datetime

faq_data = pd.read_csv("data/faqs.csv")

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main App */
.stApp{
    background:#0E1117;
    color:white;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#161B22;
    border-right:1px solid #30363d;
}

/* Sidebar Titles */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3{
    color:white;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    padding:10px;
    background:#1F2937;
    color:white;
    border:1px solid #3B82F6;
    transition:0.3s;
}

.stButton>button:hover{
    background:#2563EB;
    border:1px solid #60A5FA;
    color:white;
}

/* Metrics */
[data-testid="stMetric"]{
    background:#1C2333;
    border-radius:12px;
    padding:10px;
    border:1px solid #2F3B52;
}

/* Chat Input */

/* Chat Messages */
[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:10px;
}

/* Welcome Card */
.welcome-card{
    background:#1E293B;
    border:1px solid #3B82F6;
    border-radius:18px;
    padding:28px;
}

/* Footer */
.footer{
    text-align:center;
    color:gray;
    font-size:14px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "conversation_count" not in st.session_state:
    st.session_state.conversation_count = 0

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title("🤖 AI FAQ Assistant")

    st.markdown("---")

    st.subheader("📚 About")

    st.write(
        """
This chatbot answers questions from a predefined
FAQ database using Python and Streamlit.
"""
    )

    st.markdown("---")

    st.subheader("🛠 Built With")

    st.markdown("""
- 🐍 Python
- 📊 Pandas
- ⚡ Streamlit
- 🤖 AI FAQ Engine
""")

    st.markdown("---")

    st.subheader("💡 Quick Questions")

    quick_questions = [
        "What is AI?",
        "What is Machine Learning?",
        "What is Python?",
        "What is Streamlit?",
        "What is GitHub?",
        "What is Power BI?",
        "Who developed Python?"
    ]

    for question in quick_questions:

        if st.button(question, use_container_width=True):

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question,
                    "time":datetime.now().strftime("%I:%M %p")
                }
            )

            st.session_state.conversation_count += 1

            with st.spinner("🤖 Thinking..."):
                time.sleep(0.7)

            answer = get_answer(question)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer,
                    "time": datetime.now().strftime("%I:%M %p")
                }
            )

            st.rerun()

    st.markdown("---")

    st.subheader("📊 Project Stats")

    col1, col2 = st.columns(2)

    with col1:
       st.metric("FAQs", len(faq_data))

    with col2:
        st.metric("Version", "2.0")

        st.metric( "Questions Asked",
        st.session_state.conversation_count
        )

        st.metric(
    "Knowledge Base",
    f"{len(faq_data)} FAQs"
)
    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = []

        st.rerun()

    st.markdown("---")

    st.success("AI Assistant Online")

    st.caption("👨‍💻 Developed by")

    st.markdown("**Balaji Nadar**")

    # ==========================================================
# MAIN PAGE
# ==========================================================

# ---------- Header ----------

st.markdown("""
<div style="text-align:center;">

<h1 style="
color:#4F8BF9;
font-size:52px;
margin-bottom:0px;
">

🤖 AI FAQ Assistant

</h1>

<p style="
font-size:20px;
color:#9CA3AF;
margin-top:5px;
">

Ask questions about AI, Python, Power BI and GitHub.

</p>

</div>

""", unsafe_allow_html=True)

# ---------- Welcome Card ----------

if len(st.session_state.messages) == 0:

    st.markdown("""

<div class="welcome-card">

<h2>👋 Welcome!</h2>

<p>

Ask me anything about:

</p>

<ul>

<li>🤖 Artificial Intelligence</li>

<li>🐍 Python</li>

<li>📊 Power BI</li>

<li>💻 GitHub</li>

</ul>

<p>

💡 Select a question from the sidebar
or type your own question below.

</p>

</div>

""", unsafe_allow_html=True)

# ---------- Chat History ----------

for message in st.session_state.messages:

    avatar = "🤖" if message["role"] == "assistant" else "🙂"

    with st.chat_message(message["role"], avatar=avatar):

        st.markdown(message["content"])

        if "time" in message:
            st.caption(message["time"])

# ---------- Chat Input ----------

prompt = st.chat_input("💬 Ask me anything...")

if prompt:

    # Save user message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt,
             "time":datetime.now().strftime("%I:%M %p")
        }
    )

    # Thinking animation

    with st.spinner("🤖 Thinking..."):

        time.sleep(0.4)

        answer = get_answer(prompt)

    # Save bot reply

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    st.rerun()

    # ==========================================================
# PROJECT STATS
# ==========================================================

if len(st.session_state.messages) > 0:

    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

st.markdown(
    """
<div class="footer">

🚀 <b>Horizon TechX Internship Project</b>

🐍 Python • 📊 Pandas • ⚡ Streamlit

<br><br>

© 2026 Balaji Nadar

</div>
""",
    unsafe_allow_html=True
)

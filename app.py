import streamlit as st
import time
from chatbot import get_answer

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI FAQ Assistant",
    page_icon="🤖",
    layout="wide",
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Background */
.stApp{
    background-color:#0E1117;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background-color:#161B22;
    border-right:1px solid #30363d;
}

/* Buttons */
.stButton>button{
    width:100%;
    border-radius:12px;
    background:#21262D;
    color:white;
    border:1px solid #4F8BF9;
    transition:0.3s;
}

.stButton>button:hover{
    background:#4F8BF9;
    color:white;
}

/* Metric */
[data-testid="stMetric"]{
    background:#1C2333;
    padding:10px;
    border-radius:15px;
    border:1px solid #2d333b;
}

/* Chat Input */
.stChatInput input{
    border-radius:20px;
}

/* Chat Messages */
[data-testid="stChatMessage"]{
    border-radius:15px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🤖 AI FAQ Assistant")

    st.markdown("---")

    st.subheader("📚 About")

    st.write("""
Welcome!

This chatbot answers questions from a predefined FAQ database.

### 🛠 Built With

🐍 Python

📊 Pandas

⚡ Streamlit

💬 NLP Matching
""")

    st.markdown("---")

    st.subheader("💡 Quick Questions")

    examples = [
        "What is AI?",
        "What is Python?",
        "What is GitHub?",
        "What is Power BI?",
        "Who developed Python?"
    ]

    for question in examples:

        if st.button(question):

            st.session_state.messages.append(
                {
                    "role":"user",
                    "content":question
                }
            )

            with st.spinner("🤖 Thinking..."):
                time.sleep(0.8)

            answer = get_answer(question)

            st.session_state.messages.append(
                {
                    "role":"assistant",
                    "content":answer
                }
            )

            st.rerun()

    st.markdown("---")

    st.subheader("📊 Project Stats")

    st.metric("FAQs", "10")
    st.metric("Version", "1.0")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages=[]

        st.rerun()

    st.markdown("---")

    st.caption("👨‍💻 Developed by")
    st.caption("**Balaji Nadar**")

# ---------------- HEADER ---------------- #

st.markdown("""
<h1 style='text-align:center;
color:#4F8BF9;
font-size:48px;'>

🤖 AI FAQ Assistant

</h1>

<p style='text-align:center;
font-size:18px;
color:gray;'>

Your Intelligent FAQ Companion

</p>

""", unsafe_allow_html=True)

# ---------------- WELCOME ---------------- #

if len(st.session_state.messages)==0:

    st.markdown("""

<div style="

padding:25px;

border-radius:20px;

background:#1C2333;

border:1px solid #4F8BF9;

">

<h2>👋 Welcome!</h2>

<p>

Ask me anything about

<ul>

<li>🤖 Artificial Intelligence</li>

<li>🐍 Python</li>

<li>📊 Power BI</li>

<li>💻 GitHub</li>

</ul>

Start by typing your question below.

</p>

</div>

""",unsafe_allow_html=True)
# ---------------- DISPLAY CHAT ---------------- #

for message in st.session_state.messages:

    avatar = "🤖" if message["role"] == "assistant" else "🙂"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------------- CHAT INPUT ---------------- #

prompt = st.chat_input("💬 Ask me anything...")

if prompt:

    # Display User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show Thinking Animation
    with st.spinner("🤖 Thinking..."):
        time.sleep(1)

    # Get Chatbot Response
    answer = get_answer(prompt)

    # Display Assistant Response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()

# ---------------- FOOTER ---------------- #

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.caption("🚀 Horizon TechX")

with col2:
    st.caption("🤖 AI FAQ Assistant")

with col3:
    st.caption("Version 1.0")

st.markdown(
    """
<div style='text-align:center;
padding:10px;
color:gray;
font-size:14px;'>

Built with ❤️ using <b>Python</b> • <b>Pandas</b> • <b>Streamlit</b>

<br><br>

© 2026 Balaji Nadar

</div>
""",
unsafe_allow_html=True
)

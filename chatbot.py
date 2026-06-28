import pandas as pd
import difflib
import re

# Load FAQ dataset
faq_data = pd.read_csv("data/faqs_200.csv")

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", "", text)
    return text.strip()

# Greetings
greetings = {
    "hi": "👋 Hello! How can I help you today?",
    "hello": "👋 Hello! Ask me anything about AI, Python, SQL, Power BI, GitHub and more.",
    "hey": "👋 Hi! I'm your AI FAQ Assistant.",
    "good morning": "☀️ Good morning! How can I help you?",
    "good afternoon": "🌤️ Good afternoon! What would you like to know?",
    "good evening": "🌙 Good evening! Ask me any technical question.",
    "thanks": "😊 You're welcome! Happy to help.",
    "thank you": "😊 You're welcome! Have a great day!",
    "bye": "👋 Goodbye! Have a wonderful day!"
}

small_talk = {
    "who are you": "🤖 I'm an AI FAQ Assistant developed by Balaji Nadar. I answer questions from my knowledge base about AI, Python, SQL, Power BI, GitHub and more.",

    "what are you": "🤖 I'm an AI FAQ Assistant built using Python, Streamlit and Pandas.",

    "who made you": "👨‍💻 I was developed by Balaji Nadar as part of the Horizon TechX Internship.",

    "who created you": "👨‍💻 I was developed by Balaji Nadar as part of the Horizon TechX Internship.",

    "how are you": "😊 I'm doing great! Thanks for asking. How can I help you today?",

    "what can you do": "🚀 I can answer questions about AI, Python, SQL, GitHub, Streamlit, Power BI, Data Science and more.",

    "help": "💡 Try asking questions like:\n\n• What is AI?\n• Explain Python\n• What is SQL?\n• What is GitHub?\n• What is Power BI?",

    "your name": "🤖 My name is AI FAQ Assistant.",

    "who is balaji": "👨‍💻 Balaji Nadar is the developer of this AI FAQ Assistant."
}

def get_answer(user_question):

    user_question = clean_text(user_question)

    # -----------------------------
    # Greetings
    # -----------------------------
    if user_question in greetings:
        return greetings[user_question]
    
    if user_question in small_talk:
        return small_talk[user_question]

    questions = faq_data["Question"].apply(clean_text).tolist()

    # -----------------------------
    # Exact Match
    # -----------------------------
    if user_question in questions:
        index = questions.index(user_question)
        return faq_data.iloc[index]["Answer"]

    # -----------------------------
    # Fuzzy Match
    # -----------------------------
    match = difflib.get_close_matches(
        user_question,
        questions,
        n=1,
        cutoff=0.60
    )

    if match:
        index = questions.index(match[0])
        return faq_data.iloc[index]["Answer"]

    # -----------------------------
    # Keyword Match
    # -----------------------------
    user_words = set(user_question.split())

    best_score = 0
    best_answer = None

    for _, row in faq_data.iterrows():

        question = clean_text(row["Question"])

        question_words = set(question.split())

        score = len(user_words & question_words)

        if score > best_score:
            best_score = score
            best_answer = row["Answer"]

    if best_score >= 2:
        return best_answer

    # -----------------------------
    # Not Found
    # -----------------------------
    return """
❌ Sorry! I couldn't find an answer.

### 💡 Try asking:

• What is AI?

• Explain Python

• What is SQL?

• Tell me about GitHub

• What is Streamlit?

• What is Power BI?

Or choose a question from the sidebar.
"""
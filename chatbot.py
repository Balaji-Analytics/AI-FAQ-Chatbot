import pandas as pd

print("✅ NEW chatbot.py loaded")

faq_data = pd.read_csv("data/faqs.csv")


def get_answer(user_question):

    # Clean user input
    user_question = (
        user_question.lower()
        .strip()
        .replace("?", "")
    )

    # Compare against each FAQ
    for _, row in faq_data.iterrows():

        question = (
            row["Question"]
            .lower()
            .strip()
            .replace("?", "")
        )

        if question == user_question:
            return row["Answer"]

    return """
🤖 Sorry! I couldn't find a matching answer.

💡 Try one of these:

• What is AI?
• What is Python?
• What is Power BI?
• What is GitHub?
• Who developed Python?
"""

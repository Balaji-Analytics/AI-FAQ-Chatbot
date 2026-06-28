# 🤖 AI FAQ Assistant

An intelligent FAQ chatbot built using **Python**, **Pandas**, and **Streamlit**. It answers user questions using **exact matching**, **fuzzy matching**, and **keyword search**, providing fast and interactive responses through a modern chat interface.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

# 📖 Overview

The **AI FAQ Assistant** is a simple yet intelligent chatbot that helps users find answers from a predefined FAQ database.

The chatbot supports:

- Exact Question Matching
- Fuzzy Search (handles typing mistakes)
- Keyword Matching
- Greetings & Small Talk
- Interactive Chat Interface
- Quick Question Buttons
- Responsive Streamlit UI

This project was developed as part of the **Horizon TechX Internship** to demonstrate Python programming, chatbot development, data handling, and Streamlit web application skills.

---

# ✨ Features

- 🤖 AI FAQ Chatbot
- 💬 Interactive Chat Interface
- 🔍 Exact Question Matching
- 🧠 Fuzzy Search using Difflib
- 🔑 Keyword Based Search
- 👋 Greetings & Small Talk Support
- 📚 200+ Frequently Asked Questions
- ⚡ Fast Response Time
- 🎨 Modern Dark Theme UI
- 📊 Project Statistics
- 🗑️ Clear Chat Functionality
- 📱 Responsive Sidebar
- 💻 Easy to Customize
- 🚀 Ready for Streamlit Cloud Deployment

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Logic |
| Pandas | FAQ Data Management |
| Streamlit | Web Application |
| Difflib | Fuzzy Search |
| Regex (re) | Text Cleaning |
| Git | Version Control |
| GitHub | Source Code Hosting |

---

# 📂 Project Structure

```
AI-FAQ-Chatbot
│
├── assets
│   └── style.css
│
├── data
│   └── faqs_200.csv
│
├── images
│
├── app.py
├── chatbot.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📸 Screenshots

## Home Screen

Add a screenshot here.

```
images/home.png
```

---

## Chat Interface

Add a screenshot here.

```
images/chat.png
```

---

## Sidebar

Add a screenshot here.

```
images/sidebar.png
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Balaji-Analytics/AI-FAQ-Chatbot.git
```

Go to the project folder

```bash
cd AI-FAQ-Chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

The application will open at

```
http://localhost:8501
```

---

# 💬 Example Questions

You can ask questions like:

- What is AI?
- What is Machine Learning?
- Explain Python
- What is Streamlit?
- What is GitHub?
- What is Power BI?
- What is SQL?
- What is Data Science?
- Who developed Python?
- What is Deep Learning?

The chatbot also understands greetings such as:

- Hi
- Hello
- Hey
- Thanks
- Thank You
- Bye

---

# 🧠 Search Methods

The chatbot searches answers in three stages.

### 1️⃣ Exact Match

Returns the answer immediately if the question exactly matches the FAQ.

---

### 2️⃣ Fuzzy Match

Uses Python's **Difflib** to understand spelling mistakes.

Example:

```
What is Pyhton?
```

↓

```
What is Python?
```

---

### 3️⃣ Keyword Match

Finds the closest FAQ based on common keywords.

Example:

```
Tell me about GitHub
```

↓

Returns the GitHub FAQ.

---

# 📈 Current Statistics

- 📚 200+ FAQs
- 🤖 AI FAQ Engine
- 💬 Interactive Chat UI
- 🔍 Smart Search
- ⚡ Fast Responses
- 🌙 Dark Theme
- 🚀 Streamlit Web App

---

# 🔮 Future Improvements

- Voice Input
- Voice Output
- AI Generated Responses
- OpenAI API Integration
- User Authentication
- FAQ Search Filter
- Conversation History
- Export Chat
- Admin Dashboard
- Database Integration
- Multi-language Support

---

# 👨‍💻 Author

**Balaji Nadar**

Data Analytics Enthusiast

- Python
- SQL
- Power BI
- Excel
- Streamlit
- GitHub

GitHub

https://github.com/Balaji-Analytics

LinkedIn

https://www.linkedin.com/in/balaji-nadar-3830a22a5/

---

# ⭐ If you like this project

Give this repository a ⭐ on GitHub.

It motivates me to build more open-source projects.

---

## 📄 License

This project is developed for learning and internship purposes.

© 2026 Balaji Nadar. All Rights Reserved.
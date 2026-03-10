# c v1.0

## Description

**Groq Desktop Chatbot** is a desktop-based conversational assistant developed in **Python** that integrates the **Groq API** with a graphical user interface built using **Tkinter**.

The application enables users to interact with a **Large Language Model (LLM)** in real time through a clean and intuitive desktop interface. It supports multiple conversational styles through configurable **chatbot personalities**, allowing the assistant to adapt its tone and behavior depending on the selected mode.

The system is designed with a modular architecture that separates **configuration, chatbot logic, and user interface**, making the project easy to maintain, extend, and integrate with additional features in the future.

The application also includes features for **conversation management**, such as clearing the chat history and exporting conversations to text files.

---

# Features

* **Real-time AI Chat:** Communicate with a Groq-powered LLM directly from a desktop interface.
* **Multiple Chatbot Personalities:** Change the chatbot's behavior dynamically.
* **Conversation History:** Maintains contextual conversation during the session.
* **Export Conversations:** Save chats locally as `.txt` files.
* **Error Handling:** Displays connection or API errors inside the chat window.
* **Dynamic Personality Switching:** Changing the personality automatically resets the conversation context.

---

# Available Personalities

The chatbot behavior can be modified using the personality selector:

* **Friendly:** Helpful and polite responses.
* **Serious:** Professional and direct communication style.
* **Sarcastic:** Humor and sarcastic tone.
* **Motivational:** Positive and encouraging responses.
* **Unfriendly:** Cold and blunt responses.

These personalities are implemented through system prompts that modify the model's behavior.

---

# System Architecture

The project follows a **modular architecture** to separate responsibilities between components.

```
groq-chatbot/
│
├── main.py        # Application entry point
├── ui.py          # Graphical user interface (Tkinter)
├── chatbot.py     # Chatbot logic and Groq API integration
├── config.py      # Environment configuration and personalities
├── .env           # Environment variables (API key)
└── README.md
```

### Component Overview

**main.py**

* Initializes the Tkinter application.
* Loads the graphical interface.

**ui.py**

* Handles all UI components and user interactions.
* Sends messages to the chatbot and displays responses.

**chatbot.py**

* Manages the conversation logic.
* Communicates with the Groq API.
* Maintains message history and context.

**config.py**

* Loads environment variables.
* Defines available chatbot personalities.

---

# Tech Stack

### Programming Language

* **Python**

### Libraries

* **Tkinter** — Desktop graphical interface
* **Groq** — Communication with Groq LLM API
* **python-dotenv** — Environment variable management

### AI Model

```
llama-3.1-8b-instant
```

Provided through the **Groq API** for high-performance inference.

---

# Project Setup

## 1. Clone the repository

```bash
git clone https://github.com/OvidioMT/Groq-Desktop-Chatbot.git
cd groq-chatbot
```

---

## 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
.\venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install groq python-dotenv
```

---

## 4. Configure environment variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can obtain an API key from:

https://console.groq.com

---

## 5. Run the application

```bash
python main.py
```

The chatbot desktop interface should open automatically.

---

# Application Usage

1. Select a **chatbot personality** from the dropdown menu.
2. Type a message in the input box.
3. Press **Enter** or click **Send**.
4. The chatbot will generate a response using the Groq API.
5. Additional options:

   * **Clear:** Reset the chat history.
   * **Save:** Export the conversation to a `.txt` file.

---

# Credits

### Author

* Ovidio Martinez Taleno


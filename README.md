# autostream-ai-agent
AI conversational agent with RAG and lead capture

AutoStream AI Agent 
📌 Project Overview

This project is a Conversational AI Agent built for a fictional SaaS product, AutoStream. The agent simulates a real-world business use case where social interactions are converted into qualified leads. It can understand user intent, answer product-related queries using a knowledge base, and capture lead information when a user shows high purchase intent.

How to Run the Project Locally

Step 1: Clone the Repository
git clone https://github.com/your-username/autostream-ai-agent.git
cd autostream-ai-agent
Step 2: Install Dependencies
pip install -r requirements.txt
Step 3: Run the Application
python app.py
Step 4: Interact with the Chatbot

Type queries like:
"Hi"
"Tell me pricing"
"I want to try Pro plan"


🧠 Architecture Explanation
This project uses a modular architecture inspired by agent-based systems. Although lightweight, it follows principles similar to LangGraph workflows, where different components handle specific responsibilities such as intent detection, knowledge retrieval, and action execution.

LangGraph-style design was chosen because it allows structured control over conversational flow, making it easier to manage multi-step interactions like lead collection. Instead of a single monolithic function, the logic is broken into smaller units like intent detection, RAG response, and tool execution.

State management is handled using a Python dictionary that persists user information across multiple conversation turns. This includes tracking user intent, lead capture stage, and collected details such as name, email, and platform. This ensures the chatbot can maintain context over 5–6 turns, which is essential for real-world conversational systems.


📱 WhatsApp Integration (Using Webhooks)
To integrate this AI agent with WhatsApp, a service like Twilio API can be used. Twilio provides a WhatsApp Business API that allows sending and receiving messages programmatically.

When a user sends a message on WhatsApp, Twilio forwards the message to a backend server via a webhook (HTTP request). This webhook endpoint will contain the chatbot logic (our Python application). The server processes the incoming message, generates a response using the agent, and sends the reply back to the user via Twilio’s API.

The flow works as follows:

User sends message on WhatsApp
Twilio receives message
Twilio triggers webhook (POST request to backend)
Backend processes message using chatbot logic
Response sent back through Twilio API

This setup enables real-time conversational AI deployment on WhatsApp.


🎬 Demo (Video Link)
https://drive.google.com/drive/folders/1G74ivM7FyeR3rLNDn5dlfhHXWh6vWaD1?usp=sharing

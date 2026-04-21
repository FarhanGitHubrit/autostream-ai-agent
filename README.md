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

This project has a modular design that was inspired by systems based on agents. It is lightweight, but it works in a way that is similar to LangGraph workflows, where different parts are in charge of different tasks like finding information, executing actions, and detecting intent.

I chose a LangGraph-style design because it lets you control the flow of conversation in a structured way, which makes it easier to handle multi-step interactions like collecting leads. Instead of one big function, the logic is split up into smaller pieces, such as intent detection, RAG response, and tool execution.


A Python dictionary keeps track of user information across multiple conversation turns, which is how state management works. This includes keeping track of the user's intent, the lead capture stage, and the information that was collected, like their name, email address, and platform. This makes sure that the chatbot can keep track of what's going on over 5–6 turns, which is important for real-world


📱 WhatsApp Integration (Using Webhooks)

You can use a service like Twilio API to connect this AI agent to WhatsApp. You can send and receive messages through the WhatsApp Business API from Twilio.

Twilio sends a message from WhatsApp to a backend server through a webhook (HTTP request) when the user sends it. The chatbot logic (our Python app) will be in this webhook endpoint. The server handles the incoming message, uses the agent to create a response, and then sends the response back to the user through Twilio's API.


The flow works as follows:

User sends message on WhatsApp
Twilio receives message
Twilio triggers webhook (POST request to backend)
Backend processes message using chatbot logic
Response sent back through Twilio API

This setup enables real-time conversational AI deployment on WhatsApp.


🎬 Demo (Video Link)
https://drive.google.com/drive/folders/1G74ivM7FyeR3rLNDn5dlfhHXWh6vWaD1?usp=sharing

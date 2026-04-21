import json

# ---------------------------
# Load Knowledge Base (RAG)
# ---------------------------
with open("knowledge.json", "r") as f:
    knowledge = json.load(f)

# ---------------------------
# Memory (State Management)
# ---------------------------
memory = {
    "intent": None,
    "name": None,
    "email": None,
    "platform": None,
    "lead_stage": False
}

# ---------------------------
# Intent Detection (FIXED)
# ---------------------------
def detect_intent(user_input):
    text = user_input.lower()

    # HIGH INTENT FIRST (strong signals)
    if any(word in text for word in ["buy", "start", "subscribe", "try", "want"]):
        return "high_intent"

    # Greeting
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    # Pricing
    elif any(word in text for word in ["price", "pricing", "cost"]):
        return "pricing"

    # Plan info (only when not high intent)
    elif "plan" in text:
        return "pricing"

    else:
        return "other"

# ---------------------------
# RAG Response
# ---------------------------
def get_rag_response(query):
    q = query.lower()

    if "basic" in q:
        return knowledge["pricing"]["basic"]

    elif "pro" in q:
        return knowledge["pricing"]["pro"]

    elif "refund" in q:
        return knowledge["policies"]["refund"]

    elif "support" in q:
        return knowledge["policies"]["support"]

    else:
        return (
            f"{knowledge['pricing']['basic']}\n"
            f"{knowledge['pricing']['pro']}"
        )

# ---------------------------
# Lead Capture Tool
# ---------------------------
def mock_lead_capture(name, email, platform):
    print(f"\n✅ Lead captured successfully: {name}, {email}, {platform}\n")

# ---------------------------
# Chatbot Logic (FIXED FLOW)
# ---------------------------
def chatbot(user_input):

    # ✅ PRIORITY: If already collecting lead → DO NOT detect intent again
    if memory["lead_stage"]:

        if memory["name"] is None:
            memory["name"] = user_input
            return "Great! Please provide your email."

        elif memory["email"] is None:
            memory["email"] = user_input
            return "Which platform do you create content on? (YouTube/Instagram)"

        elif memory["platform"] is None:
            memory["platform"] = user_input

            # ✅ Call tool ONLY after full data
            mock_lead_capture(
                memory["name"],
                memory["email"],
                memory["platform"]
            )

            # Reset flow (important)
            memory["lead_stage"] = False
            return "🎉 You're all set! Our team will reach out soon."

    # ---------------------------
    # Normal Intent Flow
    # ---------------------------
    intent = detect_intent(user_input)
    memory["intent"] = intent

    if intent == "greeting":
        return "Hi! Welcome to AutoStream 🚀 How can I help you today?"

    elif intent == "pricing":
        return get_rag_response(user_input)

    elif intent == "high_intent":
        memory["lead_stage"] = True
        memory["name"] = None
        memory["email"] = None
        memory["platform"] = None
        return "Awesome! Let's get you started. What's your name?"

    else:
        return "I can help with pricing, plans, or getting you started!"

# ---------------------------
# Run Chat Loop
# ---------------------------
if __name__ == "__main__":
    print("🤖 AutoStream AI Agent (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = chatbot(user_input)
        print("Bot:", response)
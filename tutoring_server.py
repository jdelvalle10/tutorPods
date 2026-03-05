import threading
import ctypes
import datetime
import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic K-12 Guardrail Keywords
FORBIDDEN_WORDS = [
    "violence", "kill", "suicide", "bomb", "drugs", "sex", "porn", 
    "hack", "cheat", "plagiarize", "write my essay", "terrorism", 
    "weapon", "abuse", "self-harm", "bullying", "racism", "hate speech", 
    "harassment", "profanity", "explicit content", "gambling", 
    "alcohol", "tobacco", "vaping", "dark web", "illegal activity", 
    "child exploitation", "extremism", "graphic content", "violence against animals", "fuck", "dick", "pussy", "tits", "boobs", "blowjob"
]

# Socratic System Prompt for DeepSeek R1 8B
SYSTEM_PROMPT = {
    "role": "system",
    "content": """
    You are a helpful, encouraging, and safe AI tutor for K-12 students. 
    Your goal is to help the student learn using the Socratic method. 
    DO NOT give the student direct answers to their assignments, code, or math problems. 
    Instead, ask guiding questions, provide hints, and break down the problem into smaller steps 
    to help them arrive at the answer themselves. Always maintain a positive and age-appropriate tone.
    """
}

def show_windows_popup(ip_address, timestamp, user_prompt):
    """Generates a native Windows 11 OS pop-up alert on the server desktop."""
    title = "K-12 AI Guardrail Alert"
    message = f"Inappropriate Prompt Detected!\n\nIP Address: {ip_address}\nTime: {timestamp}\nPrompt: {user_prompt}"
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x10 | 0x40000)

def is_inappropriate(prompt):
    """Checks the student's prompt against forbidden keywords."""
    prompt_lower = prompt.lower()
    return any(word in prompt_lower for word in FORBIDDEN_WORDS)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    
    # Extract the conversation history sent by the JavaScript frontend
    conversation_history = data.get("messages", [])
    
    if not conversation_history:
        return jsonify({"error": "No messages provided."}), 400

    # Get the latest message to check against guardrails and logs
    latest_user_message = conversation_history[-1].get("content", "")
    client_ip = request.remote_addr 
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardrail Check on the newest prompt
    if is_inappropriate(latest_user_message):
        terminal_alert = f"""
        =========================================================
        [!] INAPPROPRIATE CONTENT BLOCKED
        =========================================================
        Time:      {timestamp}
        IP Address: {client_ip}
        Prompt:    {latest_user_message}
        =========================================================
        """
        print(terminal_alert)
        
        threading.Thread(target=show_windows_popup, args=(client_ip, timestamp, latest_user_message)).start()
        
        return jsonify({"response": "I am a school AI tutor. Please keep your questions appropriate for a classroom environment."}), 403

    # Combine the Socratic System Prompt with the entire conversation history
    full_payload_messages = [SYSTEM_PROMPT] + conversation_history

    # Forward the context-aware payload to Local DeepSeek-R1-8B via Ollama
    payload = {
        "model": "deepseek-r1:8b",
        "messages": full_payload_messages,
        "stream": False
    }

    try:
        ollama_response = requests.post("http://localhost:11434/api/chat", json=payload)
        ollama_response.raise_for_status()
        reply = ollama_response.json().get("message", {}).get("content", "")
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": "Failed to connect to the AI model."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, render_template_string
from chatbot.nlp import preprocess, classify_intent
from chatbot.db_handler import get_prerequisites, get_schedule, get_policies, get_course_info
from chatbot.response import generate_response

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>Academic Advisor Chatbot</title>
<style>
body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; padding: 0 20px; }
h1 { color: #333; }
#chatbox { border: 1px solid #ddd; padding: 15px; height: 400px; overflow-y: auto; margin-bottom: 10px; border-radius: 8px; background: #fafafa; }
.user-msg { text-align: right; margin: 8px 0; }
.user-msg span { background: #007bff; color: white; padding: 8px 14px; border-radius: 18px; display: inline-block; }
.bot-msg { text-align: left; margin: 8px 0; }
.bot-msg span { background: #e9ecef; color: #333; padding: 8px 14px; border-radius: 18px; display: inline-block; }
#input-row { display: flex; gap: 8px; }
#user-input { flex: 1; padding: 10px; border: 1px solid #ddd; border-radius: 20px; font-size: 14px; }
button { padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 20px; cursor: pointer; font-size: 14px; }
button:hover { background: #0056b3; }
</style></head>
<body>
<h1>Academic Advisor Chatbot</h1>
<div id="chatbox"><div class="bot-msg"><span>Hi! I'm your Academic Advisor. Ask me about course prerequisites, schedules, or department policies.</span></div></div>
<div id="input-row">
<input id="user-input" type="text" placeholder="Ask a question..." onkeypress="if(event.key==='Enter')sendMsg()">
<button onclick="sendMsg()">Send</button>
</div>
<script>
function sendMsg() {
  const input = document.getElementById('user-input');
  const msg = input.value.trim();
  if (!msg) return;
  const box = document.getElementById('chatbox');
  box.innerHTML += '<div class="user-msg"><span>' + msg + '</span></div>';
  input.value = '';
  fetch('/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({message:msg})})
    .then(r=>r.json()).then(d=>{box.innerHTML+='<div class="bot-msg"><span>'+d.response+'</span></div>';box.scrollTop=box.scrollHeight;});
}
</script>
</body></html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    tokens = preprocess(user_message)
    intent = classify_intent(tokens)
    response = generate_response(intent, user_message, tokens)
    return jsonify({"response": response, "intent": intent})

if __name__ == "__main__":
    app.run(debug=True, port=5000)

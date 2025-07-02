from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

VOICEFLOW_API_URL = "https://general-runtime.voiceflow.com/state/user/685bc71600cd24f6c102cf12/interact"

@app.route('/zadarma', methods=['POST'])
def zadarma_webhook():
    data = request.form.to_dict() or request.get_json()
    user_id = data.get("caller_id") or "zadarma_user"
    message = {"type": "text", "payload": {"message": "A sunat cineva pe numărul Zadarma."}}

    headers = {
        "Content-Type": "application/json"
    }

    vf_response = requests.post(
        f"{VOICEFLOW_API_URL}",
        headers=headers,
        json={
            "userID": user_id,
            "request": message
        }
    )

    return jsonify({"status": "forwarded", "vf_status": vf_response.status_code}), 200

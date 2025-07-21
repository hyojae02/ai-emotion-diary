from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.model import analyze_emotion_korean

app = Flask(__name__)
CORS(app)  # 👈 이 줄 추가! 모든 도메인에서 접근 허용

@app.route("/")
def home():
    return "Hello, Sentiment Diary!"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    result = analyze_emotion_korean(text)

    return jsonify({
        "input": text,
        "translation": result.get("translation", ""),
        "emotions": result.get("emotions", [])
    })


if __name__ == "__main__":
    app.run(debug=True)

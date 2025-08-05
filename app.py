from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from backend.model import analyze_emotion_korean
from backend.db import save_diary_entry, init_db

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

CORS(app)  # 👈 이 줄 추가! 모든 도메인에서 접근 허용

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        text = data["text"]
        result = analyze_emotion_korean(text)

        # DB 저장
        save_diary_entry(
            text=text,
            translation=result.get("translation", ""),
            emotions=result.get("emotions", [])
        )
        return jsonify({
            "input": text,
            "translation": result.get("translation", ""),
            "emotions": result.get("emotions", [])
        })
    except Exception as e:
        print(f"[ERROR] /analyze: {e}")
        return jsonify({"error": "서버 내부 오류가 발생했습니다."}), 500



if __name__ == "__main__":
    init_db()
    app.run(debug=True)

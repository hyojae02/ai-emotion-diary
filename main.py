from backend.model import analyze_emotion_korean

if __name__ == "__main__":
    user_input = input("내용을 입력하세요: ")
    result = analyze_emotion_korean(user_input)

    print("⎯" * 40)
    print(f"[입력] {result['input']}")
    print(f"[번역] {result['translation']}")
    print(f"[감정] {result['emotions']}")

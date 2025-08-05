# model.py

from transformers import pipeline
from deep_translator import GoogleTranslator

# 한-영 번역
def translate_ko_en(text):
    return GoogleTranslator(source='ko', target='en').translate(text)

# 영-한 번역
def translate_en_ko(text):
    return GoogleTranslator(source='en', target='ko').translate(text)

# 감정 분석 모델 로딩
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

# 감정 분석 전체 함수
def analyze_emotion_korean(text):
    translated = translate_ko_en(text)
    result_list = emotion_model(translated)

    if isinstance(result_list[0], list):
        result_list = result_list[0]

    emotions = []
    for result in result_list:
        label = result["label"]
        score = result["score"]
        translated_label = translate_en_ko(label)
        emotions.append(f"{translated_label}({score:.2f})")

    # emotion_str = ", ".join(emotions)  # 이 줄 대신

    return {
        "input": text,
        "translation": translated,
        "emotions": emotions   # 문자열이 아니라 리스트 자체를 넘김
    }



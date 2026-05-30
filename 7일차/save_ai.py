import requests
from datetime import datetime

url = "http://localhost:11434/api/generate"

questions = [
    "1인 기업 운영자에게 AI가 어떻게 도움이 될 수 있어? 3줄로 요약해줘.",
    "파이썬을 처음 배우는 사람에게 가장 중요한 것은 뭐야? 3줄로.",
    "매일 반복되는 업무를 AI로 자동화하려면 어디서 시작해야 해? 3줄로."
]

def ask_ai(prompt):
    data = {
        "model": "qwen3.5:2b",
        "prompt": prompt,
        "stream": False,
        "think": False,
        "options": {"num_predict": 300}
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result.get("response", "")

filename = f"ai_answers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    for i, question in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] 질문 중...")
        answer = ask_ai(question)
        print(f"Q: {question}")
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 50 + "\n")

print(f"저장 완료: {filename}")
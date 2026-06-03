import requests
from datetime import datetime

url = "http://localhost:11434/api/generate"

def ask_ai(prompt, max_tokens=500):
    data = {
        "model": "qwen3.5:2b",
        "prompt": "반드시 한국어로만 답해줘.\n\n" + prompt,
        "stream": False,
        "think": False,
        "options": {"num_predict": max_tokens}
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result.get("response", "")

def make_questions():
    prompt = """1인 기업가이자 AI 유튜버에게 오늘 도움이 될 질문 3개를 만들어줘.
반드시 아래 형식으로만 답해줘:
1. (질문)
2. (질문)
3. (질문)

다른 설명 없이 질문 3개만 작성해."""
    raw = ask_ai(prompt, max_tokens=300)
    lines = [l.strip() for l in raw.strip().splitlines() if l.strip()]
    questions = []
    for line in lines:
        if line.startswith(("1.", "2.", "3.")):
            questions.append(line[2:].strip())
    return questions if len(questions) == 3 else lines[:3]

today = datetime.now().strftime('%Y%m%d')
filename = f"briefing_{today}.txt"

print(f"[Cravveo 아침 브리핑 — {datetime.now().strftime('%Y-%m-%d')}]")
print("질문 생성 중...")
print("-" * 50)

questions = make_questions()

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== Cravveo 아침 브리핑 {datetime.now().strftime('%Y-%m-%d')} ===\n\n")

    for i, question in enumerate(questions, 1):
        print(f"[{i}/3] 답변 중: {question}")
        answer = ask_ai(question)
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 40 + "\n\n")

print(f"저장 완료: {filename}")
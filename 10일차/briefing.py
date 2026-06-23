import requests
import random
from datetime import datetime

url = "http://localhost:11434/api/generate"

def ask_ai(prompt, max_tokens=150):
    data = {
        "model": "qwen2.5:1.5b",
        "prompt": "반드시 한국어로만 답해줘.\n\n" + prompt,
        "stream": False,
        "options": {"num_predict": max_tokens}
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result.get("response", "")

CRAVVEO_CONTEXT = """크라베오 컴퍼니(Cravveo Company)는 한국의 1인 기업이다.
운영자는 AI 초보자로, 100일 동안 AI 파인튜닝을 완전 정복하는 도전을 유튜브에 공개(Build in Public)하고 있다.
매일 배운 것을 영상으로 기록하며, 현재 Google Colab + Unsloth + Gemma-2B 모델로 LoRA 파인튜닝을 실험 중이다.
목표는 크라베오만의 AI 어시스턴트를 만드는 것이다.
유튜브 채널명: 크라베오 컴퍼니 (Cravveo Company)"""

QUESTION_POOL = [
    "크라베오 컴퍼니는 어떤 회사인가요?",
    "크라베오 컴퍼니의 운영자는 어떤 사람인가요?",
    "100일 AI 파인튜닝 도전을 시작한 이유는 무엇인가요?",
    "Build in Public이란 무엇인가요?",
    "크라베오가 파인튜닝에 사용하는 도구는 무엇인가요?",
    "Gemma-2B 모델은 어떤 모델인가요?",
    "LoRA 파인튜닝이란 무엇인가요?",
    "크라베오 컴퍼니의 최종 목표는 무엇인가요?",
    "Google Colab을 사용하는 이유는 무엇인가요?",
    "Unsloth란 무엇이고 왜 사용하나요?",
    "크라베오 컴퍼니의 유튜브 채널에서는 어떤 내용을 다루나요?",
    "AI 초보자가 파인튜닝을 혼자 배울 수 있나요?",
    "크라베오 AI 어시스턴트는 어떤 역할을 할 예정인가요?",
    "파인튜닝과 일반 AI 사용의 차이점은 무엇인가요?",
    "크라베오 컴퍼니는 어떻게 매일 진행 상황을 공개하나요?",
    "HuggingFace란 무엇이고 크라베오는 왜 사용하나요?",
    "크라베오의 데이터셋은 어떤 내용으로 구성되어 있나요?",
    "1인 기업이 AI 파인튜닝을 하면 어떤 장점이 있나요?",
    "크라베오 컴퍼니의 100일 도전 중 가장 어려운 점은 무엇인가요?",
    "파인튜닝한 AI 모델은 어디에 활용할 수 있나요?",
    "크라베오가 매일 영상을 올리는 이유는 무엇인가요?",
    "AI 파인튜닝을 배우는 데 얼마나 걸리나요?",
    "크라베오 컴퍼니의 수익 모델은 무엇인가요?",
    "크라베오 컴퍼니를 시작하게 된 계기는 무엇인가요?",
    "파인튜닝 중 loss란 무엇을 의미하나요?",
    "LoRA 어댑터를 사용하면 어떤 점이 좋은가요?",
    "크라베오의 AI 도전이 일반인에게 주는 영감은 무엇인가요?",
    "크라베오 컴퍼니는 앞으로 어떤 방향으로 성장할 계획인가요?",
    "GPU 없이도 AI 파인튜닝이 가능한가요?",
    "크라베오의 유튜브 채널을 구독해야 하는 이유는 무엇인가요?",
]

today = datetime.now().strftime('%Y%m%d')
filename = f"briefing_{today}.txt"

print(f"[Cravveo 아침 브리핑 — {datetime.now().strftime('%Y-%m-%d')}]")
print("-" * 50)

random.seed(today)
questions = random.sample(QUESTION_POOL, 3)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== Cravveo 아침 브리핑 {datetime.now().strftime('%Y-%m-%d')} ===\n\n")

    for i, question in enumerate(questions, 1):
        print(f"[{i}/3] 답변 중: {question}")
        answer = ask_ai(f"{CRAVVEO_CONTEXT}\n\n질문: {question}\n\n위 정보를 바탕으로 간결하게 답변해줘.")
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 40 + "\n\n")

print(f"저장 완료: {filename}")

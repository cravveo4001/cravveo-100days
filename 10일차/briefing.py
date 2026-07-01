# 크라베오 AI 아침 브리핑 자동화
# Cravveo AI Morning Briefing Automation
#
# Day 010: qwen2.5:1.5b 기본 모델 + 하드코딩 컨텍스트
# Day 034: cravveo 파인튜닝 모델로 업그레이드 (크라베오를 이미 알고 있음)
#
# 실행 방법 | How to run:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/10일차/briefing.py

import ollama
import random
from datetime import datetime

def ask_cravveo(question):
    response = ollama.chat(
        model='cravveo',
        messages=[{'role': 'user', 'content': question}]
    )
    return response['message']['content']

# 질문 풀 (Day 036 개선 — 짧고 명확한 질문만 유지)
# 긴 질문, 추상적 질문, 비교 질문은 3B 모델에서 다국어 혼합 발생
QUESTION_POOL = [
    "크라베오 컴퍼니가 뭐야?",
    "크라베오의 목표가 뭐야?",
    "Build in Public이 뭐야?",
    "파인튜닝을 왜 배우고 있어?",
    "크라베오의 기술 스택이 뭐야?",
    "LoRA가 뭐야?",
    "Unsloth가 뭐야?",
    "Ollama가 뭐야?",
    "HuggingFace가 뭐야?",
    "크라베오 유튜브는 어떤 채널이야?",
    "왜 1인 기업을 선택했어?",
    "크라베오 AI가 완성되면 뭘 할 거야?",
    "loss가 뭐야?",
    "파인튜닝이 뭐야?",
    "cravveo 모델이 뭐야?",
    "GGUF가 뭐야?",
    "크라베오를 한 마디로 설명하면?",
    "오늘의 크라베오 한 마디는?",
    "크라베오가 요즘 하는 작업이 뭐야?",
    "크라베오 AI 어시스턴트는 뭐야?",
    "크라베오의 기술 스택이 뭐야?",
    "Ollama가 뭐야?",
]

today = datetime.now().strftime('%Y%m%d')
filename = f"briefing_{today}.txt"

print(f"[Cravveo AI 아침 브리핑 — {datetime.now().strftime('%Y-%m-%d')}]")
print("-" * 50)

random.seed(today)
questions = random.sample(QUESTION_POOL, 3)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== Cravveo AI 아침 브리핑 {datetime.now().strftime('%Y-%m-%d')} ===\n\n")

    for i, question in enumerate(questions, 1):
        print(f"[{i}/3] 답변 중: {question}")
        answer = ask_cravveo(question)
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 40 + "\n\n")

print(f"저장 완료: {filename}")

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

QUESTION_POOL = [
    "크라베오 컴퍼니는 어떤 회사인가요?",
    "크라베오 컴퍼니의 운영자는 어떤 사람인가요?",
    "100일 AI 파인튜닝 도전을 시작한 이유는 무엇인가요?",
    "Build in Public이란 무엇인가요?",
    "크라베오가 파인튜닝에 사용하는 도구는 무엇인가요?",
    "LoRA 파인튜닝이란 무엇인가요?",
    "크라베오 컴퍼니의 최종 목표는 무엇인가요?",
    "Google Colab을 사용하는 이유는 무엇인가요?",
    "Unsloth란 무엇이고 왜 사용하나요?",
    "크라베오 컴퍼니의 유튜브 채널에서는 어떤 내용을 다루나요?",
    "AI 초보자가 파인튜닝을 혼자 배울 수 있나요?",
    "크라베오 AI 어시스턴트는 어떤 역할을 할 예정인가요?",
    "파인튜닝과 RAG의 차이점은 무엇인가요?",
    "HuggingFace란 무엇이고 크라베오는 왜 사용하나요?",
    "1인 기업이 AI 파인튜닝을 하면 어떤 장점이 있나요?",
    "파인튜닝 중 loss란 무엇을 의미하나요?",
    "크라베오 컴퍼니는 앞으로 어떤 방향으로 성장할 계획인가요?",
    "파인튜닝한 AI 모델은 어디에 활용할 수 있나요?",
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

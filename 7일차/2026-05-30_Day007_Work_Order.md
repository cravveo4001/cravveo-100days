# 📋 Day 007 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-30
> **단계** | Phase: Day 007 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| Day 002 | 작업 폴더 생성 + Python 가상환경(venv) 구성 | ✅ 완료 |
| Day 003 | Git 저장소 초기화 + 첫 번째 커밋 + GitHub push | ✅ 완료 |
| Day 004 | Ollama 설치 + 로컬 LLM 첫 실행 (gemma4:e2b) | ✅ 완료 |
| Day 005 | Ollama 모델 비교 + 프롬프트 실습 | ✅ 완료 |
| Day 006 | Python으로 Ollama API 연동 + 코드로 AI 호출 | ✅ 완료 |
| **Day 007** | **여러 질문을 반복 실행 + 결과를 파일로 저장** | 🔥 오늘 |
| Day 008~ | Python 스크립트 심화 (입력 받기, 조건 처리) | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 006에서 질문 하나를 코드로 AI에게 보내는 데 성공했습니다.
> 오늘은 여러 질문을 반복(루프)으로 처리하고,
> AI 답변을 텍스트 파일로 저장하는 스크립트를 만듭니다.
> 수동으로 복사하지 않아도 결과가 파일에 쌓이는 자동화입니다.

**English**
> In Day 006, I sent one question to AI from code.
> Today I'll loop through multiple questions and save all AI answers to a text file automatically.
> No more copy-pasting — results accumulate in a file on their own.

---

## 📌 왜 파일 저장인가? | Why Save to File?

**한국어**
AI 답변을 터미널에만 출력하면 창을 닫는 순간 사라집니다.
파일로 저장하면 나중에 검토하고, 정리하고, 다른 프로그램에서 활용할 수 있습니다.
이것이 "AI를 도구처럼 쓰는 것"의 핵심입니다.

**English**
If AI answers only appear in the terminal, they disappear when you close the window.
Saving to a file means you can review, organize, and reuse the results later.
This is the heart of "using AI as a tool."

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 가상환경 활성화 | Activate virtual environment
```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
cd ~/finetuning-project/7일차
```
> 📝 터미널 앞에 `(venv)` 가 보이면 성공입니다.

### Step 2 — Python 스크립트 작성 | Write Python script

아래 내용으로 `save_ai.py` 파일을 만드세요:

```bash
nano save_ai.py
```

파일 내용:

```python
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
```

> 📝 nano 저장: `Ctrl + O` → Enter → `Ctrl + X`

### Step 3 — 스크립트 실행 | Run the script
```bash
python save_ai.py
```

### Step 4 — 저장된 파일 확인 | Check the saved file
```bash
cat ai_answers_*.txt
```

터미널에 파일 내용이 출력되면 성공입니다.

### Step 5 — (심화) 질문 목록 바꿔보기 | (Bonus) Change the questions

`save_ai.py` 안의 `questions` 리스트를 원하는 질문으로 바꿔서 다시 실행해보세요.

---

## ✅ 성공 조건 | Success Criteria

- [ ] 가상환경 활성화 완료 `(venv)` 표시 확인
- [ ] `save_ai.py` 파일 작성 완료
- [ ] `python save_ai.py` 실행 → 3개 질문 순서대로 처리
- [ ] `ai_answers_XXXXXX.txt` 파일 생성 확인
- [ ] 파일 안에 Q/A가 저장되어 있는 것 확인

---

## 🚨 막혔을 때 | Troubleshooting

**`Connection refused` 오류가 나면**
Ollama 서버가 꺼져 있습니다. 새 터미널에서:
```bash
ollama serve
```

**응답이 비어있으면 (빈 칸)**
qwen3 thinking 모드 문제입니다. `ask_ai()` 함수 안에 `"think": False` 가 있는지 확인하세요.

**너무 오래 걸리면**
질문 수를 3개 → 1개로 줄여서 먼저 테스트하세요.

---

## 📅 다음 단계 | Next Step

**Day 008**: 터미널에서 직접 질문을 입력하면 AI가 답변하는 간단한 대화 루프를 만듭니다.
**Day 008**: Build a simple chat loop — type a question in the terminal, get an AI answer, repeat.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-30_Day007_Log|Day 007 로그]] | [[Day007_YouTube_Upload|Day 007 유튜브]] | [[../6일차/2026-05-29_Day006_Work_Order|← Day 006]] | [[../8일차/2026-05-31_Day008_Work_Order|Day 008 →]]

# 📋 Day 006 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-29
> **단계** | Phase: Day 006 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| Day 002 | 작업 폴더 생성 + Python 가상환경(venv) 구성 | ✅ 완료 |
| Day 003 | Git 저장소 초기화 + 첫 번째 커밋 + GitHub push | ✅ 완료 |
| Day 004 | Ollama 설치 + 로컬 LLM 첫 실행 (gemma4:e2b) | ✅ 완료 |
| Day 005 | Ollama 모델 비교 + 프롬프트 실습 | ✅ 완료 |
| **Day 006** | **Python으로 Ollama API 연동 + 코드로 AI 호출** | 🔥 오늘 |
| Day 007~ | Python 스크립트 확장 (대화 루프, 파일 저장) | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 지금까지는 터미널에서 직접 AI와 대화했습니다.
> 오늘은 Python 코드로 Ollama API를 호출해서,
> 프로그램이 AI에게 질문하고 답변을 받아오도록 만듭니다.
> 자동화의 첫 번째 문을 여는 날입니다.

**English**
> Until now, I've been chatting with AI directly in the terminal.
> Today I'll call the Ollama API from Python code —
> making a program that sends a question to AI and gets the answer back.
> This is the first step toward full automation.

---

## 📌 왜 API 연동인가? | Why API Integration?

**한국어**
Ollama는 터미널 대화뿐 아니라 HTTP API를 제공합니다.
Python 코드에서 API를 호출하면 "질문 → AI 답변"을 자동화할 수 있습니다.
나중에 이메일 요약, 문서 분석, 챗봇 등 모든 자동화의 핵심이 바로 이 API 호출입니다.

**English**
Ollama provides an HTTP API, not just a terminal chat interface.
Calling the API from Python means we can automate the "question → AI answer" flow.
This is the foundation for everything that comes later: email summaries, document analysis, chatbots.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — Ollama 실행 상태 확인 | Verify Ollama is running
```bash
ollama list
```
> 📝 모델 목록이 보이면 Ollama가 정상 실행 중입니다.

### Step 2 — 가상환경 활성화 | Activate virtual environment
```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
```
> 📝 터미널 앞에 `(venv)` 가 보이면 성공입니다.

### Step 3 — requests 라이브러리 설치 | Install requests library
```bash
pip install requests
```

### Step 4 — Python 스크립트 작성 | Write Python script

아래 내용으로 `ask_ai.py` 파일을 만드세요:

```bash
nano ask_ai.py
```

파일 내용:

```python
import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "wen3.5:2b",
    "prompt": "1인 기업 운영자에게 AI가 어떻게 도움이 될 수 있어? 3줄로 요약해줘.",
    "stream": False
}

response = requests.post(url, json=data)
result = response.json()

print("AI 답변:")
print(result["response"])
```

> 📝 nano 저장: `Ctrl + O` → Enter → `Ctrl + X`

### Step 5 — 스크립트 실행 | Run the script
```bash
python ask_ai.py
```

### Step 6 — 결과 확인 | Check result

터미널에 AI 답변이 출력되면 성공입니다.

### Step 7 — (심화) 질문을 바꿔서 다시 실행 | (Bonus) Change the prompt and re-run

`ask_ai.py` 안의 `prompt` 부분을 원하는 질문으로 바꿔서 다시 실행해보세요.

```python
"prompt": "파이썬을 처음 배우는 사람에게 가장 중요한 것은 뭐야?"
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] `ollama list` 에서 모델 확인
- [ ] 가상환경 활성화 완료 `(venv)` 표시 확인
- [ ] `pip install requests` 완료
- [ ] `ask_ai.py` 파일 작성 완료
- [ ] `python ask_ai.py` 실행 → AI 답변 출력 확인
- [ ] 질문을 바꿔서 다시 실행해보기 (심화)

---

## 🚨 막혔을 때 | Troubleshooting

**`Connection refused` 오류가 나면**
Ollama 서버가 꺼져 있습니다. 새 터미널에서:
```bash
ollama serve
```

**`ModuleNotFoundError: No module named 'requests'` 오류가 나면**
가상환경이 비활성화된 상태입니다:
```bash
source ~/projects/cravveo_ai/venv/bin/activate
pip install requests
```

**모델 이름 오류가 나면**
`ollama list`로 정확한 모델명을 확인 후 `ask_ai.py`의 `"model"` 값을 수정하세요.

**응답이 너무 오래 걸리면**
더 작은 모델로 변경:
```python
"model": "qwen3.5:2b"
```

---

## 📅 다음 단계 | Next Step

**Day 007**: Python 스크립트를 확장해서 여러 질문을 반복 실행하고 결과를 파일로 저장합니다.
**Day 007**: Extend the Python script to ask multiple questions in a loop and save results to a file.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-29_Day006_Log|Day 006 로그]] | [[Day006_YouTube_Upload|Day 006 유튜브]] | [[../5일차/2026-05-28_Day005_Work_Order|← Day 005]] | [[../7일차/2026-05-30_Day007_Work_Order|Day 007 →]]

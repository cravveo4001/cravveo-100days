# 📋 Day 008 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-31
> **단계** | Phase: Day 008 / 100

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
| Day 007 | 15개 질문 자동 처리 + AI 답변 파일 저장 | ✅ 완료 |
| **Day 008** | **터미널 대화 루프 — 직접 입력하고 AI가 바로 답한다** | 🔥 오늘 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 007에서 미리 정해진 질문 목록을 자동으로 처리했습니다.
> 오늘은 내가 직접 터미널에 질문을 입력하면 AI가 바로 답하는
> **실시간 대화 루프**를 만듭니다.
> `"종료"` 라고 입력할 때까지 계속 대화가 이어집니다.

**English**
> In Day 007, I automated a fixed list of questions.
> Today I'll build a **live chat loop** — I type a question in the terminal, AI answers immediately.
> The conversation continues until I type `"quit"`.

---

## 📌 왜 대화 루프인가? | Why a Chat Loop?

**한국어**
지금까지는 질문이 코드 안에 고정돼 있었습니다.
대화 루프를 만들면 코드를 수정하지 않고도 어떤 질문이든 바로 할 수 있습니다.
이것이 챗봇의 가장 기본 형태입니다.

**English**
Until now, questions were hardcoded in the script.
A chat loop lets me ask anything without touching the code.
This is the most basic form of a chatbot.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 가상환경 활성화 | Activate virtual environment
```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
cd ~/finetuning-project/8일차
```
> 📝 터미널 앞에 `(venv)` 가 보이면 성공입니다.

### Step 2 — Python 스크립트 작성 | Write Python script

아래 내용으로 `chat_ai.py` 파일을 만드세요:

```bash
nano chat_ai.py
```

파일 내용:

```python
import requests

url = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    data = {
        "model": "qwen3.5:2b",
        "prompt": "반드시 한국어로만 답해줘.\n\n" + prompt,
        "stream": False,
        "think": False,
        "options": {"num_predict": 500}
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result.get("response", "")

print("AI 대화를 시작합니다. 종료하려면 '종료' 또는 'quit'을 입력하세요.")
print("-" * 50)

while True:
    user_input = input("\n나: ")

    if user_input.strip() in ["종료", "quit", "exit"]:
        print("대화를 종료합니다.")
        break

    if not user_input.strip():
        continue

    print("AI 생각 중...")
    answer = ask_ai(user_input)
    print(f"\nAI: {answer}")
```

> 📝 nano 저장: `Ctrl + O` → Enter → `Ctrl + X`

### Step 3 — 스크립트 실행 | Run the script
```bash
python chat_ai.py
```

### Step 4 — 대화해보기 | Try chatting

실행 후 질문을 직접 입력해보세요:
```
나: 안녕
나: 1인 기업 운영에서 가장 중요한 것은?
나: 종료
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] 가상환경 활성화 완료 `(venv)` 표시 확인
- [ ] `chat_ai.py` 파일 작성 완료
- [ ] `python chat_ai.py` 실행 → 대화 시작 메시지 출력 확인
- [ ] 직접 질문 입력 → AI 답변 출력 확인
- [ ] `"종료"` 입력 시 프로그램 정상 종료 확인

---

## 🚨 막혔을 때 | Troubleshooting

**`Connection refused` 오류가 나면**
Ollama 서버가 꺼져 있습니다:
```bash
sudo systemctl restart ollama
```

**AI가 한자로 답하면**
`ask_ai()` 함수 안에 `"반드시 한국어로만 답해줘.\n\n"` 가 프롬프트 앞에 붙어있는지 확인하세요.

**응답이 너무 오래 걸리면**
`num_predict` 값을 300으로 줄여보세요.

**Ctrl+C로 종료되지 않으면**
`"종료"` 를 입력해서 while 루프를 정상 종료하세요.

---

## 📅 다음 단계 | Next Step

**Day 009**: 대화 내용을 파일로 저장하는 기능을 추가합니다. (Day 007 파일 저장 + Day 008 대화 루프 합치기)
**Day 009**: Add file logging to the chat — combine Day 007 file save with Day 008 chat loop.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-31_Day008_Log|Day 008 로그]] | [[Day008_YouTube_Upload|Day 008 유튜브]] | [[../7일차/2026-05-30_Day007_Work_Order|← Day 007]] | [[../9일차/2026-06-01_Day009_Work_Order|Day 009 →]]

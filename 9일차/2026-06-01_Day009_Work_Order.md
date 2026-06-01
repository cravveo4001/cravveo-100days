# 📋 Day 009 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-01
> **단계** | Phase: Day 009 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 | ✅ 완료 |
| Day 002 | 작업 폴더 + Python 가상환경 구성 | ✅ 완료 |
| Day 003 | Git 초기화 + GitHub 첫 push | ✅ 완료 |
| Day 004 | Ollama 설치 + 로컬 LLM 첫 실행 | ✅ 완료 |
| Day 005 | 모델 비교 + 프롬프트 실습 | ✅ 완료 |
| Day 006 | Python으로 Ollama API 연동 | ✅ 완료 |
| Day 007 | AI 답변 자동 저장 스크립트 완성 | ✅ 완료 |
| Day 008 | 터미널 대화 루프 구현 | ✅ 완료 |
| **Day 009** | **대화 내용 파일 저장 — Day 007 + Day 008 합치기** | 🔥 오늘 |
| Day 010 | Python 자동화 미니 프로젝트 | ⏳ 예정 |
| Day 011 | AnythingLLM 설치 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 007에서 파일 저장을 배웠고, Day 008에서 대화 루프를 배웠습니다.
> 오늘은 이 두 가지를 합쳐서 대화할수록 내용이 파일에 자동으로 쌓이는
> **대화 로그 저장 챗봇**을 만듭니다.
> 종료하면 `chat_log_XXXXXX.txt` 파일에 전체 대화 내역이 남습니다.

**English**
> Day 007 taught file saving. Day 008 taught chat loops.
> Today I combine both — a chatbot that automatically logs every conversation to a file.
> When I quit, `chat_log_XXXXXX.txt` contains the full conversation history.

---

## 📌 왜 대화 로그인가? | Why Chat Logging?

**한국어**
대화는 터미널 창을 닫으면 사라집니다.
로그 파일로 저장하면 나중에 AI와 나눈 내용을 다시 꺼내볼 수 있고,
더 나아가 이 데이터가 파인튜닝 학습 데이터가 될 수 있습니다.

**English**
Conversations disappear when the terminal closes.
Saving to a log file lets me review past conversations — and eventually,
this data can become fine-tuning training data.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 가상환경 활성화
```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
cd ~/finetuning-project/9일차
```

### Step 2 — Python 스크립트 작성

```bash
nano chat_log.py
```

파일 내용:

```python
import requests
from datetime import datetime

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

filename = f"chat_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

print("AI 대화를 시작합니다. 종료하려면 '종료' 또는 'quit'을 입력하세요.")
print(f"대화 내용은 {filename} 에 저장됩니다.")
print("-" * 50)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== 대화 시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")

    while True:
        user_input = input("\n나: ")

        if user_input.strip() in ["종료", "quit", "exit"]:
            print("대화를 종료합니다.")
            f.write("\n=== 대화 종료 ===\n")
            break

        if not user_input.strip():
            continue

        print("AI 생각 중...")
        answer = ask_ai(user_input)
        print(f"\nAI: {answer}")

        f.write(f"나: {user_input}\n")
        f.write(f"AI: {answer}\n")
        f.write("-" * 30 + "\n")

print(f"\n저장 완료: {filename}")
```

> 📝 nano 저장: `Ctrl + O` → Enter → `Ctrl + X`

### Step 3 — 실행
```bash
python chat_log.py
```

### Step 4 — 대화 후 파일 확인
```bash
cat chat_log_*.txt
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] 가상환경 활성화 완료
- [ ] `chat_log.py` 파일 작성 완료
- [ ] `python chat_log.py` 실행 → 파일명 안내 메시지 출력 확인
- [ ] 직접 질문 입력 → AI 답변 출력 확인
- [ ] `"종료"` 입력 후 `chat_log_XXXXXX.txt` 파일 생성 확인
- [ ] 파일 안에 대화 내용이 저장되어 있는 것 확인

---

## 🚨 막혔을 때 | Troubleshooting

**Ollama 연결 안 되면**
```bash
sudo systemctl restart ollama
```

**AI가 한자로 답하면**
프롬프트 앞에 `"반드시 한국어로만 답해줘.\n\n"` 붙어있는지 확인

---

## 📅 다음 단계 | Next Step

**Day 010**: 지금까지 배운 것(API + 루프 + 파일)을 합쳐 나만의 자동화 도구 하나 완성. Python 자동화 기초 마무리.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-01_Day009_Log|Day 009 로그]] | [[Day009_YouTube_Upload|Day 009 유튜브]] | [[../8일차/2026-05-31_Day008_Work_Order|← Day 008]] | [[../10일차/2026-06-02_Day010_Work_Order|Day 010 →]]

# 📋 Day 010 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-02
> **단계** | Phase: Day 010 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama 설치 + 모델 실습 | ✅ 완료 |
| Day 006 | Python으로 Ollama API 연동 | ✅ 완료 |
| Day 007 | AI 답변 자동 저장 스크립트 | ✅ 완료 |
| Day 008 | 터미널 대화 루프 | ✅ 완료 |
| Day 009 | 대화 내용 파일 저장 챗봇 | ✅ 완료 |
| **Day 010** | **Python 자동화 미니 프로젝트 — 기초 챕터 마무리** | 🔥 오늘 |
| Day 011 | AnythingLLM 설치 | ⏳ 예정 |
| Day 016~ | 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 006부터 Day 009까지 배운 것을 전부 합쳐서
> **나만의 실용적인 자동화 도구**를 하나 완성합니다.
> 오늘 만들 것: **매일 아침 브리핑 스크립트**
> 실행하면 오늘 날짜 + 정해진 질문 3개를 AI에게 자동으로 보내고
> 날짜별 파일(`briefing_20260602.txt`)로 저장합니다.

**English**
> Combine everything from Day 006~009 into one practical automation tool.
> Today's build: **Daily Morning Briefing Script**
> Run it → sends 3 fixed questions to AI → saves results to a dated file (`briefing_20260602.txt`).

---

## 📌 왜 아침 브리핑인가? | Why Morning Briefing?

**한국어**
지금까지 배운 기술들의 최종 조합입니다.
- API 호출 (Day 006)
- 파일 저장 + 날짜 파일명 (Day 007)
- 반복 처리 (Day 007~008)
- 자동 실행 → 결과 누적 (Day 009)

이 스크립트를 매일 실행하면 AI가 오늘의 업무 힌트를 파일로 남겨줍니다.
나중에 이 파일들이 쌓이면 파인튜닝 데이터가 됩니다.

**English**
This is the final combination of everything learned.
Run it every morning → AI leaves daily insights in a file → files stack up → eventually become fine-tuning data.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 가상환경 활성화
```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
cd ~/finetuning-project/10일차
```

### Step 2 — 스크립트 작성
```bash
nano briefing.py
```

파일 내용:

```python
import requests
from datetime import datetime

url = "http://localhost:11434/api/generate"

questions = [
    "오늘 1인 기업가가 집중해야 할 가장 중요한 한 가지는 뭐야? 3줄로.",
    "유튜브 콘텐츠 아이디어를 하나 제안해줘. AI 자동화 주제로, 초보자 눈높이로.",
    "오늘 하루 동기부여가 되는 짧은 한마디를 해줘."
]

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

today = datetime.now().strftime('%Y%m%d')
filename = f"briefing_{today}.txt"

print(f"[Cravveo 아침 브리핑 — {datetime.now().strftime('%Y-%m-%d')}]")
print("-" * 50)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== Cravveo 아침 브리핑 {datetime.now().strftime('%Y-%m-%d')} ===\n\n")

    for i, question in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] 처리 중...")
        answer = ask_ai(question)
        print(f"Q: {question}")
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 40 + "\n\n")

print(f"저장 완료: {filename}")
```

> 📝 nano 저장: `Ctrl + O` → Enter → `Ctrl + X`

### Step 3 — 실행
```bash
python briefing.py
```

### Step 4 — 파일 확인
```bash
cat briefing_*.txt
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] 가상환경 활성화 완료
- [ ] `briefing.py` 파일 작성 완료
- [ ] `python briefing.py` 실행 → 3개 질문 순서대로 처리
- [ ] `briefing_20260602.txt` 파일 생성 확인
- [ ] 파일 안에 오늘 날짜 + Q/A 저장 확인

---

## 🚨 막혔을 때 | Troubleshooting

**Ollama 연결 안 되면**
```bash
sudo systemctl restart ollama
```

**AI가 한자로 답하면**
프롬프트 앞에 `"반드시 한국어로만 답해줘.\n\n"` 확인

---

## 📅 다음 단계 | Next Step

**Day 011**: Python 자동화 기초 챕터 완료. AnythingLLM 설치로 넘어갑니다.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-02_Day010_Log|Day 010 로그]] | [[Day010_YouTube_Upload|Day 010 유튜브]] | [[../9일차/2026-06-01_Day009_Work_Order|← Day 009]] | [[../11일차/2026-06-03_Day011_Work_Order|Day 011 →]]

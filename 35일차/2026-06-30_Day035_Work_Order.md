# 📋 Day 035 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-30
> **단계** | Phase: Day 035 / 100 — Phase 3

---

## 💻 노트북 사양 & 사용 모델 | Hardware & Model

| 항목 Item | 사양 Spec |
|------|------|
| 노트북 Laptop | 한성 TFX5556U |
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | AMD Radeon Vega (내장 Integrated) |
| OS | Linux (Ubuntu) |
| 사용 모델 Model | cravveo:latest (Llama 3.2 3B + LoRA, q8_0 GGUF) |
| 작업 환경 Environment | 로컬 Ollama + Python |
| **신규 장비 New Gear** | **🎙️ 마이크 Microphone (오늘부터 음성 설명 시작!)** |

---

## 🎙️ 오늘 말할 멘트 | Today's Narration Script

> 완벽한 대본이 아니어도 됩니다. 이 포인트들만 자기 말로 자연스럽게 풀어서 말하면 충분해요.
> Doesn't need to be perfect. Just hit these points naturally in your own words.

**오프닝 | Opening**
> "안녕하세요, 크라베오입니다. 오늘은 Day 035, 마이크를 처음 써보는 날이에요.
> 그동안 화면만 녹화하고 음악만 깔았었는데, 오늘부터는 직접 설명하면서 진행해볼게요."

**Step 시작할 때 (예시) | When starting a Step (example)**
> "지금 하는 건 유튜브 스크립트를 AI가 자동으로 써주는 걸 테스트하는 거예요."

**에러 났을 때 | When an error happens**
> "어, 에러 났네요. 이런 것도 그대로 보여드릴게요. (에러 내용) 이게 왜 이러는지 같이 찾아볼게요."

**성공했을 때 | When something works**
> "오, 이거 됐다! (결과 보여주면서) 이렇게 나왔어요."

**클로징 | Closing**
> "오늘은 여기까지입니다. 다음에는 [내일 할 일]을 해볼게요. 구독과 좋아요는 큰 힘이 됩니다. 감사합니다."

---

## 🗺️ 100일 전체 로드맵 | Roadmap

| 단계 Phase | 내용 Content | 상태 Status |
|------|------|------|
| Day 001~029 | Phase 1+2: 환경 구축 + 파인튜닝 + 로컬 배포 | ✅ 완료 Done |
| Day 030~034 | Phase 3 시작: RAG 통합 + API + cron 자동화 | ✅ 완료 Done |
| **Day 035** | **유튜브 스크립트 자동 생성 + 첫 음성 녹음** | 🔥 오늘 Today |
| Day 036~ | 답변 품질 개선 (데이터 확장) Quality improvement | ⏳ 예정 Next |
| Day 100 | 1인 기업 자동화 시스템 완성 Automation complete | 🎯 목표 Goal |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 033에서 Python으로 크라베오 AI를 호출했고, Day 034에서 아침 브리핑 자동화를 연결했습니다.
> 오늘은 크라베오 AI에게 **유튜브 영상 스크립트 초안**을 써달라고 요청합니다.
> 그리고 오늘부터 마이크로 직접 설명하면서 영상을 만듭니다.

**English**
> Day 033 connected Python to Cravveo AI. Day 034 connected it to morning briefing automation.
> Today we ask Cravveo AI to draft a **YouTube video script**.
> And starting today, we narrate videos with a microphone.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
지금까지 유튜브 업로드 문서(제목, 설명, 태그 등)는 전부 제가 직접 만들어왔습니다.
크라베오 AI가 스크립트 초안을 쓸 수 있으면, 매일 작업이 줄어듭니다.
완벽하지 않아도 됩니다 — 초안만 만들어주면 다듬는 건 빠릅니다.

**English**
Until now, all YouTube upload docs were manually created.
If Cravveo AI can draft scripts, daily work decreases.
Doesn't need to be perfect — a draft to polish is enough.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 스크립트 생성 함수 작성 | Write Script Generation Function

```python
# cravveo_script_writer.py
# 실행 방법: cd ~/projects/cravveo_ai && source venv/bin/activate
#           python3 ~/finetuning-project/35일차/cravveo_script_writer.py

import ollama

def write_script(day_number, topic):
    prompt = f"""크라베오 컴퍼니의 100일 AI 파인튜닝 도전 유튜브 영상 스크립트를 써줘.
Day {day_number}, 주제: {topic}

다음 구조로 짧게 써줘:
1. 오프닝 (1줄)
2. 오늘 한 일 (2~3줄)
3. 클로징 (1줄)
"""
    response = ollama.chat(
        model='cravveo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    script = write_script(35, "유튜브 스크립트 자동화 + 마이크로 첫 음성 녹음")
    print(script)
```

---

### Step 2 — 실행 + 결과 확인 | Run and Check Result

```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
python3 ~/finetuning-project/35일차/cravveo_script_writer.py
```

품질이 어떤지 직접 확인합니다. 완벽하지 않아도 괜찮습니다 — 오늘은 가능성을 확인하는 게 목표입니다.
Check the quality. Doesn't need to be perfect — today's goal is to verify feasibility.

---

### Step 3 — 마이크 테스트 | Microphone Test

녹화 시작 전, 마이크 음량과 노이즈를 짧게 테스트합니다.
Before recording, briefly test mic volume and noise.

```bash
# 리눅스에서 간단히 녹음 테스트 (선택)
arecord -d 5 -f cd test.wav && aplay test.wav
```

---

### Step 4 — 음성과 함께 영상 녹화 | Record Video with Narration

위의 "오늘 말할 멘트"를 참고해서 자연스럽게 설명하며 녹화합니다.
Record while explaining naturally, using the narration script above.

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] `write_script()` 함수 작성 완료 | Function written
- [ ] 크라베오 AI가 스크립트 초안 생성 | AI generates script draft
- [ ] 마이크 음량/노이즈 테스트 완료 | Mic test done
- [ ] **음성 설명과 함께 영상 녹화** | **Video recorded with narration** ← 핵심 Key
- [ ] 영상 녹화 완료 | Video recorded

---

## 🔧 트러블슈팅 | Troubleshooting

**마이크 노이즈가 심할 때 | Heavy mic noise**
→ 마이크와 입 사이 거리 조정 (15~20cm 권장)
→ Adjust distance between mic and mouth (15-20cm recommended)

**스크립트 품질이 낮을 때 | Low script quality**
→ Day 031~034에서 본 3B 모델의 한계. 초안만 받고 직접 다듬기.
→ 3B model limitation seen since Day 031. Use as draft, polish manually.

**말하면서 녹화가 어색할 때 | Awkward narrating while recording**
→ 처음엔 다 어색합니다. 완벽한 발음/톤 필요 없음. 편하게 말하면 됩니다.
→ Everyone's awkward at first. No need for perfect tone. Just talk naturally.

---

## 📅 다음 단계 예고 | Next Up

**Day 036** — 답변 품질 개선: 질문 풀 다듬기 + 데이터 확장
오늘 cron 브리핑에서 본 언어 섞임 문제를 데이터로 개선합니다.

Improve answer quality by refining the question pool and expanding data,
addressing the language-mixing issue seen in today's cron briefing.

---

[[2026-06-30_Day035_Work_Order|Day 035 작업지시서]] | [[../34일차/2026-06-29_Day034_Work_Order|← Day 034]] | [[../Cravveo_100Day_Master_Guide]]

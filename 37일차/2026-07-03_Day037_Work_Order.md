# 📋 Day 037 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-07-03
> **단계** | Phase: Day 037 / 100 — 데이터 고도화 1일차

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
| 작업 환경 Environment | 로컬 Python |
| 🎙️ 녹음 방식 | 음성 내레이션 (BGM 없음, Day 050까지) |

---

## 🎙️ 오늘 말할 멘트 | Today's Narration Script

**오프닝**
> "안녕하세요 크라베오입니다. Day 037이에요.
> 오늘부터 데이터 고도화를 시작합니다.
> 지금까지 Q&A를 손으로 직접 만들었는데,
> 오늘은 제가 36일 동안 써온 데일리로그를 AI 학습 데이터로 자동 변환하는 스크립트를 만들어볼 거예요."

**작업 중**
> "Daily_Log 폴더에 36개 파일이 있어요.
> 이걸 파이썬으로 읽어서 질문/답변 쌍으로 자동 변환합니다.
> 36개 파일 → 수백 개 학습 데이터가 자동으로 생겨요."

**클로징**
> "오늘 만든 데이터로 내일 재학습을 돌려볼 거예요. 감사합니다."

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> `Daily_Log` 폴더의 36개 마크다운 파일을 읽어서
> 질문/답변 JSONL 포맷으로 자동 변환하는 Python 스크립트 작성.

**English**
> Write a Python script that reads 36 markdown files from the `Daily_Log` folder
> and auto-converts them into question/answer JSONL format for fine-tuning.

---

## 🔧 작동 원리 | How It Works

```
Daily_Log/*.md 읽기
    ↓
섹션별 파싱 (목표, 실행 작업, 핵심 발견 등)
    ↓
Q&A 쌍 자동 생성
    ↓
JSONL 파일로 저장
    ↓
HuggingFace 업로드 (내일)
```

**생성되는 Q&A 예시 | Example Q&A pairs:**
```
Q: "Day 036에서 뭘 했어?"
A: "Phase 3 점검 + 64일 수정 로드맵 확정..."

Q: "Day 035의 핵심 발견이 뭐야?"
A: "자동화 함수를 만들었다와 완전 자동화는 다르다..."

Q: "Day 029에서 막힌 지점이 뭐야?"
A: "GGUF 변환 후 Ollama에서 Unknown 출력..."
```

---

## 📌 단계별 실행 | Step-by-Step

### Step 1 — 스크립트 작성
`37일차/obsidian_to_jsonl.py` 작성

### Step 2 — 테스트 실행
```bash
cd ~/projects/cravveo_ai && source venv/bin/activate
python3 ~/finetuning-project/37일차/obsidian_to_jsonl.py
```

### Step 3 — 결과 확인
생성된 JSONL 파일 열어서 Q&A 쌍 확인

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] `obsidian_to_jsonl.py` 스크립트 작성 완료
- [ ] 36개 데일리로그 전부 파싱 성공
- [ ] JSONL 파일 생성 확인 (최소 100개 Q&A 쌍)
- [ ] 영상 녹화 완료
- [ ] 커밋 + 푸시 완료

---

## 📅 다음 단계 예고 | Next Up

**Day 038** — 생성된 데이터로 Colab 재학습
Day 038 — Retrain on Colab with the new generated data

---

[[../36일차/2026-07-02_Day036_Work_Order|← Day 036]] | [[../Cravveo_100Day_Master_Guide]]

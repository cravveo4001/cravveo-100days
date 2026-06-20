# 📋 Day 026 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-20
> **단계** | Phase: Day 026 / 100

---

## 💻 노트북 사양 & 사용 모델 | Hardware & Model

| 항목 | 사양 |
|------|------|
| 노트북 | 한성 TFX5556U |
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | AMD Radeon Vega (내장) |
| 저장소 | NVMe SSD 468GB |
| OS | Linux |
| ~~사용 모델~~ | ~~Gemma 2B (Unsloth + LoRA, 코랩 T4 GPU)~~ |
| **사용 모델 (변경)** | **Llama 3.2 1B Instruct (Unsloth + LoRA, 코랩 T4 GPU)** |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019~023 | 데이터셋 제작 + HuggingFace 업로드 + cron 자동화 | ✅ 완료 |
| Day 024 | 파인튜닝 뼈대 코드 — 모델 + 데이터 연결 | ✅ 완료 |
| Day 025 | LoRA + SFTTrainer + 첫 학습 — loss 25.5→15.4 | ✅ 완료 |
| **Day 026** | **학습 실패 → 모델 교체 (Gemma→Llama) → loss 3.4 정상화** | ✅ 오늘 |
| Day 027~ | 데이터 확장 + 학습 강화 + 모델 테스트 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 025에서 loss가 25.5로 높게 시작하는 문제를 해결하려 했습니다.
> 프롬프트 포맷 수정, 데이터 필터링 등 여러 시도를 했지만 Gemma 2B에서는
> 어떤 포맷을 써도 loss 1200이 나왔습니다.
> 디버그 테스트로 모델 자체의 호환 문제임을 확인하고,
> Llama 3.2 1B로 교체하여 loss 3.4로 정상화에 성공했습니다.

**English**
> Tried to fix the high loss (25.5) from Day 025.
> Attempted prompt format fixes and data filtering, but Gemma 2B showed
> loss ~1200 regardless of format — even with 3 trivial entries.
> Debug test confirmed it was a model compatibility issue with Unsloth.
> Switched to Llama 3.2 1B — loss dropped to 3.4 (normal range).

---

## 📌 오늘의 핵심 발견 | Key Discovery

**한국어**
1. Gemma 2B + 현재 Unsloth 버전에서 loss가 비정상적으로 높음 (1200)
2. 데이터 3개, 16토큰짜리 초간단 테스트에서도 loss 1135 → 모델 호환 문제 확정
3. Llama 3.2 1B로 교체하자 같은 코드, 같은 데이터에서 loss 3.4~5.5 (정상)
4. HuggingFace 데이터셋 62개 중 40개가 LLM 생성 쓰레기 데이터 → 29개로 필터링
5. 파인튜닝에서 모델 선택이 얼마나 중요한지 체감

**English**
1. Gemma 2B + current Unsloth version produces abnormally high loss (~1200)
2. Even a 3-entry, 16-token trivial test showed loss 1135 → confirmed model issue
3. Switching to Llama 3.2 1B: same code, same data → loss 3.4~5.5 (normal)
4. Filtered garbage LLM-generated data: 62 → 29 clean entries
5. Learned how critical model selection is in fine-tuning

---

## ✅ 오늘 실행한 내용 | What We Did

### 시도 1 — Gemma + 프롬프트 포맷 수정
- `<start_of_turn>` Gemma 채팅 템플릿 적용 → loss 1200
- `get_chat_template` + `apply_chat_template` → loss 1200
- 단순 `질문:/답변:` 포맷 → loss 1135
- **결론: 포맷 문제가 아님**

### 시도 2 — 데이터 필터링
- 62개 중 output 300자 초과 쓰레기 데이터 제거 → 29개
- 같은 Gemma에서 재학습 → loss 여전히 1200+
- **결론: 데이터 문제가 아님**

### 시도 3 — 디버그 테스트
- 데이터 3개 (16~26 토큰) 초간단 테스트
- Gemma: loss 1135 / **Llama 3.2: loss 4.2**
- **결론: Gemma 모델 호환 문제 확정**

### 최종 — Llama 3.2 1B로 전체 학습
- 필터링된 29개 데이터로 3 epoch 학습
- loss 3.44 → 3.23 (정상 범위, 감소 추세)
- 학습 시간 20.3초, 에러 없음
- **파인튜닝 파이프라인 정상 작동 확인**

---

## ✅ 성공 조건 체크리스트

- [x] 프롬프트 포맷 수정 시도
- [x] 데이터 필터링 (62개 → 29개)
- [x] 디버그 테스트로 원인 확정 (Gemma 호환 문제)
- [x] Llama 3.2 1B 모델 교체
- [x] loss 정상 범위 (3.4) 확인
- [x] 학습 완료 (24스텝, 20.3초, 에러 없음)
- [x] 영상 녹화 완료

---

## 📅 다음 단계 예고 | Next Up

**Day 027** — 데이터 확장 + 학습 강화 + Before/After 비교
- 크라베오 데이터 200개 이상으로 확장
- 10 epoch 이상 학습
- 학습 전 모델 vs 학습 후 모델 답변 비교 테스트

Day 027 — Expand Dataset + Stronger Training + Before/After Comparison
- Expand Cravveo dataset to 200+ entries
- Train for 10+ epochs
- Compare base model vs fine-tuned model responses

---

[[2026-06-20_Day026_Work_Order|Day 026 작업지시서]] | [[../25일차/2026-06-17_Day025_Work_Order|← Day 025]] | [[../Cravveo_100Day_Master_Guide]]

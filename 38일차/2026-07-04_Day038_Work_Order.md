# Day 038 작업지시서 | Day 038 Work Order
# 크라베오 AI 최적화 — q4_0 변환 + 컨텍스트 축소
# Cravveo AI Optimization — q4_0 Conversion + Context Reduction

---

## 노트북 사양 및 사용 모델 | Specs & Model

| 항목 | 내용 |
|------|------|
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | Radeon Vega 내장 (AI 연산 불가) |
| 베이스 모델 | Llama 3.2 3B Instruct |
| LoRA 가중치 | cravveo/cravveo-llama-lora (HuggingFace) |
| 변경 사항 | q8_0 → q4_0 + num_ctx 16384 → 2048 |

---

## 오늘의 목표 | Today's Goal

어제 발견한 문제: CPU 100% + 메모리 5.3GB 점유
Today's problem found: 100% CPU + 5.3GB memory usage

해결 방법 | Solution:
1. GGUF 양자화를 q8_0 → q4_0으로 교체 (용량 절반↓, CPU 부담 절반↓)
2. Modelfile에 `num_ctx 2048` 추가 (컨텍스트 16384 → 2048)
3. 이전/이후 메모리 + CPU 사용량 비교

재학습 없음 — HuggingFace의 기존 LoRA 가중치를 불러와서 변환만 합니다.
No retraining — just load existing LoRA weights from HuggingFace and convert.

---

## 오늘 말할 멘트 | Narration Script

> "어제 모델을 테스트하다가 CPU가 100%까지 올라가는 걸 발견했어요.
> OBS, 크롬, VS Code, Ollama를 동시에 켜야 하는데 이러면 너무 힘들죠.
> 오늘은 재학습 없이 양자화 방식만 바꿔서 성능을 최적화해볼게요."

---

## 작업 순서 | Steps

### Step 1. Colab — q4_0 변환 노트북 실행
- `Day038_Convert_q4.ipynb` 코랩에서 실행
- HuggingFace에서 기존 LoRA 가중치 로드
- q4_0으로 GGUF 변환 후 다운로드

### Step 2. 새 모델 Ollama 등록
- `38일차/` 폴더로 GGUF 파일 이동
- `Modelfile-v3` 적용 (q4_0 + num_ctx 2048)
- `ollama create cravveo:v3 -f Modelfile-v3`

### Step 3. 성능 비교
- v2 (q8_0) vs v3 (q4_0) 메모리 사용량 비교
- `ollama ps`로 확인
- 응답 품질 간단 테스트

---

## 성공 조건 | Success Criteria

- [ ] q4_0 GGUF 변환 완료
- [ ] Ollama에 v3 모델 등록
- [ ] 메모리 사용량 3GB 이하 확인
- [ ] 응답 품질 이상 없음 확인
- [ ] 영상 녹화
- [ ] 커밋 + 푸시

---

## 로드맵 | Roadmap

| 구간 | 내용 |
|------|------|
| **Day 038** ← 오늘 | q4_0 변환 + Modelfile 최적화 |
| Day 039 | 환각 문제 분석 + RAG 도입 준비 |
| Day 040~045 | GitHub 데이터 추출 + 학습 데이터 고도화 |
| Day 046~060 | 로컬 RAG 구축 (ChromaDB) |
| Day 091~100 | Part 1 총정리 |

---

[[../Daily_Log/2026-07-04_Day038_Log|Day 038 로그]] | [[../37일차/2026-07-03_Day037_Work_Order|← Day 037]]

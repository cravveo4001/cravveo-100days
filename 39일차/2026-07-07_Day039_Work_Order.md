# Day 039 작업지시서 | Day 039 Work Order
# ~~환각 문제 심화 분석 + RAG 개선~~ → q4_K_M 재변환 (진행 중 방향 전환)
# ~~Deep Hallucination Analysis + RAG Improvement~~ → q4_K_M Re-conversion (pivoted mid-day)

> **방향 전환 | Mid-day pivot**: RAG 테스트 중 `cravveo:v3`(q4_0)가 문맥과 무관한 헛소리를 생성하는 걸 발견. RAG 매칭 문제보다 더 급한 모델 품질 문제로 오늘 목표를 전환함. 원래 계획(날짜↔Day 매핑 문서 보강 실험)은 Day 040 이후로 이월.
> While testing RAG, found `cravveo:v3` (q4_0) generating incoherent, off-context text. Pivoted today's goal from RAG matching to this more urgent model quality issue. Original plan (date-mapping document enrichment) rolled over to Day 040+.

---

## 노트북 사양 및 사용 모델 | Specs & Model

| 항목 | 내용 |
|------|------|
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | Radeon Vega 내장 (AI 연산 불가) |
| 베이스 모델 | Llama 3.2 3B Instruct |
| LoRA 가중치 | cravveo/cravveo-llama-lora (HuggingFace) |
| 사용 툴 | AnythingLLM (RAG) + Ollama |

---

## 오늘의 목표 | Today's Goal (수정본 | revised)

체계적 테스트(Step 1) 도중, `cravveo:v3`가 RAG 매칭 여부와 무관하게 **문맥과 상관없는 헛소리를 생성**하는 걸 발견함. `cravveo:latest`(v2, q8_0)와 A/B 비교한 결과 v2는 느리지만 말이 되는 문장을 생성 — 원인이 **q4_0 양자화 자체**로 좁혀짐.

**원인 분석:**
`Day038_Convert_q4.ipynb`에서 `quantization_method="q4_0"`을 사용했는데, `q4_0`은 오래된(legacy) 양자화 방식이다. 요즘 GGUF 생태계 표준은 같은 크기대에서 품질 손실이 훨씬 적은 **K-quant 방식(`q4_K_M`)**이다. v2(q8_0)는 느리지만 정상, v3(q4_0)는 빠르지만 깨짐 — 그렇다면 `q4_K_M`으로 다시 변환하면 "빠르면서도 정상"인 중간 지점을 찾을 수 있는지 확인한다.

오늘 할 일 | Today's plan:
0. Colab에서 `Day039_Convert_q4km.ipynb` 실행 — 같은 LoRA 가중치를 `q4_K_M`으로 재변환
1. `Modelfile-v4`로 `cravveo:v4` 등록
2. v2 / v3 / v4 3자 비교 — 동일 질문 3개로 답변 품질(말이 되는지) 확인
3. v4가 정상이면 그걸로 확정, 아니면 `q5_K_M`으로 한 번 더 시도
4. (원래 계획이었던) 날짜↔Day 매핑 문서 보강 실험은 Day 040 이후로 이월

재학습 없음 — 기존 LoRA 가중치 그대로, 양자화 방식만 재시도.
No retraining — reuse existing LoRA weights, only retry the quantization method.

---

## 오늘 말할 멘트 | Narration Script

> "원래 오늘은 RAG 검색 정확도를 테스트하려고 했는데, 테스트 중간에 더 급한 문제를 발견했어요.
> 어제 가볍게 만든 v3 모델이 질문이랑 상관없는 헛소리를 하더라고요.
> 원인을 추적해보니 q4_0이라는 양자화 방식이 너무 오래된 방식이었어요.
> 오늘은 방향을 틀어서, 더 나은 양자화 방식(q4_K_M)으로 다시 변환해볼게요."

---

## 작업 순서 | Steps

### Step 1 (완료, 방향 전환의 계기). 체계적 테스트 — 진행 중 헛소리 문제 발견

`cravveo:v3`로 아래 질문을 테스트하던 중 RAG 매칭 여부와 무관하게 답변 자체가 헛소리로 나오는 걸 발견해서 중단, 방향 전환.

| # | 질문 | 정답 파일 | 결과(O/X) | 비고 |
|---|------|-----------|-----------|------|
| 1 | 2026-05-23일에 뭐했어? | 2026-05-23_Day001_Log.md | X | v3 답변이 문맥과 무관한 내용 |
| 2 | 2026-05-27일에 뭐했어? | 2026-05-27_Day004_Log.md | X | v3 답변 헛소리, 방향 전환 결정 |
| 3~10 | (나머지 8개) | - | - | Day 040 이후 v4 확정 후 재개 |

### Step 2. q4_K_M 재변환 (오늘의 핵심)
- Colab에서 `39일차/Day039_Convert_q4km.ipynb` 실행 (셀 1~4 순서대로)
- 셀 4에서 `quantization_method="q4_k_m"`으로 변환 → GGUF 다운로드
- 다운로드한 파일을 `39일차/cravveo-v4.gguf`로 저장 (파일명 `Modelfile-v4`와 맞추기)

### Step 3. Ollama 등록 + 3자 비교
- `39일차/` 폴더에서 `ollama create cravveo:v4 -f Modelfile-v4` 실행
- AnythingLLM 워크스페이스 모델을 `cravveo:v4`로 변경
- 아래 질문 3개로 v2 / v3 / v4 답변 품질 비교 (문장이 말이 되는지만 확인, 날짜 정확도는 이번엔 안 봄)
  - "2026-05-23일에 뭐했어?"
  - "2026-05-27일에 뭐했어?"
  - "크라베오 컴퍼니가 뭐야?"

### Step 4. 결론 및 다음 단계 결정
- v4가 v2 수준으로 말이 되면서 v3만큼 빠르면 → v4로 확정, cravveo:v3(q4_0)는 폐기
- v4도 여전히 깨지면 → `q5_K_M`으로 한 번 더 시도하거나, Day 040으로 이월
- 날짜↔Day 매핑 문서 보강 실험(원래 Step 2~3 계획)은 v4 확정 이후 Day 040에서 재개

---

## 성공 조건 | Success Criteria

- [x] v2/v3 A/B 비교로 헛소리 원인이 q4_0 양자화임을 확인
- [x] q4_K_M으로 재변환 완료 (`llama-3.2-3b-instruct.Q4_K_M.gguf`, [Colab 노트북](https://colab.research.google.com/drive/1tkvdG80gHwN40VcbbAHk73-MEnebc1vO?usp=sharing))
- [x] Ollama에 cravveo:v4 등록 (num_predict 200→500 수정 포함)
- [x] v2/v3/v4 3자 비교로 v4 품질 정상 여부 확인 → v4 정상 채택
- [x] 문서 보강 실험(날짜↔Day 매핑 문장) 시도 → 실패, RAG 임베딩 검색의 구조적 한계 확인
- [ ] 영상 녹화
- [ ] 커밋 + 푸시

**보류 | Deferred**: 날짜→Day 번호 룩업 테이블 구현은 Day 040으로 이월.

---

## 로드맵 | Roadmap

| 구간 | 내용 |
|------|------|
| Day 038 | q4_0 변환 + RAG 버그 3개 수정 |
| **Day 039** ← 오늘 | q4_0 품질 문제 발견 → q4_K_M 재변환 확정 + 문서 보강 실험(실패) → 룩업 테이블 방향 결정 |
| Day 040 | 날짜→Day 번호 룩업 테이블 구현 (파이썬 딕셔너리 방식) |
| Day 041~045 | GitHub 데이터 추출 + 학습 데이터 고도화 |
| Day 046~060 | 로컬 RAG 구축 (ChromaDB) |
| Day 091~100 | Part 1 총정리 |

---

[[../Daily_Log/2026-07-07_Day039_Log|Day 039 로그]] | [[../38일차/2026-07-04_Day038_Work_Order|← Day 038]]

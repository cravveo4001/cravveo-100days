# Day 046 작업지시서 | Day 046 Work Order
# v10 재학습 — 정체성 데이터 80개로 되돌려 원인 검증
# v10 Retrain — Reverting Identity Data to 80 to Test the Cause

---

## 노트북 사양 및 사용 모델 | Specs & Model

| 항목 | 내용 |
|------|------|
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | Radeon Vega 내장 (AI 연산 불가) |
| 현재 모델 | cravveo:v7 (Llama 3.1 8B + LoRA) — 기준 모델 유지 중 |
| 오늘 작업 | v10 재학습 (44일차 노트북 재사용, Colab T4) |

---

## 오늘의 목표 | Today's Goal

Day 045.5까지 v8, v9 둘 다 v7보다 저하됐다(O5/△5/X20, O3/△9/X18 vs O8/△12/X10). cell 4 로그로 데이터 조합 자체는 정상이었음을 확인했으므로, 남은 유력한 원인은 **정체성 데이터를 80개→94개로 늘린 것 자체**다.

오늘은 이 가설을 직접 검증한다: 정체성 데이터를 **80개(3B→8B 버그 수정은 유지)**로 되돌려서 재학습하고, v7 수준(O8/△12/X10 근처)으로 회복되는지 확인한다.

오늘 할 일 | Today's plan:
1. **HuggingFace 데이터셋을 80개로 되돌리기**: `44일차/cravveo_identity_80.jsonl`(3B→8B 수정은 반영된 상태) 그대로 재업로드 — 완료
2. **v10 재학습**: 같은 44일차 노트북, cell 4에서 이번엔 "정체성 80개 + Obsidian 203개 = 283개"가 나오는지 확인 후 학습
3. **정식 평가**: `정체성_평가세트.py cravveo:v10`로 자동 채점 후 30개 답변 직접 재확인
4. **판단**: v10이 v7 수준으로 돌아오면 → "94개 확장" 가설 확정. 여전히 나쁘면 → 다른 원인(학습 자체의 불안정성 등)을 다시 찾아야 함

---

## 작업 순서 | Steps

### Step 1. HuggingFace 데이터셋 되돌리기 (완료)
- `44일차/cravveo_identity_80.jsonl` → HuggingFace `cravveo/cravveo-briefing-dataset`에 재업로드 (80개, 3B→8B 수정 유지)
- `10일차/cravveo_briefing_dataset.jsonl`도 동일하게 동기화

### Step 2. Colab cell 4 실행 및 확인
- [Colab 노트북](https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing) 열기
- cell 4에서 obsidian 파일 업로드 시 **반드시** `44일차/obsidian_dataset_cleaned.jsonl` 선택
- 출력에 "정체성 80개 + Obsidian 203개 = 283개"가 나오는지 확인
- **학습(cell 5) 실행 전 출력 캡처 — 계속 지키는 규칙**

### Step 3. 학습 및 GGUF 변환
- cell 5(학습) ~ GGUF 변환/다운로드까지 기존과 동일하게 진행

### Step 4. v10 등록 및 평가
- `cravveo-v10.gguf`로 이름 변경, Modelfile-v10 작성(num_predict 100 유지) 후 Ollama 등록
- `정체성_평가세트.py cravveo:v10`로 30문항 자동 채점
- 30개 답변 전부 직접 확인하며 최종채점

### Step 5. 결과 판단 및 기록
- v7/v8/v9/v10 비교하여 "94개 확장" 가설이 맞았는지 최종 판단
- `정체성_평가세트.md` 표에 v10 열 추가, Daily_Log 작성

---

## 성공 조건 | Success Criteria

- [x] HuggingFace 데이터셋 80개로 되돌리기
- [x] cell 4 출력 캡처 (학습 실행 전)
- [x] v10 재학습 완료 + Ollama 등록
- [x] 정체성 평가세트 30문항 자동 채점 + 수동 재채점
- [x] v7/v8/v9/v10 비교하여 "94개 확장" 가설 검증 — 부분 지지(O 개수는 v7보다 많음, O+△ 종합은 여전히 못 미침)
- [ ] 영상 녹화
- [x] 커밋 + 푸시

---

## 로드맵 | Roadmap

| 구간 | 내용 |
|------|------|
| Day 045 | v7 약점 보강 + 같은 날 v8 재학습 → O5/△5/X20으로 저하 |
| Day 045.5 | 같은 데이터로 v9 재학습(로그 확인) → O3/△9/X18, 파일 업로드 실수 가설 배제 |
| **Day 046** ← 오늘 | 정체성 데이터 80개로 되돌려 v10 재학습, "94개 확장" 가설 직접 검증 |

---

[[../Daily_Log/2026-07-22_Day046_Log|Day 046 로그]] | [[../45.5일차/2026-07-20_Day045.5_Work_Order|← Day 045.5]]

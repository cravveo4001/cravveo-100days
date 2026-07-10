# Day 041 작업지시서 | Day 041 Work Order
# 학습 데이터 정체성 오류 수정 + 재학습
# Fix Training-Data Identity Errors + Retrain

---

## 노트북 사양 및 사용 모델 | Specs & Model

| 항목 | 내용 |
|------|------|
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | Radeon Vega 내장 (AI 연산 불가) |
| 베이스 모델 | Llama 3.2 3B Instruct |
| 재학습 데이터 | 정체성 20개(신규) + Obsidian 203개 = 223개 |

---

## 오늘의 목표 | Today's Goal

Day 040에서 발견한 "쇼핑몰" 정체성 오류를 고치려고 학습 데이터(`10일차/cravveo_briefing_dataset.jsonl`, 92개)를 열어보니, 예상보다 훨씬 심각한 오염을 발견했다:

- 92개 중 약 40개가 크라베오랑 아예 무관한 내용이었다 (AI 유튜버 마케팅 전략, 저작권 법적 대응, 자산 증식 전략 등 — 중국어 한자가 섞이고 문법이 깨진 것도 다수)
- 나머지도 "쇼핑몰"(실제로 없음), "Gemma-2B"(Day 026에 Llama 3.2로 교체됨) 같은 오래된/틀린 정보를 포함
- 원인 추적: Day 010~023에 만든 `briefing_pipeline.py`가 매일 아침 일반 AI 질문/답변("아침 브리핑")을 자동 생성해서 같은 파일에 계속 append하고 HuggingFace에 push하는 구조였음. 이게 정체성 데이터랑 섞여버린 것. (다행히 크론잡은 현재 꺼져있어 더 이상 오염되지 않음)

**오늘 한 일:**
1. 실제 사업 현황 확인 (사용자 인터뷰): Chrome 확장 프로그램 4개 게시(Posture Alert Studio, Gesture Remote Controller, Private Web Highlighter, HeadScroll), cravveo.com(도구 모음 사이트), ablescan.app(EU 웹접근성 검사 도구, WCAG 기반), 유튜브 100일 챌린지. 수익은 아직 0원.
2. 오염된 92개를 정확한 사실 기반 20개로 전체 교체, `10일차/cravveo_briefing_dataset.jsonl`에 반영
3. `20일차/cravveo_identity.jsonl`의 "쇼핑몰" 문장도 동일하게 수정
4. HuggingFace `cravveo/cravveo-briefing-dataset`에 재업로드 완료 (20개로 덮어쓰기, 검증됨)
5. `41일차/Day041_Retrain.ipynb` 작성 — 새 정체성 20개 + Obsidian 203개로 재학습, q4_K_M으로 GGUF 변환까지

---

## 오늘 말할 멘트 | Narration Script

> "어제 발견한 '쇼핑몰' 오류를 고치려고 학습 데이터를 열어봤는데, 생각보다 훨씬 심각했어요.
> 92개 데이터 중에 40개 정도가 저랑 아예 상관없는 내용이었어요.
> 예전에 만든 아침 브리핑 자동화 스크립트가 일반 AI 질문들을 계속 같은 파일에 쌓아놨더라고요.
> 오늘은 그걸 다 걷어내고, 진짜 정확한 사실 20개로 완전히 새로 만들어서 재학습할게요."

---

## 작업 순서 | Steps

### Step 1~4 (완료)
위 "오늘 한 일" 참고 — 데이터 정리 + HuggingFace 재업로드까지 완료.

### Step 5. Colab 재학습
- `41일차/Day041_Retrain.ipynb`를 Colab에서 실행 (셀 1~8 순서대로)
- 셀 4에서 `obsidian_dataset.jsonl` 업로드 필요 (`37일차/obsidian_dataset.jsonl` 사용)
- 셀 6 테스트에서 "크라베오 컴퍼니가 뭐야?" 등 질문에 쇼핑몰/Gemma-2B 언급 없이 정확히 답하는지 확인
- 셀 8에서 q4_K_M GGUF 다운로드

### Step 6. Ollama 등록
- 다운로드한 파일을 `41일차/cravveo-v5.gguf`로 저장
- `cd 41일차 && ollama create cravveo:v5 -f Modelfile-v5`

### Step 7. 검증
- AnythingLLM 또는 터미널에서 "크라베오 컴퍼니가 뭐야?" 재질문 → 쇼핑몰/Gemma-2B 언급 사라졌는지 확인
- **주의**: RAG 문서가 붙은 워크스페이스에서 테스트하면 검색된 문서 내용이 섞여 들어와 순수한 모델 답변인지 판단 어려움. 문서 없는 워크스페이스(또는 `ollama run` 터미널)로 테스트해야 정확함
- 답변이 여전히 산만하게 이어지는 건(Day 040에서 이미 기록한 소형 모델의 알려진 한계) 오늘 목표와 별개이므로 더 파고들지 않음

---

## 성공 조건 | Success Criteria

- [x] 학습 데이터 오염 범위 파악 (92개 중 40개 무관 + 정체성 오류 확인)
- [x] 정확한 사실 기반 20개로 데이터 교체
- [x] HuggingFace 재업로드 + 검증
- [x] Day041_Retrain.ipynb 작성 (Colab CUDA fix 이슈 발견/수정 포함)
- [x] Colab 재학습 실행
- [x] cravveo:v5 등록
- [x] "쇼핑몰"/"Gemma-2B" 언급 사라짐 확인 (RAG 없는 순수 워크스페이스로 재검증)
- [ ] 영상 녹화
- [x] 커밋 + 푸시

---

## 로드맵 | Roadmap

| 구간 | 내용 |
|------|------|
| Day 040 | 날짜 룩업 프로토타입 + 300일 로드맵 재점검 |
| **Day 041** ← 오늘 | 학습 데이터 정체성 오류 수정 (92개→20개) + 재학습 준비 |
| Day 042~ | Part 1 계속: Obsidian/GitHub 데이터 기반 파인튜닝 고도화 |

---

[[../Daily_Log/2026-07-09_Day041_Log|Day 041 로그]] | [[../40일차/2026-07-08_Day040_Work_Order|← Day 040]]

# Day 038 YouTube Upload

> 영상 파일: `38일차.mp4`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 038 | RAG가 안 됐던 진짜 이유 3가지 찾은 하루
```
*(50자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 038.
Cravveo Company 100-Day Project, Day 038.

오늘은 모델 경량화 작업으로 시작했다가, RAG 디버깅으로 하루를 다 썼습니다.
Today started as a model optimization task, but turned into a full day of RAG debugging.

한 것 | What I did:
- Colab에서 LoRA 가중치를 q4_0으로 GGUF 변환 (용량/CPU 부담 절반↓)
- Modelfile에 num_ctx 2048 설정 후 cravveo:v3 모델 등록
- AnythingLLM에서 "특정 날짜에 뭐 했어?" 질문 테스트 중 RAG 완전 실패 발견
- 앱의 SQLite DB와 벡터 저장소를 직접 열어서 원인 추적

- Converted LoRA weights to q4_0 GGUF on Colab (halved size/CPU load)
- Set num_ctx 2048 in Modelfile, registered cravveo:v3 model
- While testing "what did I do on [date]?" in AnythingLLM, found RAG totally failing
- Opened the app's SQLite DB and vector store directly to trace the cause

발견한 것 | Discovery — 버그 3개가 순서대로 숨어 있었습니다:
1. 채팅 모드가 "에이전트"로 되어 있어서 검색 자체가 실행이 안 됨
2. Search Preference가 "Default"라서 관련 없는 문서를 가져옴
3. 문맥 조각을 100개로 설정해서 정답 문서가 오히려 잘려나감

3 bugs were stacked, one behind another:
1. Chat mode was set to "Agent" — search never even ran
2. Search Preference was "Default" — pulled irrelevant documents
3. Context chunks set to 100 — the right document got truncated out

하나씩 고치면서 증상이 계속 바뀌는 걸 보고 원인을 좁혀갔습니다.
Fixed them one at a time, watching the symptom shift each time to narrow down the cause.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora

#Cravveo #파인튜닝 #FineTuning #AnythingLLM #RAG #디버깅 #Debugging #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, AnythingLLM, RAG, retrieval augmented generation, 디버깅, debugging, GGUF 변환, quantization, q4_0, Ollama, 환각, hallucination, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 038 완료 | Day 038 Complete

q4_0 변환으로 모델 경량화 완료. 그리고 AnythingLLM RAG가 안 되던 버그 3개를 순서대로 찾아 고쳤습니다.
Finished q4_0 model optimization. Also found and fixed 3 stacked bugs breaking AnythingLLM's RAG.

오늘의 핵심 발견 | Key discovery:
"모델을 바꿔도 안 된다"는 증상만 보고 판단하지 않고, 앱 내부 DB를 직접 열어봐야 진짜 원인이 보였습니다.
Instead of judging by symptoms alone ("still broken after switching models"), opening the app's internal DB revealed the real cause.

다음 단계 | Next step:
Day 039 — 환각 문제 심화 분석 + RAG 개선

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 038 완료 + Day 039 예고 | Day 038 Done + Day 039 Preview

오늘은 모델 경량화(q4_0)로 시작했는데, RAG 디버깅으로 하루를 다 썼습니다.
Today started with model optimization (q4_0), but turned into a full day of RAG debugging.

버그가 3개나 쌓여 있었습니다 | 3 bugs were stacked on top of each other:
1️⃣ 채팅 모드 "에이전트" → 검색 자체가 안 됨
2️⃣ Search Preference "Default" → 엉뚱한 문서 검색
3️⃣ 문맥 조각 100개 → 정답 문서가 잘려나감

1️⃣ Chat mode "Agent" → search never ran
2️⃣ Search Preference "Default" → wrong documents retrieved
3️⃣ 100 context chunks → correct document got truncated

하나씩 고치니 증상이 바뀌었고, 결국 정확한 날짜 문서를 찾아내는 데 성공했습니다.
Fixing them one by one changed the symptoms each time, until it finally found the right document.

내일 Day 039 — 환각 문제 심화 분석
Tomorrow Day 039 — deeper hallucination analysis

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #RAG #디버깅
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `38일차.mp4` 선택
- [ ] 제목 입력
- [ ] 설명 입력
- [ ] 썸네일 등록
- [ ] 공개 범위는 먼저 `비공개`로 업로드
- [ ] HD 처리 완료 확인
- [ ] 고정 댓글 작성
- [ ] 커뮤니티 게시물 작성
- [ ] 최종 공개 또는 예약 공개

---

## 썸네일 이미지 프롬프트

```text
Create a 1280x720 YouTube thumbnail for a Korean tech learning video.

Channel: Cravveo Company.
Episode: Day 038.
Topic: a complete beginner set out to optimize a fine-tuned AI model (quantization), but instead spent the day debugging a RAG system that was completely failing — eventually tracing it down to 3 stacked configuration bugs by opening the app's internal database directly. Build in Public.

Main text must be large and readable:
"DAY 038"
"버그 3개를 찾아낸 하루"

Small supporting text:
"RAG가 안 됐던 진짜 이유"
"모델 문제가 아니었다"

Visual style:
- visual metaphor: a magnifying glass or flashlight revealing hidden layers/gears inside a machine, or a debugging/detective theme
- feeling: "persistence pays off" — frustration turning into a methodical breakthrough
- clean tech documentary style
- mood: focused, investigative, satisfying resolution
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-04_Day038_Work_Order|Day 038 작업지시서]] | [[../Daily_Log/2026-07-06_Day038_Log|Day 038 로그]] | [[../37일차/Day037_YouTube_Upload|← Day 037 유튜브]]

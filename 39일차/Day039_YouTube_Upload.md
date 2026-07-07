# Day 039 YouTube Upload

> 영상 파일: `39일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1tkvdG80gHwN40VcbbAHk73-MEnebc1vO?usp=sharing

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 039 | 재변환 성공, 근데 검색은 또 실패했다
```
*(46자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 039.
Cravveo Company 100-Day Project, Day 039.

오늘은 원래 RAG 검색 테스트를 하려고 했는데, 두 번이나 방향을 틀었습니다.
Today I set out to test RAG search, but ended up pivoting direction twice.

한 것 | What I did:
- 날짜 질문 테스트 중 어제 만든 v3 모델이 헛소리하는 걸 발견 (1차 방향 전환)
- v2와 A/B 비교 → 원인이 q4_0 양자화 방식이라고 결론
- Colab에서 q4_K_M(더 나은 양자화 방식)으로 재변환, cravveo:v4 등록
- 답변이 200토큰에서 잘리는 버그도 발견해서 수정
- 문서에 "이 날짜는 Day 몇 번입니다"라는 힌트 문장을 추가하는 실험 진행 (2차 시도)

- While testing date-based questions, found yesterday's v3 model generating gibberish (1st pivot)
- A/B compared with v2 → traced the cause to the q4_0 quantization method
- Re-converted with q4_K_M (better quantization) on Colab, registered cravveo:v4
- Also found and fixed a bug where answers got cut off at 200 tokens
- Tried adding "this date is Day N" hint sentences into documents (2nd attempt)

발견한 것 | Discovery:
모델 품질 문제는 해결했지만, 문서 힌트 추가는 실패했습니다.
37개 파일이 구조적으로 너무 비슷해서, 짧은 날짜 문장 하나로는 임베딩 검색이 못 바뀝니다.
Model quality was fixed, but the document-hint experiment failed.
With 37 nearly-identical documents, a short date sentence isn't enough to shift embedding search.

결론 | Conclusion:
AI 검색에 계속 기대는 대신, 날짜→Day번호를 코드로 직접 매핑하는 방식으로 전환하기로 했습니다.
Instead of relying further on AI search, decided to switch to a direct code-based date-to-day lookup table.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
Colab: https://colab.research.google.com/drive/1tkvdG80gHwN40VcbbAHk73-MEnebc1vO?usp=sharing

#Cravveo #파인튜닝 #FineTuning #양자화 #Quantization #AnythingLLM #RAG #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, 양자화, quantization, q4_K_M, GGUF, AnythingLLM, RAG, retrieval augmented generation, Ollama, 임베딩 검색, embedding search, 디버깅, debugging, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 039 완료 | Day 039 Complete

q4_K_M 재변환으로 모델 품질 문제 해결. 문서 보강으로 RAG 검색 고치려던 시도는 실패했지만, 왜 안 되는지는 명확히 확인했습니다.
Fixed the model quality issue with q4_K_M re-conversion. The document-enrichment fix for RAG search failed, but I now clearly understand why.

오늘의 핵심 발견 | Key discovery:
안 되는 걸 계속 붙잡는 대신, 다른 도구(날짜→Day 룩업 테이블)로 바꾸기로 결정했습니다.
Instead of continuing to force something that wasn't working, decided to switch tools (date-to-day lookup table).

다음 단계 | Next step:
Day 040 — 날짜→Day 번호 룩업 테이블 구현

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 039 완료 + Day 040 예고 | Day 039 Done + Day 040 Preview

오늘은 계획을 두 번이나 바꿨습니다.
Today I changed plans twice.

1️⃣ RAG 테스트하다가 → 모델이 헛소리하는 걸 발견 → 양자화 방식(q4_0→q4_K_M) 문제로 해결
2️⃣ 문서에 날짜 힌트 추가 실험 → 실패 → 임베딩 검색의 구조적 한계 확인

1️⃣ Testing RAG → found the model generating gibberish → fixed by switching quantization (q4_0→q4_K_M)
2️⃣ Tried adding date hints to documents → failed → confirmed a structural limit of embedding search

계속 안 되는 방법을 붙잡는 대신, 다른 방법으로 바꾸기로 했습니다.
Instead of forcing a method that wasn't working, decided to switch approaches.

내일 Day 040 — 날짜→Day 번호 룩업 테이블 구현
Tomorrow Day 040 — building a date-to-day lookup table

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #RAG #양자화
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `39일차.mp4` 선택
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
Episode: Day 039.
Topic: a complete beginner planned to test RAG search accuracy, but twice had to change direction mid-day — first discovering a broken quantization method causing the AI to generate gibberish, fixing it, then trying a document-hint experiment to fix search that ultimately failed, leading to the decision to build a simple code-based lookup table instead of relying on AI search. Build in Public.

Main text must be large and readable:
"DAY 039"
"계획을 두 번 바꾼 하루"

Small supporting text:
"양자화 문제는 해결"
"검색은 다른 방법으로"

Visual style:
- visual metaphor: a forked road or a compass changing direction, or two paths merging into one clearer path
- feeling: "adapting under pressure" — plans changing but ending with clarity, not defeat
- clean tech documentary style
- mood: resilient, resourceful, calm resolution after a winding day
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-07_Day039_Work_Order|Day 039 작업지시서]] | [[../Daily_Log/2026-07-07_Day039_Log|Day 039 로그]] | [[../38일차/Day038_YouTube_Upload|← Day 038 유튜브]]

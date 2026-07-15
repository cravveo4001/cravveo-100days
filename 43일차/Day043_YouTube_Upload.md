# Day 043 YouTube Upload

> 영상 파일: `43일차.mp4`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 043 | 믿고 있던 버전도 사실 다 고장나 있었다
```
*(47자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 043.
Cravveo Company 100-Day Project, Day 043.

어제 만든 고정 평가세트로, 오늘은 재학습 없이 딱 하나만 했습니다 — 지금 쓰고 있던 v4를 30문항으로 제대로 채점하는 것.
Using yesterday's fixed evaluation set, today I did just one thing — properly scoring the v4 I'd been relying on, across 30 questions.

한 것 | What I did:
- 정체성 질문 20개 + 표현 바꾼 질문 10개, 총 30문항으로 v4 전체 테스트
- AnythingLLM에서 응답이 계속 끊기고 타임아웃나서 터미널로 우회
- 30개 전부 채점해서 결과표 완성

- Tested v4 against all 30 questions (20 verbatim + 10 rephrased)
- AnythingLLM kept timing out, switched to testing via terminal
- Scored all 30 and completed the results table

발견한 것 | Discovery:
결과는 O 0개, 부분 정답 2개, 완전 오답 28개였습니다.
그동안 "v4는 그나마 안정적이다"라고 믿고 있었는데, 사실 날짜 질문 몇 개로만 테스트했던 거지 정체성 질문은 제대로 검증한 적이 없었습니다.
The result: 0 fully correct, 2 partially correct, 28 completely wrong.
I had been assuming "v4 is relatively stable" — but that was based on testing a few date questions, never a proper identity check.

결론 | Conclusion:
지금 있는 모든 버전(v2, v4, v5, v6)이 이 평가세트를 통과하지 못합니다. 다음 재학습이 사실상 첫 진지한 시도가 될 것 같습니다.
None of the existing versions (v2, v4, v5, v6) pass this evaluation set. The next retrain will essentially be the first serious attempt.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora

#Cravveo #파인튜닝 #FineTuning #평가세트 #Evaluation #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, 평가세트, evaluation set, 벤치마크, benchmark, LoRA, Llama 3.2, HuggingFace, Ollama, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 043 완료 | Day 043 Complete

30문항 고정 평가세트로 v4를 처음 제대로 채점했습니다. 결과: O 0 / △ 2 / X 28.
Properly scored v4 for the first time with a fixed 30-question set. Result: 0 correct, 2 partial, 28 wrong.

오늘의 핵심 발견 | Key discovery:
"안정적이다"라고 믿어온 버전도, 제대로 재보니 사실 다 고장나 있었습니다. 감이 아니라 데이터로 확인해야 했던 이유입니다.
The version I trusted as "stable" turned out to be broken too, once properly measured. This is exactly why relying on gut feeling wasn't enough.

다음 단계 | Next step:
Day 044 — 정체성 데이터 60~80개로 보강 + 더 큰 베이스 모델 실험

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 043 완료 + Day 044 예고 | Day 043 Done + Day 044 Preview

오늘은 재학습 없이 딱 하나만 했습니다 — 지금 쓰던 모델을 제대로 채점하는 것
Today I did just one thing — properly scoring the model I'd been relying on

30문항 고정 평가세트로 v4 테스트 결과:
Testing v4 with a fixed 30-question set:

✅ 정답: 0개
🔶 부분 정답: 2개
❌ 완전 오답: 28개

믿고 있던 버전이 사실 처음부터 다 고장나 있었습니다 😅
The version I trusted turned out to be broken from the start 😅

내일 Day 044 — 정체성 데이터 보강 + 더 큰 모델 실험 시작
Tomorrow Day 044 — beefing up identity data + testing a bigger model

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #평가세트
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `43일차.mp4` 선택
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
Episode: Day 043.
Topic: a complete beginner built a fixed 30-question evaluation set for their AI model, then properly scored the version they had trusted as "stable" — only to discover it scored 0 out of 30 correct, revealing that all existing model versions were actually broken. Build in Public.

Main text must be large and readable:
"DAY 043"
"믿던 버전도 사실 0점이었다"

Small supporting text:
"30문항 중 정답 0개"
"감 대신 데이터로 확인"

Visual style:
- visual metaphor: a report card or scoresheet revealing a shocking failing grade, or a magnifying glass exposing cracks in something that looked solid
- feeling: "sobering but clarifying" — an uncomfortable truth revealed through rigorous testing
- clean tech documentary style
- mood: analytical, a little deflating but ultimately constructive
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-14_Day043_Work_Order|Day 043 작업지시서]] | [[../Daily_Log/2026-07-14_Day043_Log|Day 043 로그]] | [[../42일차/Day042_YouTube_Upload|← Day 042 유튜브]]

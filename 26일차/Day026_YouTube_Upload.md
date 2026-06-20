# Day 026 YouTube Upload

> 영상 파일: `26일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 026 | 3일간의 사투 — 1일차 실패, 하루 쉬고, 3일차에 모델 바꿔서 성공
```
*(60자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 026.
Cravveo Company 100-Day Project, Day 026.

3일간의 기록입니다.
This is a 3-day story.

1일차: Gemma 2B로 파인튜닝 학습을 3시간 넘게 돌렸습니다. 
포맷을 바꿔보고, 데이터를 필터링하고, 공식 방법도 써봤습니다.
어떤 방법을 써도 loss 1200. 전부 실패했습니다.

2일차: 하루 쉬었습니다.
머리를 좀 식히고 다시 생각했습니다.

3일차: 다시 도전했습니다.
데이터 3개짜리 초간단 테스트를 만들어서 돌렸습니다.
Gemma: loss 1135. Llama 3.2: loss 4.2.
같은 코드, 같은 데이터인데 모델만 바꿨더니 바로 됐습니다.
최종 학습: loss 3.44 → 3.23. 20.3초 만에 완료.

Day 1: Ran Gemma 2B fine-tuning for over 3 hours.
Tried format changes, data filtering, official methods.
Loss stayed at 1200 no matter what. Complete failure.

Day 2: Took a break.
Cleared my head and rethought the approach.

Day 3: Tried again.
Created a minimal 3-entry debug test.
Gemma: loss 1135. Llama 3.2: loss 4.2.
Same code, same data — switching the model fixed everything.
Final training: loss 3.44 → 3.23. Done in 20.3 seconds.

오늘의 핵심 교훈 | Key lesson:
파인튜닝에서 가장 중요한 건 코드가 아니라 모델 호환성이었습니다.
막히면 가장 작은 단위로 테스트하라. 답이 보인다.
쉬는 것도 전략이다. 3시간 삽질한 뒤 하루 쉬고 오니까 30분 만에 해결.

The most important thing in fine-tuning wasn't the code — it was model compatibility.
When stuck, test with the smallest unit. The answer will show itself.
Rest is a strategy. After 3 hours of failure, a day off led to a 30-minute fix.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 027에서는 데이터를 200개 이상으로 늘리고, 학습 전/후 모델 답변을 비교합니다.
In Day 027, we expand data to 200+ entries and compare model responses before vs after training.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Unsloth #Llama #Gemma #모델교체 #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, Llama 3.2, Gemma 2B, 모델 교체, model switch, loss, 학습 loss, 구글 코랩, Google Colab, T4 GPU, LoRA, SFTTrainer, 디버그, debug, 호환성, compatibility, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 실패, failure, 재도전, retry
```

---

### 고정 댓글

```text
Day 026 완료 | Day 026 Complete

3일간의 기록:
1일차 — Gemma 2B로 3시간 넘게 시도. 전부 실패. loss 1200.
2일차 — 하루 쉼. 머리 식히기.
3일차 — 데이터 3개로 디버그 테스트 → 모델 문제 확인 → Llama 3.2로 교체 → loss 3.4 성공!

3-day story:
Day 1 — 3+ hours with Gemma 2B. Everything failed. Loss 1200.
Day 2 — Took a break. Reset my mind.
Day 3 — Debug test with 3 entries → found model issue → switched to Llama 3.2 → loss 3.4 success!

핵심: 같은 코드 + 같은 데이터 + 다른 모델 = 완전히 다른 결과
Key: Same code + same data + different model = completely different results

📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

다음 Day 027 | Next Day 027
데이터 200개로 확장 + 학습 전/후 모델 답변 비교
Expand to 200+ entries + before/after model comparison
```

---

### 커뮤니티 게시물

```text
Day 026 완료 ✅ | Day 026 Complete ✅

3일간의 사투를 기록합니다.
A 3-day battle, documented.

1일차: Gemma 2B로 파인튜닝 3시간. 전부 실패.
포맷 바꾸고, 데이터 필터링하고, 공식 방법 써봤는데
뭘 해도 loss 1200. 정상은 1~5입니다.
Day 1: 3 hours of Gemma 2B fine-tuning. Everything failed.
Format changes, data filtering, official methods — loss 1200 no matter what.

2일차: 하루 쉬었습니다.
삽질만 계속하면 답이 안 보입니다. 쉬는 것도 전략입니다.
Day 2: Took a break.
When you keep digging, you can't see the answer. Rest is a strategy.

3일차: 데이터 3개짜리 초간단 테스트를 돌렸습니다.
Gemma: loss 1135 / Llama 3.2: loss 4.2
모델을 바꿨더니 30분 만에 해결됐습니다.
최종 학습: loss 3.44 → 3.23. 성공.
Day 3: Ran a minimal 3-entry debug test.
Gemma: loss 1135 / Llama 3.2: loss 4.2
Switching models solved it in 30 minutes.
Final training: loss 3.44 → 3.23. Success.

오늘의 교훈:
3시간 삽질한 뒤 하루 쉬고 오니까 30분 만에 해결.
막히면 가장 작은 단위로 테스트하라. 답이 보인다.
Today's lesson:
After 3 hours of failure, a day off led to a 30-minute fix.
When stuck, test with the smallest unit. The answer will show itself.

---

Day 027 예고 | Day 027 Preview
데이터를 200개 이상으로 확장하고, 학습 전/후 모델 답변을 비교합니다.
Expand data to 200+ entries and compare before vs after training.

#Cravveo #파인튜닝 #Llama #Gemma #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `26일차.mp4` 선택
- [ ] 제목 입력 (60자 확인)
- [ ] 설명 입력
- [ ] 썸네일 등록
- [ ] 공개 범위는 먼저 `비공개`로 업로드
- [ ] HD 처리 완료 확인
- [ ] 설명/해시태그/태그 확인
- [ ] 고정 댓글 작성
- [ ] 커뮤니티 게시물 작성
- [ ] 최종 공개 또는 예약 공개

---

## 썸네일 이미지 프롬프트

```text
Create a 1280x720 YouTube thumbnail for a Korean tech learning video.

Channel: Cravveo Company.
Episode: Day 026.
Topic: a complete beginner's 3-day battle with AI fine-tuning — Day 1 failure (3+ hours), Day 2 rest, Day 3 model switch success. Gemma loss 1200 vs Llama loss 3.4, Build in Public.

Main text must be large and readable:
"DAY 026"
"3일간의 사투 — 드디어 성공"

Small supporting text:
"Gemma: 1200 → Llama: 3.4"
"1일차 실패 → 하루 쉬고 → 3일차 성공"

Visual style:
- visual metaphor: a 3-step timeline — red X (failure), pause/rest, green checkmark (success)
- feeling: "persistence wins" — exhaustion turning into triumph
- clean tech documentary style
- mood: hard-earned victory after multiple days of struggle
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 026" and "3일간의 사투 — 드디어 성공" prominent, 3-day journey visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 026 영상에 사용할 배경음악 콘셉트를 만들어줘.
이 영상은 3일간의 기록이야. 1일차에 3시간 넘게 시도했지만 전부 실패하고, 하루 쉬고, 3일차에 모델을 바꿔서 30분 만에 성공했어.
"삽질 끝에 답은 의외로 간단했다"는 안도감과 "쉬는 것도 전략이다"는 깨달음이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, relieved discovery, 85 BPM, loopable.
```

### 2. 1일차 실패 파트

```text
배경음악을 만들어줘. 1일차에 Gemma로 3시간 넘게 시도하며 계속 실패하는 파트야.
loss 1200이 계속 나오고 포맷도 바꿔보고 데이터도 바꿔봤지만 안 되는 답답함이 담겼으면 좋겠어.
repeated failure, growing frustration, 3 hours of struggle, minor key electronic, no vocals, 가사 없음, loopable.
```

### 3. 2일차 휴식 파트

```text
배경음악을 만들어줘. 1일차 실패 후 하루 쉬면서 머리를 식히는 파트야.
"오늘은 쉬자... 내일 다시 하면 돼" 하는 차분하고 여유로운 분위기가 담겼으면 좋겠어.
rest day, mental reset, calm breathing space, ambient electronic, no vocals, 가사 없음, loopable.
```

### 4. 3일차 재도전 파트

```text
배경음악을 만들어줘. 하루 쉬고 3일차에 다시 도전하는 파트야.
"이번에는 다르게 접근하자" 하는 차분하지만 결의에 찬 분위기가 담겼으면 좋겠어.
calm determination, fresh approach, clean electronic, no vocals, 가사 없음, loopable.
```

### 5. 디버그 테스트 파트

```text
배경음악을 만들어줘. 데이터 3개짜리 초간단 테스트를 돌리는 파트야.
"이걸로 원인을 잡자" 하는 집중되고 긴장된 분위기가 담겼으면 좋겠어.
focused debugging, last chance test, tense electronic, no vocals, 가사 없음, loopable.
```

### 6. 원인 발견 + 모델 교체 파트

```text
배경음악을 만들어줘. Gemma loss 1135 vs Llama loss 4.2를 보고 원인을 발견하고 모델을 교체하는 파트야.
"아... 모델이 문제였구나! 바꾸자!" 하는 깨달음과 새로운 시작이 담겼으면 좋겠어.
realization and pivot, fresh start, brightening electronic, no vocals, 가사 없음, loopable.
```

### 7. 성공 확인 파트

```text
배경음악을 만들어줘. Llama 3.2에서 loss 3.4가 나오며 드디어 성공하는 파트야.
3일간의 사투 끝에 "됐다!!!" 하는 안도감과 감동이 담겼으면 좋겠어.
hard-earned breakthrough, emotional relief, bright warm electronic, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: a 3-day struggle — Day 1 failure after 3+ hours with Gemma, Day 2 rest, Day 3 model switch to Llama and success in 30 minutes. Build in Public.
Mood: persistence through failure, rest as strategy, simple answer after complex struggle.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 026 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"3일간의 기록이다 — 실패하고, 쉬고, 다시 도전해서 성공했다" 하는 예고 느낌이 담겼으면 좋겠어.
short opener, epic mini-journey preview, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner spent 3 days on AI fine-tuning — Day 1 failure, Day 2 rest, Day 3 success by switching models.
Mood: tired but deeply satisfied, "persistence and rest both matter", forward-looking.
Style: warm electronic pad, slow resolution, no vocals, 가사 없음, 80 BPM.
```

---

[[2026-06-20_Day026_Work_Order|Day 026 작업지시서]] | [[../25일차/Day025_YouTube_Upload|← Day 025 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

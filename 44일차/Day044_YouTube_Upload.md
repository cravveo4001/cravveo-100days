# Day 044 YouTube Upload

> 영상 파일: `44일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 044 | 드디어 쓸만한 모델이 나왔습니다
```
*(42자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 044.
Cravveo Company 100-Day Project, Day 044.

Day 043에서 전 버전이 0점(30문항 중)이었던 걸 확인한 뒤, 오늘은 처음으로 진짜 나아진 모델을 만들었습니다.
After Day 043 revealed every existing version scored 0/30, today I finally built a version that's actually better.

한 것 | What I did:
- 정체성 데이터 20개를 80개로 확장 (같은 사실을 3~4가지 표현으로, 억지 복제 아님)
- 베이스 모델을 3B에서 8B로 교체 — 무료 Colab T4에서 문제없이 로드됨을 확인
- Obsidian 자동 추출 데이터에도 옛날 "쇼핑몰" 오답이 남아있던 걸 발견해서 정리
- 8B + 정체성 80개 + Obsidian 203개로 재학습 → v7

- Expanded identity data from 20 to 80 samples (same facts in 3-4 phrasings, not forced duplication)
- Switched base model from 3B to 8B — confirmed it loads fine on free Colab T4
- Found the old "online shop" error still lingering in auto-extracted Obsidian data, cleaned it
- Retrained with 8B + 80 identity + 203 Obsidian samples → v7

발견한 것 | Discovery:
5개 질문만 던져봤을 때는 결과가 안 좋아 보여서 "처음부터 다시 하자"는 유혹이 있었습니다.
근데 30문항 전체로 다시 확인해보니, 실제로는 훨씬 나은 결과였습니다.
Testing just 5 questions looked bad enough to tempt me into starting over from scratch.
But checking the full 30 questions instead showed a much better picture than the sample suggested.

결과 | Result:
30문항 중 O(정답) 8개, △(부분 정답) 12개, X(오답) 10개 — 이전 버전(0점)과는 완전히 다른 수준입니다.
8 fully correct, 12 partially correct, 10 wrong out of 30 — a completely different level from the previous version (0 correct).

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
Colab: https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Llama3 #8B #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Llama 3.1, 8B 모델, large language model, 평가세트, evaluation set, LoRA, HuggingFace, Ollama, Google Colab, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 044 완료 | Day 044 Complete

정체성 데이터 80개 + 8B 모델로 재학습해서 30문항 중 O8/△12를 받았습니다. 이전 버전은 전부 0점이었습니다.
Retrained with 80 identity samples + an 8B model, scoring 8 correct/12 partial out of 30. Every previous version scored 0.

오늘의 핵심 발견 | Key discovery:
5개 질문만 보고 "다시 하자"고 할 뻔했는데, 30문항 전체로 재확인하니 완전히 다른 그림이었습니다. 감으로 판단하지 않는 게 진짜 중요했습니다.
Almost restarted from scratch based on just 5 questions — but the full 30-question check told a completely different story. Not judging by gut feeling really mattered here.

다음 단계 | Next step:
Day 045 — v7의 남은 약점(구체적 제품 정보, 지어내는 습관) 개선 계획

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 044 완료 + Day 045 예고 | Day 044 Done + Day 045 Preview

드디어 쓸만한 모델이 나왔습니다 🎉
Finally got a model that actually works 🎉

Day 043: 전 버전 30문항 중 0점
Day 044: 데이터 80개 + 8B 모델로 재도전

Day 043: every version scored 0/30
Day 044: retried with 80 samples + an 8B model

결과 | Result:
✅ 정답 8개
🔶 부분 정답 12개
❌ 오답 10개

중간에 "5개만 봐도 답 나온다, 처음부터 다시 하자"는 유혹이 있었지만
30문항 다 채점해보니 완전히 다른 결과였습니다.

Midway I almost gave up based on just 5 sample questions —
but the full 30-question check told a very different story.

내일 Day 045 — 남은 약점 보완 계획
Tomorrow Day 045 — planning fixes for the remaining weaknesses

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #8B모델
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `44일차.mp4` 선택
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
Episode: Day 044.
Topic: after every previous fine-tuned model version scored zero on a 30-question evaluation, a complete beginner expanded their training data, switched to a larger 8B base model, and finally produced a version that scores meaningfully well — resisting the temptation to judge and restart based on just a few sample questions, instead verifying with the full test set. Build in Public.

Main text must be large and readable:
"DAY 044"
"드디어 쓸만한 모델이 나왔다"

Small supporting text:
"30문항 중 0점 → 8+12점"
"8B 모델로 교체"

Visual style:
- visual metaphor: a graph or bar chart breaking through a ceiling, or a scoreboard flipping from zero to a real number
- feeling: "breakthrough after a long struggle" — genuine milestone, earned progress
- clean tech documentary style
- mood: triumphant but grounded, not overhyped
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-17_Day044_Work_Order|Day 044 작업지시서]] | [[../Daily_Log/2026-07-17_Day044_Log|Day 044 로그]] | [[../43일차/Day043_YouTube_Upload|← Day 043 유튜브]]

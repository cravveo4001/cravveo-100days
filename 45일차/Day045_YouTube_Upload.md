# Day 045 YouTube Upload

> 영상 파일: `45일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing (44일차 노트북 재사용 — cell 4가 HuggingFace 최신 데이터를 자동으로 가져오기 때문에 가능)

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 045 | 고쳐서 재학습했는데 더 나빠졌습니다
```
*(41자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 045.
Cravveo Company 100-Day Project, Day 045.

Day 044에서 v7이 받은 O8/△12/X10 결과를 보고, 남은 약점을 고쳐서 다시 학습해봤습니다. 결과는 예상과 반대였습니다.
After v7 scored 8/12/10 on Day 044, I fixed its remaining weaknesses and retrained. The result went the opposite way I expected.

한 것 | What I did:
- 베이스 모델을 8B로 바꿔놓고 학습 데이터엔 "3B"라고 남아있던 오류 발견 및 수정
- 계속 틀리던 항목(Chrome 확장, ablescan.app, cravveo.com, 하루 일과) 데이터 14개 보강 → 정체성 데이터 94개
- 지어내기(confabulation) 원인 조사: 학습 답변 평균 72자 vs 생성 설정 120~500자 불일치 발견
- 페이스 원칙(주 1~2회 재학습)을 깨고 같은 날 바로 v8 재학습 진행

- Found and fixed a stale bug: switched to an 8B base model but training data still said "3B"
- Reinforced 14 weak items (Chrome extensions, ablescan.app, cravveo.com, daily routine) → 94 identity samples total
- Investigated the confabulation cause: training answers average 72 characters vs a 120-500 token generation setting
- Broke my own pacing rule (retrain 1-2x/week) and retrained the same day → v8

발견한 것 | Discovery:
자동 채점(키워드 매칭)으로는 O12/△10/X8로 v7보다 나아 보였습니다. 그런데 30개 답변을 직접 다시 읽어보니 실제로는 O5/△5/X20 — v7보다 더 나빠졌습니다.
Automatic keyword-based scoring showed 12/10/8, looking better than v7. But re-reading all 30 answers by hand revealed the real score: 5/5/20 — actually worse than v7.

자동 채점이 "불가능"이라는 단어 안의 "가능"을 정답 키워드로 잘못 인식하는 등, 숫자만 보고 판단하면 안 되는 이유를 직접 확인했습니다.
The auto-scorer even matched "impossible" as a hit because it contains the substring "possible" — a hands-on lesson in why raw numbers alone can mislead.

원인을 더 파려고 했지만 Colab 세션이 끊겨서, 학습에 실제로 어떤 데이터가 들어갔는지 보여주는 로그가 사라졌습니다.
I tried to dig deeper into the cause, but the Colab session disconnected — the log showing exactly what data went into training was gone for good.

결과 | Result:
v8은 폐기하고 v7을 계속 기준 모델로 사용합니다. 대신 "재학습 로그는 실행 중에 반드시 캡처해둔다"는 규칙을 새로 만들었습니다.
v8 is discarded; v7 remains the reference model. In exchange, I added a new rule: always capture retrain logs while they're still running.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다. 오늘처럼 잘 안 풀린 날도 그대로 보여드립니다.
It is a beginner's learning journal — including days like today, where things didn't go as planned.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
Colab: https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Llama3 #8B #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Llama 3.1, 8B 모델, large language model, 평가세트, evaluation set, confabulation, 자동채점, keyword matching, LoRA, HuggingFace, Ollama, Google Colab, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 045 완료 | Day 045 Complete

v7의 약점(모델 버전 오류, ablescan.app 등)을 데이터로 고쳐서 재학습했는데, 자동채점(O12/△10/X8)과 달리 직접 재채점하니 O5/△5/X20으로 v7보다 나빠졌습니다.
Retrained after fixing v7's weaknesses (stale model-version bug, ablescan.app, etc.), but manual re-grading showed 5/5/20 — worse than v7, despite auto-scoring saying otherwise (12/10/8).

오늘의 핵심 발견 | Key discovery:
숫자로 재보는 것도 중요하지만, 그 숫자를 만드는 채점 방식 자체를 의심해야 할 때가 있습니다. "불가능"이라는 단어에 "가능"이 들어있다는 이유로 자동채점이 오답을 정답으로 셌습니다.
Measuring with numbers matters, but sometimes you have to question the scoring method itself. The auto-scorer counted a wrong answer as correct simply because "impossible" contains the substring "possible."

다음 단계 | Next step:
Day 046~ — v7을 기준 모델로 유지. 재학습 로그 캡처 규칙 적용 후 v9 재학습 예정.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 045 완료 + Day 046 예고 | Day 045 Done + Day 046 Preview

오늘은 좋은 소식이 아닙니다 — 고쳐서 재학습했는데 더 나빠졌습니다.
Not great news today — I fixed things, retrained, and it got worse.

Day 044: v7 → O8/△12/X10
Day 045: 데이터 고치고 재학습(v8) → 자동채점 O12/△10/X8 (좋아보임)
       → 직접 재채점하니 O5/△5/X20 (실제로는 더 나쁨)

Day 044: v7 → 8 correct/12 partial/10 wrong
Day 045: fixed data, retrained (v8) → auto-score looked better (12/10/8)
       → manual re-grading showed the truth: worse (5/5/20)

결과 | Result:
🔻 v8 폐기, v7을 계속 사용
🐛 자동채점의 허점 발견 ("불가능"을 "가능"으로 오인식)
📝 재학습 로그 캡처 규칙 신설 (Colab 세션이 끊겨서 원인 추적 실패)

🔻 v8 discarded, sticking with v7
🐛 found a flaw in auto-scoring (miscounted "impossible" as "possible")
📝 added a new rule to always capture retrain logs (lost the trail when Colab disconnected)

숫자가 좋아 보인다고 바로 믿으면 안 된다는 걸 배운 하루였습니다.
A day that taught me not to trust good-looking numbers at face value.

다음 Day 046~ — v9 재학습 준비
Next, Day 046~ — preparing for v9

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #8B모델
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `45일차.mp4` 선택
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
Episode: Day 045.
Topic: a complete beginner fixed known weaknesses in their fine-tuned AI model and retrained it, expecting improvement — but automatic scoring turned out to be misleading, and manually re-checking every answer revealed the new version was actually worse than before. A honest, unglamorous setback in a Build in Public journey.

Main text must be large and readable:
"DAY 045"
"고쳐서 재학습했는데 더 나빠졌다"

Small supporting text:
"자동채점 12점 → 직접 채점 5점"
"숫자만 믿지 말 것"

Visual style:
- visual metaphor: a graph or score counter that looks like it's going up, then a second reveal showing it actually went down (two contrasting numbers/arrows)
- feeling: honest, slightly deflated but not devastated — a real setback shown transparently
- clean tech documentary style
- mood: grounded, reflective, not overhyped or falsely positive
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-18_Day045_Work_Order|Day 045 작업지시서]] | [[../Daily_Log/2026-07-18_Day045_Log|Day 045 로그]] | [[../44일차/Day044_YouTube_Upload|← Day 044 유튜브]]

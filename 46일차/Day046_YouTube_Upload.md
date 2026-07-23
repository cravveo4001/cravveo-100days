# Day 046 YouTube Upload

> 영상 파일: `46일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1bUcVLTS7Y_5LTIFmJ0fHggDdo5vUnNiS?usp=sharing
> 편집 노트: 오늘부터 반복되는 Colab 작업 과정은 편집으로 잘라내고 핵심만 담음 — 그래서 영상 길이가 약 5분으로 짧아짐

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 046 | 가설을 직접 검증해봤습니다
```
*(40자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 046.
Cravveo Company 100-Day Project, Day 046.

Day 045~045.5에서 v8, v9 둘 다 v7보다 나빠진 걸 확인했습니다. cell4 로그로 데이터가 제대로 들어간 것도 확인했으니, 남은 용의자는 하나 — 정체성 데이터를 80개에서 94개로 늘린 것 자체였습니다. 오늘은 이 가설을 직접 검증했습니다.
After both v8 and v9 turned out worse than v7 (Day 045~045.5), and after confirming the training data itself was combined correctly, one suspect remained — expanding the identity dataset from 80 to 94 items. Today I tested that hypothesis directly.

한 것 | What I did:
- HuggingFace 데이터셋을 80개로 되돌림 (모델 버전 오류 수정은 그대로 유지)
- 같은 조건으로 재학습 → v10
- 30문항 정식 평가로 v7/v8/v9와 비교

- Reverted the HuggingFace dataset back to 80 items (kept the model-version bug fix)
- Retrained under the same conditions → v10
- Compared against v7/v8/v9 with the full 30-question evaluation

발견한 것 | Discovery:
결과가 단순하지 않았습니다. v10의 완전정답(O) 개수는 9개로, v7의 8개보다 많았습니다. GPU 없이 파인튜닝이 가능한지, 왜 1인 개발을 선택했는지 같은 질문은 이전 어떤 버전도 못 맞췄는데 이번에 처음 정확히 맞췄습니다.
The result wasn't simple. v10 got 9 fully-correct answers — more than v7's 8. Questions that every previous version got wrong (can you fine-tune without a GPU, why did you go solo) were finally answered correctly.

하지만 애매하게 맞던 부분(△)이 크게 줄고 완전 오답(X)이 늘어서, 종합 점수는 여전히 v7에 못 미쳤습니다. 가설은 "부분적으로만" 맞았던 셈입니다.
But partial credit dropped sharply and wrong answers increased, so the overall score still fell short of v7. The hypothesis was only "partially" confirmed.

결과 | Result:
v7: O8/△12/X10 (합 20) → v8: O5/△5/X20 (합 10) → v9: O3/△9/X18 (합 12) → v10: O9/△4/X17 (합 13)
v7: 8/12/10 (total 20) → v8: 5/5/20 (total 10) → v9: 3/9/18 (total 12) → v10: 9/4/17 (total 13)

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
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Llama 3.1, 8B 모델, large language model, 평가세트, evaluation set, 가설 검증, hypothesis testing, LoRA, HuggingFace, Ollama, Google Colab, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 046 완료 | Day 046 Complete

정체성 데이터를 80개로 되돌려 재학습(v10)했더니 완전정답 개수는 v7보다 많아졌지만(9 vs 8), 종합 점수는 여전히 v7에 못 미쳤습니다(13 vs 20).
Reverted the identity data to 80 items and retrained (v10) — fully-correct answers went up (9 vs v7's 8), but the overall score still fell short (13 vs 20).

오늘의 핵심 발견 | Key discovery:
"94개로 늘린 게 원인"이라는 가설은 부분적으로만 맞았습니다. 같은 총점이라도 O/△/X 구성이 완전히 다를 수 있다는 걸 배웠습니다.
The "expanding to 94 caused it" hypothesis was only partially right. Learned that the same total score can hide a completely different mix of right/partial/wrong answers.

다음 단계 | Next step:
Day 047~ — v7을 계속 기준 모델로 유지. ablescan.app/cravveo.com을 계속 헷갈리는, 데이터 확장과 무관해 보이는 반복 약점을 다음에 다뤄볼 예정.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 046 완료 + Day 047 예고 | Day 046 Done + Day 047 Preview

가설을 직접 검증해봤습니다 🔍
Tested the hypothesis directly 🔍

"정체성 데이터를 94개로 늘린 게 v8/v9가 나빠진 원인이다" — 이걸 확인하려고 80개로 되돌려서 다시 학습했습니다.
"Expanding identity data to 94 items caused v8/v9 to get worse" — reverted to 80 and retrained to check.

결과 | Result:
v7: 8/12/10 (합 20)
v8: 5/5/20 (합 10)
v9: 3/9/18 (합 12)
v10: 9/4/17 (합 13)

완전정답 개수는 v10이 제일 많았는데(9개), 종합 점수는 여전히 v7에 못 미쳤습니다.
v10 had the most fully-correct answers (9) — but the overall score still trailed v7.

가설은 "부분적으로만" 맞았습니다. 단순한 숫자 하나로는 다 설명이 안 되네요.
The hypothesis was only "partially" right. One number alone doesn't tell the whole story.

다음 Day 047~ — 남은 반복 약점(ablescan.app 혼동 등) 다루기
Next, Day 047~ — tackling the remaining recurring weaknesses (like the ablescan.app mix-up)

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #가설검증
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `46일차.mp4` 선택 (반복 Colab 구간 편집으로 생략, ~5분)
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
Episode: Day 046.
Topic: a complete beginner formed a hypothesis about why their fine-tuned model regressed, tested it directly by reverting a dataset change and retraining, and got a nuanced result — more fully-correct answers than before, but a lower overall score, meaning the hypothesis was only partially right. A story about testing an idea and getting a "yes, but" answer instead of a clean win.

Main text must be large and readable:
"DAY 046"
"가설을 검증해봤다"

Small supporting text:
"완전정답 9개 (v7보다 많음)"
"종합 점수는 아직 부족"

Visual style:
- visual metaphor: a scale or balance showing mixed results, or a magnifying glass over data with two arrows pointing different directions (one up, one down)
- feeling: analytical curiosity — a real experiment with a mixed, honest result, not a clean win or loss
- clean tech documentary style
- mood: thoughtful, methodical, quietly satisfied with the process even though the answer is ambiguous
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-22_Day046_Work_Order|Day 046 작업지시서]] | [[../Daily_Log/2026-07-23_Day046_Log|Day 046 로그]] | [[../45.5일차/2026-07-20_Day045.5_Work_Order|← Day 045.5]]

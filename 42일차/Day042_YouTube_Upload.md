# Day 042 YouTube Upload

> 영상 파일: `42일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1DlimmrDxXVZTwk3hwODwLl42eVM26rLu?usp=sharing

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 042 | 고치려다 두 번 다 더 망가뜨렸다
```
*(43자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 042.
Cravveo Company 100-Day Project, Day 042.

오늘은 원래 깃허브 커밋 로그를 학습 데이터로 뽑으려고 했는데, 알고 보니 이미 있는 데이터랑 거의 똑같았습니다.
Today I planned to extract GitHub commit logs as training data — turns out it was nearly identical to data I already had.

한 것 | What I did:
- 방향을 바꿔서 어제 재학습한 cravveo:v5를 제대로 테스트
- 첫 질문("크라베오 컴퍼니가 뭐야?")부터 완전히 지어낸 URL과 서비스를 나열함
- 원인 파악: 정체성 데이터 20개가 다른 데이터 203개에 묻혀서 제대로 안 배워짐
- 20개를 10배로 늘려서 다시 재학습 → cravveo:v6
- 근데 v6는 한국어에 아랍어, 힌디어, 태국어 글자까지 무작위로 섞여 나오는 더 심한 상태가 됨

- Pivoted to properly testing yesterday's retrained cravveo:v5
- The very first question ("what is Cravveo Company?") returned completely fabricated URLs and services
- Diagnosed the cause: 20 identity samples were drowned out by 203 other samples, so they weren't learned properly
- Retrained with the 20 samples repeated 10x → cravveo:v6
- But v6 came out even worse — Arabic, Hindi, and Thai characters randomly mixed into Korean output

발견한 것 | Discovery:
고치려던 시도가 두 번 다 실패했습니다. 첫 번째는 너무 적게 배워서, 두 번째는 같은 문장을 너무 많이 반복해서.
작은 데이터셋으로 파인튜닝할 때 "적당한 비율"을 찾는 게 생각보다 훨씬 예민한 작업이라는 걸 배웠습니다.
Both fix attempts failed — first from learning too little, then from repeating the same text too much.
Learned that finding the "right ratio" when fine-tuning on a small dataset is far more delicate than expected.

결론 | Conclusion:
오늘 세 번째 재학습을 또 시도하는 대신, 여기서 멈추고 원인을 기록했습니다. 당분간은 이전 버전(v4)을 그대로 씁니다.
Instead of trying a third retrain today, I stopped here and documented the causes. Sticking with the previous version (v4) for now.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
Colab: https://colab.research.google.com/drive/1DlimmrDxXVZTwk3hwODwLl42eVM26rLu?usp=sharing

#Cravveo #파인튜닝 #FineTuning #과적합 #Overfitting #과소적합 #Underfitting #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, 과적합, overfitting, 과소적합, underfitting, 학습 데이터 비율, data ratio, LoRA, Llama 3.2, HuggingFace, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 042 완료 | Day 042 Complete

정체성 데이터 비율을 맞추려고 두 번 재학습했는데 둘 다 실패했습니다. 그래도 왜 실패했는지는 명확히 알아냈습니다.
Retrained twice trying to fix the identity data ratio — both failed. But I now clearly understand why each one failed.

오늘의 핵심 발견 | Key discovery:
너무 적게 배우면 지어내고, 너무 많이 반복하면 망가집니다. 그 사이 어딘가를 찾아야 하는데, 오늘은 못 찾았습니다.
Too little training causes hallucination; too much repetition causes collapse. The right spot is somewhere in between — didn't find it today.

다음 단계 | Next step:
Day 043 — 당분간 v4 유지, Part 1 계속

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 042 완료 + Day 043 예고 | Day 042 Done + Day 043 Preview

오늘은 고치려다가 두 번 다 더 망가뜨린 하루였습니다 😅
Today I tried to fix something and broke it worse — twice 😅

1️⃣ v5: 정체성 데이터가 너무 적어서 → 가짜 URL/서비스 지어냄
2️⃣ v6: 20개를 10배로 늘렸더니 → 이번엔 아랍어/힌디어까지 섞여 나옴

1️⃣ v5: too little identity data → fabricated URLs/services
2️⃣ v6: 10x'd it → this time Arabic/Hindi characters mixed in

세 번째 재학습을 또 시도하는 대신, 오늘은 여기서 멈추고 원인만 정리했습니다.
Instead of a third retrain, stopped here today and just documented the causes.

내일 Day 043 — 당분간 이전 버전 유지, Part 1 계속
Tomorrow Day 043 — sticking with the previous version for now, Part 1 continues

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #과적합 #과소적합
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `42일차.mp4` 선택
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
Episode: Day 042.
Topic: a complete beginner tried twice to fix an AI model's identity training data by adjusting the data ratio, but both attempts failed in opposite ways — one from too little training signal, the other from too much repetition causing the model to break down and mix random foreign scripts into its output. Build in Public.

Main text must be large and readable:
"DAY 042"
"두 번 고치려다 두 번 다 망가졌다"

Small supporting text:
"너무 적으면 지어내고"
"너무 많으면 무너진다"

Visual style:
- visual metaphor: a balance scale tipping too far in both directions, or two broken attempts side by side showing opposite failure modes
- feeling: "honest failure, real learning" — two setbacks in one day, but a clear diagnosis
- clean tech documentary style
- mood: slightly frustrated but analytical, ending on calm resolve
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-11_Day042_Work_Order|Day 042 작업지시서]] | [[../Daily_Log/2026-07-11_Day042_Log|Day 042 로그]] | [[../41일차/Day041_YouTube_Upload|← Day 041 유튜브]]

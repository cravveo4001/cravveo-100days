# Day 027 YouTube Upload

> 영상 파일: `27일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 027 | 드디어 AI가 "크라베오"를 알아듣는다 — Before vs After 파인튜닝
```
*(57자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 027.
Cravveo Company 100-Day Project, Day 027.

드디어 파인튜닝의 효과를 눈으로 확인했습니다.
Today I finally saw the effect of fine-tuning with my own eyes.

학습 전: "크라베오가 뭐야?" → "유대인 종목... 주식 재단..." (엉뚱한 답)
학습 후: "크라베오가 뭐야?" → "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야." (정확한 답!)

Before: "What is Cravveo?" → random nonsense about stock funds
After: "What is Cravveo?" → "A one-person business running IT development, online shopping, and YouTube." (exact answer!)

오늘 한 일 | What I did today:
- 크라베오 전용 데이터 50개 추가 작성 (29개 → 83개)
- HuggingFace 데이터셋 업데이트
- Before 테스트: 학습 전 모델에게 질문 → 엉뚱한 답 기록
- 30 epoch + learning_rate 5e-5로 학습 → loss 3.95 → 0.08
- After 테스트: 학습 후 모델에게 같은 질문 → 정확한 크라베오 답변!

Before/After 비교 | Comparison:
질문: 크라베오 컴퍼니가 뭐야?
  Before: "유대인 종목, 주식 재단..." (모델이 크라베오를 모름)
  After: "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야."

질문: 크라베오의 목표가 뭐야?
  Before: "전재가의 성과를 달성하여..." (의미 없는 답)
  After: "1인 스타트업으로 살아남는 거야. 그게 지금 목표야."

질문: Build in Public이 뭐야?
  Before: "사람들의 삶을 개선하고자..." (틀린 답)
  After: "배우는 과정을 숨기지 않고 공개하면서 진행하는 방식이야. 실패도 에러도 다 공개하는 거야."

오늘의 핵심 | Key takeaway:
파인튜닝은 진짜로 작동합니다.
데이터 83개, 30 epoch이면 1B 모델도 내 데이터를 정확히 학습합니다.
27일 걸렸지만, AI가 "크라베오를 아는 AI"가 됐습니다.

Fine-tuning actually works.
83 entries + 30 epochs is enough for a 1B model to learn my data precisely.
It took 27 days, but the AI now "knows Cravveo."

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 028에서는 학습된 LoRA 가중치를 저장하고 모델을 내보냅니다.
In Day 028, we save the trained LoRA weights and export the model.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Unsloth #Llama #BeforeAfter #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, Llama 3.2, Before After, 학습 전후, loss, 데이터셋, dataset, 구글 코랩, Google Colab, T4 GPU, LoRA, SFTTrainer, HuggingFace, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 1인 기업, one person business
```

---

### 고정 댓글

```text
Day 027 완료 | Day 027 Complete

27일 만에 처음으로 AI가 내 데이터를 정확히 답했습니다.
After 27 days, the AI answered my data correctly for the first time.

학습 전 → 학습 후:
"크라베오가 뭐야?"
  Before: "유대인 종목... 주식 재단..." 😂
  After: "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야." ✅

"Build in Public이 뭐야?"
  Before: "사람들의 삶을 개선하고자..." ❌
  After: "배우는 과정을 숨기지 않고 공개하면서 진행하는 방식이야. 실패도 에러도 다 공개하는 거야." ✅

데이터 83개 + 30 epoch + loss 3.95→0.08
파인튜닝은 진짜로 작동합니다.

📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
🔗 GitHub: https://github.com/cravveo4001/cravveo-100days

다음 Day 028 | Next Day 028
학습된 LoRA 가중치 저장 + 모델 내보내기
Save trained LoRA weights + export model
```

---

### 커뮤니티 게시물

```text
Day 027 완료 ✅ | Day 027 Complete ✅

드디어 AI가 "크라베오"를 알아듣습니다.
The AI finally "knows" Cravveo.

학습 전에 물었습니다: "크라베오 컴퍼니가 뭐야?"
Before training: "What is Cravveo Company?"
→ "유대인 종목... 주식 재단이자 유도하는..." 😂
→ Complete nonsense about stock funds

학습 후에 같은 질문을 했습니다:
After training, asked the same question:
→ "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야." ✅
→ Exact correct answer!

4개 질문 전부 정확하게 답했습니다.
All 4 test questions answered correctly.

오늘 한 일:
- 크라베오 데이터 50개 추가 (29개 → 83개)
- 30 epoch 학습 → loss 3.95 → 0.08
- Before vs After 비교 → 눈에 보이는 차이 확인

What I did:
- Added 50 Cravveo entries (29 → 83)
- 30 epoch training → loss 3.95 → 0.08
- Before vs After comparison → visible difference confirmed

Day 001에서 리눅스 설치부터 시작해서, Day 027에서 AI가 내 데이터를 학습했습니다.
27일 걸렸지만, 파인튜닝은 진짜로 작동합니다.
From Linux installation on Day 001 to AI learning my data on Day 027.
It took 27 days, but fine-tuning actually works.

---

Day 028 예고 | Day 028 Preview
학습된 LoRA 가중치를 저장하고 모델을 내보냅니다.
Save trained LoRA weights and export the model.

#Cravveo #파인튜닝 #BeforeAfter #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `27일차.mp4` 선택
- [ ] 제목 입력 (57자 확인)
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
Episode: Day 027.
Topic: a complete beginner's AI finally answering correctly after fine-tuning — dramatic Before vs After comparison. Before: random nonsense. After: exact correct answer about Cravveo Company. Build in Public.

Main text must be large and readable:
"DAY 027"
"AI가 크라베오를 알아듣는다"

Small supporting text:
"Before: 엉뚱한 답 → After: 정확한 답"
"loss 3.95 → 0.08"

Visual style:
- visual metaphor: split screen — left side blurry/red/confused (Before), right side sharp/green/clear (After)
- feeling: "it actually works!" — amazement and pride
- clean tech documentary style
- mood: milestone achievement, proof of concept moment
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 027" and "AI가 크라베오를 알아듣는다" prominent, Before/After split clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 027 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 27일간의 여정에서 처음으로 AI가 내 데이터를 정확히 학습한 날이야.
"드디어 됐다... 진짜 되는 거였어"라는 감동과 뿌듯함이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, proud achievement, 85 BPM, loopable.
```

### 2. Before 테스트 파트

```text
배경음악을 만들어줘. 학습 전 모델에게 질문했더니 엉뚱한 답이 나오는 파트야.
"주식 재단? 유대인 종목? 뭔 소리야..." 하는 황당하고 웃긴 분위기가 담겼으면 좋겠어.
absurd results, comedic confusion, quirky electronic, no vocals, 가사 없음, loopable.
```

### 3. 데이터 확장 파트

```text
배경음악을 만들어줘. 크라베오 데이터 50개를 하나씩 만들어가는 파트야.
"하나하나 정성껏 만들자" 하는 꾸준하고 집중된 분위기가 담겼으면 좋겠어.
steady craftsmanship, focused building, clean electronic, no vocals, 가사 없음, loopable.
```

### 4. 학습 진행 파트

```text
배경음악을 만들어줘. 30 epoch 학습이 돌아가면서 loss가 3.95에서 0.08까지 떨어지는 파트야.
"되고 있다... 숫자가 계속 내려간다" 하는 기대와 긴장이 담겼으면 좋겠어.
training in progress, building anticipation, steady pulse electronic, no vocals, 가사 없음, loopable.
```

### 5. After 테스트 — 첫 정확한 답 파트

```text
배경음악을 만들어줘. 학습 후 모델이 처음으로 정확한 답을 하는 순간이야.
"크라베오가 뭐야?" → "IT 프로그램 개발, 쇼핑몰, 유튜브를 혼자 운영하는 1인 기업이야."
이 답이 나오는 순간의 감동과 짜릿함이 담겼으면 좋겠어. 27일간의 노력이 보상받는 순간.
breakthrough moment, emotional payoff, bright uplifting electronic, no vocals, 가사 없음, loopable.
```

### 6. 4개 질문 전부 정답 파트

```text
배경음악을 만들어줘. 4개 질문을 하나씩 물어볼 때마다 전부 정확한 답이 나오는 파트야.
"1개 맞고, 2개 맞고, 3개... 4개 전부!" 하는 점점 고조되는 기쁨이 담겼으면 좋겠어.
sequential wins, growing excitement, escalating electronic, no vocals, 가사 없음, loopable.
```

### 7. 회고 파트

```text
배경음악을 만들어줘. Day 001 리눅스 설치부터 Day 027 파인튜닝 성공까지를 돌아보는 파트야.
"여기까지 오는 데 27일 걸렸다"는 감회와 뿌듯함이 담겼으면 좋겠어.
looking back, proud reflection, warm nostalgic electronic, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: Day 027 — after 27 days of building from scratch, the AI finally answers correctly about Cravveo Company. Before/After comparison shows dramatic improvement. Proof that fine-tuning works.
Mood: quiet pride, "I built this from nothing", milestone achievement.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 027 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘 AI가 크라베오를 처음으로 알아듣는 날이 됐다" 하는 기대감과 의미 있는 시작이 담겼으면 좋겠어.
short opener, meaningful beginning, anticipation, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but deeply satisfying ending music for a YouTube episode where a beginner finally sees their fine-tuned AI answer correctly for the first time after 27 days of learning from scratch.
Mood: "this was all worth it", quiet triumph, grateful and forward-looking.
Style: warm electronic pad, emotional resolution, no vocals, 가사 없음, 80 BPM.
```

---

[[2026-06-21_Day027_Work_Order|Day 027 작업지시서]] | [[../26일차/Day026_YouTube_Upload|← Day 026 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

# Day 028 YouTube Upload

> 영상 파일: `28일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
> HuggingFace 모델: https://huggingface.co/cravveo/cravveo-llama-lora

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 028 | 학습된 AI를 저장하고 다시 불러왔더니 기억하고 있었다
```
*(50자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 028.
Cravveo Company 100-Day Project, Day 028.

어제 파인튜닝한 AI가 크라베오를 정확히 답했습니다.
하지만 코랩 세션이 꺼지면 학습된 모델이 사라집니다.
오늘은 학습된 모델을 저장하고, HuggingFace에 업로드하고,
다시 불러와서 기억하고 있는지 확인했습니다.

Yesterday the fine-tuned AI answered Cravveo correctly.
But when the Colab session ends, the trained model disappears.
Today I saved the model, uploaded to HuggingFace,
and reloaded it to check if it still remembers.

오늘 한 일 | What I did today:
- 83개 데이터로 30 epoch 학습 재실행 → loss 0.08
- LoRA 가중치 저장 (model.save_pretrained)
- HuggingFace에 모델 업로드 (cravveo/cravveo-llama-lora)
- 런타임 재시작 후 HuggingFace에서 모델 재로드
- 재로드한 모델이 크라베오를 정확히 답하는지 확인 → 성공!

오늘의 삽질 | Today's struggle:
처음에 FastLanguageModel.from_pretrained()으로 직접 로드했더니
LoRA 어댑터가 적용 안 돼서 엉뚱한 답이 나왔습니다.
기본 모델을 먼저 로드하고 PeftModel.from_pretrained()으로
어댑터를 따로 붙여야 한다는 걸 배웠습니다.

First I tried loading directly with FastLanguageModel.from_pretrained()
but the LoRA adapter wasn't applied — got random answers.
Learned that you must load the base model first, then attach
the adapter separately with PeftModel.from_pretrained().

또 하나: 셀 실행 순서가 꼬여서 학습 안 된 모델이 업로드될 뻔했습니다.
"학습 → After 확인 → 저장" 순서가 중요합니다.
Another lesson: messed-up cell order almost uploaded an untrained model.
The order "Train → Verify → Save" matters.

재로드 후 결과 | Reload results:
질문: 크라베오 컴퍼니가 뭐야?
답변: IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야. ✅

질문: Build in Public이 뭐야?
답변: 배우는 과정을 숨기지 않고 공개하면서 진행하는 방식이야. 실패도 에러도 다 공개하는 거야. ✅

파인튜닝 파이프라인 완성:
학습 → 저장 → 업로드 → 불러오기 → 정확한 답변 ✅
Fine-tuning pipeline complete:
Train → Save → Upload → Reload → Correct answers ✅

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 029에서는 모델을 GGUF로 변환하고 로컬 Ollama에서 돌릴 준비를 합니다.
In Day 029, we convert the model to GGUF format and prepare to run it locally with Ollama.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
🤖 Model: https://huggingface.co/cravveo/cravveo-llama-lora
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Unsloth #Llama #LoRA #HuggingFace #모델저장 #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, Llama 3.2, LoRA, 가중치 저장, model save, HuggingFace, push to hub, PeftModel, 모델 재로드, model reload, 구글 코랩, Google Colab, T4 GPU, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 파이프라인, pipeline
```

---

### 고정 댓글

```text
Day 028 완료 | Day 028 Complete

파인튜닝 파이프라인이 완성됐습니다.
The fine-tuning pipeline is complete.

학습 → 저장 → HuggingFace 업로드 → 런타임 재시작 → 재로드 → 정확한 답변 ✅
Train → Save → HuggingFace upload → Runtime restart → Reload → Correct answers ✅

재로드 후 테스트:
"크라베오 컴퍼니가 뭐야?"
→ "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야." ✅

코랩 세션이 꺼져도 AI가 크라베오를 기억합니다.
Even after Colab restarts, the AI remembers Cravveo.

오늘의 교훈:
1. LoRA 어댑터 재로드 시 기본 모델 + PeftModel 따로 로드해야 함
2. 셀 순서: 학습 → After 확인 → 저장 (순서 중요!)

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
🤖 Model: https://huggingface.co/cravveo/cravveo-llama-lora
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

다음 Day 029 | Next Day 029
GGUF 변환 + 로컬 Ollama 배포 준비
GGUF conversion + local Ollama deployment prep
```

---

### 커뮤니티 게시물

```text
Day 028 완료 ✅ | Day 028 Complete ✅

코랩 세션이 꺼져도 AI가 크라베오를 기억합니다.
Even after Colab restarts, the AI remembers Cravveo.

오늘 한 일:
학습된 모델을 HuggingFace에 저장하고,
코랩을 완전히 재시작한 뒤 다시 불러왔습니다.

What I did:
Saved the trained model to HuggingFace,
fully restarted Colab, and reloaded it.

"크라베오가 뭐야?"
→ "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야." ✅

기억하고 있었습니다.
It still remembered.

오늘의 삽질:
처음에 모델을 잘못된 방법으로 불러와서 엉뚱한 답이 나왔습니다.
기본 모델 + LoRA 어댑터를 따로 로드해야 한다는 걸 배웠습니다.
셀 순서도 꼬여서 학습 안 된 모델이 업로드될 뻔했습니다.

Today's struggle:
First loaded the model wrong way — got random answers.
Learned to load base model + LoRA adapter separately.
Cell order mix-up almost uploaded an untrained model.

파인튜닝 파이프라인 완성:
학습 → 저장 → 업로드 → 불러오기 → 정확한 답변 ✅

Fine-tuning pipeline complete:
Train → Save → Upload → Reload → Correct answers ✅

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
🤖 Model: https://huggingface.co/cravveo/cravveo-llama-lora
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
---

Day 029 예고 | Day 029 Preview
모델을 GGUF로 변환하고 로컬 Ollama에서 돌릴 준비를 합니다.
Convert model to GGUF and prepare for local Ollama deployment.

#Cravveo #파인튜닝 #LoRA #HuggingFace #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `28일차.mp4` 선택
- [ ] 제목 입력 (50자 확인)
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
Episode: Day 028.
Topic: a complete beginner saves a fine-tuned AI model to HuggingFace, restarts everything, reloads it, and the AI still remembers. The fine-tuning pipeline is complete. Build in Public.

Main text must be large and readable:
"DAY 028"
"AI가 기억하고 있었다"

Small supporting text:
"저장 → 재시작 → 불러오기 → 정확한 답변"
"파이프라인 완성"

Visual style:
- visual metaphor: a brain or memory chip being saved/stored, then restored — the knowledge persists
- feeling: "it works even after restart" — reliability and permanence
- clean tech documentary style
- mood: satisfaction, completion, milestone
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 028" and "AI가 기억하고 있었다" prominent, save/reload cycle visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 028 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 학습된 AI 모델을 저장하고 다시 불러왔더니 기억하고 있었던 날이야.
"파이프라인이 완성됐다"는 달성감과 안정감이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, stable achievement, 85 BPM, loopable.
```

### 2. 학습 재실행 파트

```text
배경음악을 만들어줘. 어제 했던 학습을 다시 돌리는 파트야.
"어제 됐으니까 오늘도 되겠지" 하는 익숙하고 안정적인 분위기가 담겼으면 좋겠어.
familiar routine, confident repetition, steady electronic, no vocals, 가사 없음, loopable.
```

### 3. 가중치 저장 파트

```text
배경음악을 만들어줘. 학습된 모델의 가중치를 저장하는 파트야.
"이걸 저장해두면 사라지지 않아" 하는 안전하고 든든한 분위기가 담겼으면 좋겠어.
saving progress, secure backup, warm pad electronic, no vocals, 가사 없음, loopable.
```

### 4. HuggingFace 업로드 파트

```text
배경음악을 만들어줘. 저장된 모델을 HuggingFace에 업로드하는 파트야.
"클라우드에 올려놓으면 어디서든 쓸 수 있어" 하는 개방적이고 자유로운 분위기가 담겼으면 좋겠어.
cloud upload, open access, airy electronic, no vocals, 가사 없음, loopable.
```

### 5. 삽질 파트 (잘못된 로드)

```text
배경음악을 만들어줘. 재로드했는데 엉뚱한 답이 나와서 당황하는 파트야.
"어? 왜 기억을 못 하지?" 하는 불안하고 혼란스러운 분위기가 담겼으면 좋겠어.
unexpected failure, confused moment, uneasy electronic, no vocals, 가사 없음, loopable.
```

### 6. 해결 — PeftModel 로드 파트

```text
배경음악을 만들어줘. 기본 모델 + LoRA 어댑터를 따로 로드하는 방법을 찾은 파트야.
"이렇게 하면 되는구나!" 하는 깨달음과 해결의 기쁨이 담겼으면 좋겠어.
problem solved, clean solution, brightening electronic, no vocals, 가사 없음, loopable.
```

### 7. 재로드 성공 — 기억하고 있다 파트

```text
배경음악을 만들어줘. 재로드한 모델이 크라베오를 정확히 답하는 순간이야.
코랩을 완전히 껐다 켰는데도 AI가 기억하고 있었다.
"됐다... 진짜 살아남았다" 하는 감동과 안도가 담겼으면 좋겠어.
persistence confirmed, emotional relief, warm triumphant electronic, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: Day 028 — saving the fine-tuned model to HuggingFace, restarting Colab completely, reloading, and confirming the AI still remembers Cravveo. The complete fine-tuning pipeline is now proven. Build in Public.
Mood: quiet completion, "the system works", reliability confirmed.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 028 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 학습된 AI를 저장하고 다시 불러올 수 있는지 테스트하는 날이다" 하는 기대감이 담겼으면 좋겠어.
short opener, testing persistence, anticipation, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but deeply satisfying ending music for a YouTube episode where a beginner completed the full fine-tuning pipeline — train, save, upload, reload — and confirmed the AI remembers everything after restart.
Mood: "the foundation is solid now", quiet pride, ready for the next chapter.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 80 BPM.
```

---

[[2026-06-22_Day028_Work_Order|Day 028 작업지시서]] | [[../27일차/Day027_YouTube_Upload|← Day 027 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

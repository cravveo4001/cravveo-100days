# Day 024 YouTube Upload

> 영상 파일: `24일차.mp4`
> 썸네일: `day024-model-dataset-connect-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 024 | AI 모델과 내 데이터가 처음으로 연결됐습니다 — Unsloth + HuggingFace 파인튜닝 뼈대 코드 완성
```
*(88자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 024.
Cravveo Company 100-Day Project, Day 024.

Unsloth로 Gemma 2B 모델을 불러오고, 어제 HuggingFace에 올린 내 데이터셋을 코드 한 줄로 연결했습니다.
파인튜닝에 필요한 뼈대 코드가 오늘 완성됐습니다.
Loaded Gemma 2B with Unsloth and connected yesterday's HuggingFace dataset with one line of code.
The fine-tuning skeleton code is now complete.

오늘 한 일 | What I did today:
- Unsloth FastLanguageModel로 Gemma 2B 4비트 양자화 로드 | Loaded Gemma 2B in 4-bit quantization via Unsloth FastLanguageModel
- load_dataset() 한 줄로 내 HuggingFace 데이터셋 연결 | Connected my HuggingFace dataset with one line of code
- 프롬프트 포맷 변환 (instruction + output → 하나의 텍스트) | Converted to prompt format (instruction + output → single text)
- 토크나이저로 모델-데이터 연결 확인 | Verified model-data connection via tokenizer
- max_length 512 → 2048 수정 (데이터 잘림 방지) | Fixed truncation: max_length 512 → 2048

오늘의 트러블슈팅 | Troubleshooting today:
NameError: 'ample' — sample에서 s가 또 빠짐 (어제 ataset에 이어 두 번째) 💀
토큰 수가 딱 512 → max_length 제한으로 잘린 것 확인 → 2048로 수정

오늘의 핵심 발견 | Key discovery today:
토큰 수가 정확히 max_length와 같으면 잘리고 있는 겁니다.
모델 max_seq_length(2048)와 토크나이저 max_length를 반드시 맞춰야 합니다.
어제 올린 내 데이터가 오늘 처음으로 모델 안으로 들어갔습니다.

If token count equals exactly max_length, the text is being truncated.
Always match tokenizer max_length with model max_seq_length (2048).
The data I uploaded yesterday entered the model for the first time today.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 025에서는 LoRA 어댑터를 붙이고 SFTTrainer로 실제 학습을 돌립니다. loss가 줄어드는 걸 처음 봅니다.
In Day 025, we attach the LoRA adapter and run real training with SFTTrainer. First time watching loss go down.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

#Cravveo #파인튜닝 #FineTuning #Unsloth #HuggingFace #Gemma #LoRA #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, HuggingFace, Gemma, Gemma 2B, LoRA, FastLanguageModel, 4비트 양자화, 4-bit quantization, load_dataset, 토크나이저, tokenizer, 프롬프트 포맷, prompt format, SFTTrainer, 구글 코랩, Google Colab, Build in Public, 100일 챌린지, 100 day challenge, Phase 2
```

---

### 고정 댓글

```text
Day 024 완료 | Day 024 Complete

AI 모델과 내 데이터가 처음으로 연결됐습니다.
My model and my data connected for the first time today.

오늘 완성한 뼈대 | Skeleton completed today:
Unsloth → Gemma 2B 로드 ✅
load_dataset("cravveo/cravveo-briefing-dataset") ✅
프롬프트 포맷 변환 ✅
토크나이저 연결 확인 (2048 토큰) ✅

오늘의 실수 | Today's mistake:
NameError: 'ample' — sample에서 s 빠짐 💀 (어제 ataset 이후 또...)
토큰 512개 = 잘린 것 → max_length 2048로 수정 ✅

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

다음 Day 025 | Next Day 025
LoRA 어댑터 설정 + SFTTrainer + 첫 학습 실행.
loss가 줄어드는 걸 처음으로 봅니다.
LoRA adapter config + SFTTrainer + first training run.
Watching the loss drop for the very first time.
```

---

### 커뮤니티 게시물

```text
Day 024 완료 ✅ | Day 024 Complete ✅

오늘 처음으로 내 모델이 내 데이터를 읽었습니다.
Today my model read my data for the first time.

직접 만든 데이터 → HuggingFace 업로드 → 코드 한 줄 → 모델 안으로.
My own data → HuggingFace → one line of code → inside the model.

이 흐름이 완성된 날입니다.
This is the day the pipeline came full circle.

오늘의 실수:
sample을 ample로 또 오타 냈습니다. s가 두 번 빠졌습니다 (어제는 d).
반복되는 오타가 영상 콘텐츠가 됩니다. Build in Public이 이런 겁니다.

Today's mistake:
Typed 'ample' instead of 'sample'. Missing 's' — two days in a row now (yesterday was 'd').
Repeated typos become content. That's what Build in Public is.

---

Day 025 예고 | Day 025 Preview
LoRA 어댑터를 붙이고 SFTTrainer를 설정합니다.
처음으로 loss 숫자가 줄어드는 걸 봅니다.
Attaching the LoRA adapter and setting up SFTTrainer.
Watching the loss number drop for the very first time.

#Cravveo #파인튜닝 #Unsloth #HuggingFace #Gemma #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `24일차.mp4` 선택
- [ ] 제목 입력 (88자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day024-model-dataset-connect-thumbnail-1280x720.png` 등록
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
Episode: Day 024.
Topic: a complete beginner successfully connecting a Gemma 2B AI model with their own custom HuggingFace dataset using Unsloth — the fine-tuning skeleton code is now complete, as part of Build in Public.

Main text must be large and readable:
"DAY 024"
"모델 + 데이터 연결 완료"

Small supporting text:
"Unsloth + HuggingFace"
"파인튜닝 뼈대 완성"

Visual style:
- visual metaphor: two objects (model brain + data stream) connecting or clicking together, pipeline or bridge imagery
- feeling: "the pieces finally fit together" — quiet connection moment
- clean tech documentary style
- mood: "I built the foundation today" — focused beginner pride
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 024" and "모델 + 데이터 연결 완료" prominent, connection/pipeline visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 024 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 Unsloth로 AI 모델을 불러오고, 내 HuggingFace 데이터셋을 처음으로 모델 안에 연결하는 날이야.
"두 개가 처음으로 맞물리는 순간"의 조용하고 집중된 분위기가 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, focused connection, 82 BPM, loopable.
```

### 2. 모델 로드 파트

```text
배경음악을 만들어줘. Unsloth로 Gemma 2B 모델이 4비트로 로드되는 파트야.
"무거운 것이 천천히 깨어나는" 묵직하고 안정적인 분위기가 담겼으면 좋겠어.
heavy model loading, slow awakening, deep electronic, steady, no vocals, 가사 없음, loopable.
```

### 3. 데이터셋 연결 파트

```text
배경음악을 만들어줘. load_dataset() 한 줄로 내 HuggingFace 데이터가 불러와지는 파트야.
"연결됐다"는 깔끔하고 빠른 성취감이 담겼으면 좋겠어.
clean connection, one-line solution, light electronic, no vocals, 가사 없음, loopable.
```

### 4. 오타 에러 파트

```text
배경음악을 만들어줘. sample을 ample로 오타 내서 NameError가 나는 파트야.
어제도 같은 실수를 했고, 오늘 또 했어. "또야..." 하는 자조적인 분위기가 담겼으면 좋겠어.
self-deprecating humor, minor blooper, light and dry, no vocals, 가사 없음, loopable.
```

### 5. 토큰 512개 발견 파트

```text
배경음악을 만들어줘. 토큰 수가 딱 512개 나와서 "혹시 잘린 건가?" 하고 확인하는 파트야.
"어? 이게 맞나?" 하고 조심스럽게 검토하는 분위기가 담겼으면 좋겠어.
careful inspection, quiet detective, steady electronic, no vocals, 가사 없음, loopable.
```

### 6. 2048 수정 완료 파트

```text
배경음악을 만들어줘. max_length를 512에서 2048로 수정하고 다시 확인하는 파트야.
"이제 제대로 됐다"는 차분하고 정돈된 분위기가 담겼으면 좋겠어.
clean fix, settled and correct, warm electronic, no vocals, 가사 없음, loopable.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: loading a Gemma 2B model with Unsloth and connecting a personal HuggingFace dataset — the fine-tuning skeleton is complete, the pipeline is in place, Build in Public.
Mood: quiet milestone, "the foundation is set", focused and grounded.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 024 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 모델과 데이터를 처음으로 연결한다"는 집중되고 기대되는 분위기가 담겼으면 좋겠어.
short electronic opener, connection anticipation, focused and warm, no vocals, 가사 없음.
```

### 9. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner successfully connects a Gemma 2B model with their own HuggingFace dataset and completes the fine-tuning skeleton code.
Mood: quiet foundation pride, "the pieces are in place now", steady and forward.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 80-85 BPM.
```

### 10. Day 025 예고 파트

```text
배경음악을 만들어줘. 다음 날 LoRA 어댑터를 붙이고 처음으로 실제 학습을 돌린다는 예고 파트야.
"드디어 학습이 시작된다 — loss가 줄어드는 걸 처음 본다"는 긴장되고 기대되는 분위기가 담겼으면 좋겠어.
first training anticipation, rising tension, new chapter energy, no vocals, 가사 없음, loopable.
```

---

[[2026-06-16_Day024_Work_Order|Day 024 작업지시서]] | [[../23일차/Day023_YouTube_Upload|← Day 023 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

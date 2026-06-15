# Day 023 YouTube Upload

> 영상 파일: `23일차.mp4`
> 썸네일: `day023-huggingface-dataset-upload-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 023 | 데이터셋 HuggingFace 업로드 + cron 자동화 완성 — 매일 AI 학습 데이터가 자동으로 쌓인다 | Auto Pipeline
```
*(100자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 023.
Cravveo Company 100-Day Project, Day 023.

직접 만든 42개 브리핑 데이터셋을 HuggingFace에 업로드하고, 매일 자동으로 데이터가 쌓이는 파이프라인을 완성했습니다.
Uploaded 42 briefing Q&A entries to HuggingFace and built a pipeline that automatically adds new data every morning.

오늘 한 일 | What I did today:
- push_to_hub() 로 HuggingFace 데이터셋 업로드 완료 | Pushed dataset to HuggingFace with push_to_hub()
- load_dataset() 한 줄로 불러오기 성공 | Successfully loaded dataset with one line of code
- briefing_pipeline.py 제작 — JSONL 변환 + 자동 업로드 | Built briefing_pipeline.py — auto JSONL conversion + upload
- cron에 파이프라인 연결 — 매일 오전 9시 전체 자동화 완성 | Wired pipeline into cron — full automation at 9am every day

오늘의 트러블슈팅 | Troubleshooting today:
- NameError: 'ataset' → dataset 오타 (d 빠짐) | Typo: missing 'd' in dataset
- 403 Forbidden → HuggingFace 사용자명 혼동 (cravveo4001 ≠ cravveo) | Wrong namespace: GitHub ID ≠ HuggingFace ID
- pip externally-managed-environment → pip install --break-system-packages 로 해결 | Fixed with --break-system-packages flag
- huggingface-cli deprecated → ~/.local/bin/hf auth login 으로 대체 | Replaced with hf auth login

오늘의 핵심 발견 | Key discovery today:
GitHub 이름과 HuggingFace 이름이 달라도 됩니다. 하지만 push_to_hub()에는 HuggingFace 이름을 써야 합니다.
데이터셋이 한 번 올라가면 코드 한 줄로 언제 어디서든 불러올 수 있습니다.
cron + 파이프라인 조합으로 이제 매일 아침 데이터가 자동으로 인터넷에 쌓입니다.

Your GitHub name and HuggingFace name can be different — but push_to_hub() needs the HuggingFace name.
Once uploaded, one line of code loads the dataset from anywhere, anytime.
With cron + pipeline combined, data now accumulates on the internet automatically every morning.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 024에서는 업로드된 데이터셋으로 실제 파인튜닝 코드를 작성합니다.
In Day 024, we write the actual fine-tuning code using the uploaded dataset.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

#Cravveo #파인튜닝 #FineTuning #HuggingFace #허깅페이스 #데이터셋 #Dataset #cron #자동화 #Automation #BuildInPublic #AI초보 #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, HuggingFace, 허깅페이스, 데이터셋 업로드, dataset upload, push_to_hub, load_dataset, cron 자동화, cron automation, 리눅스 자동화, Linux automation, 브리핑 파이프라인, briefing pipeline, JSONL, 구글 코랩, Google Colab, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 학습 일지, learning journal
```

---

### 고정 댓글

```text
Day 023 완료 | Day 023 Complete

데이터셋 HuggingFace 업로드 + cron 자동화 파이프라인 완성.
Uploaded dataset to HuggingFace + completed cron automation pipeline.

오늘의 트러블슈팅 | Troubleshooting:
NameError 'ataset' → dataset 오타 (d 빠짐) 💀
403 Forbidden → GitHub ID(cravveo4001) ≠ HuggingFace ID(cravveo) 혼동 ⚠️
pip externally-managed → --break-system-packages 로 해결 ✅
huggingface-cli deprecated → hf auth login 으로 대체 ✅

완성된 구조 | Final structure:
로컬 cron (매일 9시) → briefing.py → briefing_pipeline.py → HuggingFace 자동 업로드
Local cron (9am daily) → briefing.py → briefing_pipeline.py → auto upload to HuggingFace

코드 한 줄 불러오기 | One-line load:
load_dataset("cravveo/cravveo-briefing-dataset", split="train")

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

다음 Day 024 | Next Day 024
업로드된 데이터셋으로 실제 파인튜닝 코드 작성 시작.
Start writing actual fine-tuning code using the uploaded dataset.
```

---

### 커뮤니티 게시물

```text
Day 023 완료 ✅ | Day 023 Complete ✅

드디어 내가 만든 데이터가 인터넷에 올라갔습니다.
My data is finally on the internet.

오늘 완성한 것:
HuggingFace에 42개 브리핑 데이터셋 업로드 완료.
이제 코드 한 줄이면 어디서든 불러올 수 있습니다.

What I completed today:
Uploaded 42 briefing Q&A entries to HuggingFace.
Now one line of code loads it from anywhere.

그리고 더 중요한 것:
매일 아침 브리핑이 생성되면 자동으로 데이터셋이 갱신됩니다.
cron + 파이프라인 조합으로 데이터가 스스로 쌓이기 시작했습니다.

And something even bigger:
Every morning, when the briefing generates, the dataset updates automatically.
With cron + pipeline, data now accumulates on its own.

오늘의 실수 모음:
dataset을 ataset으로 오타 → NameError 💀
GitHub ID(cravveo4001)로 업로드 시도 → 403 Forbidden ⚠️

Today's mistakes:
Typo: dataset → ataset → NameError 💀
Tried GitHub ID instead of HuggingFace ID → 403 Forbidden ⚠️

실수도 전부 기록합니다. 그게 Build in Public입니다.
Every mistake goes on record. That's what Build in Public means.

---

Day 024 예고 | Day 024 Preview
이제 데이터가 준비됐습니다.
다음은 Unsloth + LoRA로 실제 파인튜닝 코드를 작성합니다.
The data is ready.
Next: write actual fine-tuning code with Unsloth + LoRA.

#Cravveo #파인튜닝 #HuggingFace #데이터셋 #cron자동화 #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `23일차.mp4` 선택
- [ ] 제목 입력 (100자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day023-huggingface-dataset-upload-thumbnail-1280x720.png` 등록
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
Episode: Day 023.
Topic: a complete beginner uploading a custom dataset to HuggingFace and building a cron-based automation pipeline that automatically updates the dataset every morning — all as part of Build in Public.

Main text must be large and readable:
"DAY 023"
"HuggingFace 업로드 완료"

Small supporting text:
"cron 자동화 파이프라인"
"매일 자동으로 쌓인다"

Visual style:
- visual metaphor: data flowing upward into a cloud or hub, pipeline/conveyor belt imagery, HuggingFace logo element
- feeling: "it's running by itself now" — quiet automation, small but real victory
- clean tech documentary style
- mood: "I built something that works without me touching it" — beginner's pride in automation
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 023" and "HuggingFace 업로드 완료" prominent, automated pipeline visual clear, quiet automation energy.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 023 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 직접 만든 데이터셋을 HuggingFace에 업로드하고, 매일 자동으로 데이터가 쌓이는 파이프라인을 완성하는 날이야.
"드디어 내 데이터가 인터넷에 올라갔다"는 조용하고 뿌듯한 분위기가 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, quiet pride, 80 BPM, loopable.
```

### 2. 오타 에러 파트

```text
배경음악을 만들어줘. dataset을 ataset으로 잘못 입력해서 NameError가 나는 파트야.
"어? 왜 안 되지?" 하고 잠깐 멈추는 분위기가 담겼으면 좋겠어.
minor confusion, brief pause, curious debugging, no vocals, 가사 없음, loopable.
```

### 3. 403 Forbidden 에러 파트

```text
배경음악을 만들어줘. GitHub ID와 HuggingFace ID가 달라서 403 Forbidden 오류가 나는 파트야.
"이번엔 또 뭐야..." 당황하지만 차분하게 원인을 찾는 분위기가 담겼으면 좋겠어.
steady debugging, calm problem-solving, no vocals, 가사 없음, loopable.
```

### 4. 업로드 성공 순간

```text
배경음악을 만들어줘. push_to_hub()가 성공하고 HuggingFace에 데이터셋이 올라가는 순간이야.
"내 데이터가 인터넷에 올라갔다"는 작고 확실한 성취감이 담겼으면 좋겠어.
quiet upload success, small milestone, warm electronic, no vocals, 가사 없음, loopable.
```

### 5. 한 줄 불러오기 성공 파트

```text
배경음악을 만들어줘. load_dataset() 코드 한 줄로 데이터가 불러와지는 순간이야.
"이 한 줄이면 어디서든 된다"는 간결하고 깔끔한 분위기가 담겼으면 좋겠어.
clean and simple, one-line solution energy, light electronic, no vocals, 가사 없음, loopable.
```

### 6. 파이프라인 완성 파트

```text
배경음악을 만들어줘. briefing_pipeline.py가 완성되고 cron에 연결되는 파트야.
"이제 내가 건드리지 않아도 알아서 돌아간다"는 자동화의 쾌감이 담겼으면 좋겠어.
automation satisfaction, systems running on their own, steady electronic, no vocals, 가사 없음, loopable.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI learning journey.
Episode theme: uploading a custom dataset to HuggingFace and building a cron automation pipeline — small real wins, real mistakes, real automation as Build in Public.
Mood: quiet beginner pride, "something I built is running by itself now", grounded and warm.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 023 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 내 데이터를 인터넷에 올린다"는 분위기가 담겼으면 좋겠어.
short electronic opener, upload anticipation, warm and focused, no vocals, 가사 없음.
```

### 9. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner successfully uploads a custom dataset to HuggingFace and builds a cron-based automation pipeline that runs every morning.
Mood: quiet automation pride, "it's running without me now", grounded and forward.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 78-85 BPM.
```

### 10. Day 024 예고 파트

```text
배경음악을 만들어줘. 다음 날 업로드된 데이터셋으로 실제 파인튜닝 코드를 작성한다는 예고 파트야.
"드디어 진짜 파인튜닝이 시작된다"는 기대감이 담겼으면 좋겠어.
fine-tuning anticipation, rising electronic, new chapter energy, no vocals, 가사 없음, loopable.
```

---

[[2026-06-15_Day023_Work_Order|Day 023 작업지시서]] | [[../22일차/Day022_YouTube_Upload|← Day 022 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

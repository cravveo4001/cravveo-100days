# Day 025 YouTube Upload

> 영상 파일: `25일차.mp4`
> 썸네일: `day025-first-loss-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 025 | 드디어 loss가 줄어드는 걸 봤습니다 — CUDA 오류와 싸운 하루
```
*(63자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 025.
Cravveo Company 100-Day Project, Day 025.

LoRA 어댑터를 붙이고 SFTTrainer로 첫 학습을 돌렸습니다.
그런데 bitsandbytes CUDA 오류가 가로막았습니다. 오늘의 절반은 오류와 싸웠습니다.
We attached the LoRA adapter and ran the first training with SFTTrainer.
But bitsandbytes CUDA errors blocked us. Half of today was spent fighting errors.

오늘 한 일 | What I did today:
- LoRA 어댑터 설정 (get_peft_model, r=16) | LoRA adapter setup (get_peft_model, r=16)
- SFTTrainer 설정 (max_steps=30, adamw_torch) | SFTTrainer configuration
- bitsandbytes CUDA 오류 트러블슈팅 | bitsandbytes CUDA error troubleshooting
- ctypes RTLD_GLOBAL로 libnvJitLink.so.13 해결 | Fixed with ctypes RTLD_GLOBAL preload
- 첫 학습 완료 — Step 1~30, loss 25.5 → 15.4 | First training done — loss 25.5 → 15.4

오늘의 트러블슈팅 | Troubleshooting today:
RuntimeError: CUDA SETUP ERROR: Missing dependency: libnvJitLink.so.13
→ bitsandbytes가 CUDA 라이브러리를 못 찾는 오류. 버전 교체만 6번.
→ 결국 ctypes.CDLL(mode=RTLD_GLOBAL)로 해결 — 셀 위치도 중요했습니다.
→ FastLanguageModel.from_pretrained() 바로 앞, 런타임 재시작 이후에 배치

오늘의 핵심 발견 | Key discovery today:
pip install은 디스크에만 설치됩니다. 런타임 재시작이 필요한 이유가 있었습니다.
ctypes.CDLL의 기본 모드는 RTLD_LOCAL — 다른 라이브러리에서 못 찾습니다. RTLD_GLOBAL이 핵심.
loss가 줄어드는 걸 처음으로 눈으로 확인했습니다. Step 1: 25.5 → Step 30: 15.4.

pip install only writes to disk. There's a real reason runtime restart is needed.
ctypes.CDLL default mode is RTLD_LOCAL — other libraries can't see it. RTLD_GLOBAL is the key.
I watched the loss go down for the very first time. Step 1: 25.5 → Step 30: 15.4.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 026에서는 LoRA 가중치를 저장하고, 파인튜닝된 모델이 실제로 다르게 답하는지 테스트합니다.
In Day 026, we save the LoRA weights and test whether the fine-tuned model actually responds differently.

※ 오늘 영상이 길어서 250% 배속으로 올렸습니다. 정상 영상입니다.
※ Today's video is long, so I uploaded it at 250% speed. The content is completely normal.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

#Cravveo #파인튜닝 #FineTuning #Unsloth #LoRA #SFTTrainer #bitsandbytes #CUDA #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, LoRA, SFTTrainer, bitsandbytes, CUDA 오류, CUDA error, libnvJitLink, ctypes, RTLD_GLOBAL, loss, 학습 loss, 구글 코랩, Google Colab, T4 GPU, FastLanguageModel, get_peft_model, 런타임 재시작, runtime restart, Build in Public, 100일 챌린지, 100 day challenge, Phase 2
```

---

### 고정 댓글

```text
Day 025 완료 | Day 025 Complete

오늘 처음으로 loss가 줄어드는 걸 봤습니다.
Today I watched the loss go down for the very first time.

Step 1:  25.5190
Step 15: 19.2071
Step 30: ~15.4  ← 줄어들었습니다 ✅

오늘의 진짜 싸움 | The real battle today:
RuntimeError: CUDA SETUP ERROR: Missing dependency: libnvJitLink.so.13
버전 바꿔가며 6번 시도... 결국 ctypes RTLD_GLOBAL로 해결

핵심 해결법 | Key fix:
import ctypes
ctypes.CDLL("...libnvJitLink.so.13", mode=ctypes.RTLD_GLOBAL)
← FastLanguageModel 로드 직전, 런타임 재시작 이후에 배치

※ 오늘 영상이 길어서 250% 배속으로 올렸습니다. 정상 영상입니다.
※ Today's video is long, so I uploaded it at 250% speed. The content is completely normal.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset

다음 Day 026 | Next Day 026
LoRA 가중치 저장 + 파인튜닝 모델 테스트.
내가 만든 AI가 실제로 다르게 답하는지 확인합니다.
Save LoRA weights + test the fine-tuned model.
Does my AI actually respond differently now?
```

---

### 커뮤니티 게시물

```text
Day 025 완료 ✅ | Day 025 Complete ✅

오늘 처음으로 loss가 줄어드는 걸 눈으로 봤습니다.
Today I watched the loss drop for the very first time.

Step 1: 25.5 → Step 30: 15.4
AI가 내 데이터를 학습하기 시작했습니다.
The AI started learning from my data.

오늘의 진짜 이야기:
Today's real story:
LoRA + SFTTrainer 세팅 자체는 10분이면 됐습니다.
그런데 bitsandbytes CUDA 오류 하나가 하루를 잡아먹었습니다.
libnvJitLink.so.13 파일이 있는데 시스템이 못 찾는 상황.
버전 바꿔보고, 경로 설정해보고, symlink 걸어보고...
결국 ctypes RTLD_GLOBAL 모드로 해결했습니다. 셀 위치도 중요했습니다.

The LoRA + SFTTrainer setup itself took 10 minutes.
But one bitsandbytes CUDA error ate the entire day.
The file libnvJitLink.so.13 existed — the system just couldn't find it.
Tried version changes, path settings, symlinks...
Fixed it with ctypes RTLD_GLOBAL mode. Cell position mattered too.

오늘의 교훈:
pip install은 디스크에만 씁니다. 런타임 재시작이 필요한 이유가 있습니다.
ctypes 기본 모드는 RTLD_LOCAL — RTLD_GLOBAL이어야 다른 라이브러리에서 보입니다.

Today's lesson:
pip install only writes to disk. Runtime restart exists for a reason.
ctypes default is RTLD_LOCAL — must use RTLD_GLOBAL for other libraries to see it.

---

참고 | Note:
오늘 영상이 길어서 250% 배속으로 올렸습니다. 정상 영상입니다.
Today's video is long, so I uploaded it at 250% speed. The content is completely normal.

---

Day 026 예고 | Day 026 Preview
LoRA 가중치를 저장하고, 파인튜닝된 모델이 실제로 다르게 답하는지 테스트합니다.
Save the LoRA weights and test if the fine-tuned model actually responds differently.

#Cravveo #파인튜닝 #LoRA #SFTTrainer #bitsandbytes #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `25일차.mp4` 선택
- [ ] 제목 입력 (63자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day025-first-loss-thumbnail-1280x720.png` 등록
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
Episode: Day 025.
Topic: a complete beginner finally watching loss go down for the first time after a full day fighting bitsandbytes CUDA errors — LoRA + SFTTrainer first training run, Build in Public.

Main text must be large and readable:
"DAY 025"
"드디어 loss가 줄어들었다"

Small supporting text:
"Step 1: 25.5 → Step 30: 15.4"
"LoRA + SFTTrainer"

Visual style:
- visual metaphor: a descending line/graph going down, or a number decreasing — the "first proof of learning"
- feeling: "exhausted but victorious" — hard-won milestone after a long battle
- clean tech documentary style
- mood: relief and quiet triumph after hours of debugging
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 025" and "드디어 loss가 줄어들었다" prominent, descending loss graph visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 025 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 LoRA + SFTTrainer로 첫 학습을 돌리는 날인데, CUDA 오류와 하루 종일 싸우고 결국 해결했어.
"긴 싸움 끝에 드디어 됐다"는 안도감과 피로한 승리감이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, exhausted victory, 80 BPM, loopable.
```

### 2. LoRA 설정 파트

```text
배경음악을 만들어줘. LoRA 어댑터를 모델에 붙이는 파트야.
"이제 진짜 시작이다"라는 집중되고 기대되는 분위기가 담겼으면 좋겠어.
LoRA adapter setup, focused preparation, clean electronic, no vocals, 가사 없음, loopable.
```

### 3. CUDA 오류 첫 등장 파트

```text
배경음악을 만들어줘. bitsandbytes CUDA 오류가 처음 나오는 파트야.
"또 오류야..." 하는 당황하고 지친 분위기가 담겼으면 좋겠어.
first error shock, frustrated blocker, slightly tense electronic, no vocals, 가사 없음, loopable.
```

### 4. 오류 반복 파트

```text
배경음악을 만들어줘. 버전 바꿔가며 같은 오류가 계속 나오는 파트야.
버전 교체만 6번, "이게 왜 안 되지..." 하고 계속 막히는 분위기가 담겼으면 좋겠어.
repeated failure loop, dry persistence, minor key electronic, no vocals, 가사 없음, loopable.
```

### 5. 런타임 재시작 반복 파트

```text
배경음악을 만들어줘. 런타임 재시작을 반복하면서 처음부터 다시 실행하는 파트야.
"또 처음부터..." 하는 지루하고 집요한 분위기가 담겼으면 좋겠어.
repetitive restart loop, stubborn patience, dry minimal electronic, no vocals, 가사 없음, loopable.
```

### 6. ctypes RTLD_GLOBAL 해결 파트

```text
배경음악을 만들어줘. ctypes RTLD_GLOBAL로 오류를 드디어 해결하는 파트야.
"됐다!!!" 하는 갑작스럽고 짜릿한 돌파감이 담겼으면 좋겠어.
sudden breakthrough, relief and excitement, bright electronic, no vocals, 가사 없음, loopable.
```

### 7. 학습 진행 파트

```text
배경음악을 만들어줘. 드디어 trainer.train()이 돌아가고 loss가 내려가는 파트야.
Step 1: 25.5 → Step 30: 15.4. "진짜 되고 있다" 하는 조용한 감동이 담겼으면 좋겠어.
training running, quiet awe, steady electronic pulse, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: fighting bitsandbytes CUDA errors all day, finally solving it with ctypes RTLD_GLOBAL, and watching the loss go down for the very first time — exhausted but victorious, Build in Public.
Mood: hard-won milestone, "I earned this one", tired but proud.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 025 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 드디어 첫 학습을 돌린다 — 근데 왜 이렇게 안 되지" 하는 기대와 불안이 섞인 분위기가 담겼으면 좋겠어.
short opener, mixed anticipation and tension, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner finally gets the first training run to work after fighting CUDA errors all day, and watches the loss go down for the very first time.
Mood: exhausted relief, "I survived today", quiet satisfaction, forward-looking.
Style: warm electronic pad, slow resolution, no vocals, 가사 없음, 75-80 BPM.
```

---

[[2026-06-17_Day025_Work_Order|Day 025 작업지시서]] | [[../24일차/Day024_YouTube_Upload|← Day 024 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

# Day 018 YouTube Upload

> 영상 파일: `18일차.mp4`
> 썸네일: `day018-unsloth-intro-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 018 | 파인튜닝 최강 도구 Unsloth 등장 — 속도 2~5배↑ 메모리 60%↓ | Google Colab LoRA
```
*(86자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 018.
Cravveo Company 100-Day Project, Day 018.

오늘은 파인튜닝 속도를 2~5배 높이고 메모리를 60% 절약해 주는 Unsloth를 소개했습니다.
Today I introduced Unsloth — making fine-tuning 2~5x faster with 60% less memory.

오늘 한 일 | What I did today:
- Unsloth vs 표준 방식 비교 (속도/메모리/난이도) | Compared Unsloth vs standard fine-tuning
- Unsloth 코랩 설치 완료 | Installed Unsloth in Google Colab
- FastLanguageModel로 Gemma 2B 모델 로드 성공 | Loaded Gemma 2B via FastLanguageModel
- LoRA 어댑터 설정 코드 실행 | Applied LoRA adapter config
- GPU 메모리 사용량 확인 | Checked GPU memory usage

오늘의 핵심 발견 | Key discovery today:
코랩 무료 T4 GPU는 메모리가 겨우 15GB입니다.
표준 방식으로 파인튜닝을 돌리면 세션이 뻗습니다.
Unsloth는 같은 결과를 내면서 메모리를 60% 아낍니다.
코랩 무료 환경에서 파인튜닝을 완주하려면 Unsloth는 필수입니다.

Colab's free T4 GPU has only ~15GB of memory.
Standard fine-tuning often crashes the session.
Unsloth achieves the same results using 60% less memory.
For free Colab fine-tuning, Unsloth is not optional — it's essential.

오늘의 에러 & 해결 | Today's error & fix:
17일차 셀을 먼저 다 실행하고 18일차(Unsloth)를 실행했더니 ImportError가 터졌습니다.
원인: Unsloth는 반드시 transformers, peft, trl보다 먼저 import 되어야 합니다.
해결: 18일차(Unsloth 설치 + import)를 먼저 실행하고, 그 다음에 17일차 라이브러리를 실행하면 정상 작동합니다.
순서가 거꾸로였을 뿐인데 에러가 났습니다. 순서 하나가 전부였습니다.

Today's error & fix:
Ran Day 017 cells first (transformers, peft, trl), then tried to import Unsloth — got an ImportError.
Cause: Unsloth must be imported BEFORE transformers, peft, and trl — not after.
Fix: Run Day 018 (Unsloth install + import) first, then run the Day 017 libraries. That's all it took.
Wrong order = error. Right order = success.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 019에서는 파인튜닝 학습 데이터 포맷인 JSONL을 분석합니다.
AI에게 먹일 질문-답변 데이터가 어떤 구조인지 직접 손으로 써봅니다.
In Day 019, I'll analyze JSONL — the format for fine-tuning training data.
We'll write our first Q&A entries by hand to understand the structure.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days

#Cravveo #파인튜닝 #FineTuning #Unsloth #구글코랩 #GoogleColab #LoRA #FastLanguageModel #BuildInPublic #AI초보
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Unsloth, unsloth 설치, FastLanguageModel, 구글 코랩, Google Colab, LoRA, LoRA 파인튜닝, PEFT, Gemma, gemma-2b-it, 허깅페이스, HuggingFace, GPU 메모리 절약, memory optimization, 4비트 양자화, 4bit quantization, T4 GPU, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 학습 일지, learning journal, 코랩 파인튜닝
```

---

### 고정 댓글

```text
Day 018 완료 | Day 018 Complete
Unsloth 설치 + Gemma 2B 모델 로드 성공. 이제 파인튜닝 직전 단계까지 왔습니다.
Unsloth installed and Gemma 2B loaded. We're one step away from actual fine-tuning.

오늘의 핵심 수치 | Today's key numbers:
- 표준 방식 대비 속도: 2~5배 빠름 | 2~5x faster than standard
- 메모리 절약: 60~80% | 60~80% less memory
- GPU 가용 메모리 (15GB T4): 충분히 남음 | Plenty left with 4-bit loading

오늘의 에러 & 해결 | Error & fix:
17일차 먼저 실행 → 18일차 실행 = ImportError 💥
18일차 먼저 실행 → 17일차 실행 = 정상 작동 ✅
Unsloth는 반드시 다른 라이브러리보다 먼저 import 해야 합니다.
Unsloth must be imported BEFORE transformers / peft / trl.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days

다음 Day 019 | Next Day 019
JSONL 포맷 분석 — AI에게 먹일 학습 데이터의 생김새.
JSONL Format — what fine-tuning training data actually looks like.
```

---

### 커뮤니티 게시물

```text
Day 018 완료 ✅ | Day 018 Complete ✅

오늘은 Unsloth를 소개하고 직접 설치해서 모델까지 로드했습니다.
Today I introduced Unsloth, installed it, and loaded a model.

오늘 배운 것:
코랩 무료 T4는 메모리가 15GB밖에 없습니다.
표준 방식으로 파인튜닝하면 세션이 뻗거나 몇 시간이 걸립니다.
Unsloth는 메모리를 60% 아끼고 속도는 2~5배 빠릅니다.
코랩 무료 플랜으로 파인튜닝을 완주하려면 Unsloth는 필수입니다.

What I learned:
Free T4 Colab only has 15GB VRAM.
Standard fine-tuning crashes it. Unsloth saves 60% memory and runs 2~5x faster.
For free Colab fine-tuning, Unsloth is not optional.

---

Day 019 예고 | Day 019 Preview
JSONL 포맷 분석 — AI에게 먹일 데이터가 어떻게 생겼는지 직접 써봅니다.
Analyzing JSONL — writing fine-tuning training data by hand.

#Cravveo #파인튜닝 #Unsloth #구글코랩 #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `18일차.mp4` 선택
- [ ] 제목 입력 (86자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day018-unsloth-intro-thumbnail-1280x720.png` 등록
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
Episode: Day 018.
Topic: a complete beginner discovering Unsloth — a fine-tuning library that is 2~5x faster and uses 60% less GPU memory than standard methods. Today they installed Unsloth in Google Colab and successfully loaded Gemma 2B via FastLanguageModel.

Main text must be large and readable:
"DAY 018"
"Unsloth 등장"

Small supporting text:
"속도 2~5배"
"메모리 60% 절약"

Visual style:
- bold visual contrast between "standard slow path" and "Unsloth fast path" (e.g., turtle vs lightning bolt, or heavy load vs streamlined arrow)
- visible elements: speed indicator, memory bar going down, Unsloth sloth logo concept (a sloth icon but with a lightning bolt — fast sloth)
- clean tech documentary style
- dramatic improvement mood — a breakthrough moment, not just a setup step
- beginner-friendly, not expert-guru
- no human face
- no robot
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 018" and "Unsloth 등장" text prominent, speed and memory comparison visible, energetic but clean layout.
```

---

## Gemini BGM 프롬프트 10개

### 1. Day 018 기본 배경음

```text
Cravveo Company Day 018 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 파인튜닝 속도를 확 끌어올려주는 Unsloth 라이브러리를 처음 소개하는 날이야.
어제의 차분한 설치 분위기와 달리 오늘은 "이런 도구가 있었어?" 하는 발견의 에너지가 담겼으면 좋겠어.
no vocals, 가사 없음, upbeat electronic, discovery energy, 90 BPM, loopable.
```

### 2. 비교표 설명 파트

```text
배경음악을 만들어줘. 표준 방식 vs Unsloth 비교표를 설명하는 파트야.
숫자들이 대조를 이루는 느낌 — 느린 것과 빠른 것이 명확하게 비교되는 분위기가 담겼으면 좋겠어.
analytical but engaging, contrast rhythm, clean electronic, no vocals, 가사 없음, loopable.
```

### 3. Unsloth 설치 대기 장면

```text
배경음악을 만들어줘. Unsloth 설치 로그가 길게 출력되는 대기 장면이야.
어제 설치와는 달리 "더 강력한 게 들어오고 있다"는 기대감이 담겼으면 좋겠어.
slightly rising tension, patient electronic pulse, anticipation build, no vocals, 가사 없음, loopable.
```

### 4. FastLanguageModel 모델 로드 장면

```text
배경음악을 만들어줘. FastLanguageModel.from_pretrained()를 실행하고 Gemma 2B 모델이 코랩으로 다운로드되는 장면이야.
2GB짜리 모델이 스트리밍으로 내려오는 기다림과 설렘이 담겼으면 좋겠어.
steady electronic flow, calm loading energy, soft rhythm, curiosity, no vocals, 가사 없음, loopable.
```

### 5. 모델 로드 성공 순간

```text
배경음악을 만들어줘. "✅ 모델 로드 성공" 메시지가 뜨는 순간이야.
어제의 라이브러리 설치 완료 느낌보다 조금 더 크고 의미 있는 성취감이 담겼으면 좋겠어.
warm triumphant chime, quiet but satisfying breakthrough, soft electronic lift, no vocals, 가사 없음, loopable.
```

### 6. LoRA 어댑터 설정 파트

```text
배경음악을 만들어줘. LoRA 어댑터 설정 코드를 설명하는 파트야.
처음 보는 파라미터들(r, lora_alpha, target_modules)을 하나씩 짚어가는 신중하고 집중된 분위기가 담겼으면 좋겠어.
focused electronic, careful and methodical, clean synth, no vocals, 가사 없음, loopable.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI learning journey.
Episode theme: discovering Unsloth — a breakthrough tool that makes fine-tuning dramatically faster and lighter.
Mood: quiet revelation, "this changes things", methodical excitement.
Style: clean electronic with slight upward energy, subtle momentum, no vocals, 가사 없음.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 018 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 게임 체인저가 등장한다" 라는 분위기가 담겼으면 좋겠어.
short electronic opener, game-changer energy, bold intro, clean and punchy, no vocals, 가사 없음.
```

### 9. 엔딩 — 준비 완성

```text
Create calm but forward-looking ending music for a YouTube episode where a beginner discovers Unsloth, installs it, and successfully loads a Gemma 2B model — realizing for the first time that full fine-tuning is now within reach.
Mood: quiet confidence, the tools are ready, something big is next.
Style: warm electronic pad, gentle momentum, subtle build, no vocals, 가사 없음, 80-88 BPM.
```

### 10. Day 019 예고 파트

```text
배경음악을 만들어줘. 다음 날 JSONL 포맷 분석 — AI에게 먹일 학습 데이터를 직접 만들기 시작한다는 예고 파트야.
드디어 "내 데이터를 만든다"는 창작의 기대감이 담겼으면 좋겠어.
creative electronic anticipation, building energy, crafting mood, no vocals, 가사 없음, loopable.
```

---

[[2026-06-10_Day018_Work_Order|Day 018 작업지시서]] | [[../17일차/Day017_YouTube_Upload|← Day 017 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

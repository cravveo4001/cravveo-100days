# Day 029 YouTube Upload

> 영상 파일: `29일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
> HuggingFace 모델: https://huggingface.co/cravveo/cravveo-llama-lora

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 029 | 내 컴퓨터에서 내가 만든 AI가 돌아간다 — GGUF 변환 + Ollama 등록
```
*(57자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 029.
Cravveo Company 100-Day Project, Day 029.

드디어 내 노트북에서 내가 파인튜닝한 AI가 돌아갑니다.
Finally, my fine-tuned AI runs on my own laptop.

코랩에서 학습한 모델을 GGUF 포맷으로 변환하고,
Day 004에서 설치한 Ollama에 등록했습니다.
터미널에서 ollama run cravveo를 치면 크라베오를 아는 AI가 답합니다.

Converted the Colab-trained model to GGUF format,
registered it with Ollama (installed on Day 004).
Now typing "ollama run cravveo" gives me a Cravveo-aware AI.

오늘 한 일 | What I did today:
- 83개 데이터로 30 epoch 학습 (코랩)
- GGUF 변환 (q4_k_m, 771MB)
- Google Drive로 파일 전송
- 로컬 Ollama에 cravveo 모델 등록
- ollama run cravveo 테스트

테스트 결과 | Test results:
"크라베오 컴퍼니가 뭐야?"
→ "한국의 IT 기업이야. 파인튜닝을 배우고 있는 AI 어시스턴트야."
핵심(IT 기업, 파인튜닝)은 맞지만 일부 텍스트가 깨짐.
Core info (IT company, fine-tuning) is correct but some text is garbled.

왜 완벽하지 않은가 | Why not perfect:
1B 모델 + 4비트 양자화 + 83개 데이터의 한계입니다.
더 큰 모델, 더 많은 데이터, 더 높은 양자화로 개선 가능합니다.
Limitations of 1B model + 4-bit quantization + 83 entries.
Improvable with larger model, more data, higher quantization.

하지만 핵심은 이것:
Day 001에서 리눅스를 설치하고,
Day 004에서 Ollama를 설치하고,
Day 016에서 코랩 파인튜닝을 시작해서,
Day 029에서 내 컴퓨터에 내 AI를 등록했습니다.
Phase 1(로컬 환경)과 Phase 2(파인튜닝)가 합쳐진 순간입니다.

But the key point is this:
Day 001: installed Linux.
Day 004: installed Ollama.
Day 016: started Colab fine-tuning.
Day 029: registered my own AI on my own computer.
Phase 1 (local env) and Phase 2 (fine-tuning) finally merged.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 030에서는 Phase 2 전체 회고 + Phase 3 계획을 세웁니다.
In Day 030, we do a full Phase 2 retrospective and plan Phase 3.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤗 Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
🤖 Model: https://huggingface.co/cravveo/cravveo-llama-lora
📒 Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

#Cravveo #파인튜닝 #FineTuning #GGUF #Ollama #로컬AI #Unsloth #Llama #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, GGUF, GGUF 변환, Ollama, 로컬 AI, local AI, Unsloth, Llama 3.2, 양자화, quantization, q4_k_m, 구글 코랩, Google Colab, T4 GPU, LoRA, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 1인 기업, Modelfile
```

---

### 고정 댓글

```text
Day 029 완료 | Day 029 Complete

내 컴퓨터에서 내가 만든 AI가 돌아갑니다.
My own fine-tuned AI runs on my own computer.

$ ollama run cravveo
>>> 크라베오 컴퍼니가 뭐야?
→ "한국의 IT 기업이야. 파인튜닝을 배우고 있는 AI 어시스턴트야."

29일간의 여정:
Day 001: 리눅스 설치
Day 004: Ollama 설치
Day 016: 코랩 파인튜닝 시작
Day 026: Gemma→Llama 모델 교체
Day 027: Before/After 파인튜닝 효과 확인
Day 028: HuggingFace에 모델 저장
Day 029: GGUF 변환 → 내 컴퓨터 Ollama에 등록 ← 오늘!

29-day journey:
Day 001: Linux install → Day 029: My AI on my computer

완벽하진 않지만 돌아갑니다.
Not perfect, but it runs.
품질 개선은 다음 단계에서.
Quality improvement comes next.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
🤖 Model: https://huggingface.co/cravveo/cravveo-llama-lora

다음 Day 030 | Next Day 030
Phase 2 전체 회고 + Phase 3 계획
Phase 2 retrospective + Phase 3 planning
```

---

### 커뮤니티 게시물

```text
Day 029 완료 ✅ | Day 029 Complete ✅

$ ollama run cravveo

내 컴퓨터에서 내가 만든 AI가 돌아갑니다.
My own fine-tuned AI runs on my own computer.

"크라베오 컴퍼니가 뭐야?"
→ "한국의 IT 기업이야. 파인튜닝을 배우고 있는 AI 어시스턴트야."

완벽하진 않습니다.
1B 모델 + 4비트 양자화 + 83개 데이터라서
텍스트가 깨지는 부분이 있습니다.
Not perfect. 1B model + 4-bit quantization + 83 entries
means some garbled text.

하지만 핵심은 맞습니다.
크라베오 = IT 기업, 파인튜닝, 공개 학습.
이 연결은 정확히 학습되어 있습니다.
But the core is correct.
Cravveo = IT company, fine-tuning, public learning.

29일 전에는 리눅스 설치도 못 했습니다.
오늘 내 컴퓨터에서 내가 만든 AI가 돌아갑니다.
29 days ago I couldn't even install Linux.
Today my own AI runs on my own computer.

품질 개선은 다음 단계에서 합니다.
Quality improvement comes next.

---

Day 030 예고 | Day 030 Preview
Phase 2 전체 회고 + Phase 3 (로컬 RAG + 자동화) 계획을 세웁니다.
Phase 2 full retrospective + Phase 3 planning.

#Cravveo #파인튜닝 #GGUF #Ollama #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `29일차.mp4` 선택
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
Episode: Day 029.
Topic: a complete beginner runs their own fine-tuned AI on their local laptop for the first time — GGUF conversion + Ollama registration. Phase 1 meets Phase 2. Build in Public.

Main text must be large and readable:
"DAY 029"
"내 컴퓨터에서 내 AI가 돌아간다"

Small supporting text:
"GGUF → Ollama → 로컬 실행"
"ollama run cravveo"

Visual style:
- visual metaphor: a laptop with a glowing AI brain inside — "it lives on my machine now"
- feeling: "I built this from nothing" — pride and ownership
- clean tech documentary style
- mood: milestone achievement, independence from cloud
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 029" and "내 컴퓨터에서 내 AI가 돌아간다" prominent, laptop + AI visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 029 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 29일간의 여정 끝에 내 컴퓨터에서 내가 만든 AI가 처음으로 돌아가는 날이야.
"드디어 내 것이 됐다"는 소유감과 독립의 느낌이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, proud ownership, 85 BPM, loopable.
```

### 2. GGUF 변환 파트

```text
배경음악을 만들어줘. 코랩에서 학습된 모델을 GGUF 포맷으로 변환하는 파트야.
"클라우드에서 로컬로 가져간다" 하는 전환의 느낌이 담겼으면 좋겠어.
format conversion, cloud to local, transitional electronic, no vocals, 가사 없음, loopable.
```

### 3. 파일 다운로드 파트

```text
배경음악을 만들어줘. GGUF 파일을 Google Drive를 통해 로컬로 가져오는 파트야.
"771MB짜리 내 AI를 가져가는 중" 하는 기대감이 담겼으면 좋겠어.
downloading treasure, anticipation, steady electronic, no vocals, 가사 없음, loopable.
```

### 4. Ollama 등록 파트

```text
배경음악을 만들어줘. ollama create cravveo 명령어로 모델을 등록하는 파트야.
Day 004에서 설치한 Ollama에 내 AI를 넣는 순간이야.
"Phase 1과 Phase 2가 합쳐진다" 하는 의미 있는 연결의 느낌이 담겼으면 좋겠어.
meaningful connection, two paths merging, warm electronic, no vocals, 가사 없음, loopable.
```

### 5. 첫 로컬 실행 — ollama run cravveo 파트

```text
배경음악을 만들어줘. 터미널에서 ollama run cravveo를 치고 첫 답변이 나오는 순간이야.
내 컴퓨터에서 내가 만든 AI가 처음으로 답하는 순간의 짜릿함이 담겼으면 좋겠어.
first local run, electric moment, bright electronic, no vocals, 가사 없음, loopable.
```

### 6. 답변 확인 — 맞는 거 같으면서 파트

```text
배경음악을 만들어줘. AI가 답하는데 핵심은 맞지만 텍스트가 깨지는 파트야.
"맞는 거 같으면서 아닌데..." 하는 웃기면서도 아쉬운 분위기가 담겼으면 좋겠어.
almost there, bittersweet humor, quirky electronic, no vocals, 가사 없음, loopable.
```

### 7. 회고 파트

```text
배경음악을 만들어줘. Day 001부터 029까지를 돌아보는 파트야.
리눅스 설치부터 시작해서 내 컴퓨터에 내 AI를 등록하기까지.
"여기까지 오는 데 29일 걸렸다"는 감회가 담겼으면 좋겠어.
looking back, 29-day journey, warm nostalgic electronic, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: Day 029 — converting the fine-tuned model to GGUF, registering it with local Ollama, and running it on a personal laptop for the first time. Phase 1 (local setup) meets Phase 2 (fine-tuning). Not perfect yet, but it runs. Build in Public.
Mood: "I built this from nothing", quiet pride, independence from cloud.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 029 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘 내 AI가 드디어 내 컴퓨터에서 돌아가는 날이다" 하는 기대와 설렘이 담겼으면 좋겠어.
short opener, exciting independence day, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner finally runs their own fine-tuned AI on their local laptop after 29 days of learning from scratch — from Linux install to local AI deployment.
Mood: "not perfect, but it's mine", quiet pride, ready for the next chapter.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 80 BPM.
```

---

[[2026-06-23_Day029_Work_Order|Day 029 작업지시서]] | [[../28일차/Day028_YouTube_Upload|← Day 028 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

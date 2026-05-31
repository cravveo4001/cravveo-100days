# Day 007 YouTube Upload

> 영상 파일: `7일차.mp4`
> 썸네일: `day007-save-ai-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 007 | AI 답변 자동 저장 성공 + 모델 한계 직접 확인 | Python + Ollama
```

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 007.
Cravveo Company 100-Day Project, Day 007.

오늘은 15개 질문을 AI에게 자동으로 보내고 답변을 텍스트 파일로 저장하는 스크립트를 완성했습니다.
단순 출력에서 파일 저장으로 한 단계 진화했습니다.
Today I completed a script that sends 15 questions to the AI automatically and saves all responses to a text file.
One step up from just printing — now it actually saves.

오늘 한 일 | What I did today:
- save_ai.py 작성 (15개 질문 → 파일 저장) | Wrote save_ai.py (15 questions → file save)
- 날짜 자동 파일명 생성 (datetime.strftime) | Auto timestamp filename with datetime.strftime
- 모델 한계 직접 확인 (날짜 오류, 한자 출력, 컨텍스트 부족) | Tested model limits hands-on
- Ollama 먹통 → 프로세스 강제 종료 → 재시작 경험 | Dealt with Ollama freeze, killed process, restarted
- 토큰 한도 실험 (300 → 800 → 2000 → 500) | Token limit experiments

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 008에서는 터미널에서 직접 질문을 입력하면 AI가 답변하는 대화 루프를 만듭니다.
In Day 008, I will build an interactive chat loop in the terminal.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days

#Cravveo #Ollama #Python #파일저장 #로컬AI #BuildInPublic #Linux #파인튜닝
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, Ollama, 올라마, Python, 파이썬, 파일 저장, file save, 로컬 AI, local AI, local LLM, qwen, qwen3, Linux, 리눅스, Build in Public, 1인 기업, one person business, AI 파인튜닝, AI fine tuning, requests, 자동화, automation, 오프라인 AI, offline AI, 할루시네이션, hallucination, 지식 컷오프, knowledge cutoff, 토큰, token
```

---

### 고정 댓글

```text
Day 007 완료 | Day 007 Complete
AI 15개 질문 자동 처리 + 파일 저장 성공. 그리고 AI가 틀리는 순간도 직접 확인했습니다.
15 questions auto-processed and saved to file. Also caught the AI making confident mistakes.

오늘의 발견 | Key finding:
작은 모델(2B)은 자신감 있게 틀립니다. 날짜도 모르고, 한자로 답하고, 긴 답변은 중간에 잘립니다.
Small models (2B) fail with confidence. Wrong dates, Chinese responses, truncated answers. That's the limit.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days

다음 Day 008 | Next Day 008
터미널에서 직접 질문하고 AI가 바로 답하는 대화 루프를 만듭니다.
Building an interactive terminal chat loop — type a question, get an answer, repeat.
```

---

### 커뮤니티 게시물

```text
Day 007 완료 ✅ | Day 007 Complete ✅

오늘은 AI한테 15개 질문을 자동으로 보내고 답변을 텍스트 파일로 저장했습니다.
Today I automated 15 questions to the AI and saved all the responses to a text file.

그런데 실험하면서 재미있는 걸 발견했어요.
But I found something interesting while experimenting.

AI한테 "오늘 날짜가 몇 년 몇 월 몇 일이야?"라고 물었더니
"2024년 10월 10일"이라고 자신있게 틀렸습니다.
실제 오늘은 2026년 5월 30일인데요.
Asked the AI "What's today's date?" — it confidently answered "October 10, 2024."
Today is actually May 30, 2026.

그리고 한국어로 질문했는데 한자로 답하질 않나,
답변이 3단계에서 갑자기 잘리질 않나...
It also responded in Chinese to a Korean question, and cut off mid-answer at step 3 of 5.

작은 모델의 한계를 몸으로 배웠습니다.
I learned the limits of small models firsthand.

---

Day 008 예고 | Day 008 Preview
터미널에서 직접 질문하면 AI가 바로 답하는 대화 루프를 만듭니다.
Building a live terminal chat loop — type a question, get an answer in real time.

#Cravveo #Python #Ollama #BuildInPublic
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `7일차.mp4` 선택
- [ ] 제목 입력
- [ ] 설명 입력
- [ ] 썸네일 `day007-save-ai-thumbnail-1280x720.png` 등록
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
Episode: Day 007.
Topic: a complete beginner automating 15 AI questions and saving the responses to a text file.

Main text must be large and readable:
"DAY 007"
"AI 답변 자동 저장 성공"

Small supporting text:
"15 questions → .txt file"

Visual style:
- dark terminal background
- visible elements: Python script on one side, saved text file output on the other
- deep navy background with bright green terminal text accent
- clean modern tech documentary style
- beginner-friendly, not expert-guru
- no human face
- no robot
- high contrast
- readable at small size
- no watermark

Composition:
large text at top, code vs saved file split panel below, simple and uncluttered.
```

---

## Gemini BGM 프롬프트 10개

### 1. Day 007 기본 배경음

```text
Cravveo Company Day 007 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 Python 스크립트로 AI에게 15개 질문을 자동으로 보내고 파일로 저장하는 날이야.
반복 실행되는 자동화의 느낌, 묵묵히 일하는 기계 같은 리듬감이 있으면 좋겠어.
no vocals, soft electronic, repetitive but calming, minimal beat, 85 BPM, loopable.
```

### 2. 스크립트 실행 대기 장면용

```text
Create background music for a scene where a Python script runs 15 questions one by one.
The mood is steady and methodical — watching the terminal output scroll line by line.
Style: lo-fi electronic, soft keys, gentle pulse, no vocals, 82 BPM, calm not tense.
```

### 3. AI가 틀리는 순간 발견 장면

```text
배경음악을 만들어줘. AI한테 오늘 날짜를 물었더니 2년 전 날짜를 자신있게 말하는 장면이야.
약간 어이없는 유머와 함께 "이게 AI의 한계구나" 깨닫는 순간의 음악이면 좋겠어.
soft electronic with a slight quirky accent, no vocals, lighthearted documentary tone, loopable.
```

### 4. 파일 저장 성공 순간

```text
Python 스크립트가 15개 AI 답변을 텍스트 파일로 저장하는 데 성공하는 순간의 배경음악.
작지만 확실한 성취감. 자동화가 처음으로 결과물을 만들어낸 느낌.
soft synth, gentle electronic lift, no vocals, warm and minimal, loopable.
```

### 5. Ollama 먹통 → 복구 장면

```text
배경음악을 만들어줘. 스크립트가 갑자기 멈추고, 프로세스를 강제 종료하고, 서비스를 재시작하는 장면이야.
당황 → 침착하게 문제 해결 → 다시 정상 복구의 흐름으로 음악이 변화하면 좋겠어.
soft electronic, slight tension then calm resolution, no vocals, documentary style, loopable.
```

### 6. 토큰 실험 설명 파트용

```text
토큰 한도를 300에서 800, 2000, 500으로 바꿔가며 실험하는 장면에 깔릴 배경음악.
말소리를 방해하지 않으면서 실험적인 느낌을 살짝 줘야 해.
minimal ambient electronic, soft pulse, no melody overload, no vocals, clean and calm.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI learning journey.
Episode theme: automating repetitive AI tasks and discovering the limits of a small language model.
Avoid epic trailer music. Use soft electronic textures, gentle piano, warm pads, minimal percussion, no vocals.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 007 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 AI한테 15개 질문을 자동으로 보내보자" 같은 조용한 실험 느낌이면 좋겠어.
minimal electronic intro, warm synth, soft piano accent, no vocals, clean tech documentary tone.
```

### 9. 엔딩 회고용

```text
Create calm ending music for a YouTube episode where a beginner automates AI questions and discovers model limitations firsthand.
Mood: quiet learning, slight surprise, curiosity about bigger models ahead.
Style: soft ambient electronic, gentle piano, warm pad, no vocals, 72-82 BPM.
```

### 10. Gemini 최적화 요청

```text
위 조건을 바탕으로 Day 007 AI 자동 저장 + 모델 한계 발견 영상에 맞는 배경음악 프롬프트 3개를 최종 추천해줘.
각 프롬프트는 Suno, Udio, YouTube Create 같은 AI 음악 생성기에 넣기 좋게 영어로 작성하고,
말소리를 방해하지 않는 배경음악 중심으로 다듬어줘.
```

---

[[2026-05-30_Day007_Work_Order|Day 007 작업지시서]] | [[../Daily_Log/2026-05-30_Day007_Log|Day 007 로그]] | [[../6일차/Day006_YouTube_Upload|← Day 006 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

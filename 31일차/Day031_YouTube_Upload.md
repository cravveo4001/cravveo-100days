# Day 031 YouTube Upload

> 영상 파일: `31일차.mp4`
> 코랩 노트북: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing
> HuggingFace 모델: https://huggingface.co/cravveo/cravveo-llama-lora

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 031 | 모델이 문제가 아니라 형식이 문제였다 — 2일간의 삽질 끝에 발견
```
*(55자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 031.
Cravveo Company 100-Day Project, Day 031.

2일간의 삽질 기록입니다.
A 2-day debugging story.

1일차: 데이터를 184개로 확장하고 3B 모델로 업그레이드했습니다.
코랩에서는 완벽한 답변이 나왔는데, 로컬 Ollama에서는 "Unknown"이었습니다.
모델 크기 문제인가? 양자화 문제인가? 1B로 바꿔봤습니다. q4를 q8로 바꿔봤습니다.
전부 실패했습니다.

Day 1: Expanded data to 184, upgraded to 3B model.
Perfect answers in Colab, but "Unknown" in local Ollama.
Tried 1B, tried q4, tried q8. All failed.

2일차: 진짜 원인을 찾았습니다.
모델이 문제가 아니라, Modelfile의 TEMPLATE이 문제였습니다.
AI는 "질문:/답변:" 형식으로 학습했는데, Ollama가 Llama 채팅 템플릿으로 감싸서 보내고 있었습니다.
TEMPLATE을 단순하게 바꾸니까 3B 모델이 코랩과 동일하게 정확히 답했습니다.

Day 2: Found the real cause.
Not the model, but the Modelfile TEMPLATE was wrong.
AI learned with "질문:/답변:" format, but Ollama wrapped it in Llama chat template.
Changed to simple template, and the 3B model answered perfectly.

"크라베오 컴퍼니가 뭐야?"
"IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널을 혼자서 운영하면서 수익을 창출하는 1인 기업이야."

오늘의 핵심 교훈 | Key lesson:
AI가 "모른다"고 답하면, 모델이 나쁜 게 아니라 말 거는 형식이 틀린 것일 수 있다.
학습할 때 쓴 형식과 질문할 때 쓴 형식이 일치해야 한다.

When AI says "I don't know", it might not be a bad model.
It might be the wrong input format.
Training format and inference format must match.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Dataset: https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset
Model: https://huggingface.co/cravveo/cravveo-llama-lora
Colab: https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing

#Cravveo #파인튜닝 #FineTuning #Modelfile #TEMPLATE #Ollama #GGUF #AI초보 #BuildInPublic #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Modelfile, TEMPLATE, Ollama, GGUF, 양자화, quantization, q8_0, Llama 3.2, 3B, 1B, 입력 형식, input format, 디버깅, debug, Build in Public, 100일 챌린지, 100 day challenge, Phase 3
```

---

### 고정 댓글

```text
Day 031 완료 | Day 031 Complete

2일간 삽질한 진짜 원인:
모델이 문제가 아니라 Modelfile TEMPLATE이 문제였습니다.

2-day debugging root cause:
Not the model — the Modelfile TEMPLATE was wrong.

학습 형식: "질문: .../답변: ..."
Ollama 형식: Llama 채팅 템플릿 (다른 형식)
= AI가 질문을 못 알아들음 = "Unknown"

TEMPLATE을 학습 형식에 맞추니까 바로 정확한 답이 나왔습니다.
Matched the TEMPLATE to training format, and got perfect answers.

"크라베오 컴퍼니가 뭐야?"
"IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널을 혼자서 운영하면서 수익을 창출하는 1인 기업이야."

교훈: AI가 "모른다"고 하면 형식을 먼저 확인하라.
Lesson: When AI says "unknown", check the format first.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 031 완료 | Day 031 Complete

2일간의 삽질 기록입니다.
A 2-day debugging story.

코랩에서 완벽한 답을 하는 AI가 로컬 Ollama에서는 "Unknown"이라고 했습니다.
The AI answered perfectly in Colab but said "Unknown" in local Ollama.

시도한 것들:
3B 모델, 1B 모델, q4 양자화, q8 양자화, temperature 조절...
전부 실패했습니다.
Tried: 3B, 1B, q4, q8, temperature tuning... All failed.

진짜 원인:
AI는 "질문:/답변:" 형식으로 배웠는데
Ollama가 다른 형식(Llama 채팅 템플릿)으로 질문을 보내고 있었습니다.
형식을 맞추니까 바로 됐습니다.

Real cause:
AI learned with "질문:/답변:" format
but Ollama sent questions in a different format.
Matched the format, and it worked immediately.

오늘의 교훈:
AI가 "모른다"고 답하면, 모델이 나쁜 게 아니라 말 거는 형식이 틀린 것일 수 있다.
When AI says "unknown", the model might be fine. Check the format.

#Cravveo #파인튜닝 #Modelfile #Ollama #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `31일차.mp4` 선택
- [ ] 제목 입력 (55자 확인)
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
Episode: Day 031.
Topic: 2 days of debugging AI — tried different models, quantization, temperature, all failed. The real problem was the input format template, not the model. Matching training format to inference format fixed everything.

Main text must be large and readable:
"DAY 031"
"모델이 아니라 형식이 문제였다"

Small supporting text:
"2일간의 삽질"
"TEMPLATE 한 줄이 답이었다"

Visual style:
- visual metaphor: a key fitting into a lock — the right format unlocks the right answers
- feeling: "the answer was so simple" — facepalm moment after days of debugging
- clean tech documentary style
- mood: relief and realization
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 031 영상에 사용할 배경음악 콘셉트를 만들어줘.
2일간 모델 크기, 양자화, temperature를 바꿔가며 삽질했는데 진짜 원인은 Modelfile TEMPLATE 한 줄이었어.
"답은 이렇게 가까이 있었다니..." 하는 허탈한 안도감이 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, bittersweet relief, 85 BPM, loopable.
```

### 2. 1일차 시도 파트 (데이터 확장 + 3B)

```text
배경음악을 만들어줘. 데이터를 184개로 확장하고 3B 모델로 업그레이드하는 파트야.
"이번에는 확실히 되겠지" 하는 자신감과 기대가 담겼으면 좋겠어.
confident upgrade, fresh start, energetic electronic, no vocals, 가사 없음, loopable.
```

### 3. 첫 실패 — 3B Unknown 파트

```text
배경음악을 만들어줘. 코랩에서 완벽했던 3B 모델이 Ollama에서 "Unknown"이라고 답하는 파트야.
"왜 또..." 하는 답답함과 당혹감이 담겼으면 좋겠어.
unexpected failure, frustrated confusion, tense electronic, no vocals, 가사 없음, loopable.
```

### 4. 삽질 반복 파트 (1B, q4, q8, temperature)

```text
배경음악을 만들어줘. 모델을 1B로 바꿔보고, q4를 q8로 바꿔보고, temperature를 조절해보는 파트야.
뭘 바꿔도 해결이 안 되는 반복되는 좌절이 담겼으면 좋겠어.
repeated attempts, diminishing hope, minor key electronic, no vocals, 가사 없음, loopable.
```

### 5. 2일차 재도전 파트

```text
배경음악을 만들어줘. 하루 쉬고 다시 도전하는 2일차 시작 파트야.
"다른 각도로 접근해보자" 하는 차분한 결의가 담겼으면 좋겠어.
fresh perspective, calm determination, clean electronic, no vocals, 가사 없음, loopable.
```

### 6. 원인 발견 — TEMPLATE 파트

```text
배경음악을 만들어줘. Modelfile의 TEMPLATE이 문제였다는 걸 발견하는 순간이야.
학습 형식과 실행 형식이 달라서 AI가 질문을 못 알아들었던 거야.
"이게 원인이었어?!" 하는 깨달음과 허탈한 웃음이 담겼으면 좋겠어.
eureka moment, facepalm realization, bright electronic, no vocals, 가사 없음, loopable.
```

### 7. 해결 — 정확한 답변 파트

```text
배경음악을 만들어줘. TEMPLATE을 바꾸고 "크라베오 컴퍼니가 뭐야?"에 정확한 답이 나오는 파트야.
2일간의 삽질이 한 줄로 해결된 순간의 안도감과 감동이 담겼으면 좋겠어.
problem solved, emotional relief, warm triumphant electronic, no vocals, 가사 없음, loopable.
```

### 8. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI fine-tuning journey.
Episode theme: Day 031 — 2 days of debugging, tried model sizes, quantization methods, temperature tuning. The real cause was a one-line Modelfile TEMPLATE mismatch between training format and inference format. Build in Public.
Mood: "the answer was right there all along", humbling realization.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 9. 오프닝 15초

```text
Cravveo Company Day 031 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"2일간의 삽질 끝에 진짜 원인을 찾았다 — 모델이 아니라 형식이었다" 하는 예고 느낌이 담겼으면 좋겠어.
short opener, mystery revealed preview, electronic, no vocals, 가사 없음.
```

### 10. 엔딩

```text
Create calm but insightful ending music for a YouTube episode where a beginner spent 2 days debugging AI model issues, only to discover the real problem was a one-line template format mismatch.
Mood: "simple answers hide behind complex problems", humbled but wiser.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 80 BPM.
```

---

[[2026-06-25_Day031_Work_Order|Day 031 작업지시서]] | [[../30일차/Day030_YouTube_Upload|← Day 030 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

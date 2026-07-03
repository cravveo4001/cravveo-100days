# Day 037 YouTube Upload

> 영상 파일: `37일차.mp4`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 037 | 36일치 일기장이 AI 학습 데이터가 됐습니다
```
*(52자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 037.
Cravveo Company 100-Day Project, Day 037.

오늘은 36일 동안 써온 데일리로그를 AI 학습 데이터로 자동 변환했습니다.
Today I automatically converted 36 days of daily logs into AI training data.

한 것 | What I did:
- obsidian_to_jsonl.py 스크립트 작성 — 마크다운 파일 자동 파싱
- 36개 파일 → 203개 Q&A 쌍 자동 생성
- 기존 데이터 92개 + 새 데이터 203개 = 총 295개로 재학습
- Google Colab T4 GPU에서 3 에포크 학습 완료
- GGUF 변환 후 Ollama에 v2 모델 등록

- Wrote obsidian_to_jsonl.py — auto-parses Markdown daily logs
- 36 files → 203 Q&A pairs generated automatically
- Retrained with 295 total samples (92 existing + 203 new)
- Training completed on Google Colab T4 GPU, 3 epochs
- Converted to GGUF and registered v2 model in Ollama

발견한 것 | Discovery:
데이터를 늘려도 환각(hallucination) 문제가 남았습니다.
특정 날짜의 사실을 정확히 기억하려면 RAG가 필요합니다.
Even with more data, hallucination remains.
To accurately recall specific day facts, RAG is needed.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora

#Cravveo #파인튜닝 #FineTuning #Obsidian #데이터자동화 #AI초보 #BuildInPublic #100일챌린지 #1인기업 #RAG
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, Obsidian, 데이터 자동화, data automation, JSONL, Google Colab, Unsloth, Llama, GGUF, Ollama, RAG, 환각, hallucination, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 037 완료 | Day 037 Complete

36일치 데일리로그 → 203개 Q&A 자동 생성 → 재학습 완료.
36 daily logs → 203 Q&A pairs auto-generated → retraining complete.

오늘의 핵심 발견 | Key discovery:
매일 꼼꼼히 쓴 기록이 AI 학습 재료가 됩니다.
하지만 특정 날짜 사실 회상은 RAG 없이는 한계가 있습니다.
Daily logs become AI training data.
But accurate recall of specific days requires RAG.

다음 단계 | Next step:
Day 038 — 환각 문제 분석 + RAG 도입 준비

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 037 완료 + Day 038 예고 | Day 037 Done + Day 038 Preview

36일 동안 매일 쓴 일기장이 오늘 AI 학습 데이터가 됐습니다.
The journal I've written every day for 36 days became AI training data today.

스크립트 하나로 자동 변환 | Auto-converted with one script:
📂 36개 마크다운 파일
→ 203개 Q&A 쌍
→ AI 재학습 완료

📂 36 Markdown files
→ 203 Q&A pairs
→ Retraining complete

근데 문제를 발견했습니다.
But I found a problem.
데이터를 늘려도 특정 날짜 사실을 정확히 기억 못 합니다.
Even with more data, the model can't accurately recall specific day facts.
다음 단계는 RAG입니다.
Next step: RAG.

내일 Day 038 — 환각 문제 분석 + RAG 도입 시작
Tomorrow Day 038 — analyze hallucination + start RAG

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #Obsidian #RAG
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `37일차.mp4` 선택
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
Episode: Day 037.
Topic: a complete beginner automatically converted 36 days of personal daily logs (Markdown files) into AI training data using a Python script, then retrained the model — and discovered the model still hallucinates specific facts, leading to the conclusion that RAG is needed next. Build in Public.

Main text must be large and readable:
"DAY 037"
"일기장이 학습 데이터가 됐다"

Small supporting text:
"36일 → 203개 Q&A 자동 생성"
"다음 문제: 환각(RAG 필요)"

Visual style:
- visual metaphor: a handwritten diary or notebook transforming into digital data streams / code
- feeling: "small victory + honest next challenge" — productive but discovering limits
- clean tech documentary style
- mood: curiosity, forward momentum, honest about imperfection
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-03_Day037_Work_Order|Day 037 작업지시서]] | [[../Daily_Log/2026-07-03_Day037_Log|Day 037 로그]] | [[../36일차/Day036_YouTube_Upload|← Day 036 유튜브]]

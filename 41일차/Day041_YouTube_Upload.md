# Day 041 YouTube Upload

> 영상 파일: `41일차.mp4`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 041 | 오타 하나 고치려다 절반을 갈아엎었다
```
*(45자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 041.
Cravveo Company 100-Day Project, Day 041.

어제 발견한 "쇼핑몰" 오타 하나만 고치면 될 줄 알았는데, 학습 데이터를 열어보니 훨씬 심각했습니다.
Yesterday I found one wrong fact ("online shop") in the training data. I thought it'd be a one-line fix. It wasn't.

한 것 | What I did:
- 학습 데이터 92개를 전부 열어봄 → 약 40개가 크라베오랑 무관한 AI 마케팅 잡담이었음
- 원인 추적: 예전에 만든 "아침 브리핑 자동화" 스크립트가 정체성 데이터랑 같은 파일에 계속 쌓아온 것
- 실제 사업 현황(Chrome 확장 프로그램 4개, cravveo.com, ablescan.app)을 반영해 정확한 데이터 20개로 전체 교체
- Colab에서 재학습 → cravveo:v5 등록
- RAG 없는 워크스페이스로 재검증 → "쇼핑몰"/"Gemma-2B" 완전히 사라짐

- Opened all 92 training samples → about 40 were unrelated AI-marketing rambling
- Traced the cause: an old "morning briefing" automation script had been dumping unrelated content into the same file as identity data
- Rewrote 20 accurate samples reflecting the real business (4 Chrome extensions, cravveo.com, ablescan.app)
- Retrained on Colab → registered cravveo:v5
- Re-verified in a RAG-free workspace → the false facts are completely gone

발견한 것 | Discovery:
검증 과정에서도 함정이 있었습니다. RAG가 켜진 워크스페이스로 먼저 테스트했더니 여전히 이상한 답이 나왔는데,
알고 보니 그건 재학습이 실패한 게 아니라 RAG가 무관한 문서를 섞어 넣은 것이었습니다.
There was a trap in verification too. Testing in a RAG-enabled workspace still gave weird answers —
turns out that wasn't a retraining failure, it was RAG mixing in unrelated documents.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora

#Cravveo #파인튜닝 #FineTuning #데이터클리닝 #DataCleaning #AI초보 #BuildInPublic #100일챌린지 #1인기업
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, 데이터 클리닝, data cleaning, 학습 데이터, training data, HuggingFace, LoRA, RAG, Chrome 확장 프로그램, Chrome extension, Build in Public, 100일 챌린지, 100 day challenge, 1인기업, one person startup
```

---

### 고정 댓글

```text
Day 041 완료 | Day 041 Complete

학습 데이터 92개 중 절반 가까이가 오염돼 있던 걸 발견하고, 20개로 싹 정리해서 재학습했습니다.
Found nearly half of the 92 training samples were contaminated, cleaned it down to 20, and retrained.

오늘의 핵심 발견 | Key discovery:
작은 오타 하나(쇼핑몰) 고치려다가, 예전 자동화 스크립트가 학습 데이터를 오염시켜온 구조적 문제를 발견했습니다.
Trying to fix one small typo led to discovering that an old automation script had been polluting the training data all along.

다음 단계 | Next step:
Day 042 — Obsidian/GitHub 데이터 기반 파인튜닝 고도화

GitHub: https://github.com/cravveo4001/cravveo-100days
Model: https://huggingface.co/cravveo/cravveo-llama-lora
```

---

### 커뮤니티 게시물

```text
Day 041 완료 + Day 042 예고 | Day 041 Done + Day 042 Preview

"쇼핑몰"이라는 오타 하나 고치려고 학습 데이터를 열었는데
Opened the training data to fix one typo ("online shop")

92개 중 40개가 저랑 아예 상관없는 내용이었습니다 😅
40 out of 92 samples had nothing to do with me 😅

원인은 예전에 만든 자동화 스크립트가 데이터를 계속 오염시켜온 것
The cause: an old automation script had been polluting the data all along

✅ 정확한 사실 20개로 전체 교체
✅ 재학습 완료 → cravveo:v5
✅ 오류 사라짐 확인

✅ Replaced with 20 accurate samples
✅ Retrained → cravveo:v5
✅ Confirmed the errors are gone

내일 Day 042 — 파인튜닝 데이터 고도화 계속
Tomorrow Day 042 — continuing to improve fine-tuning data

#Cravveo #파인튜닝 #BuildInPublic #100일챌린지 #데이터클리닝
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `41일차.mp4` 선택
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
Episode: Day 041.
Topic: a complete beginner tried to fix one wrong fact in their AI training data, but discovered nearly half of the 92 samples were contaminated by an old automation script — leading to a full data cleanup and retraining of the model. Build in Public.

Main text must be large and readable:
"DAY 041"
"오타 하나가 절반을 오염시켰다"

Small supporting text:
"92개 중 40개 삭제"
"재학습으로 해결"

Visual style:
- visual metaphor: peeling back layers to find a much bigger mess underneath, or a magnifying glass revealing hidden contamination in clean-looking data
- feeling: "small problem, big excavation" — surprised discovery leading to thorough cleanup
- clean tech documentary style
- mood: investigative, slightly surprised, satisfying resolution
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark
```

---

[[2026-07-09_Day041_Work_Order|Day 041 작업지시서]] | [[../Daily_Log/2026-07-09_Day041_Log|Day 041 로그]] | [[../40일차/Day040_YouTube_Upload|← Day 040 유튜브]]

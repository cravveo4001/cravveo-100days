# 📋 Day 011 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-03
> **단계** | Phase: Day 011 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama + 모델 실습 | ✅ 완료 |
| Day 006~010 | Python 자동화 기초 챕터 | ✅ 완료 |
| **Day 011** | **AnythingLLM 설치 — 오프라인 RAG 챕터 시작** | 🔥 오늘 |
| Day 012 | AnythingLLM + Ollama 연결 | ⏳ 예정 |
| Day 013 | 오프라인 RAG 이론 + 와이파이 해제 테스트 | ⏳ 예정 |
| Day 014 | 옵시디언 문서 RAG 업로드 및 테스트 | ⏳ 예정 |
| Day 015 | Phase 1 총평 및 회고 | ⏳ 예정 |
| Day 016~ | 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Python 자동화 기초 챕터(Day 006~010)를 마쳤습니다.
> 오늘부터 새로운 챕터 — **오프라인 RAG**입니다.
> 첫 번째 미션: **AnythingLLM 리눅스 앱 설치**
> AnythingLLM은 GUI 기반의 로컬 AI 챗봇 도구입니다.
> 코드 없이 클릭만으로 로컬 AI와 대화하고 문서를 업로드할 수 있습니다.

**English**
> Python automation basics chapter (Day 006~010) is complete.
> Today starts a new chapter — **Offline RAG**.
> First mission: **Install AnythingLLM on Linux**
> AnythingLLM is a GUI-based local AI chat tool.
> Chat with local AI and upload documents — no code required, just clicks.

---

## 📌 왜 AnythingLLM인가? | Why AnythingLLM?

**한국어**
지금까지는 터미널에서 코드로만 AI와 대화했습니다.
AnythingLLM을 쓰면 브라우저처럼 생긴 화면에서 클릭만으로 AI와 대화할 수 있습니다.
더 중요한 건 **내 문서를 업로드하면 AI가 그 내용을 기반으로 답변**합니다.
이것이 RAG(Retrieval-Augmented Generation)입니다.

**English**
Until now, I only talked to AI through terminal code.
AnythingLLM gives a browser-like interface — just click and chat.
More importantly, **upload your own documents and AI answers based on them**.
This is RAG (Retrieval-Augmented Generation).

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — AnythingLLM 다운로드 페이지 접속

브라우저에서 접속:
```
https://anythingllm.com
```
→ **Download** 버튼 → **Linux** 선택 → `.AppImage` 파일 다운로드

### Step 2 — 다운로드 폴더로 이동 후 실행 권한 부여

```bash
cd ~/Downloads
chmod +x AnythingLLM*.AppImage
```

### Step 3 — 실행

```bash
./AnythingLLM*.AppImage
```

> 📝 처음 실행 시 시간이 걸릴 수 있습니다. 잠시 기다리세요.

### Step 4 — 화면 확인

브라우저 또는 앱 창이 열리면 성공입니다.
초기 설정 화면(온보딩)이 나오면 일단 넘어가도 됩니다.
내일(Day 012)에 Ollama 연결 설정을 진행합니다.

---

## ✅ 성공 조건 | Success Criteria

- [ ] AnythingLLM .AppImage 파일 다운로드 완료
- [ ] `chmod +x` 실행 권한 부여 완료
- [ ] `./AnythingLLM*.AppImage` 실행 → 앱 화면 열림 확인
- [ ] 앱이 정상적으로 표시되는 것 확인 (화면 캡처)

---

## 🚨 막혔을 때 | Troubleshooting

**앱이 실행되지 않으면**
```bash
sudo apt install libfuse2
./AnythingLLM*.AppImage
```

**화면이 안 열리고 에러가 나면**
```bash
./AnythingLLM*.AppImage --no-sandbox
```

---

## 📅 다음 단계 | Next Step

**Day 012**: AnythingLLM 설정 화면에서 Ollama 연결. 로컬 AI 모델을 GUI로 제어하는 첫 경험.
**Day 012**: Connect Ollama inside AnythingLLM settings. First time controlling local AI through a GUI.

---

---

## 📚 RAG란 무엇인가? | What is RAG?

### 한 줄 요약 | One-line Summary
> **한국어**: AI에게 내 문서를 먼저 읽게 하고, 그 내용을 바탕으로 질문에 답하게 만드는 기술
> **English**: A technique that lets AI read your documents first, then answer questions based on that content.

---

### 현장 비유로 이해하기 | Understanding Through a Workplace Analogy

**한국어**
일반 AI = 신입 직원
입사 교육 받은 것만 알아요. 우리 공장 특수 규정은 몰라요.

RAG = 매뉴얼 들고 있는 신입 직원
우리 공장 작업 지침서를 손에 쥐고 있어요.
모르면 매뉴얼 찾아보고 답해줘요.

**English**
Normal AI = New employee
Only knows what they learned in orientation. Doesn't know your factory's special rules.

RAG = New employee holding the manual
Has your workplace operation manual in hand.
Doesn't know something? Looks it up and answers from it.

---

### 핵심 3줄 | 3-Line Summary

> **한국어**
> 1. AI는 원래 내 자료를 몰라요
> 2. RAG = 내 자료를 AI한테 먹이는 것
> 3. 그러면 AI가 내 자료 기반으로 답해요

> **English**
> 1. AI doesn't know your personal documents by default
> 2. RAG = feeding your documents into AI
> 3. Then AI answers based on your own materials

---

### 쉬운 비유로 이해하기 | Understanding Through a Simple Analogy

**RAG 없는 AI = 오픈북 없는 시험 | AI without RAG = Closed-book exam**
AI가 학습할 때 봤던 내용만 기억합니다.
크라베오 컴퍼니가 뭔지 물어보면 → 모릅니다. 학습 데이터에 없으니까요.
AI only remembers what it saw during training.
Ask it about Cravveo Company → it doesn't know. It wasn't in the training data.

**RAG 있는 AI = 오픈북 시험 | AI with RAG = Open-book exam**
AI에게 내 문서를 먼저 줍니다.
"크라베오 컴퍼니 소개서.pdf"를 업로드하면 AI가 그 문서를 찾아보고 답합니다.
You give AI your documents first.
Upload "Cravveo_Company_Introduction.pdf" → AI looks it up and answers from it.

---

### RAG의 3단계 동작 원리 | How RAG Works — 3 Steps

```
1단계 — 문서 업로드 | Step 1 — Upload Documents
   내 파일(PDF, txt, md 등)을 AnythingLLM에 올립니다.
   Upload your files (PDF, txt, md, etc.) to AnythingLLM.
   → AI가 내용을 잘게 쪼개서 기억합니다.
   → AI splits and memorizes the content.

2단계 — 질문 입력 | Step 2 — Ask a Question
   "지난달 매출 현황이 어떻게 돼?"
   "What was last month's revenue?"
   → AI가 업로드한 문서에서 관련 부분을 찾습니다.
   → AI searches your uploaded documents for relevant sections.

3단계 — 답변 생성 | Step 3 — Generate Answer
   찾은 내용을 바탕으로 AI가 답변합니다.
   AI answers based on what it found.
   → 내 문서를 읽고 답하는 오프라인 비서 완성.
   → Your offline assistant that reads your own documents is complete.
```

---

### 왜 오프라인 RAG인가? | Why Offline RAG?

| | 클라우드 RAG (ChatGPT 등) Cloud RAG | 로컬 RAG (AnythingLLM) Local RAG |
|--|--------------------------------------|----------------------------------|
| 내 문서 My documents | 외부 서버로 전송 Sent to external server | 내 컴퓨터 안에서만 처리 Stays on my computer |
| 인터넷 Internet | 필요 Required | 필요 없음 Not needed |
| 비용 Cost | 유료 Paid | 무료 Free |
| 보안 Security | 낮음 Low | 100% 내 컴퓨터 100% local |

**한국어**: 1인 기업가에게 중요한 영업 자료, 고객 정보, 전략 문서를 외부 서버에 올리지 않고 AI에게 읽게 할 수 있습니다. 이게 오프라인 RAG의 핵심입니다.
**English**: Business materials, client info, and strategy documents never leave your computer — AI reads them locally. That's the power of offline RAG.

---

### 이 프로젝트에서 RAG로 할 것들 | What We'll Do with RAG in This Project

- Day 014: 내 옵시디언 노트 업로드 → AI가 내 메모 기반으로 답변 | Upload Obsidian notes → AI answers based on my memos
- Day 078: "오늘 작전 요약서 출력해줘" → AI가 내 일지를 읽고 정리 | "Summarize today's mission" → AI reads my logs
- Day 100: 완전 오프라인 1인 기업 AI 비서 완성 | Complete offline one-person business AI assistant

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-03_Day011_Log|Day 011 로그]] | [[Day011_YouTube_Upload|Day 011 유튜브]] | [[../10일차/2026-06-02_Day010_Work_Order|← Day 010]] | [[../12일차/2026-06-04_Day012_Work_Order|Day 012 →]]

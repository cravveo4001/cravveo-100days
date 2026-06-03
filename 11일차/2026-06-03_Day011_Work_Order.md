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

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-03_Day011_Log|Day 011 로그]] | [[Day011_YouTube_Upload|Day 011 유튜브]] | [[../10일차/2026-06-02_Day010_Work_Order|← Day 010]] | [[../12일차/2026-06-04_Day012_Work_Order|Day 012 →]]

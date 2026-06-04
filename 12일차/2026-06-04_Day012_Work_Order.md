# 📋 Day 012 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-04
> **단계** | Phase: Day 012 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama + 모델 실습 | ✅ 완료 |
| Day 006~010 | Python 자동화 기초 챕터 | ✅ 완료 |
| Day 011 | AnythingLLM 설치 — 오프라인 RAG 챕터 시작 | ✅ 완료 |
| **Day 012** | **AnythingLLM + Ollama 연결** | 🔥 오늘 |
| Day 013 | 오프라인 RAG 이론 + 와이파이 해제 테스트 | ⏳ 예정 |
| Day 014 | 옵시디언 문서 RAG 업로드 및 테스트 | ⏳ 예정 |
| Day 015 | Phase 1 총평 및 회고 | ⏳ 예정 |
| Day 016~ | 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 어제 AnythingLLM을 설치했습니다.
> 오늘은 AnythingLLM 안에서 **Ollama를 직접 연결**하고 **워크스페이스를 만듭니다.**
> 설정 화면에서 클릭 몇 번으로 내 로컬 AI 모델을 GUI에서 제어하는 첫 경험입니다.

**English**
> Yesterday we installed AnythingLLM.
> Today we **connect Ollama inside AnythingLLM** and **create a workspace.**
> A few clicks in the settings panel — the first time controlling local AI through a GUI.

---

## 📌 왜 이걸 하는가? | Why Are We Doing This?

**한국어**
AnythingLLM은 지금 혼자 떠 있는 앱입니다.
Ollama도 따로 실행되고 있습니다.
이 둘을 연결하면 AnythingLLM GUI 화면에서 Ollama 모델을 사용할 수 있습니다.
연결 후에는 워크스페이스(채팅방 같은 개념)를 만들어서 AI와 대화합니다.

**English**
Right now AnythingLLM is running on its own.
Ollama is running separately too.
Connect the two — and AnythingLLM can use Ollama models through its GUI.
After that, create a workspace (think: a chat room) and start talking to your local AI.

---

## 🛠️ 실행 순서 | Step-by-Step

### Step 1 — Ollama 실행 확인

터미널에서 Ollama가 실행 중인지 확인합니다.

```bash
ollama list
```

> 모델 목록이 나오면 Ollama가 정상 실행 중입니다.
> 아무것도 안 나오거나 에러가 나면 먼저 Ollama를 실행하세요:
> ```bash
> ollama serve
> ```

---

### Step 2 — AnythingLLM 실행

```bash
cd ~/Downloads
./AnythingLLM*.AppImage
```

> 이미 실행 중이면 이 단계는 건너뜁니다.

---

### Step 3 — Settings에서 Ollama 연결

AnythingLLM 화면 왼쪽 하단 **⚙️ Settings (설정)** 아이콘 클릭

→ **AI Provider** 클릭

→ **LLM Provider** 드롭다운에서 **Ollama** 선택

→ **Ollama Base URL** 에 입력:

```
http://127.0.0.1:11434
```

→ **Save Changes** 클릭

> 저장 후 모델 목록이 자동으로 불러와지면 연결 성공입니다.

---

### Step 4 — 사용할 모델 선택

**Chat Model Selection** 드롭다운에서 사용할 모델 선택

> 추천: `qwen2.5:latest` 또는 `gemma3:latest` (이미 설치된 모델 중 선택)

---

### Step 5 — 워크스페이스 만들기

왼쪽 사이드바 상단 **+ New Workspace** 클릭

→ 이름 입력 (예: `cravveo-test`)

→ 워크스페이스 생성 확인

---

### Step 6 — 첫 대화 테스트

워크스페이스 채팅창에 테스트 메시지 입력:

```
안녕. 지금 어떤 AI 모델이야?
```

> AI가 자기 모델명을 포함한 답변을 하면 연결 완료입니다.

---

## ✅ 성공 조건 | Success Criteria

- [ ] Ollama 실행 확인 (`ollama list` 정상 출력)
- [ ] AnythingLLM Settings → AI Provider → Ollama 선택 완료
- [ ] Base URL `http://127.0.0.1:11434` 입력 후 Save 완료
- [ ] 모델 목록이 드롭다운에 자동으로 불러와짐
- [ ] 워크스페이스 생성 완료
- [ ] 워크스페이스에서 AI와 첫 대화 성공 (화면 캡처)

---

## 🚨 막혔을 때 | Troubleshooting

**모델 목록이 안 불러와질 때**
```bash
# Ollama가 실행 중인지 확인
curl http://127.0.0.1:11434
```
> `Ollama is running` 텍스트가 나오면 Ollama는 정상. AnythingLLM 설정 URL 다시 확인.

**AnythingLLM이 실행이 안 될 때**
```bash
./AnythingLLM*.AppImage --no-sandbox
```

**Ollama가 실행되지 않을 때**
```bash
ollama serve
```
> 새 터미널 탭에서 실행하고 AnythingLLM에서 다시 연결 시도.

---

## 📅 다음 단계 | Next Step

**Day 013**: 인터넷을 완전히 끊고(Wi-Fi 해제) 로컬 AI가 오프라인 상태에서도 정상 작동하는지 직접 확인합니다. 오프라인 RAG의 핵심인 "인터넷 없이 AI 사용" 체험.
**Day 013**: Disconnect Wi-Fi completely and confirm local AI still works offline. The key experience of offline RAG — AI that works without internet.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-04_Day012_Log|Day 012 로그]] | [[Day012_YouTube_Upload|Day 012 유튜브]] | [[../11일차/2026-06-03_Day011_Work_Order|← Day 011]] | [[../13일차/2026-06-05_Day013_Work_Order|Day 013 →]]

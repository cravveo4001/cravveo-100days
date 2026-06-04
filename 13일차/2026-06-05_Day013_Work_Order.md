# 📋 Day 013 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-05
> **단계** | Phase: Day 013 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama + 모델 실습 | ✅ 완료 |
| Day 006~010 | Python 자동화 기초 챕터 | ✅ 완료 |
| Day 011 | AnythingLLM 설치 — 오프라인 RAG 챕터 시작 | ✅ 완료 |
| Day 012 | AnythingLLM + Ollama 연결 + 워크스페이스 첫 대화 | ✅ 완료 |
| **Day 013** | **RAG 첫 실전 — 내 문서를 AI에게 먹이기** | 🔥 오늘 |
| Day 014 | 옵시디언 문서 RAG 업로드 및 테스트 | ⏳ 예정 |
| Day 015 | Phase 1 총평 및 회고 | ⏳ 예정 |
| Day 016~ | 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> RAG를 이론으로만 배웠습니다. 오늘은 직접 합니다.
> 임베딩 모델을 설치하고, 내 문서를 AnythingLLM에 올리고,
> AI가 그 문서를 읽고 답하는 순간을 직접 확인합니다.
> "크라베오 컴퍼니가 뭐야?" — AI는 원래 모릅니다. 문서를 주면 압니다.

**English**
> RAG was theory. Today we make it real.
> Install an embedding model, upload a document to AnythingLLM,
> and watch AI answer questions based on that document.
> "What is Cravveo Company?" — AI doesn't know by default. Give it the document, and it does.

---

## 📌 임베딩 모델이 뭔가? | What Is an Embedding Model?

**한국어**
RAG가 작동하려면 두 가지 AI가 필요합니다.

| 역할 | 모델 | 하는 일 |
|------|------|---------|
| 대화 모델 | qwen3.5:2b | 질문을 이해하고 답변 생성 |
| 임베딩 모델 | nomic-embed-text | 문서 내용을 숫자로 변환해서 저장 |

임베딩 모델은 문서를 "기억하는" 역할입니다.
문서를 잘게 쪼개서 숫자 벡터로 변환하고, 나중에 질문이 들어오면 관련 부분을 찾아줍니다.

**English**
RAG needs two AIs working together.

| Role | Model | What it does |
|------|-------|-------------|
| Chat model | qwen3.5:2b | Understands questions and generates answers |
| Embedding model | nomic-embed-text | Converts document content into numbers for storage |

The embedding model "memorizes" the document.
It splits the document into chunks, converts them to number vectors, and retrieves relevant parts when a question comes in.

---

## 🛠️ 실행 순서 | Step-by-Step

### Step 1 — 임베딩 모델 설치

터미널에서 실행:

```bash
ollama pull nomic-embed-text
```

> 다운로드 완료 후 확인:
> ```bash
> ollama list
> ```
> `nomic-embed-text` 가 목록에 나오면 완료.

---

### Step 2 — AnythingLLM에 임베딩 모델 연결

AnythingLLM **⚙️ Settings** → **Embedding**

→ **Embedding Provider**: `Ollama` 선택

→ **Ollama Base URL**: `http://127.0.0.1:11434`

→ **Embedding Model**: `nomic-embed-text` 선택

→ **Save Changes**

---

### Step 3 — 테스트용 문서 만들기

터미널에서 아래 명령으로 간단한 소개 문서를 만듭니다:

```bash
cat > ~/cravveo_intro.txt << 'EOF'
크라베오 컴퍼니 소개

크라베오 컴퍼니는 1인 기업가가 운영하는 AI 자동화 프로젝트입니다.
AI를 전혀 모르는 초보자가 로컬 AI 파인튜닝부터 1인 기업 자동화 시스템까지
직접 구축하는 100일 도전 과정을 유튜브에 기록합니다.

채널명: Cravveo Company
프로젝트: 100일 AI 파인튜닝 도전기
목표: 완전 오프라인 1인 기업 AI 비서 구축
기술 스택: Ubuntu Linux, Ollama, AnythingLLM, Python, Google Colab
현재 단계: 오프라인 RAG 챕터 (Day 011~015)

크라베오 컴퍼니의 슬로건은 "막히고, 에러 나고, 해결하는 과정을 기록한다"입니다.
EOF
```

> 파일 생성 확인:
> ```bash
> cat ~/cravveo_intro.txt
> ```

---

### Step 4 — AnythingLLM 워크스페이스에 문서 업로드

`cravveo-test` 워크스페이스 화면 왼쪽 **Upload** 또는 문서 아이콘 클릭

→ `cravveo_intro.txt` 파일 선택해서 업로드

→ 업로드 후 **Move to Workspace** 클릭 (워크스페이스에 반드시 추가해야 작동)

→ 임베딩 처리 완료 메시지 확인

---

### Step 5 — RAG 작동 확인 (Before / After 비교)

**테스트 질문 1 — 문서 없이**

새 워크스페이스(`no-rag-test`) 하나 만들고 (문서 없는 상태) 질문:

```
크라베오 컴퍼니가 뭐야?
```

> AI가 모른다고 하거나 엉뚱한 답을 하면 정상. 학습 데이터에 없으니까요.

**테스트 질문 2 — 문서 있는 워크스페이스에서**

`cravveo-test` 워크스페이스로 돌아와서 같은 질문:

```
크라베오 컴퍼니가 뭐야?
```

> AI가 업로드한 문서 내용을 기반으로 답하면 RAG 작동 성공.

**테스트 질문 3 — 더 구체적인 질문**

```
크라베오 컴퍼니의 슬로건이 뭐야?
```

> 문서에 있는 내용 그대로 답하면 완벽한 성공.

---

## ✅ 성공 조건 | Success Criteria

- [ ] `ollama pull nomic-embed-text` 완료 + `ollama list` 확인
- [ ] AnythingLLM Settings → Embedding → nomic-embed-text 연결 완료
- [ ] `cravveo_intro.txt` 파일 생성 완료
- [ ] 워크스페이스에 문서 업로드 + 임베딩 처리 완료
- [ ] 문서 없는 AI: "크라베오 컴퍼니가 뭐야?" → 모른다 (화면 캡처)
- [ ] 문서 있는 AI: 같은 질문 → 문서 기반 답변 (화면 캡처)

---

## 🚨 막혔을 때 | Troubleshooting

**임베딩 처리 중 오류가 날 때**
```bash
# Ollama 실행 중인지 확인
curl http://127.0.0.1:11434
# nomic-embed-text 설치 확인
ollama list
```

**문서 업로드 후 AI가 여전히 모른다고 할 때**
- 워크스페이스에 문서를 올린 뒤 반드시 **Move to Workspace** 버튼을 눌렀는지 확인
- 임베딩 완료 표시(초록 체크)가 나왔는지 확인

**nomic-embed-text 다운로드가 느릴 때**
- 274MB 파일 — 와이파이 연결 상태에서 받고 이후 끊으면 됩니다

---

## 📅 다음 단계 | Next Step

**Day 014**: 이번엔 내 진짜 Obsidian 노트를 AnythingLLM에 올립니다. 직접 쓴 메모, 작업 일지, 아이디어를 AI가 읽고 답하는 나만의 오프라인 AI 비서 첫 체험.
**Day 014**: This time we upload real Obsidian notes. Your own memos, work logs, and ideas — AI reads them and answers. Your personal offline AI assistant, for real.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-06-05_Day013_Log|Day 013 로그]] | [[Day013_YouTube_Upload|Day 013 유튜브]] | [[../12일차/2026-06-04_Day012_Work_Order|← Day 012]] | [[../14일차/2026-06-06_Day014_Work_Order|Day 014 →]]

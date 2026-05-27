# 📋 Day 004 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-27
> **단계** | Phase: Day 004 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| Day 002 | 작업 폴더 생성 + Python 가상환경(venv) 구성 | ✅ 완료 |
| Day 003 | Git 저장소 초기화 + 첫 번째 커밋 + GitHub push | ✅ 완료 |
| **Day 004** | **Ollama 설치 + 로컬 LLM 첫 실행** | 🔥 오늘 |
| Day 005~ | Ollama 모델 탐색 + 프롬프트 실습 | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 080~ | Obsidian + 로컬 RAG 연결 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 오늘은 Ollama를 설치하고
> 로컬 컴퓨터에서 AI 언어모델을 처음으로 직접 실행합니다.
> 인터넷이 없어도 내 컴퓨터에서 AI가 돌아가는 것을 확인합니다.

**English**
> Today I will install Ollama
> and run an AI language model directly on my local machine for the first time.
> I will confirm that AI works on my computer even without internet.

---

## 📌 왜 Ollama인가? | Why Ollama?

**한국어**
Ollama는 로컬 LLM을 가장 쉽게 실행할 수 있는 도구입니다.
터미널 명령어 한 줄로 AI 모델을 다운받고 바로 대화할 수 있습니다.
내 데이터가 외부 서버로 나가지 않아 보안상 안전하고,
앞으로 파인튜닝한 모델을 직접 올려서 쓸 수 있는 핵심 플랫폼입니다.

**English**
Ollama is the easiest way to run LLMs locally.
A single terminal command downloads an AI model and lets you chat with it instantly.
Your data never leaves your computer — it's private and secure.
It's also the platform we'll use later to run our own fine-tuned models.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — Ollama 설치 | Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Step 2 — 설치 확인 | Verify installation
```bash
ollama --version
```

### Step 3 — Ollama 서비스 상태 확인 | Check service status
```bash
ollama list
```

### Step 4 — 첫 번째 모델 다운로드 및 실행 | Download and run first model

> ⚠️ 처음 실행 시 모델 파일을 다운받습니다 (약 9.6GB). 시간이 걸릴 수 있습니다.
> ⚠️ First run will download the model file (~9.6 GB). This may take a few minutes.

```bash
ollama run gemma4:e2b
```

### Step 5 — AI와 첫 대화 | First conversation with local AI

모델이 실행되면 `>>>` 프롬프트가 나타납니다. 아래처럼 입력해보세요:

```
안녕! 너는 누구야?
```

```
What can you do?
```

> 📝 실제 실행: `gemma4:e2b` (edge 2B, 모바일/엣지 기기 최적화 경량 버전) 로 진행. AMD GPU 인식 확인.

### Step 6 — 대화 종료 | Exit the model
```
/bye
```

### Step 7 — 설치된 모델 목록 확인 | Check installed models
```bash
ollama list
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] `ollama --version` 명령어 실행 → 버전 숫자 출력
- [ ] `ollama run gemma3:1b` 실행 → 모델 다운로드 완료
- [ ] `>>>` 프롬프트에서 AI가 대답
- [ ] `/bye` 로 정상 종료
- [ ] `ollama list` 에서 설치된 모델 확인

---

## 🚨 막혔을 때 | Troubleshooting

**`curl` 명령어가 없다고 나오면**
```bash
sudo apt install curl -y
```

**설치 후 `ollama` 명령어를 못 찾는다고 나오면**
```bash
source ~/.bashrc
# 또는 터미널을 새로 열기
```

**모델 다운로드가 너무 느리거나 끊기면**
다운로드는 중단해도 안전합니다. 같은 명령어를 다시 실행하면 이어받습니다.

**메모리 부족 오류가 나오면**
더 작은 모델로 시도:
```bash
ollama run tinyllama
```

**Ollama 서비스가 실행 안 될 때**
```bash
sudo systemctl start ollama
sudo systemctl status ollama
```

---

## 📅 다음 단계 | Next Step

**Day 005**: Ollama에서 여러 모델을 비교하고 프롬프트 실습을 합니다.
**Day 005**: Compare multiple models in Ollama and practice prompt engineering.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-27_Day004_Log|Day 004 로그]] | [[Day004_YouTube_Upload|Day 004 유튜브]] | [[../3일차/2026-05-26_Day003_Work_Order|← Day 003]] | [[../5일차/2026-05-28_Day005_Work_Order|Day 005 →]]

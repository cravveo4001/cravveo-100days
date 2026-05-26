# 📋 Day 002 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-25
> **단계** | Phase: Day 002 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| **Day 002** | **작업 폴더 생성 + Python 가상환경(venv) 구성** | 🔥 오늘 |
| Day 003 | Git 저장소 초기화 + 첫 커밋 | ⏳ 다음 |
| Day 004~ | Ollama 로컬 LLM 실행 | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 080~ | Obsidian + 로컬 RAG 연결 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Python 패키지들이 서로 꼬이지 않도록,
> 오늘은 Cravveo 전용 작업 폴더를 만들고
> Python 가상환경(venv)을 생성해 활성화합니다.

**English**
> To prevent Python packages from conflicting with each other,
> today I will create a dedicated Cravveo project folder
> and set up a Python virtual environment (venv).

---

## 📌 왜 가상환경이 필요한가? | Why Virtual Environment?

**한국어**
가상환경은 프로젝트마다 독립된 Python 작업공간입니다.
가상환경 없이 패키지를 설치하면 다른 프로젝트와 버전이 충돌할 수 있습니다.
`(venv)` 표시가 뜨면 지금 내 컴퓨터 전체가 아닌, 이 프로젝트 전용 공간에서 작업 중이라는 뜻입니다.

**English**
A virtual environment is an isolated Python workspace per project.
Installing packages without one can cause version conflicts across projects.
When `(venv)` appears in the terminal, it means you are working inside this project's private space — not the system-wide Python.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 현재 위치 확인 | Check current location
```bash
pwd
```

### Step 2 — 작업 폴더 생성 | Create project folder
```bash
mkdir -p ~/projects/cravveo_ai
cd ~/projects/cravveo_ai
pwd
```

### Step 3 — 가상환경 생성 | Create virtual environment
```bash
python3 -m venv venv
```

### Step 4 — 가상환경 활성화 | Activate virtual environment
```bash
source venv/bin/activate
```

### Step 5 — 활성화 확인 | Verify activation
```bash
which python
which pip
python --version
pip --version
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] 터미널 경로가 `/home/c/projects/cravveo_ai` 로 표시됨
- [ ] 터미널 프롬프트 앞에 `(venv)` 가 붙어 있음
- [ ] `which python` → `.../cravveo_ai/venv/bin/python` 형태
- [ ] `which pip` → `.../cravveo_ai/venv/bin/pip` 형태
- [ ] `python --version` 정상 출력

---

## 🚨 막혔을 때 | Troubleshooting

**`python3 -m venv venv` 오류 시**
```bash
sudo apt install python3-venv -y
```

**`(venv)` 가 안 보일 때**
```bash
pwd
ls
source venv/bin/activate
```

**가상환경 종료 방법 | How to deactivate**
```bash
deactivate
```

---

## 📅 다음 단계 | Next Step

**Day 003**: Git 저장소를 초기화하고 첫 번째 커밋을 올립니다.
**Day 003**: Initialize a Git repository and make the first commit.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-25_Day002_Log]]

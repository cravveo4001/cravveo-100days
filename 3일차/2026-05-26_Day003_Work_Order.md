# 📋 Day 003 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-26
> **단계** | Phase: Day 003 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| Day 002 | 작업 폴더 생성 + Python 가상환경(venv) 구성 | ✅ 완료 |
| **Day 003** | **Git 저장소 초기화 + 첫 번째 커밋 + GitHub push** | 🔥 오늘 |
| Day 004~ | Ollama 로컬 LLM 실행 | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 080~ | Obsidian + 로컬 RAG 연결 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 오늘은 Cravveo 작업 폴더를 Git 저장소로 만들고
> 첫 번째 커밋을 기록합니다.
> 그리고 GitHub에 공개 저장소를 만들어 첫 push까지 완료합니다.

**English**
> Today I will turn the Cravveo project folder into a Git repository,
> record the first commit,
> and push it to a new public GitHub repository.

---

## 📌 왜 Git과 GitHub가 필요한가? | Why Git and GitHub?

**한국어**
Git은 코드와 파일의 변경 이력을 기록하는 도구입니다.
실수로 파일을 망쳐도 이전 상태로 되돌릴 수 있습니다.
GitHub는 그 기록을 인터넷에 올려두는 공간입니다.
다른 컴퓨터에서도 작업할 수 있고, 시청자도 파일을 직접 받아볼 수 있습니다.

**English**
Git is a tool that records the history of changes to your files.
If something breaks, you can roll back to a previous state.
GitHub is where you store that history online.
It lets you work from any computer and lets viewers download your files directly.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 작업 폴더로 이동 | Move to project folder
```bash
cd ~/projects/cravveo_ai
pwd
```

### Step 2 — Git 저장소 초기화 | Initialize Git repository
```bash
git init
```

### Step 3 — Git 사용자 정보 설정 | Set Git user info
```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Step 4 — 첫 파일 만들기 | Create first file
```bash
echo "# Cravveo AI Project" > README.md
cat README.md
```

### Step 5 — 파일 스테이징 | Stage file
```bash
git add README.md
git status
```

### Step 6 — 첫 번째 커밋 | First commit
```bash
git commit -m "Day 003: first commit"
git log
```

### Step 7 — GitHub 브라우저에서 저장소 생성 | Create repository on GitHub

1. 브라우저에서 [github.com](https://github.com) 로그인
2. 우측 상단 `+` → `New repository` 클릭
3. Repository name: `cravveo-100days`
4. `Public` 선택
5. README, .gitignore 체크 **하지 않음** (이미 로컬에 있으므로)
6. `Create repository` 클릭
7. 화면에 나오는 주소 복사 (예: `https://github.com/cravveo4001/cravveo-100days.git`)

### Step 8 — 터미널에서 연결 및 push | Connect and push from terminal
```bash
git remote add origin https://github.com/cravveo4001/cravveo-100days.git
git branch -M main
git push -u origin main

```

---

## ✅ 성공 조건 | Success Criteria

- [ ] `git init` 완료 → `.git` 폴더 생성 확인
- [ ] `README.md` 파일 생성
- [ ] `git status` 에서 파일이 staged 상태로 표시
- [ ] `git commit` 완료 → `git log` 에서 첫 커밋 확인
- [ ] GitHub 공개 저장소 생성
- [ ] `git push` 완료 → GitHub 웹에서 파일 확인

---

## 🚨 막혔을 때 | Troubleshooting

**`git push` 에서 인증 오류가 나면**
GitHub Personal Access Token(PAT)이 필요합니다.
GitHub → Settings → Developer settings → Personal access tokens → Generate new token

**`git config` 를 안 했을 때 커밋 오류가 나면**
```bash
git config --global user.name "이름"
git config --global user.email "이메일"
```

**push 후 GitHub에서 안 보이면**
```bash
git remote -v
git status
```

---

### Step 9 — Obsidian에서 Vault 열기 | Open Vault in Obsidian

1. Obsidian 실행
2. `폴더를 Vault로 열기` 선택
3. `/home/c/finetuning-project` 선택
4. 좌측 파일 트리에서 `README.md` 클릭
5. 링크가 연결되는지 확인 (`[[...]]` 클릭 시 해당 문서로 이동)

---

## 📅 다음 단계 | Next Step

**Day 004**: Ollama를 설치하고 로컬 LLM을 처음 실행합니다.
**Day 004**: Install Ollama and run a local LLM for the first time.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-26_Day003_Log|Day 003 로그]] | [[../2일차/2026-05-25_Day002_Work_Order|← Day 002]] | [[../README|커맨드 센터]]

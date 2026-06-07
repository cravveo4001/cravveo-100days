# 📋 Day 015 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-07
> **단계** | Phase: Day 015 / 100
---

## 💻 노트북 사양 & 사용 모델 | Hardware & Model

| 항목 | 사양 |
|------|------|
| 노트북 | 한성 TFX5556U |
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | AMD Radeon Vega (내장) |
| 저장소 | NVMe SSD 468GB |
| OS | Linux |
| 사용 모델 | qwen2.5:3b (Ollama) |
| 임베딩 모델 | nomic-embed-text (AnythingLLM) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama + 모델 실습 | ✅ 완료 |
| Day 006~010 | Python 자동화 기초 챕터 | ✅ 완료 |
| Day 011~014 | AnythingLLM + RAG 챕터 | ✅ 완료 |
| **Day 015** | **Phase 1 전체 회고 — 14일을 돌아본다** | 🔥 오늘 |
| Day 016~ | Phase 2 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 001부터 Day 014까지, Phase 1 전체를 돌아봅니다.
> 무엇을 배웠는지, 어디서 막혔는지, 어떻게 뚫었는지 정리합니다.
> 그리고 Day 016부터 시작할 Phase 2 파인튜닝을 예고합니다.

**English**
> Look back at the full Phase 1 — Day 001 through Day 014.
> Summarize what was learned, where we got stuck, and how we broke through.
> Then preview Phase 2 fine-tuning, starting Day 016.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
회고 없이 달리면 같은 실수를 반복합니다.
14일 동안 내가 뭘 했는지 한 번 정리해야 다음 14일이 더 단단해집니다.
오늘은 쉬는 날이 아니라 정리하는 날입니다.

**English**
Running without reflection repeats the same mistakes.
Reviewing the first 14 days makes the next 14 days stronger.
Today is not a rest day — it's a consolidation day.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — Phase 1 전체 타임라인 정리 (완료 — 영상에서 그대로 활용)

| Day | 한 것 | 핵심 발견 | 막힌 것 |
|-----|-------|----------|--------|
| 001 | 리눅스 세팅, Python 환경 구축 | 터미널이 전부다 | - |
| 002 | venv 가상환경 생성 | 프로젝트마다 환경을 분리해야 한다 | - |
| 003 | Git + GitHub 첫 커밋 + push | 버전 관리 = 실수해도 되는 안전망 | - |
| 004 | Ollama 설치 + 첫 AI 대화 | 로컬 AI가 진짜 된다 | - |
| 005 | 모델 비교 (gemma4 vs qwen3) | 작은 모델은 빠르지만 할루시네이션 있음 | - |
| 006 | Python으로 Ollama API 호출 | 코드로 AI를 부르는 순간 자동화가 시작됨 | - |
| 007 | AI 답변 자동 저장 스크립트 | 작은 모델은 날짜도 모르고, 한자로 답함 | - |
| 008 | 터미널 대화 루프 구현 | while True + input() 조합 | - |
| 009 | 대화 내용 파일 저장 | Day 007 + Day 008 합치기 | - |
| 010 | 아침 브리핑 자동화 완성 | cron + Python = 진짜 자동화 | - |
| 011 | AnythingLLM 설치 | GUI로 로컬 AI와 대화 가능 | 에이전트 모드 진입 |
| 012 | AnythingLLM + Ollama 연결 | 워크스페이스 첫 대화 성공 | - |
| 013 | RAG 첫 실전 Before/After | 문서 있는 AI vs 없는 AI — 완전히 다름 | - |
| 014 | 문서 17개 대량 업로드 | RAG는 키워드 검색이다 (작은 모델 한계) | 컴퓨터 사양 + 모델 3번 교체 |

> 📌 각 Day의 솔직한 회고(한/영)는 바로 아래 "Day별 솔직한 회고" 섹션에 정리되어 있습니다. 영상에서는 표를 빠르게 훑고, 회고 멘트를 골라서 말하면 됩니다.

---

### Day별 솔직한 회고 | Honest Reflections, Day by Day

**Day 001**
처음으로 리눅스 세계에 들어왔다 (윈도우만 30년 넘게 사용). 윈도우는 너무 무거울 것 같고, 개발은 윈도우보다 리눅스를 더 많이 쓰는 것 같아서 유튜브 보고 설치했다. 새 운영체제라 적응이 쉽지 않은 것 같기도 하고 아닌 것 같기도 하다. 큰 틀은 괜찮은데 디테일한 명령어가 조금씩 달라서 헤매고 있다.
Entered the Linux world for the first time (used Windows for 30+ years). Windows felt too heavy, and development seems to lean more toward Linux, so I installed it after watching YouTube tutorials. Adapting to a new OS feels easy and hard at the same time — the big picture is fine, but small command differences keep tripping me up.

**Day 002**
가상환경(venv)을 왜 써야 하는지 아직 잘 모르겠다. 다들 해야 한다고 해서 하고 있고, 언젠가는 이해하게 되겠지. 그냥 하면 안 되나? 서버를 만들어야 해서 그런 것 같기도 하다.
I still don't really understand why I need a virtual environment (venv). I'm doing it because everyone says I should, and I'll probably get it eventually. Why can't I just skip it? Maybe it's because I'll need to build a server someday.

**Day 003**
개발자들이 파일을 올려두고 스타도 받고 버전 관리도 한다고 해서 다 해야 하는 줄 알고 하고 있지만, 디테일하게 정확히 사용하고 있는 건 아니다.
I heard developers upload their files, get stars, and manage versions, so I figured I had to do it too — but I'm not really using it precisely or in detail yet.

**Day 004**
여러 로컬 모델이 있지만 Ollama를 선택한 이유는 AI의 추천도 있었고, API 연결도 잘 되고, 많이 사용되고 있어서다.
There are many local model options, but I chose Ollama because the AI recommended it, the API connection works well, and it's widely used.

**Day 005**
두 모델 다 내가 쓰기엔 너무 무겁다. qwen3 모델은 지금 노트북에서만 쓰고 있는데, gemma4:e2b 모델은 내 갤럭시 S24에서는 빠르게 돌아가지만 노트북에서는 버벅거린다. 아마 AnythingLLM 프로그램 자체가 무거워서 그런 걸 수도 있다.
Both models are too heavy for my setup. I currently only run qwen3 on my laptop — gemma4:e2b actually runs fast on my Galaxy S24 phone but stutters on the laptop. It might be because AnythingLLM itself is a heavy program.

**Day 006**
드디어 반(半) 자동화에 성공했다. 아직 많이 부족하지만 그래도 반자동화를 성공시켰다는 쾌감은 있다.
Finally got half-automation working. It's still lacking in a lot of ways, but there's a real thrill in pulling off even partial automation.

**Day 007**
지금 노트북 자체 사양이 많이 부족하다 보니 느리고, 여러 언어가 섞여서 출력되고, 작은 모델은 부족한 게 많고, 큰 모델은 아예 작동하지 않는 문제가 있었다. 아~~ 노트북을 바꾸고 싶은 욕구와 욕망이 슬슬 올라온다.
My laptop specs are clearly lacking — it's slow, languages get mixed in the output, small models fall short in many ways, and big models don't even run properly. Ahh... the urge to upgrade my laptop is slowly creeping in.

**Day 008**
나만의 챗봇을 만드는 날이었다. 신기하기도 하다. 내가 챗봇을 만들다니 — 뭔가 되는 것 같은 느낌도 든다.
The day I built my own chatbot. It's kind of amazing — me, building a chatbot? It actually feels like I'm getting somewhere.

**Day 009**
지금까지는 휘발성으로만 만들어진 것들이었는데, 드디어 저장까지 되기 시작했다...
Everything I'd made up to now was temporary — but finally, things are starting to actually get saved...

**Day 010**
이게 진짜 완전 자동화다. 아침마다 (정해진 시간에) 스스로 질문하고 스스로 대답해서 저장하는 기능을 구현하다니!
This is real, full automation. Every morning, at a set time, it asks itself a question, answers itself, and saves the result — I actually built that!

**Day 011**
이 부분에서 리눅스와 윈도우의 차이를 느꼈다. 윈도우는 Ollama에 GUI 버전이 있는데, 리눅스는 자꾸 터미널로 작업해야 해서 따로 GUI가 필요해 AnythingLLM을 설치했다.
This is where I really felt the difference between Linux and Windows. Windows has a GUI version of Ollama, but Linux kept forcing me into the terminal — so I installed AnythingLLM to get a GUI of my own.

**Day 012**
두 개의 프로그램이 동시에 돌아가니 뭔가 엄청 느려지는 느낌이 너무 많이 든다. 모델 선택도 너무 힘들다 (종류가 너무 많아서).
Running two programs at once makes everything feel painfully slow. Choosing a model is also a struggle — there are just too many options.

**Day 013**
드디어 기본 AI와 "나의 AI"가 구별되기 시작한 시작점이라 뭔가 신기하다.
Finally — the starting point where the default AI and "my AI" began to feel different. Something about that feels genuinely amazing.

**Day 014**
아~~ 이번 편은 포기할 뻔했다. 대답도 제대로 안 나오고, 멈추고, 문서 업로드도 안 되고... 하아~ 그래도 컴퓨터 사양이 문제였던 거라 어찌어찌 도전해서 결국 성공은 했다.
Ahh~~ I almost gave up on this one. Answers wouldn't come out right, things kept freezing, document uploads failed... *sigh* But in the end it came down to my computer specs — somehow I pushed through and made it work.

---

### Step 2 — Phase 1 핵심 교훈 3가지 뽑기

영상에서 말할 핵심 교훈 3가지를 직접 말로 뽑아봅니다:

1. **환경이 전부다** — 리눅스, Python, Git, Ollama. 이것만 갖춰지면 나머지는 쌓인다.
2. **작은 모델의 현실** — 빠르지만 할루시네이션, 언어 오류, 키워드 의존. 한계를 알아야 쓸 수 있다.
3. **사양이 벽이다** — 기술보다 하드웨어가 먼저 막는다. 이건 Phase 2에서도 계속될 문제다.

---

### Step 3 — Phase 2 예고 준비

영상 마지막에 말할 Phase 2 예고:

```
Day 016부터는 파인튜닝을 시작합니다.
RAG는 문서를 참고하는 것이고,
파인튜닝은 AI의 뇌 자체를 바꾸는 것입니다.
구글 코랩, Unsloth, LoRA — 새로운 세계가 시작됩니다.
```

```
From Day 016, we start fine-tuning.
RAG is referencing documents.
Fine-tuning is changing the AI's brain itself.
Google Colab, Unsloth, LoRA — a new world begins.
```

---

### Step 4 — 영상 녹화

오늘은 코딩 없는 날입니다. 화면 녹화 + 말하기가 전부입니다.

영상 구성:
1. (오프닝) "Day 015, Phase 1 끝났습니다."
2. (타임라인) Day 001~014 빠르게 훑기
3. (핵심 교훈) 3가지 정리
4. (솔직한 후기) 컴퓨터 사양 문제, 모델 교체, 리부팅의 연속
5. (예고) Phase 2 파인튜닝 시작 선언

---

## ✅ 성공 조건 체크리스트

- [x] Day 001~014 타임라인 한 줄 정리 완료
- [ ] Phase 1 핵심 교훈 3가지 말로 뽑기 완료
- [ ] Phase 2 예고 멘트 준비 완료
- [ ] 영상 녹화 완료
- [ ] YouTube 업로드 문서 작성 완료

---

## 🔧 오늘 준비물

- 별도 설치 없음
- 터미널, AnythingLLM 화면 캡처 정도면 충분
- 말하는 것이 오늘의 핵심

---

## 📅 다음 단계 예고 | Next Up

**Day 016** — RAG vs Fine-Tuning 비교 공부
책을 펴놓고 시험 치는 것(RAG)과 통째로 암기하는 것(Fine-Tuning)의 차이.
Phase 2의 첫 날.

Day 016 — RAG vs Fine-Tuning comparison.
RAG = open-book exam. Fine-Tuning = memorizing the whole curriculum.
First day of Phase 2.

---

[[2026-06-07_Day015_Work_Order|Day 015 작업지시서]] | [[../14일차/Day014_YouTube_Upload|← Day 014 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

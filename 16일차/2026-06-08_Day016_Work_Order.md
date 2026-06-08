# 📋 Day 016 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-08
> **단계** | Phase: Day 016 / 100

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
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| **Day 016** | **RAG vs Fine-Tuning 비교 공부 + 구글 코랩 GPU 연결 — Phase 2 첫걸음 (Day 016+017 합본)** | 🔥 오늘 |
| Day 017~ | Phase 2: 코랩 환경 구축 + 데이터 수집 + 파인튜닝 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

> 📌 원래 마스터 가이드의 Day 017(코랩 GPU 연결)을 오늘 분량에 합쳤습니다. 개념 공부만으로는 영상 분량이 짧아서, 실습(코랩 GPU 켜보기)까지 함께 진행합니다. 다음 Day부터는 원래 Day 018(코랩 파이썬 가상 스택 구축) 내용으로 이어집니다.

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 지금까지는 RAG(검색 증강 생성)만 다뤘습니다.
> 오늘은 두 가지를 합쳐서 진행합니다.
> 첫째, 파인튜닝(Fine-Tuning)이 RAG와 무엇이 다른지 개념을 정리합니다.
> 둘째, 파인튜닝의 무대가 될 구글 코랩(Colab)에 접속해 GPU를 직접 켜봅니다.
> 내 노트북이 아닌 "구글의 GPU"를 처음으로 빌려 쓰는 날입니다.

**English**
> Until now, we've only worked with RAG (Retrieval-Augmented Generation).
> Today combines two things.
> First, clarify how Fine-Tuning differs from RAG.
> Second, log into Google Colab and turn on a GPU for the first time.
> Today is the day I borrow Google's GPU instead of relying on my own laptop.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
RAG와 파인튜닝을 헷갈리면 앞으로 40일이 흔들립니다.
RAG는 "책을 펴놓고 보는 시험"이고, 파인튜닝은 "시험 범위를 통째로 암기하는 것"입니다.
이 차이를 명확히 알아야 왜 굳이 더 어려운 파인튜닝에 도전하는지 이해할 수 있습니다.

**English**
Confusing RAG and Fine-Tuning will shake the next 40 days.
RAG is an "open-book exam." Fine-Tuning is "memorizing the entire syllabus."
Understanding this difference clearly is what makes the harder road of fine-tuning worth taking.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — RAG 복습: 내가 직접 경험한 것

Day 011~014에서 직접 겪은 RAG를 한 줄로 정리합니다:

```
RAG = AI 옆에 "참고 자료(내 문서)"를 놓아두고,
질문이 오면 그 자료를 먼저 찾아본 뒤 답하는 방식.

장점: 문서만 바꾸면 AI의 지식이 즉시 바뀐다 (재학습 불필요)
단점: 작은 모델은 키워드 검색에 의존 — Day 014에서 직접 확인한 한계
```

---

### Step 2 — Fine-Tuning이란 무엇인가 공부

아래 개념을 내 언어로 정리해봅니다 (AI에게 물어봐도 좋습니다):

| 개념 | 한 줄 설명 |
|------|-----------|
| Fine-Tuning (파인튜닝) | 모델의 가중치(뇌 구조) 자체를 내 데이터로 다시 학습시키는 것 |
| 데이터셋 (Dataset) | 모델에게 가르칠 질문-답변 쌍의 모음 |
| LoRA | 모델 전체가 아닌 일부분만 작게 학습시키는 효율적인 방법 |
| Loss (손실율) | 학습이 잘 되고 있는지 보여주는 숫자 — 낮아질수록 좋음 |

---

### Step 3 — RAG vs Fine-Tuning 정면 비교

아래 표를 채우면서 두 기술의 차이를 명확히 합니다:

| 비교 항목 | RAG (책 펴놓고 시험) | Fine-Tuning (통째로 암기) |
|----------|---------------------|--------------------------|
| 지식이 담기는 곳 | 외부 문서 | 모델 내부 가중치 |
| 지식 갱신 방법 | 문서만 바꾸면 즉시 반영 | 다시 학습해야 함 (시간/자원 소요) |
| 말투/성격 변화 | 어렵다 | 가능하다 (학습 데이터로 직접 주입) |
| 필요한 자원 | 상대적으로 적음 | GPU, 데이터셋, 학습 시간 필요 |
| 내가 경험한 한계 | 작은 모델은 키워드 검색에 의존 (Day 014) | 아직 경험 전 — 앞으로 직접 부딪힐 예정 |

---

### Step 4 — 왜 굳이 파인튜닝에 도전하는가

오늘 영상에서 말할 핵심 메시지를 정리합니다:

```
RAG는 AI에게 "참고서"를 쥐여주는 것이었다면,
파인튜닝은 AI의 "성격과 말투, 정체성" 자체를 바꾸는 것입니다.

크라베오 컴퍼니만의 AI를 만들고 싶다면,
결국 파인튜닝까지 가야 한다고 생각합니다.
```

```
RAG was like handing the AI a reference book.
Fine-Tuning is about reshaping the AI's personality, tone, and identity itself.

If I want an AI that's truly "Cravveo's own,"
I believe fine-tuning is the road I have to walk.
```

---

### Step 5 — 구글 코랩(Colab) 접속 및 GPU 켜보기

오늘의 실습 파트입니다. 직접 손으로 진행합니다:

1. 브라우저에서 [colab.research.google.com](https://colab.research.google.com) 접속 (구글 계정 로그인)
2. 새 노트북 생성
3. 상단 메뉴 `런타임(Runtime)` → `런타임 유형 변경(Change runtime type)` 클릭
4. 하드웨어 가속기에서 `T4 GPU` 선택 후 저장
5. 코드 셀에 아래 명령어 입력 후 실행 (Shift + Enter)

```python
!nvidia-smi
```

6. 출력 결과에서 GPU 이름(Tesla T4), 메모리 용량(약 15GB) 확인

**핵심 포인트**: 내 노트북은 GPU가 없어서(또는 미약해서) 항상 사양 문제에 부딪혔지만, 코랩은 구글의 서버 GPU를 무료로 빌려 쓸 수 있습니다. 이게 왜 파인튜닝에 코랩을 쓰는지의 답입니다.

---

## ✅ 성공 조건 체크리스트

- [ ] RAG 한 줄 정리 완료 (내 경험 기반)
- [ ] Fine-Tuning 핵심 개념 4가지 (Fine-Tuning, Dataset, LoRA, Loss) 내 언어로 정리
- [ ] RAG vs Fine-Tuning 비교표 완성
- [ ] "왜 파인튜닝에 도전하는가" 멘트 준비 완료
- [ ] 구글 코랩 접속 + 새 노트북 생성 완료
- [ ] T4 GPU 런타임 선택 완료
- [ ] `!nvidia-smi` 실행 → GPU 정보 출력 확인
- [ ] 영상 녹화 완료

---

## 🔧 오늘 준비물

- 구글 계정 (코랩 로그인용)
- 인터넷 연결 (코랩은 클라우드 서비스이므로 필수)
- 화면에는 마스터 가이드, 메모장, 비교표, 코랩 화면이면 충분

---

## 📅 다음 단계 예고 | Next Up

**Day 017** — 코랩 파이썬 가상 스택 구축
파인튜닝에 필요한 필수 라이브러리를 코랩 환경에 설치하는 연습을 진행합니다.
오늘 GPU를 켰다면, 다음은 그 위에서 돌아갈 도구들을 준비할 차례입니다.

Day 017 — Building the Python stack on Colab.
Install the essential libraries needed for fine-tuning in the Colab environment.
Now that the GPU is on, it's time to prepare the tools that will run on top of it.

---

[[2026-06-08_Day016_Work_Order|Day 016 작업지시서]] | [[../15일차/Day015_YouTube_Upload|← Day 015 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

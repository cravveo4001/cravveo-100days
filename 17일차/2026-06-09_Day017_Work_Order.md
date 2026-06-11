# 📋 Day 017 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-09
> **단계** | Phase: Day 017 / 100
> *(마스터 가이드 기준 Day 018 내용 — Day 016 합본으로 1일 당겨짐)*

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
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016 | RAG vs 파인튜닝 비교 + 코랩 GPU 첫 가동 | ✅ 완료 |
| **Day 017** | **코랩 파이썬 가상 스택 구축 — 파인튜닝 필수 라이브러리 설치** | 🔥 오늘 |
| Day 018~ | Unsloth 소개 + 데이터셋 제작 + 본격 파인튜닝 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 어제 코랩에서 GPU를 켰습니다.
> 오늘은 그 위에서 돌아갈 도구들을 설치합니다.
> 파인튜닝에 필요한 파이썬 라이브러리들을 코랩 환경에 직접 설치하고,
> 각각이 무슨 역할인지 이해하는 것이 오늘의 목표입니다.

**English**
> Yesterday we turned on the GPU in Colab.
> Today we install the tools that will run on top of it.
> The goal is to install the essential Python libraries for fine-tuning in Colab
> and understand what each one actually does.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
파인튜닝은 모델 하나만 있다고 되는 게 아닙니다.
그 모델을 학습시키는 "도구 세트"가 먼저 준비돼야 합니다.
오늘 설치하는 라이브러리들이 앞으로 파인튜닝 전체를 떠받치는 뼈대가 됩니다.

**English**
Fine-tuning isn't just about having a model.
You need the full "toolset" ready before you can train anything.
The libraries we install today are the foundation that holds up the entire fine-tuning process.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 및 GPU 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. `cravveo_finetuning.ipynb` 노트북 열기 (구글 드라이브에 저장된 것)
3. 런타임 → 런타임 유형 변경 → T4 GPU 선택
4. 아래 코드 실행으로 GPU 확인

설명: 현재 코랩에 GPU가 제대로 연결됐는지 확인하는 코드입니다. Tesla T4라는 GPU 이름과 메모리 정보가 출력되면 정상입니다. 아무 내용도 안 나오거나 에러가 뜨면 런타임 유형을 T4 GPU로 바꿔야 합니다.
⏱ 실행 시점: 코랩에 접속할 때마다 맨 처음에 실행해서 GPU가 잡혔는지 확인합니다.
```python
!nvidia-smi
```

---

### Step 2 — 필수 라이브러리 설치

아래 코드를 코랩 셀에 붙여넣고 실행합니다:
설명: 파인튜닝에 필요한 핵심 라이브러리 6개를 한 번에 설치하는 명령어입니다. 앞에 `!`가 붙은 것은 파이썬 코드가 아니라 터미널 명령어라는 뜻입니다. 처음 실행하면 설치 로그가 길게 출력되는데 정상입니다. 끝까지 기다리면 됩니다.
⏱ 실행 시점: 코랩 세션이 끊기면 설치한 라이브러리가 모두 사라집니다. 접속할 때마다 반드시 이 셀을 먼저 실행해야 합니다.
```python
!pip install transformers datasets accelerate peft trl bitsandbytes
```

설치가 끝나면 아래 코드로 정상 설치 확인:
설명: 설치된 라이브러리들을 실제로 불러와서(import) 버전 번호를 출력합니다. 에러 없이 버전 숫자들과 ✅ 메시지가 출력되면 설치가 정상입니다. 만약 `ModuleNotFoundError`가 뜨면 위의 설치 셀을 다시 실행하세요.
⏱ 실행 시점: 설치 셀 바로 다음에 한 번만 실행해서 확인용으로 씁니다.
```python
import transformers
import datasets
import peft
import trl
print("transformers:", transformers.__version__)
print("datasets:", datasets.__version__)
print("peft:", peft.__version__)
print("trl:", trl.__version__)
print("✅ 모든 라이브러리 설치 완료")
```

---

### Step 3 — 각 라이브러리 역할 정리

| 라이브러리 | 역할 | 한 줄 비유 |
|-----------|------|-----------|
| `transformers` | AI 모델을 불러오고 다루는 핵심 도구 | AI 모델의 몸통 |
| `datasets` | 학습 데이터셋을 불러오고 가공하는 도구 | AI에게 먹일 교과서 |
| `accelerate` | GPU 학습을 빠르고 효율적으로 만들어주는 도구 | GPU 연료 최적화 장치 |
| `peft` | LoRA 등 효율적 파인튜닝 방식을 지원하는 도구 | 뇌 전체 말고 일부만 건드리는 수술 도구 |
| `trl` | 지도학습(SFT) 방식으로 모델을 훈련시키는 도구 | 파인튜닝 트레이너 |
| `bitsandbytes` | 모델을 4비트로 압축해 메모리를 절약하는 도구 | 메모리 절약 압축기 |

---

### Step 4 — 간단한 모델 로드 테스트 (여유 있으면)

설치가 끝나면 아주 작은 모델 하나를 불러와 보는 테스트를 해봅니다:

설명: `transformers` 라이브러리가 제대로 작동하는지 확인하는 가벼운 테스트입니다. 토크나이저란 텍스트(글자)를 AI가 이해할 수 있는 숫자 배열로 변환하는 도구입니다. "안녕하세요" 같은 문장을 넣으면 `[15496, 11, ...]` 같은 숫자 배열이 출력되는데, 이게 정상입니다. 모델 전체를 다운받는 게 아니라 작은 도구 하나만 가져오는 것이라 빠르게 실행됩니다.
⏱ 실행 시점: 오늘 딱 한 번만 실행하면 됩니다. 다음 세션에서는 실행하지 않아도 됩니다.
```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("gpt2")
print(tokenizer("안녕하세요, 코랩 테스트입니다."))
print("✅ 토크나이저 로드 성공")
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] 6개 라이브러리 설치 완료 (`transformers`, `datasets`, `accelerate`, `peft`, `trl`, `bitsandbytes`)
- [ ] 버전 출력 코드 실행 → "✅ 모든 라이브러리 설치 완료" 확인
- [ ] 각 라이브러리 역할 내 언어로 정리
- [ ] (선택) 토크나이저 로드 테스트 성공
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**설치 도중 에러가 뜰 때**
→ 코랩 런타임을 재시작(런타임 → 런타임 재시작)한 뒤 다시 설치 셀부터 실행

**bitsandbytes 에러가 뜰 때**
→ GPU 런타임이 아닌 경우 발생할 수 있음. 런타임 유형을 T4 GPU로 바꿨는지 확인

**설치가 너무 느릴 때**
→ 코랩 무료 서버 상태에 따라 느려질 수 있음. 그냥 기다리면 됩니다

---

## 📅 다음 단계 예고 | Next Up

**Day 018** — Unsloth 라이브러리 소개 및 특징 공부
일반 파인튜닝보다 2~5배 빠르고 메모리도 적게 쓰는 Unsloth 라이브러리.
왜 다들 파인튜닝에 Unsloth를 쓰는지, 오늘 설치한 도구들과 어떻게 다른지 비교합니다.

Day 018 — Introducing Unsloth.
2~5x faster fine-tuning with significantly less memory.
Why everyone uses Unsloth — and how it compares to today's library stack.

---

[[2026-06-09_Day017_Work_Order|Day 017 작업지시서]] | [[../16일차/Day016_YouTube_Upload|← Day 016 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

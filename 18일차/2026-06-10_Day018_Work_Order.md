# 📋 Day 018 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-10
> **단계** | Phase: Day 018 / 100
> *(마스터 가이드 기준 Day 019 내용 — Day 016 합본으로 1일 당겨짐)*

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
| 사용 모델 | 없음 (코랩 T4 GPU 환경) |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016 | RAG vs 파인튜닝 비교 + 코랩 GPU 첫 가동 | ✅ 완료 |
| Day 017 | 코랩 파이썬 가상 스택 구축 — 파인튜닝 필수 라이브러리 설치 | ✅ 완료 |
| **Day 018** | **Unsloth 소개 — 파인튜닝 최강 도구 설치 + 모델 로드** | 🔥 오늘 |
| Day 019~ | JSONL 포맷 분석 + 크라베오 데이터셋 제작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 어제 파인튜닝 도구 세트를 설치했습니다.
> 오늘은 그 도구들을 훨씬 빠르고, 훨씬 가볍게 만들어주는 Unsloth를 소개합니다.
> 왜 다들 파인튜닝에 Unsloth를 쓰는지 이해하고,
> 코랩에 직접 설치한 뒤 모델까지 로드하는 것이 오늘의 목표입니다.

**English**
> Yesterday we installed the fine-tuning toolset.
> Today we introduce Unsloth — the tool that makes everything 2~5x faster with 60% less memory.
> The goal is to understand why everyone uses Unsloth for fine-tuning,
> install it in Colab, and successfully load a model with it.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
어제 설치한 라이브러리들로도 파인튜닝은 할 수 있습니다.
그런데 코랩 무료 T4 GPU는 메모리가 겨우 15GB입니다.
표준 방식으로 파인튜닝을 돌리면 세션이 뻗거나 몇 시간이 걸립니다.
Unsloth는 같은 결과를 내면서도 속도는 2~5배 빠르고, 메모리는 60% 이상 아낍니다.
코랩 무료 환경에서 현실적으로 파인튜닝을 완주하려면 Unsloth는 선택이 아니라 필수입니다.

**English**
Yesterday's libraries can technically do fine-tuning.
But Colab's free T4 GPU only has ~15GB of memory.
Standard fine-tuning often crashes the session or takes hours.
Unsloth achieves the same results — but 2~5x faster and using 60%+ less memory.
For anyone fine-tuning on free Colab, Unsloth isn't optional — it's essential.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 및 GPU 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. 기존 `cravveo_finetuning.ipynb` 열기 (구글 드라이브에 저장된 것)
3. 런타임 → 런타임 유형 변경 → T4 GPU 선택 확인
4. GPU 확인 코드 실행

설명: 코랩에 접속할 때마다 GPU가 잡혔는지 먼저 확인합니다. T4 GPU 이름과 메모리 정보가 나오면 정상입니다.
```python
!nvidia-smi
```

---

### Step 2 — Unsloth vs 기존 방식 비교 (개념 정리)

코드 실행 전에 먼저 아래 표를 노트북 텍스트 셀에 작성해서 이해합니다.

설명: Unsloth가 왜 특별한지 어제 설치한 도구들과 비교하면서 이해합니다. 이 표를 직접 타이핑해보면 개념이 훨씬 잘 잡힙니다.

| 항목 | 표준 방식 (PEFT + transformers) | Unsloth |
|------|--------------------------------|---------|
| 학습 속도 | 기준 | 2~5배 빠름 |
| GPU 메모리 사용량 | 기준 | 60~80% 절약 |
| 결과 품질 | 기준 | 동일 (손실 없음) |
| 설치 난이도 | 쉬움 | 약간 복잡 |
| 원리 | HuggingFace 기본 | 직접 최적화된 CUDA 커널 |
| 코랩 무료 플랜 적합성 | 아슬아슬 | 적합 |

---

### Step 3 — Unsloth 설치

설명: Unsloth는 CUDA(GPU 계산 엔진) 버전에 따라 설치 명령어가 달라집니다. 아래 코드를 실행하면 현재 코랩 환경을 확인한 뒤 자동으로 맞는 버전을 설치합니다. 설치 로그가 매우 길게 출력되는데 정상입니다. 끝까지 기다리세요.
⏱ 실행 시점: 코랩 세션이 끊기면 다시 설치해야 합니다. 접속할 때마다 이 셀부터 실행합니다.
```python
%%capture
!pip install unsloth
# 최신 nightly 버전 설치 (권장)
!pip uninstall unsloth -y && pip install --upgrade --no-cache-dir "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
```

설치 완료 확인:
설명: Unsloth가 정상적으로 설치됐는지 버전을 출력해서 확인합니다. 버전 숫자가 나오면 성공입니다.
```python
import unsloth
print("Unsloth version:", unsloth.__version__)
print("✅ Unsloth 설치 완료")
```

---

### Step 4 — FastLanguageModel로 모델 로드

설명: Unsloth의 핵심 도구인 `FastLanguageModel`을 사용해서 모델을 불러옵니다. 기존 `transformers`의 `AutoModelForCausalLM` 대신 이걸 씁니다. `load_in_4bit=True`는 모델을 4비트로 압축해서 불러오겠다는 뜻입니다. 약 2GB 모델이므로 다운로드에 2~3분 걸릴 수 있습니다.
⏱ 실행 시점: 세션 시작마다 실행해야 합니다. 코랩은 세션이 끊기면 모델도 사라집니다.
```python
from unsloth import FastLanguageModel
import torch

max_seq_length = 2048  # 한 번에 처리할 최대 글자 수 (토큰)
dtype = None           # 자동 감지 (T4는 Float16 자동 선택)
load_in_4bit = True    # 4비트 압축으로 메모리 절약

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gemma-2b-it",  # Gemma 2B 모델 (Unsloth 최적화 버전)
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)
print("✅ 모델 로드 성공")
```

---

### Step 5 — LoRA 어댑터 설정 (맛보기)

설명: 실제 파인튜닝에서 사용할 LoRA 어댑터 설정 코드입니다. 오늘은 설정만 하고 학습은 나중에 합니다. `r=16`은 LoRA의 핵심 수치(Rank)로, 숫자가 클수록 더 많이 학습하지만 메모리도 더 씁니다. 초보는 16으로 시작하면 됩니다.
⏱ 실행 시점: 모델 로드 셀 바로 다음에 실행합니다.
```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,                           # LoRA Rank — 16이 표준 시작값
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",  # 메모리 추가 절약
    random_state = 3407,
)
print("✅ LoRA 어댑터 설정 완료")
print("이제 파인튜닝 준비가 완전히 갖춰졌습니다.")
```

---

### Step 6 — 메모리 사용량 확인 (선택)

설명: 모델을 로드한 뒤 GPU 메모리가 얼마나 사용됐는지 확인합니다. 4비트 압축 덕분에 15GB 중 4~6GB 정도만 사용되면 정상입니다.
```python
gpu_stats = torch.cuda.get_device_properties(0)
start_gpu_memory = round(torch.cuda.max_memory_reserved() / 1024 / 1024 / 1024, 3)
max_memory = round(gpu_stats.total_memory / 1024 / 1024 / 1024, 3)
print(f"GPU: {gpu_stats.name}, 전체 메모리: {max_memory} GB")
print(f"현재 사용 중: {start_gpu_memory} GB")
print(f"남은 메모리: {round(max_memory - start_gpu_memory, 3)} GB")
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] Unsloth vs 표준 방식 비교표 이해 + 직접 정리
- [ ] Unsloth 설치 완료 — 버전 출력 확인
- [ ] FastLanguageModel로 gemma-2b-it 모델 로드 성공
- [ ] LoRA 어댑터 설정 코드 실행 완료
- [ ] (선택) GPU 메모리 사용량 출력 확인
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**Unsloth 설치 도중 에러가 뜰 때**
→ `%%capture`를 셀 맨 위에 붙이면 출력 없이 설치됩니다. 에러 없이 완료되면 정상.
→ 그래도 에러가 나면 런타임 재시작 후 다시 시도.

**모델 로드 중 메모리 부족 에러 (CUDA out of memory)**
→ T4 GPU 런타임이 맞는지 확인. CPU 런타임이면 모델을 못 올림.
→ 다른 탭에서 코랩을 열어두면 메모리 충돌 가능. 코랩 탭 하나만 열기.

**모델 다운로드가 너무 느릴 때**
→ 코랩 서버 상태에 따라 다를 수 있음. 그냥 기다리면 됩니다. 2~3분 정상.

**unsloth import 에러 (No module named 'unsloth')**
→ 설치 셀을 다시 실행하세요. 세션이 끊기면 설치가 초기화됩니다.

---

## 📅 다음 단계 예고 | Next Up

**Day 019** — JSONL 포맷 분석 — AI에게 먹일 데이터의 생김새
파인튜닝 학습 데이터는 JSONL이라는 특수한 형식으로 만들어야 합니다.
질문과 답변이 어떤 구조로 담겨야 하는지, 직접 메모장에 써보며 손에 익힙니다.

Day 019 — JSONL Format Deep Dive — What fine-tuning data looks like.
Training data must be written in JSONL format.
We'll learn the structure and write our first entries by hand.

---

[[2026-06-10_Day018_Work_Order|Day 018 작업지시서]] | [[Day018_YouTube_Upload|Day 018 유튜브]] | [[../17일차/2026-06-09_Day017_Work_Order|← Day 017]] | [[../Cravveo_100Day_Master_Guide]]

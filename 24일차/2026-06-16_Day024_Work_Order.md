# 📋 Day 024 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-16
> **단계** | Phase: Day 024 / 100

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
| 사용 모델 | Gemma 2B (Unsloth, 코랩 T4 GPU) |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019~021 | JSONL 포맷 분석 + 크라베오 데이터셋 제작 | ✅ 완료 |
| Day 022~023 | HuggingFace 업로드 + cron 자동화 파이프라인 | ✅ 완료 |
| **Day 024** | **파인튜닝 뼈대 코드 작성 — 모델 로드 + 데이터셋 연결** | 🔥 오늘 |
| Day 025~ | LoRA 설정 + SFTTrainer + 첫 학습 실행 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 데이터도 준비됐고, 모델도 있습니다.
> 오늘은 이 둘을 코랩 안에서 연결하는 뼈대 코드를 작성합니다.
> Unsloth로 모델을 불러오고, HuggingFace에서 데이터셋을 가져와서
> 두 개가 정상적으로 연결되는 것을 확인하는 것이 오늘 목표입니다.

**English**
> The data is ready. The model is ready.
> Today we write the skeleton code that connects both inside Colab.
> Load the model with Unsloth, load the dataset from HuggingFace,
> and confirm the two work together — that's today's goal.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
파인튜닝은 크게 세 단계입니다: 모델 로드 → 데이터 연결 → 학습 실행.
오늘은 첫 번째와 두 번째 단계를 완성합니다.
이 뼈대 코드가 완성되면 내일 LoRA 설정과 SFTTrainer만 붙이면 실제 학습이 돌아갑니다.
전체 파인튜닝 중에서 가장 중요한 골격을 오늘 세웁니다.

**English**
Fine-tuning has three main steps: load model → connect data → run training.
Today we complete steps one and two.
Once this skeleton is done, adding LoRA config and SFTTrainer tomorrow starts the actual training.
Today we build the most critical skeleton of the entire fine-tuning pipeline.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 & 환경 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. `cravveo_finetuning.ipynb` 열기
3. 런타임 → T4 GPU 확인

```python
!nvidia-smi
```

---

### Step 2 — Unsloth 설치

설명: 코랩 세션이 새로 시작될 때마다 설치가 필요합니다.

```python
%%capture
!pip install unsloth
!pip install --upgrade "torchvision>=0.27.0"
```

```python
import unsloth
print("Unsloth version:", unsloth.__version__)
print("✅ Unsloth 준비 완료")
```

---

### Step 3 — Unsloth로 모델 로드

설명: `FastLanguageModel`을 사용해 Gemma 2B를 4비트 양자화로 불러옵니다.
4비트 양자화를 쓰면 메모리를 60% 절약하면서도 성능 저하가 거의 없습니다.

```python
from unsloth import FastLanguageModel

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/gemma-2-2b-it",
    max_seq_length = 2048,
    dtype = None,
    load_in_4bit = True,
)

print("✅ 모델 로드 완료")
print(f"모델: {model.__class__.__name__}")
```

---

### Step 4 — HuggingFace에서 데이터셋 불러오기

설명: 어제 올린 내 데이터셋을 코드 한 줄로 가져옵니다.

```python
from datasets import load_dataset

dataset = load_dataset("cravveo/cravveo-briefing-dataset", split="train")

print(f"✅ 데이터셋 로드 완료")
print(f"데이터 수: {len(dataset)}개")
print(f"컬럼: {dataset.column_names}")
print()
print("--- 첫 번째 데이터 미리보기 ---")
print("instruction:", dataset[0]['instruction'][:80])
print("output:", dataset[0]['output'][:80])
```

---

### Step 5 — 프롬프트 포맷 정의

설명: 모델이 학습할 수 있는 형태로 데이터를 변환합니다.
Instruction + Output을 하나의 텍스트로 이어붙이는 포맷입니다.

```python
def formatting_prompts_func(examples):
    instructions = examples["instruction"]
    outputs = examples["output"]
    texts = []
    for instruction, output in zip(instructions, outputs):
        text = f"### 질문:\n{instruction}\n\n### 답변:\n{output}"
        texts.append(text)
    return {"text": texts}

dataset = dataset.map(formatting_prompts_func, batched=True)

print("✅ 프롬프트 포맷 변환 완료")
print()
print("--- 변환된 첫 번째 데이터 ---")
print(dataset[0]['text'][:300])
```

---

### Step 6 — 모델 + 데이터셋 연결 확인

설명: 토크나이저로 데이터를 실제로 처리해서 모델이 읽을 수 있는지 확인합니다.

```python
sample = tokenizer(
    dataset[0]['text'],
    truncation=True,
    max_length=512,
    return_tensors="pt"
)

print("✅ 토크나이저 처리 완료")
print(f"토큰 수: {sample['input_ids'].shape[1]}개")
print("모델 + 데이터셋 연결 성공!")
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] Unsloth 설치 완료
- [ ] `FastLanguageModel.from_pretrained()` 모델 로드 성공
- [ ] `load_dataset("cravveo/cravveo-briefing-dataset")` 데이터 로드 성공
- [ ] 데이터 개수 및 컬럼 확인
- [ ] 프롬프트 포맷 변환 완료
- [ ] 토크나이저 처리 성공 (토큰 수 출력)
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**모델 로드 중 OOM(메모리 부족) 오류**
→ 런타임 → 런타임 유형 변경 → T4 GPU 재확인
→ `load_in_4bit=True` 가 설정되어 있는지 확인

**`Repository not found` (데이터셋 로드 실패)**
→ HuggingFace 로그인이 필요할 수 있습니다:
```python
from google.colab import userdata
from huggingface_hub import login
login(token=userdata.get('HF_TOKEN'))
```
그 후 `load_dataset()` 재실행

**`unsloth/gemma-2-2b-it` 모델을 찾을 수 없을 때**
→ 모델명 확인: `unsloth/gemma-2b-it` 또는 `unsloth/gemma-2-2b` 로 변경 시도

**프롬프트 변환 후 텍스트가 비어있을 때**
→ 컬럼명 확인: `dataset.column_names` 출력 후 `instruction`, `output` 컬럼 존재 여부 확인

---

## 📅 다음 단계 예고 | Next Up

**Day 025** — LoRA 설정 + SFTTrainer + 첫 학습 실행
뼈대가 완성됐습니다. 다음은 LoRA 어댑터를 붙이고 SFTTrainer로 실제 학습을 돌립니다.
학습 loss가 줄어드는 것을 처음으로 눈으로 확인합니다.

Day 025 — LoRA Config + SFTTrainer + First Training Run
The skeleton is ready. Next: attach the LoRA adapter, set up SFTTrainer, and run the first actual training.
We'll see the training loss drop for the first time.

---

[[2026-06-16_Day024_Work_Order|Day 024 작업지시서]] | [[../23일차/2026-06-15_Day023_Work_Order|← Day 023]] | [[../Cravveo_100Day_Master_Guide]]

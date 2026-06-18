# 📋 Day 025 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-17
> **단계** | Phase: Day 025 / 100

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
| 사용 모델 | Gemma 2B (Unsloth + LoRA, 코랩 T4 GPU) |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019~023 | 데이터셋 제작 + HuggingFace 업로드 + cron 자동화 | ✅ 완료 |
| Day 024 | 파인튜닝 뼈대 코드 — 모델 + 데이터 연결 | ✅ 완료 |
| **Day 025** | **LoRA 설정 + SFTTrainer + 첫 학습 실행 — loss 확인** | 🔥 오늘 |
| Day 026~ | 학습 결과 확인 + 가중치 저장 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 뼈대가 완성됐습니다. 오늘 드디어 실제 학습을 돌립니다.
> LoRA 어댑터를 모델에 붙이고, SFTTrainer로 학습을 시작합니다.
> loss 숫자가 줄어드는 걸 처음으로 눈으로 확인하는 것이 오늘 목표입니다.

**English**
> The skeleton is ready. Today we finally run the actual training.
> Attach the LoRA adapter to the model, then launch training with SFTTrainer.
> Today's goal: watch the loss number drop for the very first time.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
LoRA는 전체 모델을 다시 학습시키지 않고, 작은 어댑터 레이어만 학습시키는 기술입니다.
덕분에 T4 GPU처럼 작은 환경에서도 대형 모델을 파인튜닝할 수 있습니다.
SFTTrainer는 이 LoRA 학습을 쉽게 돌려주는 도구입니다.
오늘 loss가 줄어드는 것을 확인하면 "AI가 내 데이터를 학습하기 시작했다"는 증거가 됩니다.

**English**
LoRA fine-tunes only small adapter layers instead of retraining the whole model.
This makes it possible to fine-tune large models even on a small GPU like T4.
SFTTrainer is the tool that runs this LoRA training easily.
When we see loss drop today, it's proof that "the AI has started learning from my data."

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 & 어제 뼈대 코드 실행

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. `cravveo_finetuning.ipynb` 열기
3. 런타임 → T4 GPU 확인
4. **어제 완성한 셀들을 순서대로 먼저 실행** (Unsloth 설치 → 모델 로드 → 데이터셋 로드 → 프롬프트 변환)

---

### Step 2 — LoRA 어댑터 설정

설명: 모델 전체 대신 작은 LoRA 레이어만 학습시키도록 설정합니다.
`r`은 LoRA의 rank(크기)입니다. 작을수록 빠르고 메모리를 적게 씁니다.

```python
model = FastLanguageModel.get_peft_model(
    model,
    r = 16,
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = "unsloth",
    random_state = 42,
)

print("✅ LoRA 어댑터 설정 완료")
print(f"학습 파라미터 수: {sum(p.numel() for p in model.parameters() if p.requires_grad):,}개")
```

---

### Step 3 — SFTTrainer 설정

설명: 학습을 실제로 돌리는 Trainer를 설정합니다.
`max_steps=30`으로 짧게 테스트합니다. 학습이 돌아가는지 확인하는 것이 목표입니다.

```python
from trl import SFTTrainer
from transformers import TrainingArguments

trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = 2048,
    args = TrainingArguments(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 30,
        learning_rate = 2e-4,
        fp16 = True,
        logging_steps = 1,
        output_dir = "outputs",
        optim = "adamw_8bit",
        seed = 42,
    ),
)

print("✅ SFTTrainer 설정 완료")
```

---

### Step 4 — 첫 학습 실행

설명: 드디어 학습을 시작합니다. 30스텝 동안 loss가 줄어드는 걸 확인합니다.
T4 GPU에서 약 3~5분 걸립니다.

```python
print("🚀 학습 시작!")
trainer_stats = trainer.train()
print("✅ 학습 완료!")
print(f"총 학습 시간: {trainer_stats.metrics['train_runtime']:.1f}초")
print(f"최종 loss: {trainer_stats.metrics['train_loss']:.4f}")
```

---

### Step 5 — loss 확인

설명: 학습 로그에서 loss가 줄어드는 패턴을 확인합니다.

```python
# 학습 중 출력된 로그에서 Step 1과 Step 30의 loss 비교
# Step 1:  loss ≈ 2.xx ~ 3.xx (높음)
# Step 30: loss ≈ 1.xx ~ 2.xx (줄어들었으면 성공)
print("loss가 줄어들었다면 AI가 내 데이터를 학습하기 시작한 것입니다.")
```

---

## ✅ 성공 조건 체크리스트

- [ ] 어제 뼈대 코드 정상 실행 확인
- [ ] `get_peft_model()` LoRA 어댑터 설정 완료
- [ ] 학습 파라미터 수 출력 확인
- [ ] `SFTTrainer` 설정 완료 (오류 없음)
- [ ] `trainer.train()` 실행 → 30스텝 완료
- [ ] Step 1 대비 Step 30에서 loss 감소 확인
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`ImportError: trl` 없음**
```python
!pip install trl
```

**OOM (Out of Memory) — 메모리 부족**
→ 런타임 → 런타임 연결 해제 및 삭제 → 다시 연결 (GPU 메모리 초기화)
→ `per_device_train_batch_size = 1` 확인
→ `max_steps`를 10으로 줄여서 테스트

**loss가 전혀 줄어들지 않을 때**
→ `learning_rate = 2e-4` 확인
→ 데이터셋 `text` 컬럼이 제대로 생성됐는지 확인: `print(dataset[0]['text'][:200])`

**`dataset_text_field = "text"` 오류**
→ 프롬프트 변환 셀을 먼저 실행했는지 확인
→ `print(dataset.column_names)` 로 `text` 컬럼 존재 확인

---

## 📅 다음 단계 예고 | Next Up

**Day 026** — LoRA 가중치 저장 + 학습 결과 확인
첫 학습이 끝났습니다. 다음은 학습된 LoRA 가중치를 저장하고,
파인튜닝된 모델이 실제로 다르게 답하는지 테스트합니다.

Day 026 — Save LoRA Weights + Test the Fine-tuned Model
First training is done. Next: save the LoRA weights and test whether
the fine-tuned model actually responds differently from the base model.

---

[[2026-06-17_Day025_Work_Order|Day 025 작업지시서]] | [[../24일차/2026-06-16_Day024_Work_Order|← Day 024]] | [[../Cravveo_100Day_Master_Guide]]

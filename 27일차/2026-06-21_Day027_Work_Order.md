# 📋 Day 027 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-21
> **단계** | Phase: Day 027 / 100

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
| 사용 모델 | Llama 3.2 1B Instruct (Unsloth + LoRA, 코랩 T4 GPU) |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019~023 | 데이터셋 제작 + HuggingFace 업로드 + cron 자동화 | ✅ 완료 |
| Day 024~025 | 파인튜닝 뼈대 코드 + 첫 학습 실행 | ✅ 완료 |
| Day 026 | Gemma→Llama 3.2 모델 교체 — loss 정상화 | ✅ 완료 |
| **Day 027** | **데이터 확장 + Before/After 비교 테스트** | 🔥 오늘 |
| Day 028~ | 가중치 저장 + 모델 배포 준비 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 026에서 파인튜닝 파이프라인이 정상 작동하는 걸 확인했습니다.
> 하지만 데이터 29개로는 모델이 크라베오를 "모릅니다."
> 오늘은 크라베오 전용 데이터를 대폭 확장하고, 학습량을 늘려서
> "학습 전 모델"과 "학습 후 모델"의 답변 차이를 눈으로 확인합니다.

**English**
> Day 026 confirmed the fine-tuning pipeline works.
> But with only 29 entries, the model doesn't "know" Cravveo yet.
> Today we massively expand the Cravveo dataset, increase training,
> and visually compare "before training" vs "after training" responses.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
Day 026에서 모델에게 "크라베오가 뭐야?"라고 물었더니 엉뚱한 답을 했습니다.
이유: 데이터 29개, 3 epoch으로는 모델의 행동을 바꾸기에 부족합니다.
파인튜닝의 진짜 목표는 "내 데이터를 학습한 AI가 다르게 답하는 것"입니다.
오늘 그걸 눈으로 확인하면 "파인튜닝이 실제로 효과가 있다"는 증거가 됩니다.

**English**
In Day 026, the model gave random answers about Cravveo.
Reason: 29 entries with 3 epochs isn't enough to change model behavior.
The real goal of fine-tuning is "an AI that responds differently after learning my data."
Seeing that difference today proves fine-tuning actually works.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 크라베오 데이터셋 확장 (로컬)

현재 깨끗한 데이터: 29개. 목표: **100개 이상**.
크라베오에 대한 질문/답변을 직접 작성합니다.

카테고리별로 나눠서 만들기:
- **크라베오 소개** (10개): 회사 소개, 목표, 운영자, 사업 분야
- **100일 프로젝트** (10개): 프로젝트 목적, 진행 상황, 사용 도구
- **기술 스택** (10개): Unsloth, LoRA, Colab, HuggingFace, Ollama
- **일상/철학** (10개): 하루 일과, 1인 기업 이유, Build in Public
- **파인튜닝 과정** (10개): Day별 기록, 에러 경험, 교훈

총 50개 추가 → 기존 29개 + 50개 = **79개**

---

### Step 2 — HuggingFace 데이터셋 업데이트

확장된 데이터셋을 HuggingFace에 업로드합니다.

---

### Step 3 — 코랩에서 Before 테스트 (학습 전)

학습하기 전에 먼저 기본 모델에게 질문해서 답변을 기록합니다.

```python
# Before — 학습 전 모델 테스트
FastLanguageModel.for_inference(model)

test_questions = [
    "질문: 크라베오 컴퍼니가 뭐야?\n답변:",
    "질문: 크라베오의 목표가 뭐야?\n답변:",
    "질문: Build in Public이 뭐야?\n답변:",
    "질문: 파인튜닝을 왜 배우고 있어?\n답변:",
]

print("📋 학습 전 모델 답변")
for q in test_questions:
    inputs = tokenizer(q, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    print("-" * 50)
```

---

### Step 4 — 확장 데이터로 학습 실행

```python
# 설정: 데이터 79개, 10 epoch, learning_rate 2e-5
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset,
    dataset_text_field = "text",
    max_seq_length = 512,
    args = TrainingArguments(
        per_device_train_batch_size = 1,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        num_train_epochs = 10,
        learning_rate = 2e-5,
        fp16 = True,
        logging_steps = 5,
        output_dir = "outputs",
        optim = "adamw_8bit",
        seed = 42,
        save_strategy = "no",
    ),
)
```

---

### Step 5 — After 테스트 (학습 후)

같은 질문으로 학습 후 모델을 테스트하고, Before와 비교합니다.

```python
# After — 학습 후 모델 테스트
FastLanguageModel.for_inference(model)

print("📋 학습 후 모델 답변")
for q in test_questions:
    inputs = tokenizer(q, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))
    print("-" * 50)
```

---

## ✅ 성공 조건 체크리스트

- [ ] 크라베오 데이터 50개 이상 추가 작성
- [ ] HuggingFace 데이터셋 업데이트
- [ ] Before 테스트 (학습 전 답변 기록)
- [ ] 확장 데이터로 학습 완료 (loss 감소 확인)
- [ ] After 테스트 (학습 후 답변 기록)
- [ ] **Before vs After 답변이 눈에 띄게 다른지 확인** ← 핵심
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**학습 후에도 답변이 비슷할 때**
→ `num_train_epochs`를 15~20으로 늘려보기
→ `learning_rate`를 5e-5로 올려보기
→ 데이터 양이 부족할 수 있음 — 더 추가

**OOM (메모리 부족)**
→ `max_seq_length = 256`으로 줄이기
→ `gradient_accumulation_steps = 8`로 올리기

**loss가 0.0으로 떨어질 때**
→ 과적합. `num_train_epochs`를 줄이거나 `learning_rate`를 낮추기

---

## 📅 다음 단계 예고 | Next Up

**Day 028** — LoRA 가중치 저장 + 모델 내보내기
학습된 모델의 가중치를 저장하고, 나중에 다시 불러올 수 있게 합니다.

Day 028 — Save LoRA Weights + Export Model
Save the trained model weights so we can reload them later.

---

[[2026-06-21_Day027_Work_Order|Day 027 작업지시서]] | [[../26일차/2026-06-20_Day026_Work_Order|← Day 026]] | [[../Cravveo_100Day_Master_Guide]]

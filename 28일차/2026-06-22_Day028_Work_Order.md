# 📋 Day 028 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-22
> **단계** | Phase: Day 028 / 100

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
| Day 016~025 | 코랩 + Unsloth + 데이터셋 + 첫 학습 | ✅ 완료 |
| Day 026 | Gemma→Llama 3.2 모델 교체 — loss 정상화 | ✅ 완료 |
| Day 027 | 데이터 83개 확장 + Before/After — 파인튜닝 효과 확인 | ✅ 완료 |
| **Day 028** | **LoRA 가중치 저장 + HuggingFace 업로드 + 모델 재로드 테스트** | ✅ 오늘 |
| Day 029~ | GGUF 변환 + 로컬 Ollama 배포 준비 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 027에서 AI가 크라베오를 정확히 답하는 걸 확인했습니다.
> 하지만 코랩 세션이 끝나면 학습된 모델이 사라집니다.
> 오늘은 학습된 LoRA 가중치를 저장하고, HuggingFace에 업로드하고,
> 다시 불러와서 제대로 작동하는지 확인합니다.
> "학습 → 저장 → 불러오기"가 되면 파인튜닝 파이프라인이 완성됩니다.

**English**
> Day 027 confirmed the AI answers Cravveo correctly.
> But when the Colab session ends, the trained model disappears.
> Today we save the LoRA weights, upload to HuggingFace,
> and reload to verify everything works.
> "Train → Save → Reload" completes the fine-tuning pipeline.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
지금까지 학습한 모델은 코랩 메모리에만 있습니다.
코랩 세션이 끝나거나 런타임이 초기화되면 전부 사라집니다.
LoRA 가중치를 저장해두면 언제든 다시 불러와서 쓸 수 있습니다.
HuggingFace에 올려놓으면 어디서든 접근할 수 있습니다.

**English**
The trained model currently lives only in Colab's memory.
When the session ends, everything disappears.
Saving LoRA weights lets us reload the model anytime.
Uploading to HuggingFace makes it accessible from anywhere.

---

## 🔢 코랩 셀 실행 순서 (매우 중요!)

> ⚠️ 노트북에 셀이 40개 있지만, 실제로 실행할 셀은 아래 목록뿐입니다.
> 목록에 없는 셀은 전부 건너뛰세요!

### Phase 1 — 라이브러리 설치

| 순서 | 셀 이름 | 할 일 | 건너뛸 셀 |
|------|--------|------|----------|
| 1 | 셀 1 | GPU 확인 | |
| 2 | 셀 2 | Unsloth 설치 | |
| 3 | 셀 3 | Unsloth 확인 | |
| 4 | 셀 4 | 라이브러리 설치 | |
| 5 | 셀 5 | huggingface_hub 설치 | |
| 6 | 셀 6 | 버전 확인 | |
| 7 | ⚠️ **런타임 재시작** | 상단 → 런타임 → 런타임 재시작 | |

### Phase 2 — 모델 로드 + 학습

| 순서 | 셀 이름 | 할 일 | 건너뛸 셀 |
|------|--------|------|----------|
| 8 | 셀 6.5 | CUDA 수정 | |
| 9 | 셀 7 | Llama 3.2 모델 로드 | |
| 10 | 셀 8 | LoRA 어댑터 설정 | 디버그 테스트 ← 건너뜀 |
| 11 | 셀 17 | HuggingFace 로그인 | 셀 9~16 전부 건너뜀 |
| 12 | 셀 18 | 로그인 확인 | |
| 13 | **셀 8.5** | **Before → 학습(30epoch) → After** | 셀 18.5~24 전부 건너뜀 |
| | | ⚠️ **After 답변이 정확한지 반드시 확인!** | |

### Phase 3 — 저장 + 업로드

| 순서 | 셀 이름 | 할 일 | 건너뛸 셀 |
|------|--------|------|----------|
| 14 | Step 2 | LoRA 가중치 저장 | 셀 23 (loss 비교) ← 건너뜀 |
| 15 | Step 3 | HuggingFace 업로드 | |
| | | ⚠️ **업로드 완료 확인 후 다음으로** | |

### Phase 4 — 재로드 테스트

| 순서 | 셀 이름 | 할 일 |
|------|--------|------|
| 16 | ⚠️ **런타임 재시작** | |
| 17 | 셀 2~7 | 라이브러리 재설치 |
| 18 | ⚠️ **런타임 재시작** | |
| 19 | Step 4 (수정버전) | 기본 모델 + LoRA 어댑터 따로 로드 → 테스트 |
| | | ⚠️ **크라베오 답변이 정확하면 성공!** |

### Step 4 수정 코드 (재로드 시 반드시 이 방식 사용)

```python
# Step 4 수정 — 기본 모델 + LoRA 어댑터 따로 로드
from unsloth import FastLanguageModel
from peft import PeftModel

# 1. 기본 모델 먼저 로드
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-1B-Instruct",
    max_seq_length = 512,
    dtype = None,
    load_in_4bit = True,
)

# 2. LoRA 어댑터 따로 붙이기 (HuggingFace에서 다운로드)
model = PeftModel.from_pretrained(model, "cravveo/cravveo-llama-lora")
FastLanguageModel.for_inference(model)

# 3. 테스트
test_questions = [
    "질문: 크라베오 컴퍼니가 뭐야?\n답변:",
    "질문: 크라베오의 목표가 뭐야?\n답변:",
    "질문: Build in Public이 뭐야?\n답변:",
]

print("✅ 기본 모델 + LoRA 어댑터 로드 완료")
print("=" * 50)
for q in test_questions:
    inputs = tokenizer(q, return_tensors="pt").to("cuda")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.7, do_sample=True)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print()
    print(answer)
    print("-" * 50)
```

> **주의**: `FastLanguageModel.from_pretrained("cravveo/cravveo-llama-lora")`로 직접 로드하면
> LoRA 어댑터가 적용되지 않습니다. 반드시 기본 모델을 먼저 로드한 후
> `PeftModel.from_pretrained()`으로 어댑터를 따로 붙여야 합니다.

---

## ✅ 단계별 실행 코드 | Step-by-Step Code

### Step 2 — LoRA 가중치 저장

```python
# LoRA 가중치를 코랩 로컬에 저장
model.save_pretrained("cravveo-lora-adapter")
tokenizer.save_pretrained("cravveo-lora-adapter")
print("✅ LoRA 가중치 저장 완료 — cravveo-lora-adapter/")

# 저장된 파일 확인
import os
for f in os.listdir("cravveo-lora-adapter"):
    size = os.path.getsize(f"cravveo-lora-adapter/{f}") / 1024
    print(f"  {f} ({size:.1f} KB)")
```

### Step 3 — HuggingFace에 모델 업로드

```python
# HuggingFace에 LoRA 어댑터 업로드
from google.colab import userdata
model.push_to_hub("cravveo/cravveo-llama-lora", token=userdata.get('HF_TOKEN'))
tokenizer.push_to_hub("cravveo/cravveo-llama-lora", token=userdata.get('HF_TOKEN'))
print("✅ HuggingFace 업로드 완료 — cravveo/cravveo-llama-lora")
```

---

## ✅ 성공 조건 체크리스트

- [x] Day 027 학습 재실행 (loss 0.08 확인)
- [x] After 답변 정확한지 확인 (크라베오 = 1인 기업)
- [x] `model.save_pretrained()` LoRA 가중치 저장
- [x] `model.push_to_hub()` HuggingFace 업로드
- [x] 런타임 재시작 후 HuggingFace에서 모델 재로드
- [x] **재로드한 모델이 "크라베오가 뭐야?"에 정확히 답하는지 확인** ← 핵심
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`push_to_hub` 권한 오류**
→ HuggingFace 토큰에 write 권한이 있는지 확인
→ 코랩 Secrets에서 HF_TOKEN 값 확인

**재로드 후 답변이 엉뚱할 때**
→ `FastLanguageModel.from_pretrained("cravveo/cravveo-llama-lora")`로 직접 로드하면 안 됨!
→ 반드시 기본 모델 로드 → `PeftModel.from_pretrained()`으로 어댑터 따로 붙이기
→ 학습 안 된 상태에서 save/upload 했을 가능성 → 다시 학습 후 save/upload

**저장 용량 부족**
→ LoRA 어댑터는 보통 50~200MB 정도로 작음 (전체 모델 대비 1~5%)

**셀 순서가 헷갈릴 때**
→ 위의 "코랩 셀 실행 순서" 표를 따라가세요
→ 핵심: 셀 1~8 → 셀 17~18 → 셀 8.5 → Step 2 → Step 3 → 재시작 → Step 4

---

## 📅 다음 단계 예고 | Next Up

**Day 029** — GGUF 변환 + Ollama 등록 준비
HuggingFace에 저장된 모델을 GGUF 포맷으로 변환하고,
로컬 Ollama에서 돌릴 수 있게 준비합니다.

Day 029 — GGUF Conversion + Ollama Deployment Prep
Convert the HuggingFace model to GGUF format
and prepare to run it locally with Ollama.

---

[[2026-06-22_Day028_Work_Order|Day 028 작업지시서]] | [[../27일차/2026-06-21_Day027_Work_Order|← Day 027]] | [[../Cravveo_100Day_Master_Guide]]

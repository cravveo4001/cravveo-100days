# 📋 Day 029 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-23
> **단계** | Phase: Day 029 / 100

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
| 작업 환경 | Google Colab (T4 GPU) + 로컬 Linux |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~025 | 코랩 + Unsloth + 데이터셋 + 첫 학습 | ✅ 완료 |
| Day 026 | Gemma→Llama 3.2 모델 교체 — loss 정상화 | ✅ 완료 |
| Day 027 | 데이터 83개 확장 + Before/After — 파인튜닝 효과 확인 | ✅ 완료 |
| Day 028 | LoRA 가중치 저장 + HuggingFace 업로드 + 재로드 성공 | ✅ 완료 |
| **Day 029** | **GGUF 변환 + 로컬 Ollama에 내 AI 등록** | 🔥 오늘 |
| Day 030~ | Ollama + AnythingLLM 연결 / 로컬 RAG 통합 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 028에서 파인튜닝 파이프라인이 완성됐습니다.
> 하지만 아직 코랩(클라우드)에서만 돌아갑니다.
> 오늘은 학습된 모델을 GGUF 포맷으로 변환하고,
> 내 노트북의 Ollama에 등록해서 로컬에서 돌려봅니다.
> "내 컴퓨터에서 크라베오를 아는 AI가 돌아간다" — 이게 오늘 목표입니다.

**English**
> Day 028 completed the fine-tuning pipeline.
> But it only runs on Colab (cloud).
> Today we convert the model to GGUF format,
> register it with Ollama on my local machine, and run it locally.
> "An AI that knows Cravveo runs on my own computer" — that's today's goal.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
코랩은 세션 시간 제한이 있고, GPU 할당이 불안정합니다.
내 노트북에서 돌리면 인터넷 없이도, 시간 제한 없이도 AI를 쓸 수 있습니다.
GGUF는 로컬 LLM 실행에 최적화된 포맷이고, Ollama는 GGUF 모델을 쉽게 돌려주는 도구입니다.
Day 004에서 설치한 Ollama에 내가 파인튜닝한 모델을 등록하는 것 — Phase 1과 Phase 2가 합쳐지는 순간입니다.

**English**
Colab has session limits and unstable GPU allocation.
Running locally means no internet needed, no time limits.
GGUF is optimized for local LLM execution, and Ollama makes it easy to run GGUF models.
Registering my fine-tuned model in Ollama (installed on Day 004) — this is where Phase 1 meets Phase 2.

---

## 🔢 코랩 셀 실행 순서

### Phase 1 — 라이브러리 설치

| 순서 | 셀 | 할 일 |
|------|-----|------|
| 1 | 셀 1~6 | GPU 확인 + 라이브러리 설치 |
| 2 | ⚠️ **런타임 재시작** | |

### Phase 2 — 모델 로드 + 학습 + GGUF 변환

| 순서 | 셀 | 할 일 | 건너뛸 셀 |
|------|-----|------|----------|
| 3 | 셀 6.5 | CUDA 수정 | |
| 4 | 셀 7 | Llama 3.2 모델 로드 | |
| 5 | 셀 8 | LoRA 어댑터 설정 | |
| 6 | 셀 17 | HuggingFace 로그인 | 셀 9~16 건너뜀 |
| 7 | 셀 18 | 로그인 확인 | |
| 8 | **셀 8.5** | **Before → 학습(30epoch) → After** | 셀 18.5~24 건너뜀 |
| 9 | **GGUF 변환 셀** | **아래 Step 2 코드 실행** | |

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩에서 학습 실행 (Day 027 반복)

셀 실행 순서표대로 학습까지 실행합니다. After 답변이 정확한지 확인!

---

### Step 2 — GGUF 포맷으로 변환 + 저장 (코랩에서 실행)

```python
# GGUF 변환 — 16비트로 저장
model.save_pretrained_gguf(
    "cravveo-gguf",
    tokenizer,
    quantization_method = "q4_k_m",
)
print("✅ GGUF 변환 완료 — cravveo-gguf/")

# 파일 확인
import os
for f in os.listdir("cravveo-gguf"):
    size = os.path.getsize(f"cravveo-gguf/{f}") / (1024*1024)
    print(f"  {f} ({size:.1f} MB)")
```

> `q4_k_m`: 4비트 양자화. 용량 작고 속도 빠름. 로컬 CPU에서 돌리기 적합.

---

### Step 3 — GGUF 파일 다운로드

코랩 왼쪽 파일 탭 → `cravveo-gguf/` 폴더 → `.gguf` 파일 우클릭 → 다운로드
(또는 코드로 다운로드)

```python
# Google Drive에 저장하는 방법
from google.colab import drive
drive.mount('/content/drive')

import shutil
shutil.copy("cravveo-gguf/unsloth.Q4_K_M.gguf", "/content/drive/MyDrive/cravveo-model.gguf")
print("✅ Google Drive에 저장 완료")
```

---

### Step 4 — 로컬에서 Ollama에 모델 등록

GGUF 파일을 로컬 노트북으로 가져온 후:

```bash
# 1. Modelfile 생성
cat > Modelfile << 'EOF'
FROM ./cravveo-model.gguf

PARAMETER temperature 0.7
PARAMETER num_predict 200

SYSTEM "너는 크라베오 컴퍼니의 AI 어시스턴트야. 크라베오에 대한 질문에 정확하게 답해줘."
EOF

# 2. Ollama에 모델 등록
ollama create cravveo -f Modelfile

# 3. 테스트
ollama run cravveo "크라베오 컴퍼니가 뭐야?"
```

---

### Step 5 — 로컬 테스트

```bash
# 크라베오 AI에게 질문
ollama run cravveo "크라베오의 목표가 뭐야?"
ollama run cravveo "Build in Public이 뭐야?"
ollama run cravveo "파인튜닝을 왜 배우고 있어?"
```

정확한 답변이 나오면 **내 컴퓨터에서 크라베오 AI가 돌아가는 것**!

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩에서 학습 완료 (After 답변 정확)
- [ ] GGUF 변환 완료 (q4_k_m)
- [ ] GGUF 파일 로컬로 다운로드
- [ ] Modelfile 생성
- [ ] `ollama create cravveo` 등록 완료
- [ ] **`ollama run cravveo "크라베오가 뭐야?"` → 정확한 답변** ← 핵심
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`save_pretrained_gguf` 오류**
→ Unsloth 최신 버전 확인: `!pip install --upgrade unsloth`
→ `quantization_method`를 `"q8_0"` 또는 `"f16"`으로 변경 시도

**GGUF 파일이 너무 클 때**
→ `q4_k_m` (약 700MB) 대신 `q4_0` (약 500MB) 시도
→ 1B 모델이라 보통 1GB 이하

**Ollama create 실패**
→ Ollama 최신 버전 확인: `ollama --version`
→ Modelfile 경로와 GGUF 파일 경로가 같은 폴더에 있는지 확인

**로컬에서 답변이 엉뚱할 때**
→ GGUF 변환이 학습된 모델에서 됐는지 확인 (학습 → After 확인 → 그 다음 변환)
→ `quantization_method`를 `"f16"` (무손실)로 변경해서 재변환

---

## 📅 다음 단계 예고 | Next Up

**Day 030** — Phase 2 회고 + Phase 3 계획
Day 016~029까지의 파인튜닝 여정을 돌아보고,
Phase 3 (Ollama + AnythingLLM + 자동화 연결)를 계획합니다.

Day 030 — Phase 2 Retrospective + Phase 3 Planning
Review the fine-tuning journey from Day 016~029,
and plan Phase 3 (Ollama + AnythingLLM + automation integration).

---

[[2026-06-23_Day029_Work_Order|Day 029 작업지시서]] | [[../28일차/2026-06-22_Day028_Work_Order|← Day 028]] | [[../Cravveo_100Day_Master_Guide]]

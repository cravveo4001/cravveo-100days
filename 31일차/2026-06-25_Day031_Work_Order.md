# 📋 Day 031 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-25
> **단계** | Phase: Day 031 / 100 — Phase 3 시작!

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
| 사용 모델 | Llama 3.2 1B / 3B Instruct (Unsloth + LoRA, 코랩 T4 GPU) |
| 작업 환경 | Google Colab (T4 GPU) + 로컬 Ollama |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기 | Roadmap

| 단계 | Phase | 내용 | Content | 상태 |
|------|-------|------|---------|------|
| Day 001~015 | Phase 1 | 환경 구축 + RAG | Environment + RAG | ✅ 완료 |
| Day 016~029 | Phase 2 | 파인튜닝 + 로컬 배포 | Fine-tuning + local deploy | ✅ 완료 |
| Day 030 | 회고 | Phase 2 회고 + Phase 3 계획 | Retrospective + planning | ✅ 완료 |
| **Day 031** | **Phase 3** | **답변 품질 개선 — 데이터 확장 + 3B 모델** | **Quality improvement** | 🔥 오늘 |
| Day 032~ | Phase 3 | Ollama + AnythingLLM RAG 통합 | RAG integration | ⏳ 예정 |
| Day 100 | 목표 | 1인 기업 자동화 시스템 완성 | Automation complete | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 029에서 로컬 Ollama에 크라베오 AI를 등록했지만, 답변 품질이 부족했습니다.
> "한국의 IT 기업이야"까지는 맞지만 텍스트가 깨지고 언어가 섞였습니다.
> 오늘은 두 가지를 개선합니다:
> 1. 데이터를 83개에서 200개로 확장
> 2. 1B 모델 대신 3B 모델로 업그레이드
> 그리고 다시 GGUF 변환 + Ollama 등록까지 해서 품질 차이를 확인합니다.

**English**
> Day 029's local Ollama answers were partially correct but garbled.
> Today we improve quality with two changes:
> 1. Expand dataset from 83 to 200 entries
> 2. Upgrade from 1B to 3B model
> Then GGUF convert + Ollama register again to compare quality.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
Day 029 로컬 테스트에서 텍스트가 깨지고 러시아어/베트남어가 섞인 이유:
1. 1B 모델은 파라미터가 적어서 한국어 생성 능력이 약함
2. 83개 데이터로는 모델이 충분히 학습하지 못함
3. 4비트 양자화로 추가 품질 손실

3B 모델은 파라미터가 3배 많아서 한국어 생성이 더 자연스럽고,
데이터를 200개로 늘리면 더 다양한 질문에 정확히 답할 수 있습니다.

**English**
Day 029 local test had garbled text and mixed languages because:
1. 1B model has limited Korean generation ability
2. 83 entries wasn't enough training data
3. 4-bit quantization added quality loss

3B model has 3x more parameters for better Korean generation,
and 200 entries covers more diverse questions.

---

## 🔢 코랩 셀 실행 순서 | Colab Cell Order

### Phase 1 — 라이브러리 설치 | Library Install

| 순서 | 셀 | 할 일 |
|------|-----|------|
| 1 | 셀 1~6 | GPU 확인 + 라이브러리 설치 |
| 2 | ⚠️ **런타임 재시작** | |

### Phase 2 — 모델 로드 + 학습 + GGUF | Model + Train + GGUF

| 순서 | 셀 | 할 일 | 건너뛸 셀 |
|------|-----|------|----------|
| 3 | 셀 6.5 | CUDA 수정 | |
| 4 | **셀 7 (수정!)** | **Llama 3.2 3B 모델 로드** | |
| 5 | 셀 8 | LoRA 어댑터 설정 | |
| 6 | 셀 17 | HuggingFace 로그인 | 셀 9~16 건너뜀 |
| 7 | 셀 18 | 로그인 확인 | |
| 8 | **셀 8.5 (수정!)** | **200개 데이터 학습** | 셀 18.5~24 건너뜀 |
| 9 | **GGUF 변환** | Step 2 코드 실행 | |

### Phase 3 — 로컬 배포 + 테스트 | Local Deploy + Test

| 순서 | 할 일 | 어디서 |
|------|------|-------|
| 10 | GGUF 파일 다운로드 | 코랩 |
| 11 | Ollama에 등록 | 로컬 터미널 |
| 12 | 1B vs 3B 답변 비교 | 로컬 터미널 |

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 데이터 200개 확장 (로컬에서 준비)

기존 83개 + 새로 117개 추가 = 200개 목표.
새 데이터는 더 다양한 카테고리로 확장합니다.

추가 카테고리:
- **기술 상세** (20개): LoRA 설정값, SFTTrainer 파라미터, loss 해석
- **에러 경험** (15개): CUDA 오류, Gemma 호환 문제, 셀 순서 실수
- **Day별 기록** (20개): Day 001~030 핵심 요약
- **비즈니스** (15개): 쇼핑몰, 유튜브 수익화, 1인 기업 운영
- **AI 일반 지식** (20개): LLM이란, 토큰이란, 양자화란, RAG vs 파인튜닝
- **크라베오 상세** (27개): 채널 방향, 콘텐츠 전략, 운영 철학

---

### Step 2 — 코랩에서 셀 7 수정 (3B 모델로 변경)

```python
# 셀 7 — 모델 로드 (Day 031: 1B에서 3B로 업그레이드)
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-3B-Instruct",
    max_seq_length = 512,
    dtype = None,
    load_in_4bit = True,
)
print("✅ 모델 로드 성공 — Llama 3.2 3B")
```

---

### Step 3 — 학습 + GGUF 변환 (코랩)

Day 027~029와 동일한 흐름:
셀 8.5 (학습) → After 확인 → GGUF 변환

**셀 8.5**: 파일명을 `cravveo_200_dataset.jsonl`로 변경!
```python
dataset = load_dataset("json", data_files="cravveo_200_dataset.jsonl", split="train")
```

**GGUF 변환**: 폴더명을 `cravveo-3b-gguf`로 변경!
```python
model.save_pretrained_gguf(
    "cravveo-3b-gguf",
    tokenizer,
    quantization_method = "q4_k_m",
)
```

---

### Step 4 — GGUF 파일 다운로드 (코랩 → 로컬)

**방법 1**: 코랩 왼쪽 파일탭에서 직접 다운로드
- `cravveo-3b-gguf_gguf/llama-3.2-3b-instruct.Q4_K_M.gguf` 우클릭 → 다운로드
- `cravveo-3b-gguf_gguf/Modelfile` 우클릭 → 다운로드

**방법 2**: Google Drive 경유
```python
from google.colab import drive
drive.mount('/content/drive')

import shutil
shutil.copy("cravveo-3b-gguf_gguf/llama-3.2-3b-instruct.Q4_K_M.gguf", "/content/drive/MyDrive/cravveo-3b-model.gguf")
shutil.copy("cravveo-3b-gguf_gguf/Modelfile", "/content/drive/MyDrive/Modelfile-3b")
print("✅ Google Drive에 저장 완료")
```

다운로드한 파일 2개를 `31일차/` 폴더에 넣기:
```
~/finetuning-project/31일차/
  ├── llama-3.2-3b-instruct.Q4_K_M.gguf
  └── Modelfile
```

---

### Step 5 — 로컬 Ollama에 모델 등록 (터미널)

**5-1. Modelfile 수정** (temperature 조정 + 시스템 프롬프트 추가)

Modelfile을 열어서 마지막 부분을 수정:
```
PARAMETER temperature 1.5    ← 이 줄을 아래로 변경
PARAMETER min_p 0.1
```
변경:
```
PARAMETER temperature 0.7
PARAMETER min_p 0.1
SYSTEM "너는 크라베오 컴퍼니의 AI 어시스턴트야. 크라베오에 대한 질문에 정확하게 답해줘."
```

**5-2. Ollama에 등록**

터미널을 열고:
```bash
# 31일차 폴더로 이동
cd ~/finetuning-project/31일차

# Ollama에 cravveo-3b 이름으로 등록
ollama create cravveo-3b -f Modelfile
```

`success` 메시지가 나오면 등록 완료!

**5-3. 등록 확인**
```bash
# 등록된 모델 목록 확인
ollama list
```

cravveo, cravveo-3b 두 개가 보이면 성공!

---

### Step 6 — 1B vs 3B 비교 테스트 (터미널)

```bash
# 1B 모델 (Day 029에서 등록한 것)
ollama run cravveo "질문: 크라베오 컴퍼니가 뭐야?
답변:"

# 3B 모델 (오늘 등록한 것)
ollama run cravveo-3b "질문: 크라베오 컴퍼니가 뭐야?
답변:"
```

**대화 모드**로 테스트하려면:
```bash
ollama run cravveo-3b
```
그 다음 자유롭게 질문 입력. 끝내려면 `/bye` 입력.

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] 데이터 200개 확장 완료
- [ ] Llama 3.2 3B 모델 로드 성공
- [ ] 학습 완료 + After 답변 정확
- [ ] GGUF 변환 완료
- [ ] 로컬 Ollama에 cravveo-3b 등록
- [ ] **1B vs 3B 답변 품질 비교** ← 핵심
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅 | Troubleshooting

**3B 모델 OOM (메모리 부족)**
→ 코랩 T4 GPU(15GB)에서 3B + 4bit는 약 6GB 사용 — 충분할 것
→ 그래도 OOM 나면 `max_seq_length = 256`으로 줄이기
→ 또는 `gradient_accumulation_steps = 8`로 올리기

**GGUF 파일이 너무 클 때**
→ 3B 모델 GGUF는 약 2GB 예상 (1B는 771MB)
→ `q4_k_m` 대신 `q4_0`으로 더 압축 가능

**Ollama에서 3B 모델이 느릴 때**
→ CPU 전용이라 1B보다 느림 (3배 정도)
→ 답변 품질과 속도 트레이드오프

---

## 📅 다음 단계 예고 | Next Up

**Day 032** — Ollama + AnythingLLM 연결
파인튜닝된 크라베오 모델을 AnythingLLM에 연결해서
내 문서를 아는 RAG + 파인튜닝 통합 AI를 만듭니다.

Day 032 — Ollama + AnythingLLM Integration
Connect the fine-tuned Cravveo model to AnythingLLM
for a combined RAG + fine-tuning AI that knows my documents.

---

[[2026-06-25_Day031_Work_Order|Day 031 작업지시서]] | [[../30일차/2026-06-24_Day030_Work_Order|← Day 030]] | [[../Cravveo_100Day_Master_Guide]]

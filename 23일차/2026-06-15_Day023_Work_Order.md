# 📋 Day 023 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-15
> **단계** | Phase: Day 023 / 100

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
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019 | JSONL 포맷 분석 | ✅ 완료 |
| Day 020+021 | 크라베오 데이터셋 수동 제작 + JSONL 변환 스크립트 완성 | ✅ 완료 |
| Day 022 | HuggingFace CLI 로그인 + 토큰 보안 실수 공개 | ✅ 완료 |
| **Day 023** | **데이터셋 HuggingFace 업로드 — 나만의 데이터셋 저장소 완성** | 🔥 오늘 |
| Day 024~ | 업로드된 데이터셋으로 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 로그인은 완료됐습니다.
> 이제 직접 만든 JSONL 데이터셋을 HuggingFace에 올립니다.
> 업로드가 완료되면 코드 한 줄로 언제 어디서든 불러올 수 있습니다.
> 오늘 목표는 `push_to_hub()` 성공 + `load_dataset()` 한 줄 불러오기 확인입니다.

**English**
> Login is already done.
> Today we push the custom JSONL dataset to HuggingFace.
> Once uploaded, a single line of code loads it anytime, anywhere.
> Today's goal: `push_to_hub()` success + confirm `load_dataset()` works.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
코랩은 세션이 끊기면 업로드한 파일이 전부 사라집니다.
HuggingFace Dataset Hub에 올려두면 세션이 새로 시작돼도 코드 한 줄로 데이터가 복원됩니다.
파인튜닝을 반복 실험할 때 데이터를 매번 재업로드할 필요가 없어집니다.
오늘 업로드가 완료되면 내일부터 진짜 파인튜닝 코드를 작성할 수 있습니다.

**English**
When a Colab session ends, all uploaded files disappear.
With the dataset on HuggingFace Hub, a single line of code restores it in any new session.
No need to re-upload data every time we restart a fine-tuning experiment.
After today's upload, we can start writing actual fine-tuning code tomorrow.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 & 환경 준비

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. `cravveo_finetuning.ipynb` 열기
3. 런타임 → T4 GPU 확인

```python
!nvidia-smi
```

---

### Step 2 — 필수 라이브러리 설치

```python
%%capture
!pip install unsloth
!pip install --upgrade "torchvision>=0.27.0"
!pip install -q datasets huggingface_hub
```

```python
import unsloth
from datasets import load_dataset, Dataset
from huggingface_hub import login, whoami
print("✅ 라이브러리 준비 완료")
```

---

### Step 3 — HuggingFace 로그인

설명: 세션이 새로 시작됐으면 다시 로그인이 필요합니다. Day 022에서 배운 방법 그대로 사용합니다.
토큰은 코랩 Secrets(🔑)에 저장된 `HF_TOKEN`에서 불러옵니다.

```python
from google.colab import userdata

hf_token = userdata.get('HF_TOKEN')
login(token=hf_token)

user_info = whoami()
print(f"✅ 로그인 성공: {user_info['name']}")
```

---

### Step 4 — JSONL 파일 코랩에 업로드

설명: GitHub 저장소에서 직접 JSONL 파일을 가져옵니다. GitHub raw URL을 사용하면 코랩에 파일을 수동으로 올리지 않아도 됩니다.

```python
!wget -q "https://raw.githubusercontent.com/cravveo4001/cravveo-100days/main/10일차/cravveo_briefing_dataset.jsonl" -O cravveo_briefing_dataset.jsonl
!wc -l cravveo_briefing_dataset.jsonl
print("✅ 데이터셋 파일 다운로드 완료")
```

---

### Step 5 — 데이터셋 로드 & 확인

설명: JSONL 파일을 HuggingFace `datasets` 형식으로 변환합니다.

```python
dataset = load_dataset('json', data_files='cravveo_briefing_dataset.jsonl', split='train')

print(f"✅ 데이터셋 로드 완료")
print(f"총 데이터 수: {len(dataset)}개")
print(f"컬럼: {dataset.column_names}")
print()
print("--- 첫 번째 데이터 미리보기 ---")
print(dataset[0])
```

---

### Step 6 — HuggingFace Hub에 업로드 (push_to_hub)

설명: 데이터셋을 내 HuggingFace 계정에 업로드합니다.
`cravveo4001/cravveo-briefing-dataset` 이름으로 새 저장소가 생성됩니다.

```python
dataset.push_to_hub(
    "cravveo/cravveo-briefing-dataset",
    private=False
)
print("✅ 업로드 완료!")
print("🔗 https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset")
```

---

### Step 7 — 코드 한 줄로 불러오기 테스트

설명: 업로드가 됐는지 확인합니다. 이제부터 이 한 줄이면 어디서든 데이터셋을 불러올 수 있습니다.

```python
# 코드 한 줄로 불러오기
loaded = load_dataset("cravveo/cravveo-briefing-dataset", split='train')

print(f"✅ 불러오기 성공!")
print(f"데이터 수: {len(loaded)}개")
print(loaded[0]['instruction'][:100])
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] `datasets`, `huggingface_hub` 설치 완료
- [ ] Colab Secrets에서 토큰 로그인 성공
- [ ] JSONL 파일 코랩에 다운로드 완료
- [ ] `load_dataset()` 로 데이터 개수 확인
- [ ] `push_to_hub()` 실행 후 업로드 완료 메시지 확인
- [ ] HuggingFace 웹사이트에서 업로드된 데이터셋 직접 확인
- [ ] `load_dataset("cravveo4001/cravveo-briefing-dataset")` 한 줄 불러오기 성공
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`403 Forbidden` 오류 (push_to_hub 실패)**
→ 토큰 권한이 Read 전용입니다. HuggingFace Settings → Access Tokens → Write 권한 토큰으로 재발급 후 재로그인하세요.

**`Repository not found` 오류 (load_dataset 실패)**
→ 업로드 직후 HuggingFace 서버 반영에 1~2분 걸릴 수 있습니다. 잠시 후 다시 시도하세요.

**`FileNotFoundError: cravveo_briefing_dataset.jsonl`**
→ Step 4의 wget 명령어를 다시 실행하세요. 파일 경로가 맞는지 확인합니다.

**GitHub raw URL 404 오류**
→ GitHub 저장소가 비공개이거나 파일 경로가 다를 수 있습니다. 저장소에서 파일을 직접 찾아 URL을 복사하세요.
→ 대안: 코랩 왼쪽 파일 패널에서 직접 업로드 후 `load_dataset('json', data_files='파일명.jsonl')` 사용.

**`datasets` import 오류**
→ `!pip install datasets` 재실행 후 런타임 다시 시작 (Runtime → Restart runtime).

---

## 📅 다음 단계 예고 | Next Up

**Day 024** — 파인튜닝 코드 작성 시작
이제 데이터가 허깅페이스에 있습니다.
다음은 Unsloth + LoRA 설정으로 실제 파인튜닝 코드를 작성하고 학습을 돌립니다.

Day 024 — Writing the Fine-Tuning Code
The dataset is now on HuggingFace.
Next: write the actual fine-tuning code using Unsloth + LoRA and run the first training loop.

---

[[2026-06-15_Day023_Work_Order|Day 023 작업지시서]] | [[../22일차/2026-06-14_Day022_Work_Order|← Day 022]] | [[../Cravveo_100Day_Master_Guide]]

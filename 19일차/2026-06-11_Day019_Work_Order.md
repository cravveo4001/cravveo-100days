# 📋 Day 019 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-11
> **단계** | Phase: Day 019 / 100

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
| Day 018 | Unsloth 소개 — 파인튜닝 최강 도구 설치 + 모델 로드 | ✅ 완료 |
| **Day 019** | **JSONL 포맷 분석 — AI에게 먹일 학습 데이터의 생김새** | 🔥 오늘 |
| Day 020~ | 크라베오 데이터셋 직접 제작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 모델도 준비됐고, 도구도 준비됐습니다.
> 이제 진짜 질문이 생깁니다 — AI에게 어떤 형식으로 데이터를 먹여야 할까?
> 오늘은 파인튜닝 학습 데이터의 기본 포맷인 JSONL을 이해하고,
> 직접 손으로 써보는 것이 목표입니다.

**English**
> The model is ready. The tools are ready.
> Now the real question: what format does the AI actually expect to eat?
> Today we learn JSONL — the standard format for fine-tuning training data —
> and write our first entries by hand.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
파인튜닝은 결국 "이 질문에는 이렇게 대답해라"를 AI에게 수백~수천 번 보여주는 과정입니다.
그런데 AI는 일반 텍스트 파일을 그냥 읽지 않습니다.
정해진 형식(포맷)으로 정리된 데이터만 받아들입니다.
그 형식이 바로 JSONL입니다.
JSONL을 모르면 데이터를 아무리 많이 만들어도 AI가 읽지 못합니다.
오늘은 그 규칙을 완전히 이해하고, 내 손으로 첫 데이터를 써봅니다.

**English**
Fine-tuning is simply showing the AI "for this question, answer like this" — hundreds or thousands of times.
But the AI doesn't read plain text files.
It only accepts data organized in a specific format.
That format is JSONL.
Without understanding JSONL, no amount of data will work.
Today we master the rules and write our first training entry by hand.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 및 환경 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. 기존 `cravveo_finetuning.ipynb` 열기
3. 런타임 → 런타임 유형 변경 → T4 GPU 확인
4. GPU 확인 코드 실행

설명: 오늘은 GPU를 많이 쓰는 날은 아니지만 환경이 맞는지 항상 먼저 확인합니다.
```python
!nvidia-smi
```

---

### Step 2 — JSON vs JSONL 차이 이해

설명: JSONL을 배우기 전에 JSON이 뭔지 먼저 이해합니다. 텍스트 셀에 아래 내용을 직접 정리해보세요.

| 항목 | JSON | JSONL |
|------|------|-------|
| 확장자 | `.json` | `.jsonl` |
| 구조 | 파일 전체가 하나의 덩어리 | 한 줄 = 하나의 데이터 |
| 읽는 방식 | 전체를 한 번에 읽음 | 한 줄씩 읽음 |
| 파인튜닝 적합성 | 불편 (전체 로드) | 적합 (스트리밍 가능) |
| 예시 | `{"name": "크라베오"}` (파일 하나) | 줄마다 JSON 한 개씩 |

핵심: JSONL은 JSON 객체들을 한 줄에 하나씩 나열한 것입니다. 파인튜닝 도구들이 JSONL을 선호하는 이유는 데이터가 수천 줄이어도 한 줄씩 읽을 수 있어서 메모리를 적게 씁니다.

---

### Step 3 — 파인튜닝 데이터 포맷 2종 비교

설명: 파인튜닝 학습 데이터에는 여러 포맷이 있지만 가장 많이 쓰이는 2가지를 이해합니다. Unsloth는 둘 다 지원합니다.

#### Alpaca 포맷 (지시-응답형)
질문(instruction) + 입력(input) + 정답(output) 구조입니다. 챗봇보다는 "이 일을 해줘" 형태의 지시 학습에 적합합니다.

```json
{"instruction": "다음 문장을 공손한 표현으로 바꿔줘", "input": "이거 당장 고쳐.", "output": "이 부분을 수정해 주시면 감사하겠습니다."}
{"instruction": "크라베오 회사를 한 문장으로 소개해줘", "input": "", "output": "크라베오는 1인 기업 자동화를 연구하는 회사입니다."}
```

#### ShareGPT 포맷 (대화형)
사람(human)과 AI(gpt)가 주고받는 대화 형식입니다. 챗봇 스타일 파인튜닝에 적합합니다.

```json
{"conversations": [{"from": "human", "value": "크라베오가 뭐야?"}, {"from": "gpt", "value": "크라베오는 1인 기업 자동화를 연구하는 회사입니다."}]}
{"conversations": [{"from": "human", "value": "파인튜닝이 뭐야?"}, {"from": "gpt", "value": "AI 모델을 내 데이터로 다시 학습시켜서 내 스타일로 만드는 과정입니다."}]}
```

---

### Step 4 — 직접 JSONL 파일 작성해보기

설명: 코랩에서 Python으로 직접 JSONL 파일을 만들어봅니다. 내용은 크라베오 회사에 관한 간단한 질문-답변 5개입니다. 형식이 맞는지 손으로 타이핑하면서 몸에 익히는 게 목적입니다.

```python
import json

# 크라베오 데이터셋 — Alpaca 포맷 예시 5개
data = [
    {
        "instruction": "크라베오 회사를 소개해줘",
        "input": "",
        "output": "크라베오는 1인 기업 자동화를 연구하는 회사입니다. AI와 Python을 활용해 반복 업무를 줄이는 시스템을 만듭니다."
    },
    {
        "instruction": "파인튜닝이 뭔지 쉽게 설명해줘",
        "input": "",
        "output": "파인튜닝은 이미 만들어진 AI 모델을 내 데이터로 추가 학습시키는 과정입니다. AI가 내 스타일과 지식을 갖게 됩니다."
    },
    {
        "instruction": "Unsloth를 쓰는 이유가 뭐야?",
        "input": "",
        "output": "Unsloth는 파인튜닝 속도를 2~5배 빠르게 하고 메모리를 60% 절약합니다. 무료 코랩 환경에서 파인튜닝을 현실적으로 가능하게 해주는 도구입니다."
    },
    {
        "instruction": "LoRA가 뭐야?",
        "input": "",
        "output": "LoRA는 모델 전체를 학습시키지 않고 일부 층에만 작은 어댑터를 붙여서 학습하는 방법입니다. 메모리와 시간을 크게 절약할 수 있습니다."
    },
    {
        "instruction": "JSONL 포맷이 뭐야?",
        "input": "",
        "output": "JSONL은 JSON 데이터를 한 줄에 하나씩 나열한 파일 형식입니다. 파인튜닝 학습 데이터를 저장하는 데 표준으로 쓰입니다."
    },
]

# JSONL 파일로 저장
with open("cravveo_sample.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✅ JSONL 파일 생성 완료 — {len(data)}개 항목")
```

---

### Step 5 — JSONL 파일 다시 읽어보기

설명: 방금 만든 파일을 다시 불러와서 각 줄을 출력해봅니다. 파일이 정상인지 확인하는 동시에 JSONL을 읽는 기본 코드를 익힙니다.

```python
# JSONL 파일 읽기
with open("cravveo_sample.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"총 {len(lines)}줄 읽음\n")
for i, line in enumerate(lines):
    item = json.loads(line)
    print(f"[{i+1}] instruction: {item['instruction']}")
    print(f"     output: {item['output'][:40]}...")
    print()
```

---

### Step 6 — Unsloth 데이터셋 포맷 연결 (개념 확인)

설명: 나중에 실제 학습 때 Unsloth가 이 데이터를 어떻게 읽는지 맛보기로 확인합니다. 오늘은 실행보다 코드 구조 이해가 목표입니다.

```python
from datasets import load_dataset

# 로컬 JSONL 파일을 HuggingFace datasets 형식으로 로드
dataset = load_dataset("json", data_files="cravveo_sample.jsonl", split="train")
print(dataset)
print()

# 전체 항목 출력
for i in range(len(dataset)):
    print(f"[{i+1}] instruction: {dataset[i]['instruction']}")
    print(f"     output: {dataset[i]['output'][:50]}...")
    print()
```

출력 예시:
```
Dataset({
    features: ['instruction', 'input', 'output'],
    num_rows: 5
})

[1] instruction: 크라베오 회사를 소개해줘
     output: 크라베오는 1인 기업 자동화를 연구하는 회사입니다...

[2] instruction: 파인튜닝이 뭔지 쉽게 설명해줘
     output: 파인튜닝은 이미 만들어진 AI 모델을 내 데이터로...

[3] instruction: Unsloth를 쓰는 이유가 뭐야?
     output: Unsloth는 파인튜닝 속도를 2~5배 빠르게 하고...

[4] instruction: LoRA가 뭐야?
     output: LoRA는 모델 전체를 학습시키지 않고 일부 층에만...

[5] instruction: JSONL 포맷이 뭐야?
     output: JSONL은 JSON 데이터를 한 줄에 하나씩 나열한...
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] JSON vs JSONL 차이 직접 정리 (텍스트 셀)
- [ ] Alpaca 포맷 vs ShareGPT 포맷 비교표 이해
- [ ] 크라베오 관련 JSONL 데이터 5개 직접 작성 + 파일 생성
- [ ] JSONL 파일 다시 읽기 코드 실행 확인
- [ ] (선택) HuggingFace datasets로 로드 확인
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`json.JSONDecodeError` 에러**
→ JSONL 한 줄에 JSON 형식이 깨진 것입니다. 따옴표가 짝이 맞는지, 쉼표가 올바른지 확인하세요.
→ 온라인 JSON 검증기(jsonlint.com)에 한 줄씩 붙여넣어 확인하면 빠릅니다.

**한글이 `\uXXXX` 형태로 저장될 때**
→ `json.dumps()` 에 `ensure_ascii=False` 옵션이 빠진 것입니다. 코드에 반드시 포함하세요.

**`ModuleNotFoundError: No module named 'datasets'`**
→ Step 6 실행 전에 `!pip install datasets` 먼저 실행하세요. (17일차에 설치했지만 세션 재시작 시 초기화됩니다)

**파일이 저장됐는데 코랩에서 안 보일 때**
→ 왼쪽 파일 탐색기 새로고침 버튼을 클릭하면 나타납니다. 코랩은 파일 목록이 자동 갱신되지 않습니다.

**세션 끊기면 파일이 사라져요**
→ 코랩 임시 저장소는 세션 종료 시 사라집니다. 중요한 파일은 구글 드라이브에 마운트해서 저장하세요.

---

## 📅 다음 단계 예고 | Next Up

**Day 020** — 크라베오 데이터셋 본격 제작
JSONL 포맷을 이해했으니 이제 실제로 씁니다.
크라베오 회사 스타일로 답변하는 AI를 만들기 위한 질문-답변 세트를 직접 작성합니다.
몇 개나 필요한지, 어떤 내용을 담아야 하는지도 함께 정리합니다.

Day 020 — Building the Cravveo Dataset
Now that we know the format, we build the real thing.
We'll write a set of Q&A pairs that teach the AI to answer in Cravveo's style.
We'll also figure out how many entries we actually need.

---

[[2026-06-11_Day019_Work_Order|Day 019 작업지시서]] | [[../18일차/2026-06-10_Day018_Work_Order|← Day 018]] | [[../Cravveo_100Day_Master_Guide]]

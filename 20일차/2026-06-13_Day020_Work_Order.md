# 📋 Day 020 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-13
> **단계** | Phase: Day 020 / 100

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
| Day 019 | JSONL 포맷 분석 — AI에게 먹일 학습 데이터의 생김새 | ✅ 완료 |
| **Day 020** | **크라베오 데이터셋 수동 제작 — 정체성 + 철학 10문 1답** | 🔥 오늘 |
| Day 021~ | JSONL 변환 스크립트 작성 + HuggingFace 업로드 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 포맷도 알고, 도구도 갖췄습니다.
> 이제 진짜 내 AI를 만들기 위한 재료를 직접 씁니다.
> 크라베오 컴퍼니의 정체성과 운영자의 철학을 담은
> 질문-답변 10개를 메모장에 직접 작성하는 것이 오늘의 목표입니다.

**English**
> We know the format. We have the tools.
> Now we write the raw material for our own AI.
> The goal today is to hand-write 10 Q&A pairs
> that capture Cravveo Company's identity and the operator's philosophy.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
브리핑 자동화로 35개 데이터가 쌓였지만, 그 데이터는 AI가 만든 AI용 데이터입니다.
AI가 크라베오를 제대로 배우려면 크라베오를 가장 잘 아는 사람이 직접 쓴 데이터가 필요합니다.
"크라베오가 뭐야?" 라는 질문에 AI가 내 목소리로 대답하게 하려면
내가 직접 그 대답을 써줘야 합니다.
오늘은 AI 학습의 핵심인 고품질 수동 데이터 10개를 완성합니다.

**English**
We have 35 entries from the briefing automation — but those are AI-generated answers about generic topics.
For the AI to truly learn Cravveo, it needs data written by the person who knows Cravveo best.
If you want the AI to answer "What is Cravveo?" in your voice,
you have to write that answer yourself.
Today we complete 10 high-quality, hand-written entries — the core of the Cravveo dataset.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 어떤 데이터를 써야 하는지 먼저 정한다

설명: 무작정 쓰기 전에 카테고리를 나눕니다. 크라베오 AI가 잘 대답해야 할 주제가 무엇인지 먼저 생각합니다. 아래 표를 텍스트 셀에 직접 정리해보세요.

| 카테고리 | 예시 질문 | 목적 |
|----------|-----------|------|
| 회사 정체성 | 크라베오가 뭐야? | AI가 크라베오를 소개할 수 있게 |
| 운영자 철학 | 왜 1인 기업을 선택했어? | AI가 내 생각으로 말하게 |
| 프로젝트 | 100일 도전이 뭐야? | AI가 이 채널을 설명할 수 있게 |
| 파인튜닝 개념 | 파인튜닝이 뭐야? | AI가 쉽게 설명할 수 있게 |
| 일상/스타일 | 하루를 어떻게 보내? | AI가 크라베오 톤으로 말하게 |

핵심 원칙: 질문은 외부인이 물어볼 법한 것, 답변은 내가 실제로 하는 말투로 작성합니다.

---

### Step 2 — 좋은 답변의 조건 이해하기

설명: 파인튜닝 데이터의 답변은 길수록 좋은 게 아닙니다. AI가 학습하기 좋은 답변의 조건을 먼저 이해합니다.

| 조건 | 좋은 예 | 나쁜 예 |
|------|---------|---------|
| 길이 | 2~5문장 (핵심만) | 10줄 이상 장황한 설명 |
| 말투 | 내 실제 말투 | 교과서체, 존댓말 남용 |
| 정보 | 사실 기반, 구체적 | 애매하고 일반적인 내용 |
| 관점 | 1인칭 (나는, 우리는) | 3인칭 (크라베오는) |

목표 길이: 답변 하나당 **2~4문장**, 100~200자 사이.

---

### Step 3 — 코랩에서 10개 직접 작성

설명: 코랩 텍스트 셀이나 코드 셀에서 직접 씁니다. 아래는 참고용 예시입니다. 이 내용을 그대로 쓰지 말고, 실제 내 언어와 경험으로 바꿔서 작성하세요.

```python
import json

# ⚠️ 아래 내용을 내 실제 생각으로 수정해서 작성하세요
cravveo_dataset = [
    {
        "instruction": "크라베오 컴퍼니가 뭐야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "왜 1인 기업을 선택했어?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "100일 AI 도전이 뭐야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "파인튜닝을 왜 배우고 있어?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "크라베오의 목표가 뭐야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "유튜브를 왜 시작했어?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "하루를 어떻게 보내?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "AI를 처음 배울 때 가장 어려웠던 게 뭐야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "Build in Public이 뭐야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
    {
        "instruction": "크라베오 AI가 완성되면 뭘 할 거야?",
        "input": "",
        "output": ""  # 내 말로 직접 채우기
    },
]

print(f"작성된 항목: {len(cravveo_dataset)}개")
for i, item in enumerate(cravveo_dataset):
    print(f"[{i+1}] Q: {item['instruction']}")
    print(f"     A: {item['output'][:50]}..." if item['output'] else f"     A: ⚠️ 미작성")
    print()
```

---

### Step 4 — JSONL 파일로 저장

설명: 10개 작성이 끝나면 JSONL 파일로 저장합니다. 파일명은 브리핑 데이터셋과 구분해서 `cravveo_identity.jsonl`로 저장합니다.

```python
# JSONL 저장
with open("cravveo_identity.jsonl", "w", encoding="utf-8") as f:
    for item in cravveo_dataset:
        if item["output"]:  # 내용이 있는 항목만 저장
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

# 확인
with open("cravveo_identity.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"✅ 저장 완료 — {len(lines)}개 항목")
print("\n--- 저장된 내용 확인 ---")
for i, line in enumerate(lines):
    item = json.loads(line)
    print(f"[{i+1}] {item['instruction']}")
```

---

### Step 5 — 브리핑 데이터셋과 합치기 (선택)

설명: 기존 브리핑 자동화로 만든 `cravveo_briefing_dataset.jsonl` (35개)과 오늘 만든 `cravveo_identity.jsonl` (10개)를 합쳐서 전체 데이터셋을 만듭니다.

```python
import json

files = [
    "cravveo_briefing_dataset.jsonl",  # 브리핑 자동화 데이터 35개
    "cravveo_identity.jsonl",           # 오늘 수동 작성 10개
]

all_data = []
for fname in files:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            for line in f:
                all_data.append(json.loads(line))
        print(f"✅ {fname} 로드 완료")
    except FileNotFoundError:
        print(f"⚠️ {fname} 없음 — 건너뜀")

with open("cravveo_full_dataset.jsonl", "w", encoding="utf-8") as f:
    for item in all_data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"\n총 {len(all_data)}개 항목 → cravveo_full_dataset.jsonl 저장 완료")
```

---

## ✅ 성공 조건 체크리스트

- [ ] 데이터 카테고리 5종 정리 (텍스트 셀에 직접 작성)
- [ ] 좋은 답변 조건 이해 (2~4문장, 내 말투, 1인칭)
- [ ] 크라베오 정체성 Q&A 10개 직접 작성 완료
- [ ] `cravveo_identity.jsonl` 파일 저장 확인
- [ ] (선택) 브리핑 데이터셋과 합쳐서 `cravveo_full_dataset.jsonl` 생성
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**답변을 뭐라고 써야 할지 모르겠을 때**
→ 누군가 실제로 이 질문을 했다면 내가 뭐라고 대답할지 생각해보세요.
→ 길게 쓰려고 하지 마세요. 짧고 진짜인 게 훨씬 좋습니다.

**한 카테고리에만 질문이 몰릴 때**
→ 회사 소개 3개, 철학 2개, 프로젝트 2개, 개념 2개, 스타일 1개 정도로 분산하세요.

**`cravveo_briefing_dataset.jsonl` 파일이 코랩에 없을 때**
→ 로컬 10일차 폴더에 있는 파일을 코랩에 직접 업로드하거나,
→ 구글 드라이브에 마운트해서 불러오세요.

**저장했는데 파일이 안 보일 때**
→ 코랩 왼쪽 파일 탐색기 새로고침 버튼 클릭.

---

## 📅 다음 단계 예고 | Next Up

**Day 021** — JSONL 변환 파이썬 코드 작성
메모장(텍스트)으로 쓴 내용을 파이썬 스크립트로 JSONL 파일에 자동 변환하는 코드를 만듭니다.
손으로 쓴 데이터를 코드로 관리하는 방법을 배웁니다.

Day 021 — Writing the JSONL Conversion Script
We'll write a Python script that converts plain text entries into a proper JSONL dataset file.
Learning to manage hand-written data through code.

---

[[2026-06-13_Day020_Work_Order|Day 020 작업지시서]] | [[../19일차/2026-06-11_Day019_Work_Order|← Day 019]] | [[../Cravveo_100Day_Master_Guide]]

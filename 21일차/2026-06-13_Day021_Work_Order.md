# 📋 Day 021 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-13
> **단계** | Phase: Day 021 / 100

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
| Day 019 | JSONL 포맷 분석 — AI에게 먹일 학습 데이터의 생김새 | ✅ 완료 |
| Day 020 | 크라베오 데이터셋 수동 제작 — 정체성 + 철학 10문 1답 | ✅ 완료 |
| **Day 021** | **JSONL 변환 파이썬 코드 작성 — 텍스트를 데이터셋으로** | 🔥 오늘 |
| Day 022~ | HuggingFace CLI 로그인 + 데이터셋 업로드 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 어제 10개 데이터를 직접 손으로 썼습니다.
> 오늘은 그 텍스트를 코드로 관리하는 방법을 배웁니다.
> 메모장처럼 편하게 쓴 내용을 파이썬 스크립트 하나로
> JSONL 파일로 자동 변환하는 파이프라인을 만드는 것이 오늘의 목표입니다.

**English**
> Yesterday we hand-wrote 10 Q&A entries.
> Today we learn to manage that text through code.
> The goal is to build a Python pipeline that automatically converts
> plain text Q&A entries into a proper JSONL dataset file.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
데이터셋을 계속 손으로 JSONL로 쓰는 건 실수가 생기기 쉽습니다.
따옴표 하나, 쉼표 하나가 틀리면 파일 전체가 깨집니다.
파이썬 스크립트를 쓰면 내용만 채우면 되고 형식은 코드가 알아서 잡아줍니다.
데이터가 10개일 때는 괜찮지만 100개, 1000개가 되면 코드 없이는 불가능합니다.
오늘은 앞으로 계속 쓸 데이터 제작 파이프라인을 완성합니다.

**English**
Manually writing JSONL by hand is error-prone.
One missing quote or comma breaks the entire file.
With a Python script, you only fill in the content — the code handles the format.
Fine with 10 entries, but impossible to manage at 100 or 1000 without code.
Today we build the data pipeline we'll keep using going forward.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 코랩 열기 및 환경 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. 기존 `cravveo_finetuning.ipynb` 열기
3. 런타임 → T4 GPU 확인

```python
!nvidia-smi
```

---

### Step 2 — 텍스트 → JSONL 변환 스크립트 작성

설명: Q&A 내용을 Python 리스트로 관리하고, 코드가 자동으로 JSONL로 바꿔주는 스크립트입니다. 앞으로 데이터를 추가할 때는 `data` 리스트에 항목만 추가하면 됩니다.

```python
import json

# 여기에 Q&A 데이터를 추가합니다
# instruction: 질문, output: 답변 (내 말투로)
data = [
    {
        "instruction": "크라베오 컴퍼니가 뭐야?",
        "input": "",
        "output": "IT 프로그램 개발, 인터넷 쇼핑몰, 유튜브 채널 등을 혼자서 운영하면서 수익을 창출하는 1인 기업이야."
    },
    {
        "instruction": "왜 1인 기업을 선택했어?",
        "input": "",
        "output": "회사 생활을 20년 넘게 하면서 이리 치이고 저리 치이다 보니까 혼자 하는 게 낫겠다 싶었어. 그래서 시작했어."
    },
    {
        "instruction": "100일 AI 도전이 뭐야?",
        "input": "",
        "output": "지금 내가 하고 있는 것들을 홍보도 하고 기록도 남기고 싶어서 도전하고 있어."
    },
    {
        "instruction": "파인튜닝을 왜 배우고 있어?",
        "input": "",
        "output": "결국 개인의 지식만이 살아남는다는 걸 배우면서 느꼈어. 클라우드 AI 비용 문제도 있고, 나만의 AI를 만들면 파인튜닝으로 수익도 낼 수 있지 않을까 싶어서 배우고 있어."
    },
    {
        "instruction": "크라베오의 목표가 뭐야?",
        "input": "",
        "output": "1인 스타트업으로 살아남는 거야. 그게 지금 목표야."
    },
    {
        "instruction": "유튜브를 왜 시작했어?",
        "input": "",
        "output": "홍보랑 기록용이야. 내가 뭘 하고 있는지 남기고 싶었어."
    },
    {
        "instruction": "하루를 어떻게 보내?",
        "input": "",
        "output": "아침에 생산직 회사에 출근해서 일하고, 오후 6시쯤 퇴근하면 1인 스타트업 만들려고 공부하고 유튜브 영상 만들어. 저녁 12시쯤에 집에 가서 새벽 1~3시쯤에 자."
    },
    {
        "instruction": "AI를 처음 배울 때 가장 어려웠던 게 뭐야?",
        "input": "",
        "output": "시작하는 거야. 컴퓨터 켜고 도전해보는 게 제일 어려웠어. 이걸 왜 해야 하는지도 몰랐으니까."
    },
    {
        "instruction": "Build in Public이 뭐야?",
        "input": "",
        "output": "배우는 과정을 숨기지 않고 공개하면서 진행하는 방식이야. 완성된 결과만 보여주는 게 아니라 실패도 에러도 다 공개하는 거야. 내가 100일 도전을 유튜브에 올리는 것도 Build in Public이야."
    },
    {
        "instruction": "크라베오 AI가 완성되면 뭘 할 거야?",
        "input": "",
        "output": "당연히 수익을 창출해야지. 그게 목적이야."
    },
]

# JSONL 저장
output_file = "cravveo_identity.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"✅ {len(data)}개 항목 → {output_file} 저장 완료")
```

---

### Step 3 — 저장된 파일 검증

설명: 저장된 JSONL 파일을 다시 읽어서 형식이 깨지지 않았는지 확인합니다. 각 줄이 정상적인 JSON인지 검사하는 코드입니다.

```python
print("--- JSONL 검증 ---\n")
errors = 0
with open("cravveo_identity.jsonl", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        try:
            item = json.loads(line)
            print(f"[{i+1}] ✅ {item['instruction'][:30]}...")
        except json.JSONDecodeError as e:
            print(f"[{i+1}] ❌ 형식 오류: {e}")
            errors += 1

print(f"\n총 오류: {errors}개" if errors else "\n✅ 모든 항목 형식 정상")
```

---

### Step 4 — 브리핑 데이터셋과 합쳐서 전체 데이터셋 완성

설명: 매일 자동으로 쌓이는 브리핑 데이터(36개)와 오늘 수동으로 만든 크라베오 정체성 데이터(10개)를 하나의 파일로 합칩니다. 이 파일이 앞으로 파인튜닝에 쓸 전체 데이터셋입니다.

```python
import glob

# 합칠 파일 목록
source_files = [
    "cravveo_briefing_dataset.jsonl",  # 브리핑 자동화 데이터
    "cravveo_identity.jsonl",           # 크라베오 정체성 수동 데이터
]

all_data = []
for fname in source_files:
    try:
        with open(fname, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_data.extend(lines)
            print(f"✅ {fname} — {len(lines)}개 로드")
    except FileNotFoundError:
        print(f"⚠️ {fname} 없음 — 건너뜀")

# 전체 데이터셋 저장
with open("cravveo_full_dataset.jsonl", "w", encoding="utf-8") as f:
    f.writelines(all_data)

print(f"\n총 {len(all_data)}개 → cravveo_full_dataset.jsonl 완성")
```

예상 출력:
```
✅ cravveo_briefing_dataset.jsonl — 36개 로드
✅ cravveo_identity.jsonl — 10개 로드

총 46개 → cravveo_full_dataset.jsonl 완성
```

---

### Step 5 — 최종 데이터셋 샘플 확인

설명: 완성된 전체 데이터셋에서 첫 3개와 마지막 3개를 출력해서 데이터가 잘 섞였는지 확인합니다.

```python
with open("cravveo_full_dataset.jsonl", "r", encoding="utf-8") as f:
    all_lines = f.readlines()

total = len(all_lines)
print(f"전체 데이터: {total}개\n")

# 첫 3개
print("=== 처음 3개 ===")
for line in all_lines[:3]:
    item = json.loads(line)
    print(f"Q: {item['instruction']}")
    print(f"A: {item['output'][:50]}...")
    print()

# 마지막 3개
print("=== 마지막 3개 ===")
for line in all_lines[-3:]:
    item = json.loads(line)
    print(f"Q: {item['instruction']}")
    print(f"A: {item['output'][:50]}...")
    print()
```

---

## ✅ 성공 조건 체크리스트

- [ ] 코랩 T4 GPU 런타임 확인
- [ ] 텍스트 → JSONL 변환 스크립트 작성 완료
- [ ] JSONL 검증 코드 실행 — 오류 0개 확인
- [ ] 브리핑 데이터 + 정체성 데이터 합치기 완료
- [ ] `cravveo_full_dataset.jsonl` 총 46개 확인
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**`json.JSONDecodeError` 오류가 뜰 때**
→ output 안에 큰따옴표(`"`)가 들어가 있으면 오류가 납니다.
→ 큰따옴표 대신 작은따옴표(`'`)를 쓰거나, `json.dumps()`가 자동으로 처리하도록 Python 딕셔너리로 관리하세요.

**`cravveo_briefing_dataset.jsonl` 파일이 없을 때**
→ 로컬 `10일차` 폴더에서 코랩으로 직접 업로드하세요.
→ 코랩 왼쪽 파일 탭 → 업로드 버튼.

**합쳐진 파일 항목 수가 예상과 다를 때**
→ 브리핑 파일이 매일 갱신되므로 실행 시점에 따라 개수가 다를 수 있습니다. 정상입니다.

---

## 📅 다음 단계 예고 | Next Up

**Day 022** — HuggingFace CLI 로그인 설정
완성된 데이터셋을 HuggingFace에 올리기 위한 계정 연결을 합니다.
읽기/쓰기 토큰을 발급받고 코랩 터미널에서 로그인까지 완료합니다.

Day 022 — HuggingFace CLI Login
We'll connect Colab to HuggingFace to upload our dataset.
Generate a read/write token and complete login from the Colab terminal.

---

[[2026-06-13_Day021_Work_Order|Day 021 작업지시서]] | [[../20일차/2026-06-13_Day020_Work_Order|← Day 020]] | [[../Cravveo_100Day_Master_Guide]]

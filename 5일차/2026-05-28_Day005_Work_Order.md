# 📋 Day 005 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-05-28
> **단계** | Phase: Day 005 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001 | 리눅스 개발 환경 구축 (Python, pip, venv, git) | ✅ 완료 |
| Day 002 | 작업 폴더 생성 + Python 가상환경(venv) 구성 | ✅ 완료 |
| Day 003 | Git 저장소 초기화 + 첫 번째 커밋 + GitHub push | ✅ 완료 |
| Day 004 | Ollama 설치 + 로컬 LLM 첫 실행 (gemma4:e2b) | ✅ 완료 |
| **Day 005** | **Ollama 모델 비교 + 프롬프트 실습** | 🔥 오늘 |
| Day 006~ | Ollama 모델 API 활용 (Python 연동) | ⏳ 예정 |
| Day 010~ | AnythingLLM 오프라인 RAG | ⏳ 예정 |
| Day 020~ | Google Colab GPU LoRA 파인튜닝 | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 오늘은 Ollama에서 두 모델을 비교해보고,
> 프롬프트를 바꿔가며 AI 답변이 어떻게 달라지는지 직접 실험합니다.
> "어떻게 물어보느냐"가 얼마나 중요한지 몸으로 느끼는 날입니다.

**English**
> Today I will compare two Ollama models side by side,
> then experiment with different prompts to see how the answers change.
> The goal is to feel firsthand why prompt wording matters so much.

---

## 📌 왜 프롬프트 실습인가? | Why Prompt Practice?

**한국어**
같은 질문이라도 어떻게 표현하느냐에 따라 AI의 답변이 완전히 달라집니다.
파인튜닝을 시작하기 전에 "좋은 입력이란 무엇인가"를 먼저 이해해야 합니다.
나중에 RAG와 자동화 파이프라인을 연결할 때 프롬프트 설계가 핵심이 됩니다.

**English**
The same question phrased differently can produce completely different AI responses.
Before fine-tuning, it's essential to understand what makes a good input.
Prompt design will be the core skill when we later connect RAG and automation pipelines.

---

## 🛠️ 실행 명령어 | Commands

### Step 1 — 현재 설치된 모델 확인 | Check installed models
```bash
ollama list
```

### Step 2 — 비교할 모델 다운로드 | Download comparison model

> 📝 실제 실행: `gemma4:e2b`와 `qwen3.5:2b` 두 모델로 비교 진행

```bash
ollama run qwen3.5:2b
```

### Step 3 — 같은 질문으로 두 모델 비교 | Compare two models with the same prompt

**gemma4:e2b 실행**
```bash
ollama run gemma4:e2b
```
아래 질문을 입력하고 답변을 기록하세요:
```
1인 기업을 운영하는 사람에게 AI가 어떻게 도움이 될 수 있어?
```

**qwen3.5:2b 실행**
```bash
ollama run qwen3.5:2b
```
같은 질문을 입력하고 답변을 비교하세요.

### Step 4 — 프롬프트 실험 | Prompt experiments

같은 주제를 다르게 물어보는 실험입니다. gemma4:e2b에서 아래를 순서대로 입력해보세요:

**실험 1 — 짧은 질문**
```
이메일 자동화란?
```

**실험 2 — 역할 부여**
```
너는 1인 기업 전문 컨설턴트야. 이메일 자동화 방법을 알려줘.
```

**실험 3 — 조건 추가**
```
너는 1인 기업 전문 컨설턴트야. 기술을 잘 모르는 초보자도 이해할 수 있게 이메일 자동화 방법을 3단계로 설명해줘.
```

---

## 📊 실험 결과 기록 | Experiment Results

### 비교 실험 — "1인 기업을 운영하는 사람에게 AI가 어떻게 도움이 될 수 있어?"

**gemma4:e2b 답변**

(여기에 직접 작성)

---

**qwen3.5:2b 답변**

(여기에 직접 작성)

---

### 프롬프트 실험 1 — "이메일 자동화란?"

**gemma4:e2b 답변**

(여기에 직접 작성)

---

**qwen3.5:2b 답변**

(여기에 직접 작성)

---

### 프롬프트 실험 2 — "너는 1인 기업 전문 컨설턴트야. 이메일 자동화 방법을 알려줘."

**gemma4:e2b 답변**

(여기에 직접 작성)

---

**qwen3.5:2b 답변**

(여기에 직접 작성)

---

### 프롬프트 실험 3 — "너는 1인 기업 전문 컨설턴트야. 기술을 잘 모르는 초보자도 이해할 수 있게 이메일 자동화 방법을 3단계로 설명해줘."

**gemma4:e2b 답변**

(여기에 직접 작성)

---

**qwen3.5:2b 답변**

(여기에 직접 작성)

---

### 📝 실험 총평 | Summary

| 항목 | gemma4:e2b | qwen3.5:2b |
|------|-----------|-----------|
| 답변 스타일 | | |
| 한국어 품질 | | |
| 답변 길이 | | |
| 속도 | | |

---

### Step 5 — 대화 종료 | Exit
```
/bye
```

### Step 6 — 설치된 모델 최종 확인 | Final model list check
```bash
ollama list
```

---

## ✅ 성공 조건 | Success Criteria

- [ ] `ollama list` 에서 기존 모델 확인
- [ ] `qwen3.5:2b` 모델 다운로드 완료
- [ ] 두 모델에 같은 질문 → 답변 차이 확인
- [ ] 프롬프트 3가지 실험 완료
- [ ] 실험 결과 메모 (어떤 프롬프트가 더 좋았는지)

---

## 🚨 막혔을 때 | Troubleshooting

**모델이 중간에 멈추거나 응답이 너무 길어지면**
```
Ctrl + C
```
중단 후 더 짧게 질문하거나 `/bye`로 종료 후 재실행하세요.

**메모리 부족 오류가 나오면**
더 작은 모델 사용:
```bash
ollama run tinyllama
```

**설치된 모델 삭제하고 싶으면**
```bash
ollama rm qwen3.5:2b
```

---

## 📅 다음 단계 | Next Step

**Day 006**: Python으로 Ollama API를 연동해서 코드로 AI를 호출합니다.
**Day 006**: Connect Ollama API with Python and call AI from code.

---

[[../Cravveo_100Day_Master_Guide]] | [[../Daily_Log/2026-05-28_Day005_Log|Day 005 로그]] | [[Day005_YouTube_Upload|Day 005 유튜브]] | [[../4일차/2026-05-27_Day004_Work_Order|← Day 004]] | [[../6일차/2026-05-29_Day006_Work_Order|Day 006 →]]

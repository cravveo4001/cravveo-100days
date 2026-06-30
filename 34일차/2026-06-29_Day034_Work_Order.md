# 📋 Day 034 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-29
> **단계** | Phase: Day 034 / 100 — Phase 3

---

## 💻 노트북 사양 & 사용 모델 | Hardware & Model

| 항목 Item | 사양 Spec |
|------|------|
| 노트북 Laptop | 한성 TFX5556U |
| CPU | AMD Ryzen 5 5560U |
| RAM | 16GB |
| GPU | AMD Radeon Vega (내장 Integrated) |
| OS | Linux (Ubuntu) |
| 사용 모델 Model | cravveo:latest (Llama 3.2 3B + LoRA, q8_0 GGUF) |
| 작업 환경 Environment | 로컬 Ollama + Python + cron |

---

## 🗺️ 100일 전체 로드맵 | Roadmap

| 단계 Phase | 내용 Content | 상태 Status |
|------|------|------|
| Day 001~015 | Phase 1: 환경 구축 + RAG Environment + RAG | ✅ 완료 Done |
| Day 016~029 | Phase 2: 파인튜닝 + 로컬 배포 Fine-tuning + local deploy | ✅ 완료 Done |
| Day 030~033 | Phase 3 시작: 품질 개선 + RAG 통합 + API Quality + RAG + API | ✅ 완료 Done |
| **Day 034** | **아침 브리핑 자동화 업그레이드 Morning briefing upgrade** | 🔥 오늘 Today |
| Day 035~ | 유튜브 스크립트 자동화 YouTube script automation | ⏳ 예정 Next |
| Day 100 | 1인 기업 자동화 시스템 완성 Automation complete | 🎯 목표 Goal |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 010에서 만든 아침 브리핑 자동화는 기본 모델(qwen2.5:1.5b)을 사용합니다.
> 크라베오에 대한 설명을 하드코딩으로 넣어줘야 했습니다.
> 오늘은 이걸 크라베오 AI(cravveo 모델)로 교체합니다.
> 파인튜닝된 모델은 크라베오를 이미 알고 있으니까, 하드코딩이 필요 없습니다.

**English**
> Day 010's morning briefing uses a base model (qwen2.5:1.5b).
> It needed hard-coded Cravveo context to answer correctly.
> Today we replace it with our fine-tuned cravveo model.
> The fine-tuned model already knows Cravveo — no hard-coding needed.

---

## 📌 Before vs After | 변경 전후 비교

| 항목 Item | Day 010 (기존 Before) | Day 034 (오늘 After) |
|------|------|------|
| 모델 Model | qwen2.5:1.5b (기본) | cravveo:latest (파인튜닝) |
| 크라베오 지식 | 하드코딩 (CRAVVEO_CONTEXT) | 모델이 이미 알고 있음 |
| API 방식 | requests + /api/generate | ollama 라이브러리 |
| 답변 품질 | 컨텍스트 의존 | 자체 지식으로 답변 |

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — 기존 briefing.py 백업 | Backup existing script

```bash
cd ~/finetuning-project/10일차
cp briefing.py briefing_old.py
```

---

### Step 2 — 새 브리핑 스크립트 작성 | Write new briefing script

기존 구조는 유지하면서 모델과 API 방식만 교체합니다.
Keep the existing structure, only replace the model and API method.

핵심 변경:
- `requests.post()` → `ollama.chat()`
- `model: "qwen2.5:1.5b"` → `model: "cravveo"`
- `CRAVVEO_CONTEXT` 하드코딩 제거 (모델이 이미 알고 있음)

---

### Step 3 — 수동 테스트 | Manual Test

```bash
cd ~/projects/cravveo_ai
source venv/bin/activate
python3 ~/finetuning-project/10일차/briefing.py
```

브리핑이 정상 생성되는지 확인.
Verify briefing generates correctly.

---

### Step 4 — cron 설정 확인 | Verify cron Setup

```bash
crontab -l
```

기존 cron이 어떻게 설정되어 있는지 확인하고, 필요하면 가상환경 경로를 업데이트.
Check existing cron setup and update venv path if needed.

---

### Step 5 — cron 테스트 실행 | Test cron Execution

cron에서 실행될 때와 동일한 환경으로 테스트.
Test in the same environment cron will use.

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] 기존 briefing.py 백업 완료 | Backup complete
- [ ] 새 스크립트에서 cravveo 모델로 브리핑 생성 | New script generates briefing with cravveo
- [ ] 하드코딩된 CRAVVEO_CONTEXT 없이 정확한 답변 | Correct answers without hard-coded context
- [ ] cron 설정 확인 및 업데이트 | cron verified and updated
- [ ] **자동 실행 테스트 성공** | **Auto-execution test passed** ← 핵심 Key
- [ ] 영상 녹화 완료 | Video recorded

---

## 🔧 트러블슈팅 | Troubleshooting

**cron에서 ollama 모듈을 못 찾을 때 | cron can't find ollama module**
→ cron은 가상환경을 모름. 스크립트 안에서 venv Python 경로를 직접 지정해야 함.
→ cron doesn't know about venv. Must specify venv Python path in the script.
→ 예: `/home/c/projects/cravveo_ai/venv/bin/python3`

**Ollama 서버가 안 켜져 있을 때 | Ollama server not running**
→ cron 실행 시 Ollama가 꺼져있으면 오류
→ `systemctl status ollama`로 확인

**답변이 느릴 때 | Slow response**
→ 3B q8_0 모델은 CPU에서 10~30초 걸림 (정상)
→ 3B q8 model takes 10-30s on CPU (normal)

---

## 📅 다음 단계 예고 | Next Up

**Day 035** — 유튜브 스크립트 자동 생성 | YouTube Script Auto-Generation
크라베오 AI가 Day별 유튜브 영상 스크립트 초안을 자동 작성합니다.

Cravveo AI auto-generates YouTube video script drafts for each Day.

---

[[2026-06-29_Day034_Work_Order|Day 034 작업지시서]] | [[../33일차/2026-06-28_Day033_Work_Order|← Day 033]] | [[../Cravveo_100Day_Master_Guide]]

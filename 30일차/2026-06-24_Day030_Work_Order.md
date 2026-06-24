# 📋 Day 030 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-24
> **단계** | Phase: Day 030 / 100

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
| 사용 모델 | Llama 3.2 1B Instruct (Unsloth + LoRA) |
| 작업 환경 | Google Colab (T4 GPU) + 로컬 Ollama |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | Phase 1-A: 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | Phase 1-B: AnythingLLM + RAG + Phase 1 회고 | ✅ 완료 |
| Day 016~029 | Phase 2: 코랩 파인튜닝 + 모델 저장 + 로컬 배포 | ✅ 완료 |
| **Day 030** | **Phase 2 회고 + Phase 3 계획** | 🔥 오늘 |
| Day 031~050 | Phase 3: 품질 개선 + 로컬 RAG 통합 + 자동화 | ⏳ 예정 |
| Day 051~075 | Phase 4: 실전 활용 + 서비스화 | ⏳ 예정 |
| Day 076~100 | Phase 5: 최적화 + 1인 기업 자동화 시스템 완성 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 100일 중 30일이 지났습니다. 전체의 30%.
> Phase 2 (파인튜닝 챕터)가 완료됐습니다.
> 오늘은 지난 14일간의 파인튜닝 여정을 돌아보고,
> 앞으로 70일의 방향을 설계합니다.

**English**
> 30 days out of 100. 30% complete.
> Phase 2 (fine-tuning chapter) is done.
> Today we review the 14-day fine-tuning journey
> and design the direction for the remaining 70 days.

---

# 📊 Phase 2 전체 회고 | Phase 2 Retrospective

## Phase 2 타임라인 (Day 016~029)

| Day | 한 일 | 핵심 성과 |
|-----|------|---------|
| 016 | RAG vs 파인튜닝 비교 + 코랩 GPU 첫 가동 | 파인튜닝 필요성 확인, T4 GPU 첫 사용 |
| 017 | 코랩 라이브러리 6개 설치 | 파인튜닝 환경 구축 완료 |
| 018 | Unsloth + Gemma 2B 모델 로드 | FastLanguageModel 첫 사용 |
| 019 | JSONL 포맷 분석 + 변환 스크립트 | 데이터 파이프라인 시작 |
| 020+021 | 크라베오 데이터셋 수동 제작 | 정체성 데이터 10개 + 전체 46개 |
| 022 | HuggingFace 로그인 | 토큰 보안 실수 → Secrets 방식 학습 |
| 023 | HuggingFace 업로드 + cron 자동화 | 데이터 파이프라인 완성 |
| 024 | 모델 + 데이터 연결 | 파인튜닝 뼈대 코드 완성 |
| 025 | LoRA + SFTTrainer 첫 학습 | loss 25.5→15.4, CUDA 오류 해결 |
| **026** | **Gemma→Llama 3.2 모델 교체** | **3일간의 사투 끝에 loss 1200→3.4** |
| **027** | **데이터 확장 + Before/After** | **AI가 크라베오를 처음으로 정확히 답함** |
| 028 | LoRA 가중치 저장 + 재로드 | 파이프라인 완성 (학습→저장→불러오기) |
| **029** | **GGUF 변환 + Ollama 등록** | **내 컴퓨터에서 내 AI 실행** |

---

## Phase 2 핵심 수치

| 항목 | 수치 |
|------|------|
| 소요 기간 | 14일 (Day 016~029) |
| 최종 모델 | Llama 3.2 1B Instruct |
| 데이터셋 | 83개 (크라베오 전용 Q&A) |
| 학습 설정 | 30 epoch, lr 5e-5, batch 1, grad_accum 4 |
| 최종 loss | 0.08 |
| GGUF 크기 | 771MB (q4_k_m) |
| HuggingFace | cravveo/cravveo-llama-lora |
| 로컬 실행 | `ollama run cravveo` |

---

## Phase 2 핵심 교훈 5가지

### 1. 모델 호환성이 코드보다 중요하다
Gemma 2B + Unsloth에서 어떤 포맷을 써도 loss 1200.
Llama 3.2로 바꾸니까 같은 코드에서 loss 3.4.
**같은 코드 + 같은 데이터 + 다른 모델 = 완전히 다른 결과.**

### 2. 디버깅은 가장 작은 단위로 테스트
데이터 3개짜리 초간단 테스트로 Gemma 문제를 확정.
복잡한 상황에서는 변수를 하나씩 줄여가면 원인이 보인다.

### 3. 쉬는 것도 전략이다
3시간 삽질한 뒤 하루 쉬고 오니까 30분 만에 해결.
막혀있을 때는 머리를 식히는 게 답이다.

### 4. 데이터 품질이 양보다 중요하다
62개 데이터 중 40개가 LLM 생성 쓰레기.
필터링 후 29개 깨끗한 데이터 + 50개 수동 작성 = 83개로 성공.

### 5. 파인튜닝은 진짜로 작동한다
Before: "유대인 종목... 주식 재단..." → After: "IT 프로그램 개발, 1인 기업이야."
83개 데이터 + 30 epoch이면 1B 모델도 정확히 학습한다.

---

## Phase 2에서 만든 자산

| 자산 | 위치 | 설명 |
|------|------|------|
| 데이터셋 | HuggingFace cravveo/cravveo-briefing-dataset | 83개 Q&A |
| LoRA 어댑터 | HuggingFace cravveo/cravveo-llama-lora | 학습된 가중치 45MB |
| GGUF 모델 | 로컬 29일차/ | 771MB, q4_k_m |
| Ollama 모델 | `ollama run cravveo` | 로컬 실행 가능 |
| 코랩 노트북 | Google Colab | 전체 파이프라인 코드 |

---

# 🗺️ Phase 3 계획 | Phase 3 Plan (Day 031~050)

## Phase 3 목표

> **"크라베오를 아는 AI"를 "크라베오를 위해 일하는 AI"로 업그레이드한다.**

Phase 2에서는 AI가 크라베오를 "아는" 수준까지 왔습니다.
Phase 3에서는 이 AI를 실제 업무에 연결합니다.

---

## Phase 3 로드맵 (잠정)

| Day | 내용 | 목표 |
|-----|------|------|
| 031 | 답변 품질 개선 — 데이터 200개 확장 + 3B 모델 시도 | 로컬 답변 품질 향상 |
| 032 | Ollama + AnythingLLM 연결 | 파인튜닝 모델로 RAG 구동 |
| 033 | 옵시디언 문서 RAG + 파인튜닝 모델 | 내 문서를 아는 크라베오 AI |
| 034~035 | Python API 서버 구축 | Ollama API로 외부 연동 |
| 036~038 | 아침 브리핑 자동화 업그레이드 | 크라베오 AI가 브리핑 생성 |
| 039~040 | 유튜브 스크립트 자동 생성 | AI가 Day별 스크립트 초안 작성 |
| 041~043 | 이메일/알림 자동화 | 중요 정보 자동 요약 + 알림 |
| 044~046 | 쇼핑몰 상품 설명 자동 생성 | AI가 상품 문구 작성 |
| 047~048 | 전체 시스템 통합 테스트 | 자동화 파이프라인 연결 |
| 049~050 | Phase 3 회고 + Phase 4 계획 | 중간 점검 |

---

## Phase 3 핵심 기술 스택 추가

| 기존 (Phase 1~2) | 추가 (Phase 3) |
|-----------------|---------------|
| Ollama | Ollama API (Python 연동) |
| AnythingLLM | AnythingLLM + 파인튜닝 모델 |
| cron + briefing.py | 크라베오 AI 기반 자동 브리핑 |
| HuggingFace 데이터셋 | 200+ 데이터셋 확장 |
| GGUF q4_k_m | 3B 모델 + q8_0 양자화 |

---

## ✅ 성공 조건 체크리스트

- [ ] Phase 2 타임라인 정리
- [ ] 핵심 교훈 5가지 정리
- [ ] Phase 3 로드맵 작성
- [ ] 영상 녹화 완료

---

## 📅 다음 단계 예고 | Next Up

**Day 031** — 답변 품질 개선: 데이터 200개 확장 + 3B 모델 시도
로컬 Ollama에서 돌아가는 크라베오 AI의 답변 품질을 올립니다.

Day 031 — Quality Improvement: 200+ dataset + 3B model trial
Improve the local Cravveo AI's response quality.

---

[[2026-06-24_Day030_Work_Order|Day 030 작업지시서]] | [[../29일차/2026-06-23_Day029_Work_Order|← Day 029]] | [[../Cravveo_100Day_Master_Guide]]

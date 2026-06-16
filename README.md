# Cravveo Company — 100일 AI 파인튜닝 도전기
# Cravveo Company — 100-Day AI Fine-Tuning Challenge

> 쌩초보가 로컬 AI 파인튜닝으로 1인 기업 자동화 시스템을 만드는 과정을 기록합니다.
> A complete beginner building a one-person business automation system with local AI fine-tuning — documented in public.

🎥 [YouTube 채널 | YouTube Channel](https://www.youtube.com/channel/UC1tM_t2Tn_w6BxHT3lrgodw)

---

## 현재 진행 상황 | Progress

| Day | 내용 | Content | 상태 |
|-----|------|---------|------|
| Day 001 | 리눅스 개발 환경 구축 | Linux dev environment setup | ✅ 완료 |
| Day 002 | 작업 폴더 + Python 가상환경 구성 | Project folder + Python venv | ✅ 완료 |
| Day 003 | Git 초기화 + GitHub 첫 push | Git init + first GitHub push | ✅ 완료 |
| Day 004 | Ollama 설치 + 로컬 LLM 첫 실행 | Ollama install + first local LLM run | ✅ 완료 |
| Day 005 | Ollama 모델 비교 + 프롬프트 실습 | Compare models + prompt practice | ✅ 완료 |
| Day 006 | Python으로 Ollama API 연동 + AI 호출 | Python Ollama API integration | ✅ 완료 |
| Day 007 | AI 답변 자동 저장 스크립트 완성 | Auto-save AI answers to text file | ✅ 완료 |
| Day 008 | 터미널 대화 루프 구현 | Terminal chat loop | ✅ 완료 |
| Day 009 | 대화 내용 파일 저장 챗봇 | Chat log saving chatbot | ✅ 완료 |
| Day 010 | Python 자동화 미니 프로젝트 (아침 브리핑 + cron) | Python automation + cron scheduler | ✅ 완료 |
| Day 011 | AnythingLLM 설치 + GUI 첫 대화 | AnythingLLM install + first GUI chat | ✅ 완료 |
| Day 012 | AnythingLLM + Ollama 연결 + 워크스페이스 첫 대화 | AnythingLLM + Ollama connect + first workspace chat | ✅ 완료 |
| Day 013 | RAG 첫 실전 — 내 문서를 AI에게 먹이기 Before/After | First real RAG test — feed my document to local AI | ✅ 완료 |
| Day 014 | 옵시디언 문서 17개 RAG 업로드 + 모델 3번 교체 | Obsidian docs RAG upload + 3 model switches | ✅ 완료 |
| Day 015 | Phase 1 전체 회고 — 14일 타임라인 + 핵심 교훈 | Phase 1 full retrospective — 14-day timeline | ✅ 완료 |
| Day 016 | RAG vs 파인튜닝 비교 + 코랩 GPU 첫 가동 | RAG vs Fine-Tuning + first Colab GPU run | ✅ 완료 |
| Day 017 | 코랩 파이썬 가상 스택 구축 — 필수 라이브러리 6개 설치 | Colab fine-tuning library stack setup | ✅ 완료 |
| Day 018 | Unsloth 소개 — 속도 2~5배↑ 메모리 60%↓ + 모델 로드 | Unsloth intro + Gemma 2B load via FastLanguageModel | ✅ 완료 |
| Day 019 | JSONL 포맷 분석 + 브리핑→JSONL 자동 변환 스크립트 | JSONL format analysis + auto-conversion script | ✅ 완료 |
| Day 020+021 | 크라베오 데이터셋 수동 제작 + JSONL 변환 완성 | Manual dataset creation + JSONL pipeline complete | ✅ 완료 |
| Day 022 | HuggingFace 로그인 + 토큰 보안 실수 공개 | HuggingFace login + token security mistake shared | ✅ 완료 |
| Day 023 | 데이터셋 HuggingFace 업로드 + cron 자동화 파이프라인 완성 | Dataset upload to HuggingFace + cron auto-pipeline | ✅ 완료 |
| Day 024 | Unsloth 모델 로드 + HuggingFace 데이터셋 연결 — 파인튜닝 뼈대 완성 | Unsloth model load + HuggingFace dataset connect — skeleton complete | ✅ 완료 |
| Day 025 | LoRA 어댑터 설정 + SFTTrainer + 첫 학습 실행 | LoRA adapter + SFTTrainer + first training run | 🔥 진행 중 |
| Day 040~ | Google Colab GPU LoRA 파인튜닝 | Google Colab GPU LoRA fine-tuning | ⏳ 예정 |
| Day 060~ | 가중치 회수 → GGUF → Ollama 등록 | Weights → GGUF → Ollama deploy | ⏳ 예정 |
| Day 080~ | Obsidian + 로컬 RAG 연결 | Obsidian + local RAG integration | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | One-person business automation complete | 🎯 목표 |

---

## 프로젝트 소개 | About This Project

**한국어**
이 저장소는 AI를 전혀 모르는 초보자가 로컬 AI 파인튜닝부터 1인 기업 자동화까지 직접 구축하는 100일 도전 기록입니다.
전문가 강의가 아닙니다. 막히고, 에러 나고, 해결하는 과정을 있는 그대로 기록합니다.

**English**
This repository documents a 100-day challenge where a complete beginner builds a local AI fine-tuning workflow and one-person business automation from scratch.
This is not an expert tutorial. It's a raw learning journal — including errors, dead ends, and breakthroughs.

---

## 폴더 구조 | Folder Structure

```
cravveo-100days/
├── 1일차/          Day 001 작업 파일, 영상, 유튜브 업로드 문서
├── 2일차/          Day 002 작업 파일, 영상, 유튜브 업로드 문서
├── 3일차/          Day 003 작업 파일, 영상, 유튜브 업로드 문서
├── 4일차/          Day 004 작업 파일, 영상, 유튜브 업로드 문서
├── 5일차/          Day 005 작업 파일, 영상, 유튜브 업로드 문서
├── 6일차/          Day 006 작업 파일, 영상, 유튜브 업로드 문서
├── 7일차/          Day 007 작업 파일, 영상, 유튜브 업로드 문서
├── 8일차/          Day 008 작업 파일, 영상, 유튜브 업로드 문서
├── 9일차/          Day 009 작업 파일, 영상, 유튜브 업로드 문서
├── 10일차/         Day 010 작업 파일, 영상, 유튜브 업로드 문서
├── 11일차/         Day 011 작업 파일, 영상, 유튜브 업로드 문서
├── 12일차/         Day 012 작업 파일, 영상, 유튜브 업로드 문서
├── 13일차/         Day 013 작업 파일, 영상, 유튜브 업로드 문서
├── 14일차/         Day 014 작업 파일, 영상, 유튜브 업로드 문서
├── 15일차/         Day 015 작업 파일, 영상, 유튜브 업로드 문서
├── 16일차/         Day 016 작업 파일, 영상, 유튜브 업로드 문서
├── 17일차/         Day 017 작업 파일, 영상, 유튜브 업로드 문서
├── 18일차/         Day 018 작업 파일, 영상, 유튜브 업로드 문서
├── 19일차/         Day 019 작업 파일, 영상, 유튜브 업로드 문서
├── 20일차/         Day 020+021 작업 파일, 영상, 유튜브 업로드 문서
├── 21일차/         Day 021 작업 파일
├── 22일차/         Day 022 작업 파일, 영상, 유튜브 업로드 문서
├── 23일차/         Day 023 작업 파일, 영상, 유튜브 업로드 문서
├── 24일차/         Day 024 작업 파일, 영상, 유튜브 업로드 문서
├── Daily_Log/      날짜별 작업 로그
├── Assets/         이미지, 스크린샷, 썸네일
└── Templates/      문서 템플릿
```

---

## 기술 스택 | Tech Stack

- **OS**: Ubuntu Linux
- **로컬 LLM**: Ollama + Gemma4
- **파인튜닝**: Google Colab + Unsloth (LoRA)
- **RAG**: AnythingLLM
- **데이터셋**: HuggingFace Hub
- **자동화**: cron + Python pipeline
- **노트**: Obsidian
- **버전 관리**: Git + GitHub

---

## Day별 링크 | Day Links

| Day | 작업지시서 | 유튜브 업로드 문서 |
|-----|-----------|-----------------|
| Day 001 | [작업지시서](2026-05-23_Day001_Work_Order.md) | [업로드 문서](1일차/Day001_YouTube_Upload.md) |
| Day 002 | [작업지시서](2일차/2026-05-25_Day002_Work_Order.md) | [업로드 문서](2일차/Day002_YouTube_Upload.md) |
| Day 003 | [작업지시서](3일차/2026-05-26_Day003_Work_Order.md) | [업로드 문서](3일차/Day003_YouTube_Upload.md) |
| Day 004 | [작업지시서](4일차/2026-05-27_Day004_Work_Order.md) | [업로드 문서](4일차/Day004_YouTube_Upload.md) |
| Day 005 | [작업지시서](5일차/2026-05-28_Day005_Work_Order.md) | [업로드 문서](5일차/Day005_YouTube_Upload.md) |
| Day 006 | [작업지시서](6일차/2026-05-29_Day006_Work_Order.md) | [업로드 문서](6일차/Day006_YouTube_Upload.md) |
| Day 007 | [작업지시서](7일차/2026-05-30_Day007_Work_Order.md) | [업로드 문서](7일차/Day007_YouTube_Upload.md) |
| Day 008 | [작업지시서](8일차/2026-05-31_Day008_Work_Order.md) | [업로드 문서](8일차/Day008_YouTube_Upload.md) |
| Day 009 | [작업지시서](9일차/2026-06-01_Day009_Work_Order.md) | [업로드 문서](9일차/Day009_YouTube_Upload.md) |
| Day 010 | [작업지시서](10일차/2026-06-02_Day010_Work_Order.md) | [업로드 문서](10일차/Day010_YouTube_Upload.md) |
| Day 011 | [작업지시서](11일차/2026-06-03_Day011_Work_Order.md) | [업로드 문서](11일차/Day011_YouTube_Upload.md) |
| Day 012 | [작업지시서](12일차/2026-06-04_Day012_Work_Order.md) | [업로드 문서](12일차/Day012_YouTube_Upload.md) |
| Day 013 | [작업지시서](13일차/2026-06-05_Day013_Work_Order.md) | [업로드 문서](13일차/Day013_YouTube_Upload.md) |
| Day 014 | [작업지시서](14일차/2026-06-06_Day014_Work_Order.md) | [업로드 문서](14일차/Day014_YouTube_Upload.md) |
| Day 015 | [작업지시서](15일차/2026-06-07_Day015_Work_Order.md) | [업로드 문서](15일차/Day015_YouTube_Upload.md) |
| Day 016 | [작업지시서](16일차/2026-06-08_Day016_Work_Order.md) | [업로드 문서](16일차/Day016_YouTube_Upload.md) |
| Day 017 | [작업지시서](17일차/2026-06-09_Day017_Work_Order.md) | [업로드 문서](17일차/Day017_YouTube_Upload.md) |
| Day 018 | [작업지시서](18일차/2026-06-10_Day018_Work_Order.md) | [업로드 문서](18일차/Day018_YouTube_Upload.md) |
| Day 019 | [작업지시서](19일차/2026-06-11_Day019_Work_Order.md) | [업로드 문서](19일차/Day019_YouTube_Upload.md) |
| Day 020+021 | [작업지시서](20일차/2026-06-12_Day020+021_Work_Order.md) | [업로드 문서](20일차/Day020+021_YouTube_Upload.md) |
| Day 022 | [작업지시서](22일차/2026-06-14_Day022_Work_Order.md) | [업로드 문서](22일차/Day022_YouTube_Upload.md) |
| Day 023 | [작업지시서](23일차/2026-06-15_Day023_Work_Order.md) | [업로드 문서](23일차/Day023_YouTube_Upload.md) |
| Day 024 | [작업지시서](24일차/2026-06-16_Day024_Work_Order.md) | [업로드 문서](24일차/Day024_YouTube_Upload.md) |

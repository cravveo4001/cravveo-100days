# Cravveo Company — 100일 AI 파인튜닝 도전기
# Cravveo Company — 100-Day AI Fine-Tuning Challenge

> 쌩초보가 로컬 AI 파인튜닝으로 1인 기업 자동화 시스템을 만드는 과정을 기록합니다.
> A complete beginner building a one-person business automation system with local AI fine-tuning — documented in public.

🎥 [YouTube 채널 | YouTube Channel](https://www.youtube.com/channel/UC1tM_t2Tn_w6BxHT3lrgodw)
🤗 [데이터셋 | Dataset](https://huggingface.co/datasets/cravveo/cravveo-briefing-dataset)
🤖 [파인튜닝 모델 | Fine-tuned Model](https://huggingface.co/cravveo/cravveo-llama-lora)
📒 [코랩 노트북 | Colab Notebook](https://colab.research.google.com/drive/1o8xlRk_v5ACE32CKQpF2I3rhOV68efSY?usp=sharing)

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
| Day 025 | LoRA 어댑터 설정 + SFTTrainer + 첫 학습 실행 — loss 25.5→15.4 확인 | LoRA adapter + SFTTrainer + first training run — loss confirmed | ✅ 완료 |
| Day 026 | 3일간의 사투 — Gemma 실패 → Llama 3.2 교체 → loss 3.4 정상화 | 3-day battle — Gemma fail → Llama 3.2 switch → loss normalized | ✅ 완료 |
| Day 027 | 데이터 83개 확장 + Before/After — AI가 크라베오를 처음으로 정확히 답함 | Dataset expansion + Before/After — AI answers Cravveo correctly | ✅ 완료 |
| Day 028 | LoRA 가중치 저장 + HuggingFace 업로드 + 재로드 성공 | LoRA weights saved + HuggingFace upload + reload test passed | ✅ 완료 |
| Day 029 | GGUF 변환 + 로컬 Ollama에 내 AI 등록 — 내 컴퓨터에서 실행 | GGUF conversion + local Ollama registration — runs on my laptop | ✅ 완료 |
| Day 030 | Phase 2 전체 회고 + Phase 3 계획 — 30일 마일스톤 | Phase 2 retrospective + Phase 3 plan — 30-day milestone | ✅ 완료 |
| Day 031 | 2일간의 삽질 — 모델이 아니라 형식(TEMPLATE)이 문제였다 | 2-day debug — format mismatch was the real cause | ✅ 완료 |
| Day 032 | AnythingLLM + 파인튜닝 모델 통합 — 크라베오 AI 어시스턴트 | AnythingLLM + fine-tuned model — Cravveo AI assistant | ✅ 완료 |
| Day 033 | Python으로 크라베오 AI 호출 + 아침 브리핑 생성 테스트 | Python Ollama API + morning briefing test | ✅ 완료 |
| Day 034 | 아침 브리핑 자동화를 크라베오 AI로 업그레이드 — cron 연결 완성 | Morning briefing upgraded to Cravveo AI — cron connected | ✅ 완료 |
| Day 035 | 유튜브 스크립트 자동 생성 함수 완성 + 마이크로 첫 음성 녹음 | YouTube script generator + first mic narration | ✅ 완료 |
| Day 036 | Phase 3 점검 — 지금까지 만든 것 정리 + 64일 수정 로드맵 확정 | Phase 3 review — inventory of completed work + revised 64-day roadmap | ✅ 완료 |
| Day 037 | Obsidian 데이터 추출 스크립트 — Daily_Log 36개 → 203개 Q&A 자동 생성 | Obsidian data extractor — 36 daily logs → 203 Q&A pairs auto-generated | ✅ 완료 |
| Day 038 | q4_0 양자화 변환 + AnythingLLM RAG 버그 3개 발견/수정 (에이전트 모드, 검색 설정, 문맥 조각 수) | q4_0 quantization + found/fixed 3 AnythingLLM RAG bugs (agent mode, search settings, context chunk count) | ✅ 완료 |
| Day 039 | q4_K_M 재변환으로 모델 품질 문제 해결 + RAG 문서 보강 실험(실패, 구조적 한계 확인) | Fixed model quality with q4_K_M re-conversion + RAG document-hint experiment (failed, confirmed structural limit) | ✅ 완료 |
| Day 040 | 날짜→Day 룩업 프로토타입 완성 + 300일 로드맵 재점검 + 불편함_기록.md 신설 | Date-lookup prototype + 300-day roadmap re-check + started pain-points log | ✅ 완료 |
| Day 041 | 학습 데이터 오염 발견(92개 중 40개 무관) → 20개로 교체 + 재학습 → cravveo:v5 | Found training-data contamination (40/92 unrelated) → replaced with 20 clean samples + retrained → cravveo:v5 | ✅ 완료 |
| Day 042 | v5 체계적 테스트 → 실패, 비율 조정 재시도(v6) → 더 심한 실패 → v4로 복귀 | Systematic v5 testing → failed, rebalance retry (v6) → worse failure → reverted to v4 | ✅ 완료 |
| Day 043~ | Part 1 계속 (정체성 데이터 비율 튜닝은 보류) | Part 1 continues (identity data ratio tuning on hold) | ⏳ 예정 |
| Day 100 | Part 1 마무리 | Part 1 wrap-up | 🎯 목표 |

---

## 프로젝트 소개 | About This Project

**한국어**
이 저장소는 AI를 전혀 모르는 초보자가 로컬 AI 파인튜닝부터 1인 기업 자동화까지 직접 구축하는 100일 도전 기록입니다.
전문가 강의가 아닙니다. 막히고, 에러 나고, 해결하는 과정을 있는 그대로 기록합니다.

**English**
This repository documents a 100-day challenge where a complete beginner builds a local AI fine-tuning workflow and one-person business automation from scratch.
This is not an expert tutorial. It's a raw learning journal — including errors, dead ends, and breakthroughs.

📍 [300일 로드맵 | 300-Day Roadmap](2026-07-01_Special_Roadmap_Design.md) — Part 1(Day 1~100)은 기존 툴 사용 + 불편함 기록, Part 3(Day 201~300)에서 직접 개발
📝 [불편함 기록 | Pain Points Log](불편함_기록.md) — Part 1에서 발견한 기존 툴의 한계들

---

## 폴더 구조 | Folder Structure

```
cravveo-100days/
├── 1일차~30일차/   Day 001~030 작업 파일 | Work files, YouTube upload docs
├── Daily_Log/      날짜별 작업 로그 | Daily work logs
├── Assets/         이미지, 스크린샷, 썸네일 | Images, screenshots, thumbnails
└── Templates/      문서 템플릿 | Document templates
```

---

## 기술 스택 | Tech Stack

| 분야 | Category | 도구 | Tools |
|------|----------|------|-------|
| OS | OS | Ubuntu Linux | Ubuntu Linux |
| 로컬 LLM | Local LLM | Ollama | Ollama |
| 파인튜닝 | Fine-tuning | Google Colab + Unsloth (LoRA) + Llama 3.2 3B | Google Colab + Unsloth (LoRA) + Llama 3.2 3B |
| RAG | RAG | AnythingLLM | AnythingLLM |
| 데이터셋 | Dataset | HuggingFace Hub | HuggingFace Hub |
| 자동화 | Automation | cron + Python 파이프라인 | cron + Python pipeline |
| 노트 | Notes | Obsidian | Obsidian |
| 버전 관리 | Version Control | Git + GitHub | Git + GitHub |

---

## Day별 링크 | Day Links

| Day | 작업지시서 Work Order | 유튜브 업로드 YouTube Upload |
|-----|---------------------|---------------------------|
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
| Day 025 | [작업지시서](25일차/2026-06-17_Day025_Work_Order.md) | [업로드 문서](25일차/Day025_YouTube_Upload.md) |
| Day 026 | [작업지시서](26일차/2026-06-20_Day026_Work_Order.md) | [업로드 문서](26일차/Day026_YouTube_Upload.md) |
| Day 027 | [작업지시서](27일차/2026-06-21_Day027_Work_Order.md) | [업로드 문서](27일차/Day027_YouTube_Upload.md) |
| Day 028 | [작업지시서](28일차/2026-06-22_Day028_Work_Order.md) | [업로드 문서](28일차/Day028_YouTube_Upload.md) |
| Day 029 | [작업지시서](29일차/2026-06-23_Day029_Work_Order.md) | [업로드 문서](29일차/Day029_YouTube_Upload.md) |
| Day 030 | [작업지시서](30일차/2026-06-24_Day030_Work_Order.md) | [업로드 문서](30일차/Day030_YouTube_Upload.md) |
| Day 031 | [작업지시서](31일차/2026-06-25_Day031_Work_Order.md) | [업로드 문서](31일차/Day031_YouTube_Upload.md) |
| Day 032 | [작업지시서](32일차/2026-06-27_Day032_Work_Order.md) | [업로드 문서](32일차/Day032_YouTube_Upload.md) |
| Day 033 | [작업지시서](33일차/2026-06-28_Day033_Work_Order.md) | [업로드 문서](33일차/Day033_YouTube_Upload.md) |
| Day 034 | [작업지시서](34일차/2026-06-29_Day034_Work_Order.md) | [업로드 문서](34일차/Day034_YouTube_Upload.md) |
| Day 035 | [작업지시서](35일차/2026-06-30_Day035_Work_Order.md) | [업로드 문서](35일차/Day035_YouTube_Upload.md) |
| Day 036 | [작업지시서](36일차/2026-07-02_Day036_Work_Order.md) | [업로드 문서](36일차/Day036_YouTube_Upload.md) |
| Day 037 | [작업지시서](37일차/2026-07-03_Day037_Work_Order.md) | [업로드 문서](37일차/Day037_YouTube_Upload.md) |
| Day 038 | [작업지시서](38일차/2026-07-04_Day038_Work_Order.md) | [업로드 문서](38일차/Day038_YouTube_Upload.md) |
| Day 039 | [작업지시서](39일차/2026-07-07_Day039_Work_Order.md) | [업로드 문서](39일차/Day039_YouTube_Upload.md) |
| Day 040 | [작업지시서](40일차/2026-07-08_Day040_Work_Order.md) | [업로드 문서](40일차/Day040_YouTube_Upload.md) |
| Day 041 | [작업지시서](41일차/2026-07-09_Day041_Work_Order.md) | [업로드 문서](41일차/Day041_YouTube_Upload.md) |
| Day 042 | [작업지시서](42일차/2026-07-11_Day042_Work_Order.md) | - |

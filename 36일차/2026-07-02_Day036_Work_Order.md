# 📋 Day 036 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-07-02
> **단계** | Phase: Day 036 / 100 — Phase 3

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
| 작업 환경 Environment | 로컬 Ollama + Python |
| 🎙️ 녹음 방식 | 음성 내레이션 (BGM 없음, Day 050까지) |

---

## 🎙️ 오늘 말할 멘트 | Today's Narration Script

**오프닝**
> "안녕하세요 크라베오입니다. Day 036이에요.
> 오늘은 지금까지 만든 것들을 점검하고 앞으로 64일 계획을 세워볼 거예요.
> 어제 번외편에서 큰 그림을 잡았는데, 오늘은 구체적인 로드맵을 확정합니다."

**작업 중**
> "원래 계획보다 30일이나 앞서 있어요.
> GGUF 변환이 Day 45 계획이었는데 Day 29에 끝냈고,
> AnythingLLM 연동도 Day 61 계획이었는데 Day 32에 끝냈어요."

**클로징**
> "Day 037부터는 Obsidian 데이터로 파인튜닝 고도화 시작합니다. 감사합니다."

---

## 🗺️ 수정된 64일 로드맵 | Revised 64-Day Roadmap

| 기간 | 주제 | 내용 |
|------|------|------|
| **Day 036** | Phase 3 점검 | 지금까지 만든 것 정리 + 64일 계획 수립 |
| **Day 037~045** | 데이터 고도화 | Obsidian + GitHub → JSONL 자동 추출 → 재학습 |
| **Day 046~060** | 로컬 RAG 구축 | ChromaDB + Obsidian 노트 벡터 검색 |
| **Day 061~075** | 자동화 스크립트 | 수익 조회, 유튜브 통계 Python 스크립트 |
| **Day 076~090** | 파인튜닝 + RAG 합체 | 내 AI + 내 지식창고 통합 |
| **Day 091~100** | Part 1 총정리 | 100일 회고 + Part 2 예고 |

---

## 📦 지금까지 만든 것 | What We've Built

| 완성물 | 파일 | 설명 |
|------|------|------|
| 파인튜닝 모델 | cravveo:latest | Llama 3.2 3B + LoRA, q8_0 GGUF |
| Modelfile | 31일차/Modelfile-3b-final | 학습 형식과 일치하는 TEMPLATE |
| AI 호출 함수 | 33일차/cravveo_ai.py | ask_cravveo() 재사용 함수 |
| 브리핑 스크립트 | 10일차/briefing.py | 짧은 질문 풀 + 수동 실행 |
| 스크립트 작성기 | 35일차/cravveo_script_writer.py | 유튜브 스크립트 초안 생성 |
| HuggingFace 모델 | cravveo/cravveo-llama-lora | LoRA 어댑터 업로드 완료 |
| 데이터셋 | cravveo/cravveo-briefing-dataset | 학습 데이터 83개 |
| RAG 연동 | AnythingLLM | 파인튜닝 모델 + 문서 검색 통합 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 1. 지금까지 만든 것들 전체 점검
> 2. 원래 계획 vs 실제 진행 비교 분석
> 3. Day 036~100 수정 로드맵 확정

**English**
> 1. Full review of everything built so far
> 2. Compare original plan vs actual progress
> 3. Confirm revised roadmap for Day 036~100

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] 지금까지 만든 것 목록 정리 | Inventory of completed work
- [ ] 수정 로드맵 확정 | Revised roadmap confirmed
- [ ] 영상 녹화 완료 | Video recorded
- [ ] 작업지시서 + 데일리로그 작성 | Work order + daily log written
- [ ] 커밋 + 푸시 완료 | Commit + push complete

---

## 📅 다음 단계 예고 | Next Up

**Day 037** — Obsidian 데이터 추출 스크립트 작성 시작
Day 037 — Start writing Obsidian data extraction script

---

[[../35일차/2026-06-30_Day035_Work_Order|← Day 035]] | [[../Cravveo_100Day_Master_Guide]]

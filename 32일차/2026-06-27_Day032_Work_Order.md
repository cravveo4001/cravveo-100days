# 📋 Day 032 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-27
> **단계** | Phase: Day 032 / 100 — Phase 3

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
| 사용 모델 | cravveo:latest (Llama 3.2 3B + LoRA, q8_0 GGUF) |
| 작업 환경 | 로컬 Ollama + AnythingLLM |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기 | Roadmap

| 단계 | Phase | 내용 | Content | 상태 |
|------|-------|------|---------|------|
| Day 001~015 | Phase 1 | 환경 구축 + RAG | Environment + RAG | ✅ 완료 |
| Day 016~029 | Phase 2 | 파인튜닝 + 로컬 배포 | Fine-tuning + local deploy | ✅ 완료 |
| Day 030 | 회고 | Phase 2 회고 + Phase 3 계획 | Retrospective | ✅ 완료 |
| Day 031 | Phase 3 | 데이터 확장 + TEMPLATE 문제 해결 | Data + format fix | ✅ 완료 |
| **Day 032** | **Phase 3** | **Ollama + AnythingLLM 연결 — 파인튜닝 모델로 RAG** | **Fine-tuned RAG** | 🔥 오늘 |
| Day 033~ | Phase 3 | Python API 서버 + 자동화 연결 | API + automation | ⏳ 예정 |
| Day 100 | 목표 | 1인 기업 자동화 시스템 완성 | Automation complete | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 011~014에서 AnythingLLM + Ollama로 RAG를 구축했습니다.
> Day 016~031에서 크라베오를 아는 파인튜닝 모델을 만들었습니다.
> 오늘은 이 두 가지를 합칩니다.
> AnythingLLM의 LLM 백엔드를 기본 모델 대신 **내가 파인튜닝한 cravveo 모델**로 교체합니다.
> "크라베오를 아는 AI" + "내 문서를 검색하는 RAG" = **크라베오 전용 AI 어시스턴트**

**English**
> Day 011~014: built RAG with AnythingLLM + Ollama.
> Day 016~031: created a fine-tuned model that knows Cravveo.
> Today we combine both.
> Replace AnythingLLM's LLM backend with our fine-tuned cravveo model.
> "AI that knows Cravveo" + "RAG that searches my docs" = **Cravveo AI Assistant**

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
지금까지 파인튜닝 모델과 RAG는 따로 놀고 있었습니다.
- 파인튜닝 모델: 크라베오에 대해 알지만, 최신 문서는 모름
- RAG: 최신 문서를 검색하지만, 크라베오 스타일로 답하지 않음

둘을 합치면:
- 크라베오 지식 + 최신 문서 검색 + 크라베오 스타일 답변
- 이게 **진짜 1인 기업 AI 어시스턴트**의 시작

**English**
Fine-tuned model and RAG have been separate until now.
Combining them creates a real AI assistant: Cravveo knowledge + document search + Cravveo-style answers.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — AnythingLLM 실행

터미널에서:
```bash
cd ~/앱
./AnythingLLMDesktop.AppImage
```

---

### Step 2 — LLM 백엔드를 cravveo 모델로 변경

AnythingLLM 화면에서:
1. 왼쪽 하단 ⚙️ (설정) 클릭
2. **LLM Preference** (또는 AI 모델 설정) 클릭
3. Provider: **Ollama** 선택
4. Ollama Base URL: `http://localhost:11434` (기본값)
5. **모델 선택**: `cravveo:latest` ← 핵심!
6. 저장

---

### Step 3 — 워크스페이스에서 테스트

1. 기존 워크스페이스 열기 (또는 새로 만들기)
2. 테스트 질문:

```
크라베오 컴퍼니가 뭐야?
```

이 질문에 파인튜닝된 답변이 나오면 성공!

---

### Step 4 — RAG 테스트 (문서 업로드 + 질문)

1. 워크스페이스에 옵시디언 문서 또는 프로젝트 문서 업로드
2. 문서 내용에 대한 질문:

```
오늘 작업지시서의 성공 조건이 뭐야?
```

파인튜닝 지식 + 문서 검색이 합쳐진 답변이 나오면 **Phase 1 + Phase 2 통합 완성**!

---

### Step 5 — 기본 모델 vs 파인튜닝 모델 비교

1. LLM을 `llama3.2:3b` (기본)로 바꿔서 같은 질문
2. LLM을 `cravveo:latest` (파인튜닝)로 바꿔서 같은 질문
3. 답변 차이 비교

---

## ✅ 성공 조건 체크리스트 | Success Criteria

- [ ] AnythingLLM 실행 확인
- [ ] LLM 백엔드를 cravveo:latest로 변경
- [ ] "크라베오가 뭐야?" 질문에 파인튜닝 답변 확인
- [ ] 문서 업로드 후 RAG 질문 테스트
- [ ] **파인튜닝 지식 + RAG 검색이 합쳐진 답변 확인** ← 핵심
- [ ] 기본 모델 vs 파인튜닝 모델 비교
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅 | Troubleshooting

**AnythingLLM에서 cravveo 모델이 안 보일 때**
→ Ollama가 실행 중인지 확인: `ollama list`
→ AnythingLLM 설정에서 Ollama URL이 `http://localhost:11434`인지 확인
→ 모델 목록 새로고침

**cravveo 모델이 "Unknown"이라고 답할 때**
→ AnythingLLM이 질문을 채팅 템플릿으로 감싸서 보낼 수 있음
→ Day 031에서 배운 교훈: 형식 불일치 문제일 수 있음
→ AnythingLLM의 프롬프트 설정에서 형식 조정 필요

**답변이 너무 느릴 때**
→ 3B q8_0 모델(3.4GB)은 CPU에서 좀 느림
→ 정상적으로 10~30초 정도 걸릴 수 있음

---

## 📅 다음 단계 예고 | Next Up

**Day 033** — Python Ollama API 서버 구축
크라베오 모델을 Python 코드에서 호출할 수 있게 API를 만듭니다.
아침 브리핑 자동화에 파인튜닝 모델을 연결하는 첫 단계.

Day 033 — Python Ollama API Server
Build an API to call the cravveo model from Python code.
First step to connecting the fine-tuned model to morning briefing automation.

---

[[2026-06-27_Day032_Work_Order|Day 032 작업지시서]] | [[../31일차/2026-06-25_Day031_Work_Order|← Day 031]] | [[../Cravveo_100Day_Master_Guide]]

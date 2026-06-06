# 📋 Day 014 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-06
> **단계** | Phase: Day 014 / 100

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~005 | 환경 구축 + Ollama + 모델 실습 | ✅ 완료 |
| Day 006~010 | Python 자동화 기초 챕터 | ✅ 완료 |
| Day 011 | AnythingLLM 설치 — 오프라인 RAG 챕터 시작 | ✅ 완료 |
| Day 012 | AnythingLLM + Ollama 연결 + 워크스페이스 첫 대화 | ✅ 완료 |
| Day 013 | RAG 첫 실전 — 내 문서를 AI에게 먹이기 Before/After | ✅ 완료 |
| **Day 014** | **옵시디언 문서 다량 RAG 업로드 — 내 프로젝트를 AI가 기억하게 만들기** | 🔥 오늘 |
| Day 015 | Phase 1 총평 및 회고 | ⏳ 예정 |
| Day 016~ | 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> Day 013에서 문서 1개로 RAG가 작동한다는 걸 확인했습니다.
> 오늘은 실제 프로젝트 문서들을 대량으로 업로드합니다.
> 작업지시서, 유튜브 업로드 문서 등 내가 직접 쓴 문서들을
> AI가 기억하게 만들고, "Day 010이 뭐야?", "채널 방향이 뭐야?" 같은 질문에 답하게 합니다.

**English**
> Day 013 confirmed RAG works with one document.
> Today we upload real project documents in bulk.
> Work orders, YouTube upload docs — documents I actually wrote.
> Make AI remember my project and answer questions like "What is Day 010?" or "What is the channel direction?"

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
문서 1개짜리 RAG는 데모입니다.
진짜 RAG는 내 문서 전체를 AI가 참고해서 답하는 것입니다.
오늘부터 AI가 내 100일 프로젝트를 "알게" 됩니다.

**English**
One-document RAG is a demo.
Real RAG is AI referencing your entire document base to answer.
From today, AI will "know" my 100-day project.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — AnythingLLM 워크스페이스 준비

1. AnythingLLM 실행
2. `cravveo-test` 워크스페이스 확인 (어제 만든 곳)
3. 문서 업로드 버튼 클릭 (↑ 아이콘)

---

### Step 2 — 문서 선택 및 업로드

아래 문서들을 순서대로 업로드합니다:

```
finetuning-project/
├── Cravveo_100Day_Master_Guide.md   ← 반드시 포함
├── Cravveo_Channel_Direction.md     ← 반드시 포함
├── 10일차/Day010_YouTube_Upload.md
├── 11일차/Day011_YouTube_Upload.md
├── 12일차/Day012_YouTube_Upload.md
├── 13일차/Day013_YouTube_Upload.md
└── 13일차/cravveo_intro.txt
```

업로드 후 각 문서 **"임베드"** 버튼 클릭 확인

---

### Step 3 — 질문 테스트

아래 질문들로 RAG 동작 확인:

```
1. 크라베오 컴퍼니 채널 방향이 뭐야?
2. Day 010에서 뭘 했어?
3. 크라베오 컴퍼니 기술 스택이 뭐야?
4. 100일 프로젝트 목표가 뭐야?
5. Day 013 슬로건이 뭐야?
```

---

### Step 4 — 결과 기록

| 질문 | AI 답변 | 출처 문서 | 정확도 |
|------|---------|----------|--------|
| 채널 방향이 뭐야? | | | |
| Day 010에서 뭘 했어? | | | |
| 기술 스택이 뭐야? | | | |

---

## ✅ 성공 조건 체크리스트

- [ ] 문서 5개 이상 업로드 + 임베딩 완료
- [ ] "크라베오 컴퍼니 채널 방향이 뭐야?" → 정확한 답변
- [ ] "Day 010에서 뭘 했어?" → Day 010 내용으로 답변
- [ ] "100일 프로젝트 목표가 뭐야?" → 정확한 답변
- [ ] 출처(Sources) 표시 확인

---

## 🔧 트러블슈팅

**임베딩이 느릴 때**
→ 정상입니다. 문서가 많을수록 시간이 걸립니다. 기다리세요.

**Ollama 연결 오류 뜰 때**
```bash
sudo systemctl restart ollama
```

**답변이 엉뚱할 때**
→ 해당 내용이 담긴 문서가 임베딩됐는지 확인. 워크스페이스에 문서가 "연결"된 상태인지 확인.

---

## 📅 다음 단계 예고 | Next Up

**Day 015** — Phase 1 총평 및 회고
Day 001~014까지 전체 회고. 무엇을 배웠고 무엇이 남았는지 정리합니다.
Day 015 — Phase 1 wrap-up and retrospective.
Review Days 001~014 — what was learned and what comes next.

---

[[2026-06-06_Day014_Work_Order|Day 014 작업지시서]] | [[../13일차/Day013_YouTube_Upload|← Day 013 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

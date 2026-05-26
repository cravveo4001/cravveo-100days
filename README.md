# Cravveo Command Center

Cravveo 100일 프로젝트의 옵시디언 시작 문서입니다.

이 Vault는 로컬 AI, Google Colab 파인튜닝, 오프라인 RAG, 1인 기업 자동화 구축 과정을 기록합니다.

---

## 빠른 시작

1. [[Cravveo_Channel_Direction|채널 방향성]]
2. [[Cravveo_100Day_Master_Guide|100일 마스터 가이드]]
3. [[2026-05-23_Day001_Work_Order|Day 001 작업지시서]]
4. [[Daily_Log/2026-05-23_Day001_Log|Day 001 작업 로그]]
5. [[1일차/Day001_YouTube_Upload|Day 001 유튜브 업로드 문서]]
6. [[2일차/2026-05-25_Day002_Work_Order|Day 002 작업지시서]]
7. [[Daily_Log/2026-05-25_Day002_Log|Day 002 작업 로그]]
8. [[2일차/Day002_YouTube_Upload|Day 002 유튜브 업로드 문서]]
9. [[Gemini_BGM_Prompts|Gemini BGM 프롬프트]]
10. [[YouTube_Channel_Setup_Cravveo_Company|YouTube 채널 생성 설정]]
11. [[Agent_Handover_Protocol|에이전트 인계 프로토콜]]

---

## 현재 상태

- 현재 Day: Day 002
- 오늘 목표: Python 가상환경 생성
- 완료 상태: Day 002 착수 준비 완료

---

## 프로젝트 흐름

1. 로컬 리눅스 개발 환경 구축
2. Ollama 기반 로컬 LLM 실행
3. AnythingLLM 기반 오프라인 RAG 실험
4. Google Colab GPU 기반 LoRA 파인튜닝
5. 학습 가중치 로컬 회수
6. GGUF 변환 및 Ollama 등록
7. 옵시디언 지식 저장소와 로컬 RAG 결합
8. 1인 기업 업무 자동화

---

## 폴더

- [[Daily_Log/2026-05-23_Day001_Log|Daily Log]]
- [[Templates/Daily_Log_Template|Daily Log Template]]
- `Assets/`: 이미지, 스크린샷, 녹화 자료 보관
- `1일차/`, `2일차/`, `3일차/` ...: 각 Day별 영상, 업로드 문서, 썸네일, 메모를 한꺼번에 보관

---

## Day별 보관 규칙

앞으로 모든 작업 자료는 Day 단위 폴더에 모읍니다.

예시:

```text
1일차/
  1일차.mp4
  Day001_YouTube_Upload.md

2일차/
  2일차.mp4
  Day002_YouTube_Upload.md

3일차/
  3일차.mp4
  Day003_YouTube_Upload.md
```

각 Day 폴더에는 가능한 한 아래 자료를 함께 둡니다.

1. 원본 또는 편집 영상
2. 유튜브 제목/설명/해시태그/태그/고정댓글 문서
3. 해당 Day 썸네일
4. 해당 Day 썸네일 이미지 생성 프롬프트
5. Gemini 배경음악 생성 프롬프트 10개
6. 녹화 중 메모 또는 오류 기록
7. 필요하면 BGM/자막/스크린샷 자료

유튜브 업로드 문서 작성 규칙:

1. 제목은 한국어와 영어를 함께 넣습니다.
2. 설명은 한국어 설명 뒤에 영어 설명을 함께 넣습니다.
3. 해시태그는 한국어/영어 키워드를 함께 넣습니다.
4. 고정 댓글도 가능하면 한국어와 영어를 함께 넣습니다.
5. 각 Day 업로드 문서에는 썸네일 프롬프트와 Gemini BGM 프롬프트 10개를 함께 작성합니다.

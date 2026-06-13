# Day 021 YouTube Upload

> 영상 파일: `21일차.mp4`
> 썸네일: `day021-jsonl-script-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 021 | JSONL 변환 스크립트 완성 + 46개 전체 데이터셋 완성 — 코랩 오류도 해결
```
*(70자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 021.
Cravveo Company 100-Day Project, Day 021.

오늘은 손으로 쓴 데이터를 파이썬으로 관리하는 스크립트를 완성하고, 전체 데이터셋 46개를 완성했습니다.
Today I wrote a Python script to manage the dataset through code and completed the full 46-entry dataset.

오늘 한 일 | What I did today:
- 텍스트 → JSONL 변환 파이썬 스크립트 작성 | Wrote text→JSONL conversion script
- JSONL 형식 검증 코드 실행 | Ran JSONL validation code
- 브리핑 36개 + 정체성 10개 = 46개 전체 데이터셋 완성 | Completed 46-entry full dataset
- 코랩 torch/torchvision 충돌 오류 해결 | Fixed torch/torchvision conflict in Colab

오늘의 에러 & 해결 | Error & fix:
코랩에서 라이브러리 설치 후 torchvision 버전 충돌로 Unsloth import 실패.
원인: pip install이 torch를 2.10 → 2.12로 올리면서 torchvision(0.25.0)과 충돌.
해결: `!pip install --upgrade "torchvision>=0.27.0"` 실행 후 런타임 재시작.

Error in Colab: torchvision version conflict caused Unsloth import to fail.
Cause: pip install upgraded torch from 2.10 to 2.12, conflicting with torchvision 0.25.0.
Fix: Run `!pip install --upgrade "torchvision>=0.27.0"`, then restart runtime.

오늘의 핵심 발견 | Key discovery today:
데이터가 10개일 때는 손으로 써도 됩니다.
100개, 1000개가 되면 코드 없이는 불가능합니다.
파이썬 스크립트를 쓰면 내용만 채우면 되고, 형식은 코드가 알아서 잡아줍니다.
이제 데이터를 코드로 관리할 수 있게 됐습니다.

With 10 entries, hand-writing works.
With 100 or 1000, it's impossible without code.
With the Python script, you only fill in the content — the code handles the format.
Now we can manage the dataset through code.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 022에서는 HuggingFace CLI 로그인을 설정합니다.
완성된 데이터셋을 HuggingFace에 올리기 위한 계정 연결을 합니다.
In Day 022, we'll set up HuggingFace CLI login.
Connecting Colab to HuggingFace to upload our completed dataset.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
📓 Google Colab: https://colab.research.google.com/drive/1YpjfWZW8FMtYRMKyDCWT_QNKiyq0AH1v

#Cravveo #파인튜닝 #FineTuning #JSONL #Python #데이터셋 #Dataset #구글코랩 #GoogleColab #BuildInPublic #AI초보
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, JSONL, JSONL 변환, 파이썬 스크립트, Python script, 파인튜닝 데이터셋, fine-tuning dataset, 학습 데이터, training data, HuggingFace, 허깅페이스, 구글 코랩, Google Colab, torchvision 오류, torch conflict, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 학습 일지, learning journal
```

---

### 고정 댓글

```text
Day 021 완료 | Day 021 Complete
JSONL 변환 스크립트 완성 + 전체 데이터셋 46개 완성.
Completed JSONL conversion script and full 46-entry dataset.

오늘의 에러 & 해결 | Error & fix:
torch 2.12.0 + torchvision 0.25.0 충돌 → Unsloth import 실패 💥
!pip install --upgrade "torchvision>=0.27.0" → 런타임 재시작 → 해결 ✅

현재 데이터셋 현황 | Dataset status:
- 브리핑 자동화 데이터: 36개 | Briefing auto-data: 36 entries
- 크라베오 정체성 수동 데이터: 10개 | Cravveo identity manual data: 10 entries
- 전체 합계: 46개 | Total: 46 entries

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
📓 Google Colab: https://colab.research.google.com/drive/1YpjfWZW8FMtYRMKyDCWT_QNKiyq0AH1v

다음 Day 022 | Next Day 022
HuggingFace CLI 로그인 — 완성된 데이터셋을 허깅페이스에 올리는 준비.
HuggingFace CLI Login — getting ready to upload our dataset.
```

---

### 커뮤니티 게시물

```text
Day 021 완료 ✅ | Day 021 Complete ✅

오늘은 JSONL 변환 스크립트를 완성하고, 전체 데이터셋 46개를 완성했습니다.
Today I completed the JSONL conversion script and the full 46-entry dataset.

오늘 배운 것:
데이터가 10개일 때는 손으로 써도 됩니다.
1000개가 되면 코드 없이는 불가능합니다.
파이썬 스크립트 하나로 내용만 채우면 형식은 자동으로 잡힙니다.

What I learned:
Hand-writing works for 10 entries. Not for 1000.
With a Python script, fill in the content — code handles the format.

오늘의 에러: torch/torchvision 버전 충돌
해결: torchvision 업그레이드 한 줄로 해결

Today's error: torch/torchvision version conflict
Fix: one line to upgrade torchvision

---

Day 022 예고 | Day 022 Preview
HuggingFace CLI 로그인 — 46개 데이터셋을 허깅페이스에 올리는 준비.
HuggingFace CLI Login — preparing to upload 46 entries to HuggingFace.

#Cravveo #파인튜닝 #JSONL #Python #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `21일차.mp4` 선택
- [ ] 제목 입력 (70자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day021-jsonl-script-thumbnail-1280x720.png` 등록
- [ ] 공개 범위는 먼저 `비공개`로 업로드
- [ ] HD 처리 완료 확인
- [ ] 설명/해시태그/태그 확인
- [ ] 고정 댓글 작성
- [ ] 커뮤니티 게시물 작성
- [ ] 최종 공개 또는 예약 공개

---

## 썸네일 이미지 프롬프트

```text
Create a 1280x720 YouTube thumbnail for a Korean tech learning video.

Channel: Cravveo Company.
Episode: Day 021.
Topic: a complete beginner writing a Python script that converts hand-written Q&A data into JSONL format, and completing a 46-entry fine-tuning dataset. Also fixed a torch/torchvision version conflict in Colab.

Main text must be large and readable:
"DAY 021"
"데이터셋 완성"

Small supporting text:
"46개 완성"
"오류도 해결"

Visual style:
- visual metaphor: handwritten notes transforming into clean structured code/data, a pipeline being completed
- show a sense of completion — pieces coming together into one final file
- clean tech documentary style
- mood: "it's all coming together" — organized, complete, satisfying
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 021" and "데이터셋 완성" text prominent, completion/pipeline visual clear.
```

---

## Gemini BGM 프롬프트 10개

### 1. Day 021 기본 배경음

```text
Cravveo Company Day 021 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 손으로 쓴 데이터를 파이썬 스크립트로 변환하고 전체 데이터셋을 완성하는 날이야.
"조각들이 하나로 완성된다"는 정리되고 성취감 있는 분위기가 담겼으면 좋겠어.
no vocals, 가사 없음, clean electronic, organized and satisfying, 85 BPM, loopable.
```

### 2. 변환 스크립트 작성 파트

```text
배경음악을 만들어줘. 텍스트 데이터를 JSONL로 변환하는 파이썬 스크립트를 작성하는 파트야.
코드가 형식을 자동으로 잡아주는 편리함을 처음 느끼는 분위기가 담겼으면 좋겠어.
methodical coding energy, clean electronic, focused and precise, no vocals, 가사 없음, loopable.
```

### 3. JSONL 검증 코드 파트

```text
배경음악을 만들어줘. 저장된 JSONL 파일의 각 줄이 정상인지 검사하는 코드를 실행하는 파트야.
"오류 0개" 결과가 나오는 꼼꼼한 확인의 분위기가 담겼으면 좋겠어.
careful verification mood, steady electronic, calm and precise, no vocals, 가사 없음, loopable.
```

### 4. 코랩 오류 발생 파트

```text
배경음악을 만들어줘. 코랩에서 torch/torchvision 버전 충돌로 Unsloth import가 실패하는 파트야.
"또 오류야?" 당황하면서도 침착하게 원인을 찾는 분위기가 담겼으면 좋겠어.
tense but calm, problem-solving electronic, investigative mood, no vocals, 가사 없음, loopable.
```

### 5. 오류 해결 순간

```text
배경음악을 만들어줘. torchvision 업그레이드 한 줄로 오류가 해결되는 순간이야.
"이게 답이었어?" 간단한 해결에서 오는 시원한 성취감이 담겼으면 좋겠어.
quick relief and satisfaction, bright electronic chime, clean resolution, no vocals, 가사 없음, loopable.
```

### 6. 데이터셋 합치기 파트

```text
배경음악을 만들어줘. 브리핑 36개와 정체성 10개를 합쳐서 cravveo_full_dataset.jsonl 46개를 완성하는 파트야.
여러 조각이 하나로 완성되는 마무리의 분위기가 담겼으면 좋겠어.
completion energy, merging rhythm, clean electronic, satisfying close, no vocals, 가사 없음, loopable.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI learning journey.
Episode theme: writing a Python script to convert hand-written Q&A data into JSONL, fixing a Colab version conflict, and completing a 46-entry fine-tuning dataset.
Mood: quiet completion, "the pipeline is working", organized and grounded.
Style: clean electronic, minimal, methodical energy, no vocals, 가사 없음.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 021 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 데이터를 코드로 완성한다" 라는 분위기가 담겼으면 좋겠어.
short electronic opener, pipeline completion energy, clean and focused, no vocals, 가사 없음.
```

### 9. 엔딩 — 데이터셋 완성

```text
Create calm but satisfying ending music for a YouTube episode where a beginner completes their first full fine-tuning dataset — 46 entries combining automated briefing data and hand-written identity data — and fixes a Colab version conflict along the way.
Mood: quiet completion, the dataset is ready, something real is about to begin.
Style: warm electronic pad, gentle resolution, subtle forward momentum, no vocals, 가사 없음, 80-88 BPM.
```

### 10. Day 022 예고 파트

```text
배경음악을 만들어줘. 다음 날 HuggingFace CLI 로그인을 설정하고 완성된 데이터셋을 업로드한다는 예고 파트야.
"드디어 내 데이터가 인터넷에 올라간다"는 새로운 단계의 기대감이 담겼으면 좋겠어.
upload anticipation, rising electronic, new stage energy, no vocals, 가사 없음, loopable.
```

---

[[2026-06-13_Day021_Work_Order|Day 021 작업지시서]] | [[../20일차/Day020_YouTube_Upload|← Day 020 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

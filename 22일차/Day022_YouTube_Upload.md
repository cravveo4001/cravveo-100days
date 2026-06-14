# Day 022 YouTube Upload

> 영상 파일: `22일차.mp4`
> 썸네일: `day022-huggingface-login-thumbnail-1280x720.png`

---

## 바로 복사해서 쓰는 최종본

### 제목

```text
AI 초보의 100일 도전 Day 022 | HuggingFace 로그인 완료 — 토큰 보안 실수도 공개합니다
```
*(56자)*

---

### 설명

```text
Cravveo Company 100일 프로젝트 Day 022.
Cravveo Company 100-Day Project, Day 022.

오늘은 완성된 46개 데이터셋을 HuggingFace에 올리기 위한 계정 로그인을 완료했습니다.
Today I completed the HuggingFace account login to prepare for uploading the 46-entry dataset.

오늘 한 일 | What I did today:
- HuggingFace 토큰 발급 (Write 권한) | Generated HuggingFace access token (Write permission)
- 코랩 노트북 처음부터 재정리 | Reorganized Colab notebook from scratch
- Colab Secrets에 토큰 안전하게 보관 | Stored token securely in Colab Secrets
- HuggingFace 로그인 완료 확인 | Confirmed successful HuggingFace login

오늘의 실수 & 해결 | Mistake & fix:
토큰을 token.txt 파일로 저장했다가 GitHub에 올라갈 뻔했습니다.
공개 노트북에 토큰을 직접 쓰면 누구나 볼 수 있습니다.
해결: Colab Secrets(🔑) 에 저장 → userdata.get('HF_TOKEN') 으로 불러오기.
토큰에 줄바꿈 문자가 섞여서 오류가 난 것도 공개합니다.
⚠️ 영상에 노출된 토큰은 즉시 삭제하고 새로 발급했습니다. 영상 속 토큰은 사용 불가입니다.

Mistake: Almost committed the token to GitHub inside token.txt.
Putting tokens directly in a public notebook exposes them to everyone.
Fix: Store in Colab Secrets (🔑) → load with userdata.get('HF_TOKEN').
Also sharing the LocalProtocolError caused by a newline in the token.
⚠️ The token shown in the video was immediately revoked and replaced. It is no longer valid.

오늘의 핵심 발견 | Key discovery today:
토큰은 절대 파일로 저장하거나 코드에 직접 쓰면 안 됩니다.
Colab Secrets는 구글 계정에 암호화 저장되어 노트북에 흔적이 남지 않습니다.
실수를 공개하는 것도 Build in Public입니다.

Never store tokens in files or write them directly in code.
Colab Secrets encrypts and stores tokens in your Google account — no trace left in the notebook.
Sharing mistakes is also part of Build in Public.

이 채널은 완성된 전문가 강의가 아닙니다.
This is not an expert tutorial channel.
AI를 잘 모르는 초보자가 직접 막히고 해결하는 과정을 기록합니다.
It is a beginner's learning journal, including mistakes, errors, and fixes.

Day 023에서는 완성된 46개 데이터셋을 HuggingFace에 실제로 업로드합니다.
In Day 023, we'll upload the completed 46-entry dataset to HuggingFace.

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
📓 Google Colab: https://colab.research.google.com/drive/1LWws9XZRvLGWL0-M7wqveZH201atf_6X?usp=sharing

#Cravveo #파인튜닝 #FineTuning #HuggingFace #허깅페이스 #ColabSecrets #토큰보안 #BuildInPublic #AI초보 #100일챌린지
```

---

### 태그

```text
Cravveo, Cravveo Company, AI 초보, beginner AI, 파인튜닝, fine tuning, HuggingFace, 허깅페이스, HuggingFace 로그인, HuggingFace login, Colab Secrets, 토큰 보안, token security, 구글 코랩, Google Colab, 코랩 비밀, 토큰 관리, access token, Build in Public, 100일 챌린지, 100 day challenge, Phase 2, 학습 일지, learning journal
```

---

### 고정 댓글

```text
Day 022 완료 | Day 022 Complete

HuggingFace 로그인 완료 + 토큰 보안 실수 공개.
Completed HuggingFace login + sharing a token security mistake.

오늘의 실수 & 해결 | Mistake & fix:
토큰을 token.txt 파일로 저장 → GitHub 올라갈 뻔 💥
Colab Secrets(🔑) 에 저장 → userdata.get('HF_TOKEN') 으로 불러오기 ✅
⚠️ 영상에 노출된 토큰은 즉시 삭제 후 재발급 완료. 영상 속 토큰은 사용 불가.
⚠️ Token shown in video was immediately revoked. It is no longer valid.

토큰 보안 3원칙 | Token security rules:
1. 코드에 직접 쓰지 않는다 | Never write directly in code
2. 파일로 저장하지 않는다 | Never save to a file
3. Colab Secrets에 저장한다 | Always use Colab Secrets

🔗 GitHub: https://github.com/cravveo4001/cravveo-100days
📓 Google Colab: https://colab.research.google.com/drive/1LWws9XZRvLGWL0-M7wqveZH201atf_6X?usp=sharing

다음 Day 023 | Next Day 023
HuggingFace에 46개 데이터셋 업로드 — 코드 한 줄로 불러올 수 있는 나만의 데이터셋 저장소 완성.
Uploading 46-entry dataset to HuggingFace — building a personal dataset repository.
```

---

### 커뮤니티 게시물

```text
Day 022 완료 ✅ | Day 022 Complete ✅

오늘은 HuggingFace 로그인을 완료했습니다.
그리고 실수도 공개합니다.
Today I completed HuggingFace login.
And I'm sharing a mistake.

오늘의 실수:
토큰을 token.txt 파일로 저장했다가 GitHub에 올라갈 뻔 했습니다.
공개 노트북에 토큰을 직접 쓰면 누구나 볼 수 있습니다.

Today's mistake:
Almost committed the token to GitHub inside token.txt.
Tokens written directly in public notebooks are visible to everyone.

해결 방법:
Colab Secrets(🔑) 에 저장하면 구글 계정에 암호화 저장됩니다.
코드에는 흔적이 남지 않아 공개 노트북에서도 안전합니다.

The fix:
Colab Secrets encrypts the token in your Google account.
No trace in the notebook — safe even in a public notebook.

실수를 공개하는 것도 Build in Public입니다.
Sharing mistakes is also part of Build in Public.

⚠️ 영상에 노출된 토큰은 즉시 삭제 후 재발급 완료. 영상 속 토큰은 사용 불가.
⚠️ Token shown in video was immediately revoked. It is no longer valid.


---

Day 023 예고 | Day 023 Preview
HuggingFace에 46개 데이터셋 업로드.
코드 한 줄로 언제든 불러올 수 있는 나만의 데이터셋 저장소를 만듭니다.
Uploading 46 entries to HuggingFace.
Building a personal dataset repository — one line of code to load it anytime.

#Cravveo #파인튜닝 #HuggingFace #ColabSecrets #토큰보안 #BuildInPublic #100일챌린지
```

---

## 업로드 체크리스트

- [ ] 영상 파일 `22일차.mp4` 선택
- [ ] 제목 입력 (56자 확인)
- [ ] 설명 입력
- [ ] 썸네일 `day022-huggingface-login-thumbnail-1280x720.png` 등록
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
Episode: Day 022.
Topic: a complete beginner setting up HuggingFace login in Google Colab using Colab Secrets for secure token storage — and sharing a token security mistake publicly as part of Build in Public.

Main text must be large and readable:
"DAY 022"
"HuggingFace 로그인"

Small supporting text:
"토큰 보안 실수 공개"
"Colab Secrets"

Visual style:
- visual metaphor: a key or lock representing secure token storage, HuggingFace logo element, connection being established
- two-part feeling: mistake (warning/caution) + solution (secure, locked)
- clean tech documentary style
- mood: "I made a mistake and fixed it — and I'm showing both" — honest and Build in Public
- beginner-friendly, not expert-guru
- no human face
- high contrast
- readable at small size
- no watermark

Composition:
large "DAY 022" and "HuggingFace 로그인" text prominent, security/key visual clear, honest mistake energy.
```

---

## Gemini BGM 프롬프트 10개

### 1. 기본 배경음

```text
Cravveo Company Day 022 영상에 사용할 배경음악 콘셉트를 만들어줘.
오늘은 HuggingFace 로그인을 완료하고, 토큰 보안 실수를 공개하는 날이야.
"실수를 공개하는 것도 성장이다"라는 솔직하고 차분한 분위기가 담겼으면 좋겠어.
no vocals, 가사 없음, warm electronic, honest and steady, 80 BPM, loopable.
```

### 2. 노트북 재정리 파트

```text
배경음악을 만들어줘. 뒤죽박죽이던 코랩 노트북을 처음부터 깔끔하게 재정리하는 파트야.
"혼란에서 정리로" 바뀌는 시원하고 정돈된 분위기가 담겼으면 좋겠어.
organizing energy, clean electronic, structured and tidy, no vocals, 가사 없음, loopable.
```

### 3. 토큰 실수 발견 파트

```text
배경음악을 만들어줘. 토큰을 파일로 저장했다가 GitHub에 올라갈 뻔한 걸 발견하는 파트야.
"아, 이거 위험한데?" 순간 긴장하는 분위기가 담겼으면 좋겠어.
tense realization, sudden caution, quiet alarm, no vocals, 가사 없음, loopable.
```

### 4. 실수 해결 파트

```text
배경음악을 만들어줘. Colab Secrets에 토큰을 안전하게 저장하고 문제를 해결하는 파트야.
"이제 안전하다"는 안도감과 정리된 느낌이 담겼으면 좋겠어.
relief and security, clean electronic, calm resolution, no vocals, 가사 없음, loopable.
```

### 5. LocalProtocolError 오류 파트

```text
배경음악을 만들어줘. 토큰에 줄바꿈 문자가 섞여서 LocalProtocolError가 나는 파트야.
"또 오류야..." 당황하지만 침착하게 원인을 찾는 분위기가 담겼으면 좋겠어.
debugging mood, steady electronic, calm problem-solving, no vocals, 가사 없음, loopable.
```

### 6. 로그인 성공 순간

```text
배경음악을 만들어줘. "사용자명: cravveo" 가 출력되면서 HuggingFace 로그인이 확인되는 순간이야.
작지만 확실한 연결 성공의 분위기가 담겼으면 좋겠어.
connection confirmed, small victory, warm electronic chime, no vocals, 가사 없음, loopable.
```

### 7. 다큐멘터리 톤

```text
Create understated documentary background music for a beginner's 100-day AI learning journey.
Episode theme: setting up secure HuggingFace login in Colab — making a token security mistake, fixing it with Colab Secrets, and sharing the whole process publicly as Build in Public.
Mood: honest and grounded, "mistakes are part of the journey", quiet authenticity.
Style: warm electronic, minimal, no vocals, 가사 없음.
```

### 8. 오프닝 15초

```text
Cravveo Company Day 022 영상 오프닝에 쓸 15초짜리 짧은 음악을 만들어줘.
"오늘은 HuggingFace에 연결하고, 실수도 공개한다" 라는 분위기가 담겼으면 좋겠어.
short electronic opener, honest and forward, warm and focused, no vocals, 가사 없음.
```

### 9. 엔딩

```text
Create calm but meaningful ending music for a YouTube episode where a beginner completes HuggingFace login, makes a token security mistake, fixes it with Colab Secrets, and shares it all publicly.
Mood: quiet honesty, "this is what real learning looks like", grounded and forward.
Style: warm electronic pad, gentle resolution, no vocals, 가사 없음, 78-85 BPM.
```

### 10. Day 023 예고 파트

```text
배경음악을 만들어줘. 다음 날 완성된 46개 데이터셋을 HuggingFace에 실제로 업로드한다는 예고 파트야.
"드디어 내 데이터가 인터넷에 올라간다"는 새로운 단계의 기대감이 담겼으면 좋겠어.
upload anticipation, rising electronic, new milestone energy, no vocals, 가사 없음, loopable.
```

---

[[2026-06-14_Day022_Work_Order|Day 022 작업지시서]] | [[../21일차/Day020+021_YouTube_Upload|← Day 020+021 유튜브]] | [[../Cravveo_100Day_Master_Guide]]

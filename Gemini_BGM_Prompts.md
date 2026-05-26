# Gemini BGM Prompts: Cravveo 배경음악 생성 프롬프트

> 목적: Cravveo 100일 프로젝트 영상에 사용할 배경음악 아이디어를 Gemini에게 요청할 때 쓰는 프롬프트 모음입니다.

---

## 1. 시리즈 공통 BGM 프롬프트

```text
Cravveo라는 100일 AI 구축 프로젝트 영상에 사용할 배경음악 콘셉트를 만들어줘.

이 프로젝트는 초보자가 리눅스 노트북, 로컬 AI, Google Colab, RAG, 파인튜닝, 자동화를 하나씩 배워가며 1인 기업용 AI 시스템을 만드는 기록형 콘텐츠야.

음악 분위기는 너무 웅장하거나 과장되지 않았으면 좋겠어.
차분하지만 앞으로 나아가는 느낌, 밤에 혼자 작업하는 집중감, 작은 성공을 쌓아가는 성장감을 담아줘.

원하는 스타일:
- lo-fi electronic
- soft synth
- light ambient
- minimal beat
- documentary background music

영상 말소리를 방해하지 않도록 보컬은 없고, 반복 재생해도 질리지 않는 루프형 음악이면 좋겠어.

이 조건에 맞는 배경음악 생성 프롬프트를 5개 만들어줘.
각 프롬프트에는 분위기, 악기, BPM, 사용 장면을 함께 적어줘.
```

---

## 2. Day 001 리눅스 세팅 영상용

```text
리눅스 터미널에서 Python, pip, venv, git을 설치하는 초보자 개발환경 세팅 영상에 어울리는 배경음악 프롬프트를 만들어줘.

영상은 화려한 튜토리얼이 아니라, 처음 시작하는 사람이 하나씩 확인하고 설치하는 실제 기록이야.

음악은 차분하고 깨끗해야 하고, 터미널 화면과 잘 어울려야 해.
긴장감은 약간 있어도 되지만 불안하거나 어둡지는 않았으면 좋겠어.
처음 프로젝트가 시작되는 설렘과 안정감을 동시에 담아줘.

조건:
- no vocals
- soft electronic
- minimal percussion
- warm synth pad
- 80-95 BPM
- loopable
- suitable for narration

이 조건으로 AI 음악 생성기에 넣을 영어 프롬프트 5개를 작성해줘.
```

---

## 3. 집중 작업용 Lo-fi 프롬프트

```text
Create background music for a Korean documentary-style YouTube series about a beginner building a local AI system over 100 days.

The scene shows Linux terminal work, Python setup, Git installation, Obsidian notes, and quiet late-night learning.

The music should feel focused, warm, calm, and quietly optimistic.
No vocals. No dramatic cinematic orchestra. No heavy bass.

Style:
- lo-fi electronic
- soft synth keys
- gentle vinyl texture
- light kick and snare
- subtle ambient pad
- 85 BPM
- seamless loop

Make it suitable as background music under spoken narration.
```

---

## 4. 오프닝 테마용 프롬프트

```text
Create a short opening theme for a YouTube series called Cravveo.

The series follows a complete beginner building a one-person AI company system using Linux, local AI, Google Colab fine-tuning, RAG, Obsidian, and automation.

The opening music should feel like the start of a long personal mission.
It should be hopeful, intelligent, clean, and modern.

Style:
- minimal electronic documentary theme
- warm analog synth
- soft piano accents
- gentle pulse
- no vocals
- no aggressive drums
- 15 to 25 seconds

The music should work before a spoken intro.
```

---

## 5. 엔딩/회고용 프롬프트

```text
Create calm ending music for a YouTube episode about a beginner completing the first day of a 100-day AI project.

The episode ends after successfully installing Python, pip, venv, and Git on Linux.
The mood should feel small but meaningful, like the first step of a long journey.

Style:
- soft ambient electronic
- gentle piano
- warm synth pad
- very light percussion
- no vocals
- 70 to 85 BPM
- peaceful and reflective

Make it suitable for a closing narration and next-episode preview.
```

---

## 6. 조금 더 다큐멘터리 느낌

```text
Create understated documentary background music for a tech learning journey.

The video shows a beginner setting up a Linux development environment for a future local AI and fine-tuning project.
The tone should be realistic, honest, and quietly inspiring.

Avoid epic trailers, corporate ads, and overly emotional music.
Use a restrained, modern sound.

Instrumentation:
- soft marimba or pluck synth
- warm pads
- light electronic beat
- subtle bass
- no vocals

Tempo: 80-90 BPM.
The track should loop naturally and stay behind narration.
```

---

## 7. Gemini에게 추가로 요청할 문장

```text
위 프롬프트들을 YouTube 초보 개발 브이로그에 맞게 더 자연스럽게 다듬어줘.
너무 광고음악 같지 않고, 말소리를 방해하지 않는 배경음악 중심으로 수정해줘.
```

```text
위 프롬프트 중에서 Day 001 영상에 가장 잘 맞는 3개를 골라주고,
각각 어떤 장면에 쓰면 좋은지 추천해줘.
```

```text
이 음악 프롬프트를 Suno, Udio, YouTube Create, Gemini용으로 각각 다르게 최적화해줘.
```

---

## 8. 추천 사용 방식

Day 001 영상에는 아래 조합을 추천합니다.

1. 오프닝: `오프닝 테마용 프롬프트`
2. 터미널 설치 장면: `Day 001 리눅스 세팅 영상용`
3. 검증 성공 마무리: `엔딩/회고용 프롬프트`

배경음악은 말소리보다 작게 깔고, 명령어를 입력하는 장면에서는 음악이 너무 튀지 않게 유지합니다.

---

[[Cravveo_Channel_Direction]] | [[Daily_Log/2026-05-23_Day001_Log]]

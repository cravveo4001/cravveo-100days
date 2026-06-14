# 📋 Day 022 Mission Brief — Cravveo Company

> **프로젝트** | Project: Cravveo Company 100일 AI 파인튜닝 도전기
> **날짜** | Date: 2026-06-14
> **단계** | Phase: Day 022 / 100

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
| 사용 모델 | 없음 (코랩 T4 GPU 환경) |
| 작업 환경 | Google Colab (T4 GPU) |

---

## 🗺️ 100일 전체 로드맵 — 지금 여기

| 단계 | 내용 | 상태 |
|------|------|------|
| Day 001~010 | 환경 구축 + Python 자동화 기초 | ✅ 완료 |
| Day 011~015 | AnythingLLM + RAG 챕터 + Phase 1 회고 | ✅ 완료 |
| Day 016~018 | 코랩 환경 구축 + Unsloth 설치 + 모델 로드 | ✅ 완료 |
| Day 019 | JSONL 포맷 분석 | ✅ 완료 |
| Day 020+021 | 크라베오 데이터셋 수동 제작 + JSONL 변환 스크립트 완성 (46개) | ✅ 완료 |
| **Day 022** | **HuggingFace CLI 로그인 — 데이터셋 업로드 준비** | 🔥 오늘 |
| Day 023~ | 코랩에 커스텀 데이터셋 업로드 + 파인튜닝 시작 | ⏳ 예정 |
| Day 100 | 1인 기업 자동화 시스템 완성 | 🎯 목표 |

---

## 🎯 오늘의 미션 | Today's Mission

**한국어**
> 46개 데이터셋이 완성됐습니다.
> 이제 이 데이터를 AI 학습에 쓰려면 HuggingFace에 올려야 합니다.
> 오늘은 허깅페이스 계정에서 토큰을 발급받고,
> 코랩 터미널에서 로그인을 완료하는 것이 목표입니다.

**English**
> The 46-entry dataset is complete.
> To use it for AI training, we need to upload it to HuggingFace.
> Today's goal is to generate an access token from HuggingFace
> and complete the login from the Colab terminal.

---

## 📌 오늘 왜 이걸 하는가 | Why This Matters

**한국어**
코랩에서 파인튜닝을 돌리려면 학습 데이터를 코랩이 읽을 수 있어야 합니다.
매번 파일을 수동으로 업로드하는 방법도 있지만, 세션이 끊기면 사라집니다.
HuggingFace에 데이터셋을 올려두면 코드 한 줄로 언제든 불러올 수 있습니다.
오늘 로그인을 완료하면 내일부터 데이터셋 업로드가 가능해집니다.

**English**
For fine-tuning in Colab, the training data must be accessible.
Uploading files manually works, but they disappear when the session ends.
If the dataset is on HuggingFace, one line of code loads it anytime.
Complete login today, and dataset upload becomes possible tomorrow.

---

## ✅ 단계별 실행 | Step-by-Step

### Step 1 — HuggingFace 계정 확인 / 생성

1. [huggingface.co](https://huggingface.co) 접속
2. 계정이 없으면 Sign Up → 이메일 인증 완료
3. 계정이 있으면 로그인

---

### Step 2 — 읽기/쓰기 토큰 발급

설명: HuggingFace에서 코랩이 내 계정에 접근할 수 있도록 열쇠(토큰)를 만듭니다. 토큰은 비밀번호와 같으므로 절대 공개하지 마세요.

1. 우측 상단 프로필 아이콘 클릭
2. **Settings** 클릭
3. 왼쪽 메뉴 → **Access Tokens** 클릭
4. **New token** 클릭
5. 이름 입력 (예: `cravveo-colab`)
6. **Type: Write** 선택 (읽기 + 쓰기 권한)
7. **Generate a token** 클릭
8. 생성된 토큰 복사 → 메모장에 임시 저장

⚠️ 토큰은 생성 직후 한 번만 보입니다. 반드시 복사해두세요.

---

### Step 3 — 코랩 열기 및 환경 확인

1. [colab.research.google.com](https://colab.research.google.com) 접속
2. 기존 `cravveo_finetuning.ipynb` 열기
3. 런타임 → T4 GPU 확인

```python
!nvidia-smi
```

---

### Step 4 — Unsloth 설치 (세션 재시작 시 필수)

설명: 코랩 세션이 끊겼으면 반드시 Unsloth부터 설치합니다.

```python
%%capture
!pip install unsloth
!pip install --upgrade "torchvision>=0.27.0"
```

```python
import unsloth
print("Unsloth version:", unsloth.__version__)
print("✅ Unsloth 준비 완료")
```

---

### Step 5 — HuggingFace CLI 로그인

설명: 코랩에서 허깅페이스에 로그인합니다. 토큰은 절대 코드 셀에 직접 쓰지 않습니다. 노트북이 공개 상태이면 토큰이 그대로 노출됩니다.

```python
!pip install -q huggingface_hub
from huggingface_hub import login

login()
```

실행하면 토큰 입력창이 뜹니다. Step 2에서 복사한 토큰을 붙여넣고 Enter.
입력창에 타이핑한 값은 노트북에 저장되지 않으므로 공개 노트북에서도 안전합니다.

⚠️ `login(token="토큰값")` 형태로 코드 셀에 직접 쓰지 마세요. 공개 노트북이면 누구나 볼 수 있습니다.

---

### Step 6 — 로그인 확인

설명: 로그인이 정상적으로 됐는지 내 계정 정보를 출력해서 확인합니다.

```python
from huggingface_hub import whoami

user_info = whoami()
print(f"✅ 로그인 성공!")
print(f"사용자명: {user_info['name']}")
print(f"이메일: {user_info['email']}")
```

---

## ✅ 성공 조건 체크리스트

- [ ] HuggingFace 계정 확인 / 생성
- [ ] Write 권한 토큰 발급 완료
- [ ] 코랩 T4 GPU 런타임 확인
- [ ] `huggingface_hub` 설치 완료
- [ ] `login()` 실행 후 토큰 입력 완료
- [ ] `whoami()` 로 로그인 확인
- [ ] 영상 녹화 완료

---

## 🔧 트러블슈팅

**토큰 입력창이 안 뜰 때**
→ `login()` 대신 `login(token="토큰값")` 방식으로 직접 입력하세요.

**`HTTPError: 401 Client Error: Unauthorized` 오류**
→ 토큰이 잘못됐거나 만료됐습니다. HuggingFace Settings → Access Tokens에서 새 토큰을 발급하세요.

**`Write` 권한 토큰인지 확인하는 방법**
→ `whoami()` 실행 후 출력에 `"auth": {"accessToken": {"role": "write"}}` 가 있으면 정상입니다.

**영상에서 토큰이 노출됐을 때**
→ HuggingFace Settings → Access Tokens → 해당 토큰 삭제 → 새 토큰 재발급. 노출된 토큰은 즉시 삭제해야 합니다.

---

## 📅 다음 단계 예고 | Next Up

**Day 023** — 코랩에 커스텀 데이터셋 업로드
로그인이 됐으니 이제 46개 데이터셋을 HuggingFace에 올립니다.
코드 한 줄로 언제든 불러올 수 있는 나만의 데이터셋 저장소를 만듭니다.

Day 023 — Uploading the Custom Dataset to Colab
Now that we're logged in, we'll push the 46-entry dataset to HuggingFace.
Creating a personal dataset repository accessible with a single line of code.

---

[[2026-06-14_Day022_Work_Order|Day 022 작업지시서]] | [[../21일차/2026-06-13_Day021_Work_Order|← Day 021]] | [[../Cravveo_100Day_Master_Guide]]

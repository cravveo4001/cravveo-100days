# Day 001 Work Order: 리눅스 기본 세팅 및 Python 개발 환경 구축

> 녹화 기준일: 2026-05-23
> 현재 목표: 터미널, 패키지 업데이트, Python, venv, git 설치 상태를 확인하고 개발 시작 가능한 리눅스 환경을 만든다.

---

## 1. 오늘의 미션
Day 001의 핵심은 "아무것도 없는 노트북을 AI 개발 작업대 상태로 만드는 것"입니다.

완료해야 할 항목은 다음과 같습니다.

1. 터미널을 열고 현재 위치와 시스템 상태를 확인합니다.
2. 패키지 목록을 업데이트합니다.
3. Python, venv, pip, git을 설치합니다.
4. 설치 결과를 버전 명령어로 검증합니다.
5. 오늘 작업 로그를 남깁니다.

---

## 2. 녹화 오프닝 멘트
오늘은 Cravveo 100일 프로젝트의 Day 001입니다.

목표는 리눅스 노트북에 Python 개발 환경과 git을 설치해서, 앞으로 로컬 AI와 파인튜닝 실습을 진행할 수 있는 기본 작업대를 만드는 것입니다.

---

## 3. 실행 명령어
아래 명령어를 순서대로 실행합니다.

```bash
pwd
python3 --version
git --version
```

`git`이 없다고 나오면 정상입니다. Day 001에서 설치할 대상입니다.

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3-pip python3-venv git -y
```

설치 후 다시 확인합니다.

```bash
python3 --version
pip3 --version
git --version
```

---

## 4. 성공 조건
아래 조건을 만족하면 Day 001은 성공입니다.

1. `python3 --version`이 정상 출력됩니다.
2. `pip3 --version`이 정상 출력됩니다.
3. `git --version`이 정상 출력됩니다.
4. `python3 -m venv --help`가 정상 출력됩니다.

---

## 5. 막힐 때 확인할 것
패키지 설치가 실패하면 먼저 인터넷 연결을 확인합니다.

```bash
ping -c 3 archive.ubuntu.com
```

권한 문제가 나오면 `sudo`를 붙였는지 확인합니다.

잠금 오류가 나오면 다른 업데이트 프로그램이 실행 중인지 확인하고 잠시 기다린 뒤 다시 시도합니다.

---

## 6. 오늘의 기록
작업이 끝나면 아래 내용을 짧게 메모합니다.

1. 사용한 리눅스 배포판과 버전
2. 설치된 Python 버전
3. 설치된 git 버전
4. 막힌 지점과 해결 방법
5. 다음 Day 002에서 이어갈 작업 폴더 위치

---

[[Cravveo_100Day_Master_Guide]] | [[Agent_Handover_Protocol]]

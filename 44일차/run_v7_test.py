import ollama
from datetime import datetime

MODEL = "cravveo:v7"
OUTPUT_FILE = "v7_테스트_결과.md"

questions = [
    ("A1", "크라베오 컴퍼니가 뭐야?"),
    ("A2", "크라베오 컴퍼니의 운영자는 누구인가요?"),
    ("A3", "100일 AI 도전이 뭐야?"),
    ("A4", "Build in Public이 뭐야?"),
    ("A5", "왜 1인 개발을 선택했어?"),
    ("A6", "파인튜닝을 왜 배우고 있어?"),
    ("A7", "크라베오의 목표가 뭐야?"),
    ("A8", "유튜브를 왜 시작했어?"),
    ("A9", "지금 파인튜닝 중인 모델은 뭐야?"),
    ("A10", "파인튜닝에 어떤 도구를 쓰고 있어?"),
    ("A11", "LoRA가 뭐야?"),
    ("A12", "GPU 없이도 파인튜닝이 가능해?"),
    ("A13", "Chrome 확장 프로그램은 어떤 걸 만들었어?"),
    ("A14", "ablescan.app은 뭐야?"),
    ("A15", "cravveo.com은 뭐야?"),
    ("A16", "지금 수익이 나고 있어?"),
    ("A17", "100일 도전 중 가장 어려웠던 게 뭐야?"),
    ("A18", "유튜브 채널에서는 어떤 내용을 다뤄?"),
    ("A19", "크라베오 AI 어시스턴트는 어떤 역할을 할 예정이야?"),
    ("A20", "하루를 어떻게 보내?"),
    ("B1", "크라베오가 뭐 하는 곳이야?"),
    ("B2", "누가 크라베오를 운영해?"),
    ("B3", "100일 챌린지가 무슨 프로젝트야?"),
    ("B4", "실패한 것도 숨기지 않고 다 보여주는 방식을 뭐라고 해?"),
    ("B5", "돈은 좀 벌고 있어?"),
    ("B6", "웹 접근성 검사해주는 도구 이름이 뭐야?"),
    ("B7", "파인튜닝할 때 어댑터만 학습하는 기술 이름이 뭐야?"),
    ("B8", "지금까지 게시한 크롬 확장프로그램이 몇 개야?"),
    ("B9", "노트북에 그래픽카드 없는데 어떻게 학습해?"),
    ("B10", "왜 혼자 일하기로 했어?"),
]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(f"# {MODEL} 30문항 테스트 결과\n\n")
    f.write(f"> 시작 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

for i, (label, q) in enumerate(questions, start=1):
    print(f"[{i}/30] {label} 질문 중... ({q})", flush=True)
    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": q}],
        options={"num_predict": 120},
    )
    answer = response["message"]["content"]

    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(f"## {label}. {q}\n답변:\n{answer}\n\n채점:\n\n---\n\n")

    print(f"  완료\n", flush=True)

with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
    f.write(f"> 종료 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print(f"전체 완료! 결과는 {OUTPUT_FILE}에 저장됨")

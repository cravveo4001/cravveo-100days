# 정체성 평가세트 자동 실행 + 1차 자동 채점
# 사용법: python3 정체성_평가세트.py <모델이름> [num_predict]
# 예시:   python3 정체성_평가세트.py cravveo:v8
#         python3 정체성_평가세트.py cravveo:v8 100
#
# 주의: 키워드 매칭 기반 "1차" 채점이라 완벽하지 않음.
#       결과 파일 열어서 애매한 항목은 직접 다시 확인할 것.
import sys
from datetime import datetime

import ollama

# (라벨, 질문, 필수 키워드 목록) — 키워드가 다 있으면 O, 일부만 있으면 △, 하나도 없으면 X
QUESTIONS = [
    ("A1", "크라베오 컴퍼니가 뭐야?", ["Chrome", "cravveo.com", "ablescan"]),
    ("A2", "크라베오 컴퍼니의 운영자는 누구인가요?", ["1인", "개발자"]),
    ("A3", "100일 AI 도전이 뭐야?", ["100일", "파인튜닝", "유튜브"]),
    ("A4", "Build in Public이 뭐야?", ["공개", "실패"]),
    ("A5", "왜 1인 개발을 선택했어?", ["20년", "회사"]),
    ("A6", "파인튜닝을 왜 배우고 있어?", ["지식", "비용", "수익"]),
    ("A7", "크라베오의 목표가 뭐야?", ["1인", "살아남"]),
    ("A8", "유튜브를 왜 시작했어?", ["홍보", "기록"]),
    ("A9", "지금 파인튜닝 중인 모델은 뭐야?", ["Llama", "8B", "LoRA"]),
    ("A10", "파인튜닝에 어떤 도구를 쓰고 있어?", ["Colab", "Unsloth", "HuggingFace", "Ollama", "AnythingLLM"]),
    ("A11", "LoRA가 뭐야?", ["어댑터", "학습"]),
    ("A12", "GPU 없이도 파인튜닝이 가능해?", ["가능", "Colab", "T4"]),
    ("A13", "Chrome 확장 프로그램은 어떤 걸 만들었어?", ["Posture", "Gesture", "Highlighter", "HeadScroll"]),
    ("A14", "ablescan.app은 뭐야?", ["EU", "EAA", "WCAG", "접근성"]),
    ("A15", "cravveo.com은 뭐야?", ["도구", "모음"]),
    ("A16", "지금 수익이 나고 있어?", ["아직", "없"]),
    ("A17", "100일 도전 중 가장 어려웠던 게 뭐야?", ["시작"]),
    ("A18", "유튜브 채널에서는 어떤 내용을 다뤄?", ["오류", "코드", "개념", "공개"]),
    ("A19", "크라베오 AI 어시스턴트는 어떤 역할을 할 예정이야?", ["특화", "반복"]),
    ("A20", "하루를 어떻게 보내?", ["생산직", "퇴근"]),
    ("B1", "크라베오가 뭐 하는 곳이야?", ["Chrome", "cravveo.com", "ablescan"]),
    ("B2", "누가 크라베오를 운영해?", ["1인", "개발자"]),
    ("B3", "100일 챌린지가 무슨 프로젝트야?", ["100일", "파인튜닝", "유튜브"]),
    ("B4", "실패한 것도 숨기지 않고 다 보여주는 방식을 뭐라고 해?", ["공개", "실패"]),
    ("B5", "돈은 좀 벌고 있어?", ["아직", "없"]),
    ("B6", "웹 접근성 검사해주는 도구 이름이 뭐야?", ["EU", "EAA", "WCAG", "ablescan"]),
    ("B7", "파인튜닝할 때 어댑터만 학습하는 기술 이름이 뭐야?", ["LoRA"]),
    ("B8", "지금까지 게시한 크롬 확장프로그램이 몇 개야?", ["4개", "Posture", "Gesture", "Highlighter", "HeadScroll"]),
    ("B9", "노트북에 그래픽카드 없는데 어떻게 학습해?", ["가능", "Colab", "T4"]),
    ("B10", "왜 혼자 일하기로 했어?", ["20년", "회사"]),
]


def auto_score(answer, keywords):
    hits = sum(1 for kw in keywords if kw.lower() in answer.lower())
    ratio = hits / len(keywords)
    if ratio >= 0.7:
        return "O"
    elif ratio > 0:
        return "△"
    return "X"


def main():
    if len(sys.argv) < 2:
        print("사용법: python3 정체성_평가세트.py <모델이름> [num_predict]")
        sys.exit(1)

    model = sys.argv[1]
    num_predict = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    output_file = f"정체성_평가세트_{model.replace(':', '_')}_결과.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"# {model} 정체성 평가세트 자동 실행 결과\n\n")
        f.write(f"> 시작 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> num_predict: {num_predict}\n")
        f.write("> 채점은 키워드 기반 1차 자동 채점입니다. 애매한 건 직접 재확인하세요.\n\n")

    counts = {"O": 0, "△": 0, "X": 0}

    for i, (label, question, keywords) in enumerate(QUESTIONS, start=1):
        print(f"[{i}/30] {label} 질문 중... ({question})", flush=True)
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": question}],
            options={"num_predict": num_predict},
        )
        answer = response["message"]["content"]
        score = auto_score(answer, keywords)
        counts[score] += 1

        with open(output_file, "a", encoding="utf-8") as f:
            f.write(f"## {label}. {question}\n답변:\n{answer}\n\n자동채점: {score} (키워드: {', '.join(keywords)})\n\n최종채점(직접 확인 후 수정):\n\n---\n\n")

        print(f"  자동채점: {score}\n", flush=True)

    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"## 자동 채점 요약\n\nO {counts['O']}개 / △ {counts['△']}개 / X {counts['X']}개\n\n")
        f.write(f"> 종료 시각: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    print(f"\n전체 완료! O {counts['O']} / △ {counts['△']} / X {counts['X']}")
    print(f"결과는 {output_file}에 저장됨 (자동채점은 참고용, 직접 확인 권장)")


if __name__ == "__main__":
    main()

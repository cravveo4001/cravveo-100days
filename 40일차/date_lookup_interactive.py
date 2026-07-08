# 직접 질문 입력해서 테스트하는 버전
# 외부 터미널에서 가상환경 활성화 후 실행할 것:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/40일차/date_lookup_interactive.py
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from date_lookup import build_date_index, ask_with_lookup  # noqa: E402

if __name__ == "__main__":
    date_to_file, day_to_file = build_date_index()
    print(f"날짜 인덱스 {len(date_to_file)}개, Day 인덱스 {len(day_to_file)}개 생성 완료")
    print("질문을 입력하세요 (종료하려면 Ctrl+C 또는 빈 줄 입력)\n")

    while True:
        question = input("질문: ").strip()
        if not question:
            print("종료합니다.")
            break

        answer, filepath = ask_with_lookup(question, date_to_file, day_to_file)
        print(f"파일: {filepath}")
        print(f"답변: {answer}\n")

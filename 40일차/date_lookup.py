# 외부 터미널에서 가상환경 활성화 후 실행할 것:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/40일차/date_lookup.py
import os
import re

import ollama

LOG_DIR = os.path.expanduser("~/finetuning-project/Daily_Log")
MODEL = "cravveo:v4"

FILENAME_PATTERN = re.compile(r"^(\d{4}-\d{2}-\d{2})_(Day\d+(?:\+\d+)?|Special)_Log\.md$")
DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")
DAY_PATTERN = re.compile(r"[Dd]ay\s*(\d+)")


def build_date_index():
    """Daily_Log 폴더를 스캔해서 날짜/Day번호 -> 파일 경로 딕셔너리를 만든다."""
    date_to_file = {}
    day_to_file = {}

    for filename in os.listdir(LOG_DIR):
        match = FILENAME_PATTERN.match(filename)
        if not match:
            continue

        date_str, day_str = match.groups()
        filepath = os.path.join(LOG_DIR, filename)
        date_to_file[date_str] = filepath

        if day_str != "Special":
            # "Day020+021" 같은 복합 Day는 두 번호 모두 등록
            for day_num in re.findall(r"\d+", day_str):
                day_to_file[f"Day{int(day_num):03d}"] = filepath

    return date_to_file, day_to_file


def extract_query_key(question):
    """질문에서 날짜(YYYY-MM-DD) 또는 Day 번호를 추출한다."""
    date_match = DATE_PATTERN.search(question)
    if date_match:
        return "date", date_match.group()

    day_match = DAY_PATTERN.search(question)
    if day_match:
        return "day", f"Day{int(day_match.group(1)):03d}"

    return None, None


def find_log_file(question, date_to_file, day_to_file):
    kind, key = extract_query_key(question)
    if kind == "date":
        return date_to_file.get(key)
    if kind == "day":
        return day_to_file.get(key)
    return None


def trim_log_content(content):
    """다음 날짜로 이어지는 '다음 단계' 섹션과 하단 링크 줄을 제거해, 그날 있었던 일만 남긴다."""
    content = content.split("## 다음 단계")[0]
    content = content.split("\n---")[0]
    return content.strip()


def ask_with_lookup(question, date_to_file, day_to_file):
    """날짜/Day 번호로 정확한 로그 파일을 찾아, 그 내용을 컨텍스트로 Ollama에 질문한다."""
    filepath = find_log_file(question, date_to_file, day_to_file)
    if not filepath:
        return "해당 날짜/Day 기록을 찾지 못했습니다.", None

    with open(filepath, encoding="utf-8") as f:
        content = trim_log_content(f.read())

    # Modelfile-v4의 TEMPLATE이 이미 "질문: ... 답변: ..." 형식을 자동으로 씌운다.
    # 여기서 또 "질문:"/"답변:"을 넣으면 형식이 이중으로 겹쳐서 모델이 혼란스러워한다.
    prompt = f"""아래는 특정 날짜의 기록입니다. 이 내용만 참고해서 아래 질문에 2~3문장으로 간결하게 답하세요. 같은 말을 반복하지 마세요.

기록:
{content}

{question}"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"num_predict": 150},
    )
    return response["message"]["content"], filepath


if __name__ == "__main__":
    date_to_file, day_to_file = build_date_index()
    print(f"날짜 인덱스 {len(date_to_file)}개, Day 인덱스 {len(day_to_file)}개 생성 완료\n")

    test_questions = [
        "2026-05-23일에 뭐했어?",
        "2026-05-27일에 뭐했어?",
        "2026-06-14일에 뭐했어?",
        "2026-06-20일에 뭐했어?",
        "2026-06-27일에 뭐했어?",
        "2026-06-28일에 뭐했어?",
        "2026-07-01일에 뭐했어?",
        "2026-07-02일에 뭐했어?",
        "2026-07-03일에 뭐했어?",
        "Day 032에 뭐했어?",
    ]

    found_count = 0
    for i, question in enumerate(test_questions, start=1):
        answer, filepath = ask_with_lookup(question, date_to_file, day_to_file)
        found = filepath is not None
        found_count += found
        mark = "O" if found else "X"
        print(f"[{i}] [{mark}] {question}")
        print(f"    파일: {filepath}")
        print(f"    답변: {answer}")
        print("---")

    print(f"\n결과: {found_count}/{len(test_questions)} 파일 정확히 매칭됨")

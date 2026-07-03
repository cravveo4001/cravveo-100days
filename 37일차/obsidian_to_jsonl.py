# Obsidian Daily Log → JSONL 자동 변환기
# Cravveo Company — Day 037
#
# Daily_Log/*.md 파일을 읽어서 질문/답변 JSONL로 자동 변환
#
# 실행 방법 | How to run:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/37일차/obsidian_to_jsonl.py

import os
import re
import json
from pathlib import Path

LOG_DIR = Path("/home/c/finetuning-project/Daily_Log")
OUTPUT_FILE = Path("/home/c/finetuning-project/37일차/obsidian_dataset.jsonl")

def extract_day_number(filename):
    match = re.search(r'Day(\d+)', filename)
    if match:
        return match.group(1).lstrip('0') or '0'
    if 'Special' in filename:
        return 'Special'
    return None

def extract_section(text, section_name):
    pattern = rf'## {section_name}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return None
    content = match.group(1).strip()
    # 코드 블록 제거
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # 체크박스 제거
    content = re.sub(r'- \[.\] ', '', content)
    # 마크다운 링크 제거
    content = re.sub(r'\[\[.*?\]\]', '', content)
    content = re.sub(r'\[.*?\]\(.*?\)', '', content)
    # 구분선 제거
    content = re.sub(r'^---+$', '', content, flags=re.MULTILINE)
    # 테이블 행 제거 (선택적 공백 후 | 로 시작하는 줄)
    content = re.sub(r'^\s*\|.*$', '', content, flags=re.MULTILINE)
    # 유출된 섹션 헤더 제거
    content = re.sub(r'^#+\s.*$', '', content, flags=re.MULTILINE)
    # 인라인 코드 백틱 제거
    content = re.sub(r'`([^`]*)`', r'\1', content)
    # 볼드 제거
    content = re.sub(r'\*\*(.*?)\*\*', r'\1', content)
    # 빈 줄 정리
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()
    if not content or content in ['없음', '해당 없음', '-']:
        return None
    return content

def make_entry(question, answer):
    if not answer or len(answer.strip()) < 10:
        return None
    return {"text": f"질문: {question}\n답변: {answer.strip()}"}

def process_log_file(filepath):
    text = filepath.read_text(encoding='utf-8')
    day = extract_day_number(filepath.name)
    if not day:
        return []

    entries = []

    목표 = extract_section(text, '오늘의 목표')
    작업 = extract_section(text, '실행한 작업')
    결과 = extract_section(text, '확인한 결과')
    막힌곳 = extract_section(text, '막힌 지점')
    해결 = extract_section(text, '해결 방법')
    발견 = extract_section(text, '오늘의 핵심 발견')
    다음 = extract_section(text, '다음 단계')

    if 목표:
        entries.append(make_entry(f"Day {day}의 목표가 뭐야?", 목표))
    if 작업:
        entries.append(make_entry(f"Day {day}에서 뭘 했어?", 작업))
    if 결과:
        entries.append(make_entry(f"Day {day}의 결과가 뭐야?", 결과))
    if 막힌곳:
        entries.append(make_entry(f"Day {day}에서 막힌 게 뭐야?", 막힌곳))
    if 해결:
        entries.append(make_entry(f"Day {day}에서 어떻게 해결했어?", 해결))
    if 발견:
        entries.append(make_entry(f"Day {day}의 핵심 발견이 뭐야?", 발견))
    if 다음:
        entries.append(make_entry(f"Day {day} 다음에 뭐 할 거야?", 다음))

    return [e for e in entries if e is not None]

def main():
    log_files = sorted(LOG_DIR.glob("*.md"))
    all_entries = []

    for filepath in log_files:
        entries = process_log_file(filepath)
        all_entries.extend(entries)
        print(f"  {filepath.name}: {len(entries)}개 생성")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for entry in all_entries:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"\n완료! 총 {len(all_entries)}개 Q&A 생성 → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

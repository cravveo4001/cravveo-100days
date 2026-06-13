import json
import re
import glob
import os

def parse_briefing(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Q/A 쌍 추출
    # 패턴: Q숫자: 내용 ... A숫자: 내용 ... (--- 또는 파일 끝까지)
    pattern = r'Q\d+:\s*(.*?)\nA\d+:\s*(.*?)(?=\nQ\d+:|\n-{3,}|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    pairs = []
    for instruction, output in matches:
        instruction = instruction.strip()
        output = output.strip()
        # 구분선(---) 제거
        output = re.sub(r'\n-{3,}\s*$', '', output).strip()
        if instruction and output:
            pairs.append({
                "instruction": instruction,
                "input": "",
                "output": output
            })
    return pairs

def convert_all(briefing_dir, output_file):
    files = sorted(glob.glob(os.path.join(briefing_dir, "briefing_*.txt")))
    all_pairs = []

    for filepath in files:
        pairs = parse_briefing(filepath)
        all_pairs.extend(pairs)
        print(f"  {os.path.basename(filepath)} → {len(pairs)}개 추출")

    with open(output_file, "w", encoding="utf-8") as f:
        for item in all_pairs:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    print(f"\n✅ 완료: 총 {len(all_pairs)}개 항목 → {output_file}")
    return all_pairs

if __name__ == "__main__":
    briefing_dir = os.path.dirname(os.path.abspath(__file__))
    output_file = os.path.join(briefing_dir, "cravveo_briefing_dataset.jsonl")
    print(f"브리핑 폴더: {briefing_dir}")
    print(f"출력 파일: {output_file}\n")
    convert_all(briefing_dir, output_file)

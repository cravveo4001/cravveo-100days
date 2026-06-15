import sys
import os
from pathlib import Path

BRIEFING_DIR = Path(__file__).parent
JSONL_FILE = BRIEFING_DIR / "cravveo_briefing_dataset.jsonl"
HF_REPO = "cravveo/cravveo-briefing-dataset"


def step1_convert_to_jsonl():
    print("\n[1/2] JSONL 변환 중...")
    sys.path.insert(0, str(BRIEFING_DIR))
    from briefing_to_jsonl import convert_all
    pairs = convert_all(str(BRIEFING_DIR), str(JSONL_FILE))
    print(f"✅ JSONL 변환 완료 — 총 {len(pairs)}개")
    return len(pairs)


def step2_push_to_hub(count):
    print(f"\n[2/2] HuggingFace 업로드 중...")
    try:
        from huggingface_hub import whoami
        from datasets import load_dataset
    except ImportError:
        print("❌ 라이브러리 없음 — 설치 후 재시도: pip install datasets huggingface_hub")
        sys.exit(1)

    user = whoami()
    print(f"  로그인 확인: {user['name']}")

    dataset = load_dataset("json", data_files=str(JSONL_FILE), split="train")
    dataset.push_to_hub(HF_REPO, private=False)
    print(f"✅ 업로드 완료 — {count}개 항목")
    print(f"🔗 https://huggingface.co/datasets/{HF_REPO}")


if __name__ == "__main__":
    print("=== Cravveo 브리핑 파이프라인 ===")
    count = step1_convert_to_jsonl()
    step2_push_to_hub(count)
    print("\n완료! 오늘 데이터가 HuggingFace에 반영됐습니다.")

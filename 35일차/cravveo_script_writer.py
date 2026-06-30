# 실행 방법: cd ~/projects/cravveo_ai && source venv/bin/activate
#           python3 ~/finetuning-project/35일차/cravveo_script_writer.py

import ollama

def write_script(day_number, topic):
    prompt = f"""크라베오 컴퍼니의 100일 AI 파인튜닝 도전 유튜브 영상 스크립트를 써줘.
Day {day_number}, 주제: {topic}

다음 구조로 짧게 써줘:
1. 오프닝 (1줄)
2. 오늘 한 일 (2~3줄)
3. 클로징 (1줄)
"""
    response = ollama.chat(
        model='cravveo',
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response['message']['content']

if __name__ == "__main__":
    script = write_script(35, "유튜브 스크립트 자동화 + 마이크로 첫 음성 녹음")
    print(script)
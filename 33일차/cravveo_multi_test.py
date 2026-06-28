# VS Code 터미널에서 실행하면 ollama 모듈 오류가 날 수 있음
# 외부 터미널에서 가상환경 활성화 후 실행할 것:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/33일차/cravveo_multi_test.py
import ollama

questions = [
    "크라베오 컴퍼니가 뭐야?",
    "크라베오의 목표가 뭐야?",
    "Build in Public이 뭐야?",
    "파인튜닝을 왜 배우고 있어?",
    "크라베오의 기술 스택이 뭐야?",
]

for q in questions:
    print(f"질문: {q}")
    response = ollama.chat(
        model='cravveo',
        messages=[{'role': 'user', 'content': q}]
    )
    print(f"답변: {response['message']['content']}")
    print("-" * 50)
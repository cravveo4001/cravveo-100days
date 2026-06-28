# VS Code 터미널에서 실행하면 ollama 모듈 오류가 날 수 있음
# 외부 터미널에서 가상환경 활성화 후 실행할 것:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/33일차/cravveo_api_test.py
import ollama

response = ollama.chat(
    model='cravveo',
    messages=[
        {'role': 'user', 'content': '크라베오 컴퍼니가 뭐야?'}
    ]
)

print(response['message']['content'])
# VS Code 터미널에서 실행하면 ollama 모듈 오류가 날 수 있음
# 외부 터미널에서 가상환경 활성화 후 실행할 것:
#   cd ~/projects/cravveo_ai && source venv/bin/activate
#   python3 ~/finetuning-project/33일차/cravveo_briefing_test.py
import ollama
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

prompt = f"""오늘은 {today}입니다.
크라베오 컴퍼니의 AI 어시스턴트로서 오늘의 아침 브리핑을 작성해주세요.
다음 항목을 포함해주세요:
1. 오늘의 날짜
2. 크라베오 프로젝트 현재 진행 상황
3. 오늘 해야 할 일 제안
"""

response = ollama.chat(
    model='cravveo',
    messages=[{'role': 'user', 'content': prompt}]
)

print("=" * 50)
print(f"크라베오 AI 아침 브리핑 — {today}")
print("=" * 50)
print(response['message']['content'])

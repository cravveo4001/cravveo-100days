import requests
from datetime import datetime

url = "http://localhost:11434/api/generate"

def ask_ai(prompt):
    data = {
        "model": "qwen3.5:2b",
        "prompt": "반드시 한국어로만 답해줘.\n\n" + prompt,
        "stream": False,
        "think": False,
        "options": {"num_predict": 500}
    }
    response = requests.post(url, json=data)
    result = response.json()
    return result.get("response", "")

filename = f"chat_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

print("AI 대화를 시작합니다. 종료하려면 '종료' 또는 'quit'을 입력하세요.")
print(f"대화 내용은 {filename} 에 저장됩니다.")
print("-" * 50)

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"=== 대화 시작: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===\n\n")

    while True:
        user_input = input("\n나: ")

        if user_input.strip() in ["종료", "quit", "exit"]:
            print("대화를 종료합니다.")
            f.write("\n=== 대화 종료 ===\n")
            break

        if not user_input.strip():
            continue

        print("AI 생각 중...")
        answer = ask_ai(user_input)
        print(f"\nAI: {answer}")

        f.write(f"나: {user_input}\n")
        f.write(f"AI: {answer}\n")
        f.write("-" * 30 + "\n")

print(f"\n저장 완료: {filename}")
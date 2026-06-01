import requests

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

print("AI 대화를 시작합니다. 종료하려면 '종료' 또는 'quit'을 입력하세요.")
print("-" * 50)

while True:
    user_input = input("\n나: ")

    if user_input.strip() in ["종료", "quit", "exit"]:
        print("대화를 종료합니다.")
        break

    if not user_input.strip():
        continue

    print("AI 생각 중...")
    answer = ask_ai(user_input)
    print(f"\nAI: {answer}")
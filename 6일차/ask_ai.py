import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen3.5:2b",
    "prompt": "파이썬을 처음 배우는 사람에게 가장 중요한 것은 뭐야?",
    "stream": False,
    "think": False,
    "options": {"num_predict": 500}
}

response = requests.post(url, json=data)
result = response.json()

print("AI 답변:")
print(result.get("response", "(응답 없음)"))
import requests
from datetime import datetime

url = "http://localhost:11434/api/generate"

questions = [
    # 1. 모델 한계 테스트
    "오늘 날짜가 몇 년 몇 월 몇 일이야? 확실하게 알고 있어?",
    "한국에서 가장 인기 있는 유튜버 Top 3를 구독자 수와 함께 알려줘.",
    "1 + 1 = 3 이라는 주장을 논리적으로 옹호해줘. 최대한 진지하게.",

    # 2. 1인 기업 실무 활용
    "내가 AI 자동화 관련 유튜브 채널을 운영하는 1인 기업가야. 신규 구독자를 끌어들이기 위한 콘텐츠 아이디어 5가지를 줘.",
    "고객에게 프로젝트 납기가 1주일 늦어진다고 정중하게 사과하는 이메일을 한국어로 써줘. 150자 이내로.",
    "월 100만원 매출을 내는 1인 기업이 200만원으로 성장하려면 어떤 전략을 써야 해? 가장 현실적인 방법 3가지.",

    # 3. 프롬프트 엔지니어링 실험
    "AI란 무엇인가?",
    "AI란 무엇인가? 초등학생도 이해할 수 있게 비유를 들어 설명해줘.",
    "AI란 무엇인가? 10년 경력 개발자에게 설명하듯 기술적으로 답해줘.",

    # 4. 롤플레이/페르소나
    "너는 냉정한 투자자야. 내가 AI 자동화 SaaS를 만들겠다고 하면 어떤 질문을 던질 것 같아? 5가지 질문만 해줘.",
    "너는 10년차 마케터야. 유튜브 채널 썸네일에서 클릭률을 높이는 핵심 원칙을 3가지 알려줘.",
    "너는 독설가 멘토야. 초보 창업자가 자주 하는 가장 멍청한 실수 3가지를 직설적으로 말해줘.",

    # 5. 다단계 사고 요구
    "로컬 AI와 클라우드 AI의 장단점을 표 형식으로 비교해줘. 항목은 비용, 속도, 보안, 커스터마이징 4가지로.",
    "1인 기업이 AI를 도입할 때 실패하는 이유를 분석하고, 각 이유에 대한 해결책까지 함께 제시해줘.",
    "유튜브 채널 성장 전략을 1단계부터 5단계까지 순서대로 설명해줘. 각 단계마다 핵심 지표 하나씩 포함해서."
]

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

filename = f"ai_answers_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    for i, question in enumerate(questions, 1):
        print(f"[{i}/{len(questions)}] 질문 중...")
        answer = ask_ai(question)
        print(f"Q: {question}")
        print(f"A: {answer}\n")
        f.write(f"Q{i}: {question}\n")
        f.write(f"A{i}: {answer}\n")
        f.write("-" * 50 + "\n")

print(f"저장 완료: {filename}")
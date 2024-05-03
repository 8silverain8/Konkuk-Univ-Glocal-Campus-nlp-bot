import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["그것은 꽤 흥미롭네요, 더 자세히 말씀해주세요.",
                    "알겠습니다. 계속 말씀해주세요.",
                    "왜 그렇게 말씀하시나요?",
                    "요즘 날씨가 참 이상하죠, 그렇지 않나요?",
                    "주제를 바꾸어 봅시다.",
                    "어제 경기 재밌지 않나요??"]

print("안녕하세요 저는 심플로봇인 라빈입니다.")
print("당신은 언제든지 'bye'를 입력하여 대화를 종료할 수 있습니다")
print("질문을 친 후'enter'를 누르세요")
print("오늘 기분 어떠신가요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("좋은 대화였어요 안녕히가세요!")
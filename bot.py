import random

# This list contains the random responses in English
random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

# This dictionary translates the English responses to Korean
translation_dict = {
    "That is quite interesting, please tell me more.": "그것은 꽤 흥미롭네요, 더 자세히 말씀해주세요.",
    "I see. Do go on.": "알겠습니다. 계속 말씀해주세요.",
    "Why do you say that?": "왜 그렇게 말씀하시나요?",
    "Funny weather we've been having, isn't it?": "요즘 날씨가 참 이상하죠, 그렇지 않나요?",
    "Let's change the subject.": "주제를 바꾸어 봅시다.",
    "Did you catch the game last night?": "어제 경기 보셨나요?"
}

print("Hello, I am Marvin, the simple robot.")
print("You can end this conversation at any time by typing 'bye'")
print("After typing each answer, press 'enter'")
print("How are you today?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "bye":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
        translated_response = translation_dict[response]
    print(translated_response)

print("It was nice talking to you, goodbye!")

from inquirer import inquire
import random
import pycountry

app_id = "28KQW5-RVLGPL3KAH"



def name_president() -> list:
    answer = list()

    for answers in range(4):
        random_num = random.randint(1, 46)
        question = f"What is the name of the {random_num} president of the United States?"
        if answers == 0:
            answer.append(question)
        ans = inquire(app_id, question).split(" (")
        answer.append(ans[0])
    return answer

def name_capital():
    countryList = list(pycountry.countries)
    print(len(countryList))
    answers = random.sample(range(249),4)
    questions = []
    ans = []
    for counter in range(4):
        country = list(pycountry.countries)[answers[counter]].name
        questions.append(f"What is the capital of {country}?")
        ans.append(inquire(app_id, questions[counter]).split(","))
    return [questions[0], ans[0][-2].lstrip(), ans[1][-2].lstrip(), ans[2][-2].lstrip(), ans[3][-2].lstrip()]


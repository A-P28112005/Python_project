print("welcome to the test!")
registered_name = input("what is your name?: ")
start = input("are you ready for the test?: ")
if start == "yes":
    print(f' okay! {registered_name} we wish you success.  Please submit all answers in lower case. \nNo googling allowed! Answers may be looked up in a bible')
elif start == "Yes":
    print(f' okay! {registered_name} we wish you success. Please submit all answers in lower case. \nNo googling allowed! Answers may be looked up in a bible')
else:
    quit()

print("each question carries one mark. good luck!")


class Question:
    def __init__(self, prompt, answer):
        self.answer = answer
        self.prompt = prompt


question_prompts = [
    "1. where was jesus christ born\n(a) jerusalem\n(b) bethlehem\n(c) jerusalem\n(d) nigeria\n\n",
    "2. who gave birth to jesus\n(a) mary\n(b) esther\n(c) anna\n(d) hannah\n\n",
    "3. who was the first man God created\n(a) michael\n(b) noah\n(c) adam\n(d) abel\n\n",
    "4. who made the ark?\n(a) noah\n(b) Jesus\n(c) peter\n(d) judas\n\n",
    "5. which angel gave the message of Jesus christ being born?\n(a) angel michael\n(b) angel gabriel\n(c) angel "
    "uriel\n(d) raphael\n\n ",
    "6. what is the first book in the bible\n(a) genesis\n(b) revelations\n(c) luke\n(d)john\n\n",
    "7. what is the longest book in the bible\n(a) luke\n(b) timothy\n(c) psalm\n(d) proverbs\n\n",
    "8. what is the last book in the bible\n(a) psalm\n(b) revelation\n(c) luke\n(d) john\n\n",
    "9. who betrayed Jesus christ\n(a) peter\n(b) paul\n(c) saul\n(d) judas\n\n",
    "10. why did Jesus die for us?\n(a) to wash away our sins\n(b) because he had a bet with God\n(c) because he was forced to "
    "to\n(d) because he wanted to go to heaven\n\n ",
    "Lets spice it up now!\n11. which one of the following is not in the new testament?\n(a) Romans\n(b) Hebrews\n(c) Colossians\n(d) Malachi\n\n",
    "12. who ate locust and wild honey?\n(a) Solomon\n(b) John the baptist\n(c) Ezekiel\n(d) Jesus\n\n",
    "13. what is the first colour mentioned in the bible?\n(a) Black\n(b) White\n(c) Purple\n(d) Green\n\n",
    "14. What king had thousands of horses and chariots?\n(a) Balaam\n(b) Solomon\n(c) Ehud\n(d) Joash\n\n",
    "15. What happened to the money the priests paid Judas\n(a) Bought a graveyard\n(b) He got robbed\n(c) Gave it away\n(d) Put it into a fish's mouth\n\n",
    "16. Who baked Bread on fire made from cow dung?\n(a) Elisha\n(b) Jesus and disciples\n\n"

]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "c"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "d"),
    Question(question_prompts[9], "a"),
    Question(question_prompts[10], "d"),
    Question(question_prompts[11], "b"),
    Question(question_prompts[12], "d"),
    Question(question_prompts[13], "b"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "a"),
    

]

def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " totally\n\n\n")
    def results():
        if score <= 20:
            print("Very well done! You broke the record!")
        else:
            print("Well done! Thanks for participating!\n\n\n")
        
    print("This is just a sample of the real bible Quiz I am in the process of making. Thanks for Your participation in my small project " + registered_name + "!\nI look forward to when it becomes a full scale program!")


run_quiz(questions)






	






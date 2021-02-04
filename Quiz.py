class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "Qual a resposta para a vida, o universo e tudo mais?\n(a) Sabre de luz\n(b) Toalha\n(c) Don't panic\n(d) 42\nResposta: ",
     "\nPlaneta natal de Spock em Star Trek\n(a) Terra\n(b) Vulcano\n(c) Asgard\n(d) Mustafar\nResposta: ",
     "\nQual o nome do dragão de O Hobbit\n(a) Frodo\n(b) Sam\n(c) Smaug\n(d) Smoug\nResposta: ",
]

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "b"),
     Question(question_prompts[2], "c"),
     
]

def run_quiz(questions):
     score = 0
     mscore = 0
     porc = 0
     
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     porc = score/len(questions)*100
     print("Você acertou","%2.f" % porc,"%","das perguntas (",score,"/",len(questions),")")


run_quiz(questions)

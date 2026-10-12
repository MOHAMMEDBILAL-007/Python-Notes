import time
questions=["who invented nuclear bomb?","who was the peace lover among them?","who killed most people among them?","who is a good man among them?","who discovered the gravity?","who is the cruelest among them"]
answers=[
    ["J. Robert Oppenheimer", "Albert Einstein", "Enrico Fermi", "Niels Bohr"],
    ["Mahatma Gandhi", "Albert Einstein", "Dalai Lama", "Martin Luther King Jr."],
    ["Adolf Hitler", "Joseph Stalin", "Genghis Khan", "Mao Zedong"],
    ["Nelson Mandela", "Abdul Kalam", "Mother Teresa", "Mahatma Gandhi"],
    ["Isaac Newton", "Galileo Galilei", "Johannes Kepler", "Albert Einstein"],
    ["Adolf Hitler", "Pol Pot", "Ivan the Terrible", "Vlad the Impaler"]
]
money=0
for i in range(0,6):
    print(questions[i])
    for j in range(0,4):
        print(f"{j}) {answers[i][j]}")
    print()
    select=int(input("enter your option:"))
    print()
    if i == 0 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    elif i == 1 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    elif i == 2 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    elif i == 3 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    elif i == 4 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    elif i == 5 and select==0:
        print("correct answer you just won 10000")
        print()
        money+=10000
        time.sleep(5)
    else:
        print("wrong answer")
        print("answer was option :",answers[i][0])
        print()
        time.sleep(5)
print("the money you are taking with you today is :",money)
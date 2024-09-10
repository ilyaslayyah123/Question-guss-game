def gess_game():
    print("                     Quize                    ")
    name=input("Enter your name :")
    print("Hello",name,"Welcome to the quize game")
    print("You have to answer 6  questions")


    question={"Q#1:copy function used for in python: ":"A",
            "Q#2:list in python is ":"B",
            "Q#3:dictionary in pythonm is ":"C",
            "Q#4:tuple in python is ":"D",
            "Q#5:set in python is ":"A",
            "Q#6:Function in python is":"C"}

    answers=[["A","creat copy of a variable",
            "B","creat copy of a list",
            "C","creat copy of a dictionary",
            "D","creat copy of a tuple",],
            
            ["A","collection of item",
            "B","collection of item in order",
            "C","list sre not changable",
            "D","list sre not used in python",],
            
            ["A","is a function",
            "B","is a data type",
            "C","is function to store key value pair",
            "D","is a data type to store key value pair",],
            
            ["A","tupleis  a data type",
            "B","tuple is a function",
            "C","tuple is a data type to store key value pair",
            "D","tuple are unchangable",],
            
            ["A","set is changable in python",
            "B","set is a function",
            "C","set is a data type to store key value pair",
            "D","set are unchangable",],
            
            ["A","function couldnot work on python",
            "B","function is a data type",
            "C","function are block of code to furthor use",
            "D","function are unchangable",]
            ]

    coorect_answer=0
    wrong_answer=0
    index=0

    for key,value in question.items():
        print(key)
        for i in answers[index]:
            print(i)
        index+=1
        print("--------------------------------")
        
        user_answer=input("enter your answer: ")
        if user_answer.lower()==value.lower():
            print("""
                 _______
                |       |
                |coorect|
                |_______|""")
            coorect_answer+=1
            
        else:
            print("""
                 _______
                |       |
                | worng |
                |_______|""")
            wrong_answer+=1
    points=coorect_answer/2
    if points>=2:
            print("congradulation you clear the ques:")
    else:
            print("you are fail:")
    print("your coorect answer is",coorect_answer)
    print("your wrong answer is",wrong_answer)
    print("you got ",points,":points out of 3")
    
    user_choice=input("doyou want to play again yes/no:")
    if user_choice.lower()=="yes":
        gess_game()

gess_game()

        
        
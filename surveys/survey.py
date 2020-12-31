#take results of questions 
# calculate the value of one set of questions
#only integer values

question_list = [
                "What do you think of X?", 
                "What do you think of Y?",
                "What do you think of Z?",
                "What do you think of a?",
                ]




def get_answer(prompt ="What do you think of X?"):
    while True:
        print("1) Strongly Agree")
        print("2) Somewhat Agree")
        print("3) Neither Agree / disagree")
        print("4) disagree")
        print("5) somewhat disagree")
        print("6) strongly disagree")
        print("0) EXIT THE QUESTIONAIRE")
        x = input("Your answer: ")
        #test user input
        try: 
           x =int(x)
        except ValueError:
            print("enter only integers")
            continue
        if x>=7 or x<0:
            print("enter a number between 0 and 6")
            continue
        return x


def result_caculator():
    if (answers[0] + answers[1]) >= 5:
        print ("consider doing X") 
    elif (answers[2] + answers[1]) >=5:
        print ("consider doing Y") 
    elif (answers[2] + answers[0]) >=5:
        print ("consider doing Z") 

def main():
    answers=[]
    name = input("What's your name?")
    print("This will take a few minutes. Let's begin.")
    for question in question_list:
        print(question)
        answer = get_answer()
        answers.append(answer)
    print(answers)
    #result calculation
    if (answers[0] + answers[1]) >= 5:
            print ("consider doing X") 
    elif (answers[2] + answers[1]) >=5:
        print ("consider doing Y") 
    elif (answers[2] + answers[0]) >=5:
        print ("consider doing Z") 



if __name__ == '__main__':
    main()    
    



#take results of questions 
# calculate the value of one set of questions
#only integer values

#the question values are registered differently in the survey


import time

#TODO
#save questions and answers to CSV for further processing
# {user_name}{day}{month}{year}.csv
# question, question_number, response, date


question_list = [
                "I feel protected by my partner.",
                # "My partner is faithful to me.",
                # "My partner is there for me financially.",
                # "Sometimes I feel uneasy around my partner.", 
                # "I don’t think my partner has intimate relationships with others.",
                # "From now on, my partner would not have children with anyone but me.",
                # "7. My partner fully loves our children and/or is at least respectful of my own children.",
                # "I believe that you can trust most people.",
                # "9. My partner helps me feel emotionally secure.",
                # "10. I know my partner will always be a very close friend.",
                # "11. My partner will commit to help provide for our children.",
                # "12. When the chips are down, I can count on my partner to sacrifice for me and our family.",
                # "13. My partner does housework.",
                # "14. My partner will work hard to increase our financial security.",
                # "15. My partner doesn’t respect me.",
                # "16. My partner makes me feel sexually desirable.",
                # "17. My partner takes my feelings into account when making decisions.",
                # "18. I know that my partner will take care of me when I’m sick.",
                # "19. When we are not getting along, my partner will work with me on our relationship.",
                # "20. My partner is there for me emotionally.",
                # "21. My partner does not overuse alcohol and drugs.",
                # "22. My partner acts romantically toward me.",
                # "23. My partner is kind to my family.",
                # "24. I can rely on my partner to talk to me when I’m sad or angry.",
                # "25. My partner belittles or humiliates me.",
                # "26. There is at least one person who comes first to my partner rather than me.",
                # "27. My partner will work with me as part of a financial unit.",
                # "28. I have power and influence in this relationship.",
                # "29. My partner shows others how much he or she cherishes me.",
                # "30. My partner helps carry the load of child care.",
                # "31. I just can’t trust my partner completely.",
                # "32. My partner keeps his or her promises.",
                # "33. My partner is a moral person.",
                # "34. My partner does what he or she agrees to do.",
                # "35. My partner will betray my confidences.",
                # "36. My partner is affectionate toward me.",
                # "37. In arguments I can trust my partner to really listen to me.",
                # "38. My partner shares in and honors my dreams.",
                # "39. I fear my partner could stray.",
                # "40. My partner’s words and deeds reflect the values we say we agree on.",
                # "41. My partner makes love to me often.",
                # "42. I can count on my partner to build or maintain a sense of family and community with me.",
                ]




def get_answer(prompt ="What do you think of X?"):
    while True:
        print("1) Strongly Agree")
        print("2) Somewhat Agree")
        print("3) Neither Agree / disagree")
        print("4) somewhat disagree")
        print("5) strongly disagree")
        print("0) exit the questionaire")
        
        x = input("Your answer: ")
        #test user input
        try: 
           x =int(x)
        except ValueError:
            print("enter only integers")
            continue
        
        if x>=6 or x<0:
            print("enter a number between 0 and 6")
            continue
        if x == 0:
            print('\ngood bye')
            break

        return x


def result_caculator():
    first_add =(answers[4] + answers[15]+ answers[25]+ answers[26]+ answers[31]+ answers[35]+ answers[39]) 
    # second_add =

def main():
    answers=[]
    name = input("What's your name?\n\n")
    print(f"Hello {name}!\nThis survey will take a few minutes. Let's begin.\n")
    for question in question_list:
        print(question, "\n")
        answer = get_answer()
        answers.append(answer)
    print(answers)
    #result calculation
    # if first_add >= 25:
    #     print(f"{first_add}")
    #     print ("consider doing X") 
    # elif (answers[2] + answers[1]) >=5:
    #     print ("consider doing Y") 
    # elif (answers[2] + answers[0]) >=5:
    #     print ("consider doing Z") 



if __name__ == '__main__':
    main()    
    



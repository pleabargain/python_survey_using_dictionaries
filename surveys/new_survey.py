#ask users a series of questions
#branching logic off of the answer
#save the questions to a csv file
#save the prompts to a csv file
#save the user name and the date title of csv


import time


# datestamp = f'{time.localtime().tm_year}_mon{time.localtime().tm_mon}_{time.localtime().tm_mday}'
# output_file_name = f'{datestamp}.{filename}.array.txt'


question_list = [
                "Winter is the hardest part of the year.",
                "Summer is the hardest part of the year.",
                "Spring is the hardest part of the year.",
                ]




point_of_views =[
                "As far as I’m concerned…(AFAIC)",
                "From my point of view...",
                "I am convinced that ...",
                "I am of the opinion that…",
                ]

arguments_to_support_POV= [
                        "Let me start by saying...",
                        "Allow me to explain...",
                        "Let me start with...",
                        ]

counter_arg = [
                "you're wrong!",
                "I'm right!",
                ]


#dictionary
display_options = {
                    "point_of_view":point_of_views,
                    "arguments_to_support_POV":arguments_to_support_POV,
                    "counter_arg": counter_arg,
                    }


def get_answer(prompt ="What do you think of X?"):
    for number, text in enumerate(display_options):
        print(number,text)
    while True:
        try:
            command = int(input('Please type your choice\n'))
        except ValueError:
            continue
        if command<0 or command > number:
            continue
        break
    display_option =list( display_options.keys())[command]
    print(f"your option was {display_option}\n")
    
    for number, text in enumerate(display_options[display_option]):
        print(number,text)
    while True:
        try:
            command = int(input('Please type your choice\n'))
        except ValueError:
            continue
        if command<0 or command > number:
            continue
        break
    
    second_option = display_options[display_option][command]
    print(f"Your second option was {second_option}\n")
    student_answer= input("student response: ")
    return display_option,second_option,student_answer

   
   
    
    return
    
    while True:

        #option point_of_view()
        #option arguments_to_support_POV()
        #option counter_arguments()
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



def main():
    answers=[]
    name = input("What's your name?\n\n")
    print(f"Hello {name}!\n Let's begin.\n")
    for question in question_list:
        print(question, "\n")
        display_option,second_option,student_answer = get_answer()
        # answers.append(answer)
        with open(f"{name}.output.csv","a") as f:
            f.write(f"'{question}', '{display_option}', '{second_option}', '{student_answer}'\n")
        command = input("q for quit or enter to continue s for skip to next     question")
        if command == 'q' or command == 'quit' or command == 'exit':
            break
        if command == 's' or command=='skip':
            pass
        


    print(answers)




if __name__ == '__main__':
    main()    
    


# name.time.csv
# {question}, {display_option}, {second_option}, {student_answer}
# "Winter is the hardest part of the year.", "From my point of view...", "student response teacher adds material"
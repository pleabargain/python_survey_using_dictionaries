#ask users a series of questions
#branching logic off of the answer
#save the questions to a csv file
#save the prompts to a csv file
#save the user name and the date title of csv


import time


# datestamp = f'{time.localtime().tm_year}_mon{time.localtime().tm_mon}_{time.localtime().tm_mday}'
# output_file_name = f'{datestamp}.{filename}.array.txt'

# #TODO Need a new dictionary of dictionaries
# #e.g. topics--> questions
# #and the questions should be randomized so that users don't see the same questions
# over and over
question_list = [
                "Winter is the hardest part of the year.",
                "Summer is the hardest part of the year.",
                "Spring is the hardest part of the year.",
                ]

complain = [
        "I hate to complain, but it’s been a tough week and I could use an ear….",
        "I hate to complain, but I sure wish we were sitting at a café right now instead of doing yet another video call.",
        "I know I shouldn’t complain, and don’t get me wrong I love my kids, but…",
        "I know I shouldn’t complain, and don’t get me wrong I really like my coworkers, but…",
        ]

expressing_agreement = [
                    "Can you say that again? I want to write it down.",
                    "I love that idea. I’m gonna write it down so I don’t forget it.",
                    "I never thought of it that way. I want to write that down.",
                    "That’s an interesting perspective. Give me a second to write that down.",
                    "Absolutely….",
                    "Actually, I think you’re right….",
                    "Definitely….",
                    "Fair enough, I think you may be right.",
                    "I agree with what you said.",
                    "I agree….",
                    "I couldn’t agree more….",
                    "I couldn’t agree with you more.",
                    "I have no objection to what you said.",
                    "I have to side with you on this one….",
                    "I hold the same opinion.",
                    "I second that….",
                    "I see exactly what you mean….",
                    "I see what you are getting at….",
                    "I see your point….",
                    "I share your view.",
                    "I suppose so….",
                    "I take your word on it….",
                    "I think so too….",
                    "I totally agree….",
                    "I’d go along with that view to a point…",
                    "I’d go along with that….",
                    "I’ve come to the same conclusion.",
                    "Ok, that’s convincing….",
                    "Precisely….",
                    "Sure, that’s one way of looking at it….",
                    "That’s a good point….",
                    "That’s true….",
                    "We are of one mind about that matter.",
                    "Well, I agree with you here….",
                    "Yes, you’re right!",
                    "You have my full agreement….",
                    "You took the words right out of my mouth…",
                    "You’re quite/absolutely right.",
                    "You’re right, that’s a good point….",
                    ]


polite_interruption = [
                        "Are you telling me that….",
                    "Are you telling us that….",
                    "Before you go much further...",
                    "Before you go on, I’d like to say something….",
                    "Before you move on, I’d like to say something….",
                    "Can I add something here….",
                    "Can I throw my two cents in….",
                    "Do you mind if I add something….",
                    "Excuse me for a second, but….",
                    "Excuse me for interrupting, but….",
                    "Excuse me, but in my opinion….",
                    "I don’t mean to intrude, but….",
                    "I would like to add something here...",
                    "If I may interrupt….",
                    "If I might add something….",
                    "Is it ok if I jump in for a moment….",
                    "Just a moment, I like to add something here….",
                    "Let me finish what I have to say first….",
                    "May I say something here….",
                    "So, you’re telling me….",
                    "Sorry I interrupted you, I get excited. Please continue.",
                    "Sorry to cut you off, but….",
                    "Sorry to interrupt, but….",
                    "Sorry to interrupt, I’m really into this topic.",
                    "Sorry to interrupt, please tell me more. What you said really got me thinking.",
                    "Sorry, but can you let me finish….",
                    "Sorry, but I’m not done yet….",
                    "Umm, well not really….",
                    "Wait a minute….",
                    "Well, if that is the case….",
                    "Well, that reminds me that….",
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

comment_negatively = [
                    "Look here, …",
                "Nothing of the kind!",
                "Oh, come on!",
                "Right!",
                "That doesn't sound convincing.",
                "What are you talking about?!",
                "You seem to have confused the point...",
                "I'm not sure you have considered...",
                "There is little evidence of...",
                "Have you considered...",
]


express_disagreement = [
                        "I don't think so.",
                        "I don't believe it .",
                        "I'm afraid I can't agree with you.",
                        "I wouldn't be so certain.",
                        "It's quite a different thing.",
                        "I doubt that…",
                        "I think you might be confusing the issues.",
                        "I don't think you have considered all of the options.",
                        "I agree up to a point, but….",
                        "I am afraid that is not quite true.",
                        "I can’t/ couldn’t go along with that….",
                        "I completely disagree….",
                        "I don’t agree with you / I disagree.",
                        "I don’t really agree with that idea….",
                        "I don’t think so.",
                        "I don’t think so….",
                        "I find that very difficult to accept….",
                        "I have to state that I think otherwise.",
                        "I see what you are getting at, but….",
                        "I still have my doubts….",
                        "I take a different view.",
                        "I wouldn’t quite put it that way myself….",
                        "I’m afraid, I disagree….",
                        "I’m not sure I go along with that view….",
                        "No, I’m not sure about that because….",
                        "Not at all!",
                        "Not necessarily….",
                        "That’s not always true….",
                        "That’s one way of looking at it, however….",
                        "That’s out of the question….",
                        "There is no way I could agree with that….",
                        "I’m not sure about that….",
                        "We don’t seem to agree here….",
                        "We don’t seem to be in complete agreement….",
                        "Well, I don’t quite agree with you….",
                        "Well, I see things rather differently….",
                        "You could say that, however….",
                        "You’re wrong (this one can easily annoy people. Use it only with your friends)",
                        "You’ve got to be kidding….",
            ]                

camera_off = [
            "Do you mind if we turn the video off?",
            "I’m a bit Zoomed out for the day. Is it cool if we just talk?",
            "I’m done with the camera today. Is it cool if we just talk?",
            "If you prefer to get up and move around when you talk, please let me know.",
            "Since the presentation is over is everyone okay with turning off the camera so we can relax?",
            "I'm turning my camera off so I can relax a bit.",
            ]


#dictionary
#don't forget the commas!
display_options = {
                    "Arguments to support your POV":arguments_to_support_POV,
                    "Let's turn the camera off": camera_off,
                    "comment negatively":comment_negatively,
                    "complain":complain,
                    "express disagreement":express_disagreement,
                    "expressing agreement":expressing_agreement,
                    "point of view":point_of_views,
                    "polite interruption":polite_interruption,
                    #"counter_arg":counter_arg,
                    }


def get_answer(prompt ="What do you think of X?"):
    '''
    This will display the dictionaries but the question is NOT part of this block.
    '''
    for number, text in enumerate(display_options):
        print(number,text)
        #too much of a line break print("\n")
    while True:
        try:
            command = int(input('Please type your choice\n'))
        except ValueError:
            continue
        if command<0 or command > number:
            continue
        break
    display_option =list( display_options.keys())[command]
    print(f"You chose option: {display_option}\n")
    
    for number, text in enumerate(display_options[display_option]):
        print(number,text)
    while True:
        try:
            command = int(input('Please type your choice: \n'))
        except ValueError:
            continue
        if command<0 or command > number:
            continue
        break
    
    second_option = display_options[display_option][command]
    print(f"Your second option was \n{second_option}\nNow use\n{second_option}\nand the question_out to form a new sentence.")
    student_answer= input("student response: ")
    return display_option,second_option,student_answer

    
    return
    
    while True:

       
        x = input("Your answer: ")
        #test user input for ints only
        try: 
           x =int(x)
        except ValueError:
            print("enter only integers")
            continue
        #no longer necessary
        # if x>=6 or x<0:
        #     print("enter a number between 0 and 6")
        #     continue
        if x == 0:
            print('\ngood bye')
            break

        return x

# get_answer.__doc__ ="This function manages the logic for displaying the dictionary of dictionaries"



def main():
    """
    This will write the code to to the csv file in the same dir as the the location of the script.
    It also starts the application. Prompting user for their name.
    """
    #TODO: logic for skipping over questions
    answers=[]
    name = input("What's your name?\n\n")
    print(f"Hello {name}!\nLet's begin.\nWhat do you think of this statement?\n")
    for question in question_list:
        print(question, "\n")
        display_option,second_option,student_answer = get_answer()
        # answers.append(answer)
        with open(f"{name}.output.csv","a") as f:
            f.write(f"'{question}', '{display_option}', '{second_option}', '{student_answer}'\n")
        command = input("q for quit\nenter to continue\ns to skip to the next random question")
        if command == 'q' or command == 'quit' or command == 'exit':
            break
        if command == 's' or command=='skip':
            pass
        
        question_out = question
        return question_out

    print(answers)




if __name__ == '__main__':
    main()    
    


# name.time.csv
# {question}, {display_option}, {second_option}, {student_answer}
# "Winter is the hardest part of the year.", "From my point of view...", "student response teacher adds material"
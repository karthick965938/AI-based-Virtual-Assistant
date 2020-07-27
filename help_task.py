import random
from output_module import output

task_list1 = ["Play music", "Change wallpaper", "Get news","Chatting", "Mathematical Expression Solver", "Many More"]
task_list2 = ["Search on youtube", "Search on google", "Set reminder", "Open Google Map", "Tell me a joke", "Many More"]
task_list3 = ["Change Assistant name", "Send Email", "Send text to a number", "On/Off Speak", "On/Off Voice Recognition", "Many More"]
task_list4 = ["Weather Conditons", "Check internet connectivity", "Music Control", "Time/Date info", "Can Learn New Questions", "Many More"]

task = [task_list1, task_list2, task_list3, task_list4]

def help_greet():
    for x in random.choice(task):
        print("-> ", x)
    print("For short help list: type --h")
    print("For complete help list: type --help")
    print()


def help(s):
    if s == "--h":
        for x in random.choice(task):
            print("-> ", x)
    else:
        for x in task:
            for i in x:
                print("-> ", i)

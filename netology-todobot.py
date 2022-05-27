HELP ="""
add - add task
all - list of all tasks
show - list of tasks for particular date
del - delete task
exit/quit - stop the bot
help - list all commands
"""

tasks = {}

while True:
    req = input("Enter command:")
    if req == "help":
        print(HELP)
    elif req == "all":
        for date in tasks:
            for task in tasks[date]:
                print(date, "-", task)
    elif req == "show":
        date = input("Enter date for show: ")
        if date in tasks:
            for task in tasks[date]:
                print(date,"-", task)
        else:
            print("There are no tasks for", date)
    elif req == "add":
        task = input("Enter new task: ")
        date = input("Enter the day to complete task: ")
        if date in tasks:
            tasks[date].append(task)
        else:
            tasks[date] = [task]
        print("Task", task,"added to", date)
    elif req == "del":
      print("Task deleted.")
    elif req == "exit" or req == "quit":
      break
    else:
      print("Unknown command. Try once more!")
      
print("Bot stopped.")

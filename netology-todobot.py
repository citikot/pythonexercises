HELP ="""
add - add task
all - list all tasks
del - delete task
exit/quit - stop the bot
help - list all commands
"""

today = []
tomorrow = []
other = []

while True:
    req = input("Enter command:")
    if req == "help":
        print(HELP)
    elif req == "all":
        print(today, tomorrow, other)
    elif req == "add":
        task = input("Enter new task: ")
        date = input("Enter the day to complete task: ")
        if date == "today":
            today.append(task)
            print("Task added to " + date + "'s list.")
        elif date == "tomorrow":
            tomorrow.append(task)
            print("Task added to " + date + "'s list.")
        else:
            other.append(task)
            print("Task added to other's list.")
    elif req == "del":
      print("Task deleted.")
    elif req == "exit" or req == "quit":
      break
    else:
      print("Unknown command. Try once more!")
      
print("Bot stopped.")

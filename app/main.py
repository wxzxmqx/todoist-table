from prettytable import PrettyTable
import os

table = PrettyTable(["Task", "Deadline"])

def add_task():
    os.system('cls')

    table.add_row([task, deadline])
    table.add_divider()

    print(table)

while True:
    task = input("Add task (or type quit): ")
    if task.lower() == "quit":
        print('\n See you next time! Bye! \n')
        break

    deadline = input("What's the deadline?: ")
    if deadline.lower() == "quit":
        print('\n See you next time! Bye! \n')
        break

    add_task()
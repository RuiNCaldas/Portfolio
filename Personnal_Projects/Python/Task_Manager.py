from tabulate import tabulate

#Creating the table
data = [
    ['Task', 'Create a new Task', 'Now', 'Check'],
]
headers = ['Type', 'Name', 'Deadline', 'Done']

print(tabulate(data, headers=headers, tablefmt='grid'))


#Creating a new task
def create_Task():
    Type = input("The Type: ")
    Task_Name = input("The Task: ")
    Deadline = input("The Deadline: ")
    new_row = [Type, Task_Name, Deadline, "X"]
    data.append(new_row)
    print(tabulate(data, headers=headers, tablefmt='grid'))


create_Task()
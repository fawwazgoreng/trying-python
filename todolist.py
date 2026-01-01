import json

# initiate class todolist
class TodolistAction:
    todolist = []
    def __init__(self):
        with open("todolist.json") as file:
            initial = json.load(file)
        self.todolist = initial
    pass
    def show(self):
        return self.todolist
    def add(self , todo):
        self.todolist.append(todo)
        with open("todolist.json" , 'w') as f:
            json.dump(self.todolist , f , indent=4)
    def remove(self , todo):
        self.todolist.remove(todo)
        with open("todolist.json" , 'w') as f:
            json.dump(self.todolist , f , indent=4)
    def edit(self , i ,todo):
        self.todolist[i] = todo
        with open("todolist.json" , 'w') as f:
            json.dump(self.todolist , f , indent=4)

# todolist class
todoAction = TodolistAction()

# show todolist
def show():
    res = todoAction.show()
    for i, value in enumerate(res):
        print(str(i + 1) + " : " + value)
    print()

def ask_method():
    action = int(input("number : "))
    if action == 1:
        return show()
    if action == 2:
        todo = str(input("input todolist : "))
        return todoAction.add(todo)
    if action == 3:
        show()
        i = int(input("input number of todolist : "))
        todo = str(input("edit todolist : "))
        return todoAction.edit(i - 1 , todo)
    if action == 4:
        todolist()
        i = int(input("input number of todolist : "))
        return  todoAction.remove(i - 1)
    else:
        return todolist()

def todolist ():
    print("prees 1 to show all todolist")
    print("prees 2 to add all todolist")
    print("prees 3 to edit all todolist")
    print("prees 4 to delete all todolist")
todolist()
while True:
    ask_method()

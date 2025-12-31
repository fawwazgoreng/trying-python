
initial = [
    'get up',
    'eating',
    'exercise'
]


def show():
    index = 1
    res = []
    for item in todoAction.todolist:
        res.append(str(index) + ":" + item)
        index += 1
    return res

class TodolistAction:
    todolist = initial.copy()
    def __init__(self):
        self.todolist = initial.copy()
    pass

    def add(self , todo):
        self.todolist.append(todo)
    def remove(self , todo):
        self.todolist.remove(todo)
    def edit(self , i ,todo):
        self.todolist[i] = todo

todoAction = TodolistAction()
def ask_method():
    action = int(input("number : "))
    if action == 2:
        todo = str(input("input todolist : "))
        return todoAction.add(todo)
    if action == 3:
        todolist()
        i = int(input("select number : "))
        todo = str(input("input todolist : "))
        return todoAction.edit(i , todo)
    if action == 4:
        todolist()
        i = int(input("select number : "))
        return  todoAction.remove(i)
    else:
        return print(show())

def todolist ():
    print("prees 1 to show all todolist")
    print("prees 2 to add all todolist")
    print("prees 3 to edit all todolist")
    print("prees 4 to delete all todolist")
todolist()
while True:
    ask_method()

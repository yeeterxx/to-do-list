import json
import os

FILENAME="dataload2.json"


if os.path.exists(FILENAME):
   with open(FILENAME,'r') as f:
    data=json.load(f)
    to_do_list=data.get("to_do_list",[])
    completed_list=data.get("completed_list",[])

else:

 to_do_list=[]
 completed_list=[]

def add_task():
        category=input("enter your task here: ")
        time=input("Enter the time you want to perform the task:")
        due_task= {'category':category, 'time':time}
        to_do_list.append(due_task)
        print("Task added sucessfully!!")
        save_data()

def view_task():
        if len(to_do_list)>0:
         for tasks in to_do_list:
            print(tasks)
        else:
           print("empty task!!")


def mark_done():
        for index,value in enumerate(to_do_list):
            print(f'{index}:{value}')
        try:
         done=int(input("enter the task you want to delete:"))
         if 0 <= done < len(to_do_list):        
          completed_tasks= to_do_list.pop(done)
          print("task sucessfully removed!!")
          completed_list.append(completed_tasks)
          save_data()
         else:
            print("no task selected!!")
        except:
            print("enter a number!!")

def view_completed_tasks():
        for comp in completed_list:
            print(comp)

def save_data():
    data={

        'to_do_list':to_do_list,
        'completed_list':completed_list
    }
    with open(FILENAME, "w") as f:
        json.dump(data,f,indent=4)


print("Enter 1 to add task, 2 to view task, 3 to mark task as done,4 to see the completed task,5 to quit:")

while True:

    try:
        choice=int(input("Enter the task you want to perform:"))
    except:
        print("sorry its invalid choice!!")
        continue   
    
    if choice==1:
        add_task()

    elif choice==2:
        view_task()

    elif choice==3:
        mark_done()

    elif choice==4:
        view_completed_tasks()

    elif choice==5:
        break


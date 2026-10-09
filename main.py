# Task Management System
from task import Task
from task_manager import TaskManager
def show_menu():
    print("================================")
    print("     TASK MANAGEMENT SYSTEM     ")
    print("================================")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Complete Task")
    print("6. Search Task")
    print("7. Exit")
    print("\n--------------------------------\n")

manager = TaskManager()   

while True:  #คำสั่งที่ต้องการทำซ้ำเมื่อเงื่อนไขเป็นจริง (ใช้ในกรณีที่ไม่รู้จำนวนรอบการทำซ้ำ)
    show_menu()
  
    choice = input("Enter your choice: ")

    if choice == "1":  #คำสั่งต่างๆเมื่อเงื่อนไขที่ 1 เป็นจริง
        manager.add_task()

    elif choice == "2":  #คำสั่งต่างๆเมื่อเงื่อนไขที่ n เป็นจริง
        manager.view_tasks()

    elif choice == "3":
        manager.update_task()

    elif choice == "4":
        manager.delete_task()

    elif choice == "5":
        manager.complete_task()

    elif choice == "6":
        manager.search_task()

    elif choice == "7":
        print("\nThank you for using Task Management System!")
        break
    
    else:  #คำสั่งต่างๆเมื่อทุกเงื่อนไขเป็นเท็จ
        
        while True:
            key = input("\nInvalid choice! Please enter a number between 1 and 7 \nPress Enter to return to menu... ")

            if key == "":
                break
            print("\nPlease press Enter only. ")
           
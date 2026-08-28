from task import Task
class TaskManager:         #def ฟั่งชั่นกำหนดค่าเริ่มต้น (Default)
    def __init__(self):    #โครงสร้าง Constructor (self เป็นตัวบ่งบอกการทำงานกับวัตถุใด ให้บอกตัวตนของวัตถุนั้นๆ)
        self.tasks = []

    def add_task(self):  #การสร้าง Methhod(กลไกที่กำหนดพฤติกรรมให้กับคลาส)

        print("\n---------- ADD TASK ----------")
        
        while True:  #while ใช้ในกรณีที่ไม่รู้จำนานรอบการทำซ้ำ
            task_id = input("Task ID: ")  #ตัวแปร = input(ข้อความที่จะแสดงผลก่อนรับขข้อมูล)

            if not (task_id.isdigit() and len(task_id) == 3):
                print("\nInvalid Task ID! Please enter 3 digits.")
                continue

            if any(task.task_id == task_id for task in self.tasks):
                print("Task ID already exists!")
                print("Please enter a different Task ID.")
                continue
            break

        while True:
            title = input("Title: ")

            if title.strip():
                break

            print("\nTitle cannot be empty!")

        while True:
            priority = input("Priority: ").capitalize()

            if priority in ["High", "Medium", "Low"]:
                break

            print("\nInvalid priority! Please choose High, Medium, or Low.")

        due_date = input("Due Date: ")

        task = Task(  #ฟังก์ชั่นจัดการ Dictonary
            task_id,
            title,
            priority,
            due_date
        )

        self.tasks.append(task)
        print("\nTask added successfully!\n")

        while True:
            key = input("\nPress Enter to return to menu...")

            if key == "":
                break
            print("Please press Enter only.")
    
    def view_tasks(self): 
        print("\n------------------------- TASKS ---------------------------\n")
        print(f"{'ID':<6}{'Title':<19}{'Priority':<12}{'Status':<13}{'Due Date'}")
        print("-" * 61)
        for task in self.tasks:
            print(
                f"{task.task_id:<6}" #(f = format string)
                f"{task.title:<19}"
                f"{task.priority:<12}"
                f"{task.status:<13}"
                f"{task.due_date}"
            )

        print("\n-------------------------------------------------------------")

        while True:
            key = input("\nPress Enter to return to menu...")
        
            if key == "":
                break
            print("Please press Enter only.")

    def view_one_task(self, task):
        print("\n------------------------- TASK ADDED ---------------------------\n")
        print(f"{'ID':<6}{'Title':<19}{'Priority':<12}{'Status':<13}{'Due Date'}")
        print("-" * 61)

        print(
            f"{task.task_id:<6}"
            f"{task.title:<19}"
            f"{task.priority:<12}"
            f"{task.status:<13}"
            f"{task.due_date}"
        )
        print("\n")
        print("-" * 61)

    def update_task(self):
        print("\n-------------- UPDATE TASK ----------------")

        while True:
            task_id = input("Enter Task ID: ")

            if task_id.isdigit() and len(task_id) == 3:
                break
            
            print("\nInvalid Task ID! Please enter 3 digits.")
            
        for task in self.tasks:  #คำสั่งที่ต้องการทำซ้ำ (ใช้ในกรณีรู้จำนวนรอบการทำซ้ำที่ชัดเจน)
            if task.task_id == task_id:  #เงื่อนไข คำสั่งต่างๆเมื่อเงื่อนไขเป็นจริง (== เท่ากับ) 

                task.title = input("New Title: ")
                task.priority = input("New Priority: ")
                task.due_date = input("New Due Date: ")

                print("\nTask updated successfully!")

                while True:
                    key = input("\nPress Enter to return to menu...")
        
                    if key == "":
                        break
                print("Please press Enter only.")
                return #ค่าที่จะส่งออก
        print("\nTask not found!")

        while True:
            key = input("\nPress Enter to return to menu...")
        
            if key == "":
                break
            print("Please press Enter only.")

    def delete_task(self):
        print("\n-------------- DELETE TASK ----------------")

        task_id = input("Enter Task ID: ")

        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully!")
            while True:
                key = input("\nPress Enter to return to menu...")
        
                if key == "":
                    break
                print("Please press Enter only.")
                return

        print("\nTask not found!")
        while True:
            key = input("\nPress Enter to return to menu...")
        
            if key == "":
                break
            print("Please press Enter only.")

    def complete_task(self):
        print("\n-------------- COMPLETE TASK ----------------")

        task_id = input("Enter Task ID: ")

        for task in self.tasks:
            if task.task_id == task_id:

                if task.status == "Completed":
                    print("\nTask is already completed!")
                else:  #คำสั่งต่างๆเมื่อเงื่อนไขเป็นเท็จ
                    task.status = "Completed"
                    print("\nTask marked as Completed!")

                while True:
                    key = input("\nPress Enter to return to menu...")
        
                    if key == "":
                        break
                    print("Please press Enter only.")
                return

        print("Task not found!")
        while True:
            key = input("\nPress Enter to return to menu...")
                
            if key == "":
                break
            print("Please press Enter only.")
            
       
    def search_task(self):
        print("\n-------------- SEARCH TASK ----------------")

        keyword = input("Search: ").lower()

        found = False  #ตอนเริ่มค้นหา เราถือว่ายังไม่เจอ Task
        for task in self.tasks:
            if keyword in task.title.lower():

                print(
                    f"{task.task_id:<6}"
                    f"{task.title:<19}"
                    f"{task.priority:<12}"
                    f"{task.status:<13}"
                    f"{task.due_date}"
                )
                
                found = True  #เมื่อเจอ Task จากเดิมที่เป็น  False จึงเปลี่ยนเป็น True
          
        if not found:
            print("\nNo matching tasks found!")

        while True:
            key = input("\nPress Enter to return to menu...")
                    
            if key == "":
                break

            print("Please press Enter only.") #แก้ไขตรงนี้
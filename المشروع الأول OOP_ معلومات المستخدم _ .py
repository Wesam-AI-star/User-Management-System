import os #ماجل نظام التشغيل
import time #ماجل الوقت (لتحسين المخرجات لدى المستخدم)
#دالة مسح شاشة الTerminal
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
#كلاس المستخدم   
class User:
    def __init__(self,first_name,last_name,id_user,password,status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.id_user = id_user
        self.password = password
        self.status = status
        #دالة لطباعة كلاس المستخدم
    def display(self):
        print(f"\nFirst Name:{self.first_name}")
        print(f"Last Name:{self.last_name}")   
        print(f"ID:{self.id_user}")   
        print(f"Status:{self.status}")
        
users_id=[]  #قائمة نحفظ فيها ID حقت المستخدمين 
#دالة ادخال بيانات المستخدمين بواسطة الكلاس وترجع.
def create_user():
    First_name=input("Enter your First Name :").title()
    Last_name=input("Enter your Last Name :")
    ID_user=input("Enter your ID :")
    #تحقق من تكرار الID
    while ID_user in users_id:
        print("\nSorry, this ID is already in use by another user! try again.")
        ID_user=input("Enter your ID :")
    users_id.append(ID_user)
    Password=input("Enter your Password :")
    Status=input("Enter membership ststus (active/inactive), or click enter: ")
    if Status:
        return User(First_name,Last_name,ID_user,Password,Status)
    else:
        return User(First_name,Last_name,ID_user,Password)
#دالة البحث عن مستخدم
def search_user(users_list):
    clear_screen()
    print("Search by:\n")
    print("1- Membership ID")
    print("2- First Name ")
    print("3- Membership Status \n")
    
    search=[] #قائمة نضع فيها الاعضاء الذين وجدناهم
    choose = input("choose the way? ")
#بحث عن المستخدم بواسطة ID
    if choose == "1":
        ID=input("\nEnter your ID: ")
        for i in users_list:
            if ID == i.id_user:      
                search.append(i)
                break
#بحث عن المستخدم بواسطة اسمه الأول.   
    elif choose == "2":
        Name=input("\nEnter your first name: ")
        for i in users_list:
            if Name.lower() == i.first_name.lower():
                search.append(i)
#بحث عن المستخدم بواسطة حالته            
    elif choose == "3":
        Available= input("\nEnter the status (inactive/active): ").lower()
        for i in users_list:
            if Available.lower() == i.status.lower():
                search.append(i)
    else:
        print("This choose is not correct!")
#طباعة المساخدمين الذين وجدناهم.
    if search:
        print("\nMembers found")
        for i in search:
            i.display()
            print("------------------------")
    time.sleep(3)
#دالة حذف مستخدم    
def Delete_user(users_list):
    found = False
    Del=input("Enter the ID of the user you want to delete: ")
    for Delete in users_list:
        if Del == Delete.id_user:
            users_list.remove(Delete)
            print("User deleted successfully!")
            if Del in users_id:
                users_id.remove(Del)
            found = True
            break
    if not found:
        print("User not found!")
#دالة تعديل مستخدم.            
def Update_user(users_list):
    found = False
    clear_screen()
    print("\n   ====== The Following Edits ======\n1- First name")
    print("2- Last name")
    print("3- Password")
    print("4- Status\n")
    Edit = input("What do you want to edit: ")
    #تعديل الأسم الأول
    if Edit == "1":  
        for First in users_list:
            if First.id_user == ID:
                First.first_name = input("Enter your new first name: ").title()
                print("The user was successfully modified...")
                found = True
                break
    #تعديل الأسم الآخر
    elif Edit == "2":
        for Last in users_list:
            if Last.id_user == ID:
                Last.last_name = input("Enter your new last name: ").title()
                print("The user was successfully modified...")
                found = True
                break
    #تعديل كلمة المرور
    elif Edit == "3":
        for Password in users_list:
            if Password.id_user == ID:
                Password.password = input("Enter the new password: ")
                print("The user was successfully modified...")
                found = True
                break
    #تعديل الحالة
    elif Edit == "4":
        for Status in users_list:
            if Status.id_user == ID:
                Status.status = input("Enter the new status (inactive/active):").lower()
                print("The user was successfully modified...")
                found = True
                break
    #اختيار خاطئ.
    else:
        print("The choice is not correct! Try again..")
    list_choice=['1','2','3','4']
    if not found and Edit in list_choice:
        print("This ID not found!")
    time.sleep(2)
  
users_list=[] # قائمة نضع فيها كل مستخدم سجل لدينا.
while True:
    clear_screen() #مسح شاشو الTerminal
#ترحيب المستخدم، والقواعد.
    print("Welcome to user management")
    print("""
    choose an Action
    
    1-Add new member
    2-Display all members
    3-Search for a member
    4-Delete User
    5-Update User
    6-Exit\n""")
    choice = int(input("Enter your choice :"))
#اضافة مستخدم.
    if choice == 1:
        clear_screen()
        new_user=create_user()
        print("User addes successfully!")
        users_list.append(new_user)
        time.sleep(2)
#عرض مستخدم.
    elif choice == 2:
        clear_screen()
        if len(users_list) == 0:
            print("No users found! Please add a user first.")
            time.sleep(3)
        else:
            clear_screen()
            print("--- Displaying All Users ---")
            for user in users_list:
                user.display()
                print("----------------------")
            time.sleep(3)
#بحث عن مستخدم.     
    elif choice == 3:
        if users_list:
            search_user(users_list)
        else:
            print("\nMembers not found")
            time.sleep(3)
#حذف مستخدم.  
    elif choice == 4:
        if users_list:
            Delete_user(users_list)
        else:
            print("Please Add member...")
        time.sleep(2)
#تعديل مستخدم.
    elif choice == 5:
        if users_list:
            ID = input("Enter the ID of the user you want to edit : ")
            Update_user(users_list)
            while True:
                choice = input("\nDo you want to change something else? (Y/N)").lower()
                if choice == "y":
                    Update_user(users_list)
                else:
                    break                    
        else:
            print("Please Add member...")
        time.sleep(2)
#خروج.
    elif choice == 6:
        break
#اختيار خاطئ.
    else:
        print("Invalid choice! Please try again.")
        time.sleep(3)
#انتهاء البرنامج
print("\nThe program is finished!")

    


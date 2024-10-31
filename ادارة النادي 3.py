import os
import time

def clear():
    """مسح الشاشة حسب نظام التشغيل."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Nady:
    """نموذج يمثل عضو في النادي."""
    def __init__(self, first_name, last_name, ID, status):
        self.first_name = first_name
        self.last_name = last_name
        self.ID = ID
        self.status = status

    def printt(self):
        """طباعة تفاصيل العضو."""
        print(f"First name : {self.first_name}")
        print(f"Last name : {self.last_name}")
        print(f"Membership ID : {self.ID}")
        print(f"Membership status : {self.status}")

def add_new_user():
    """إضافة عضو جديد."""
    first_name = input("Enter first name : ")
    last_name = input("Enter last name : ")
    ID = input("Enter membership ID : ")
    status = input("Enter membership status : ")
    return Nady(first_name, last_name, ID, status)

new_users = []  # قائمة لتخزين الأعضاء الجدد

while True:
    clear()
    print("\nWelcome to user management \n")
    print("Choose an action: ")
    print("1. Add new user")
    print("2. Display all users")
    print("3. Search for users")
    print("4. Exit\n")
    
    choice1 = input("Enter your choice : ")

    if choice1 == '1':
        clear()
        new_users.append(add_new_user())
        print("User added successfully!")
        time.sleep(2)

    elif choice1 == '2':
        clear()
        if new_users:
            print("Displaying all new users .....")
            for user in new_users:
                user.printt()
            input("Press Enter to return to the main menu...")
        else:
            print("Sorry, didn't find any user to display!")
            time.sleep(2)

    elif choice1 == '3':
        clear()
        print("Search by : ")
        print("1. Membership ID ")
        print("2. First name")
        print("3. Membership Status ")
        your_choice = input("Enter your choice : ")

        if your_choice == '1':
            clear()
            ID_search = input("Enter membership ID to search : ")
            found = False  # متغير لتتبع ما إذا تم العثور على أي مستخدم
            for user in new_users:
                if user.ID == ID_search:
                    user.printt()
                    found = True  # تم العثور على العضو
            if not found:
                print("User not found.")

        elif your_choice == '2':
            clear()
            first_name_search = input("Enter First name to search : ")
            found = False
            for user in new_users:
                if user.first_name == first_name_search:
                    user.printt()
                    found = True
            if not found:
                print("User not found.")

        elif your_choice == '3':
            clear()
            Membership_Status_search = input("Enter Membership Status to search : ")
            found = False
            for user in new_users:
                if user.status == Membership_Status_search:
                    user.printt()
                    found = True
            if not found:
                print("User not found.")

        input("Press Enter to return to the main menu...")

    elif choice1 == '4':
        break  # للخروج من الحلقة

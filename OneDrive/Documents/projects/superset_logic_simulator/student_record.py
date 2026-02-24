class User:
    def __init__(self,name,email,mobile):
        self.name=name
        self.email=email
        self.mobile=mobile
        
    def show_dashboard(self):
        print(f"New User!! Welcome {self.name} to SIRI'S PYTHON COURSE dashboard!")


class Student(User):
    def __init__(self,name,email,mobile,roll_no):
        super().__init__(name,email,mobile)
        self.roll_no=roll_no
    def show_dashboard(self):
        print(f"Welcome Student {self.name} - {self.roll_no} to your SIRI'S PYTHON COURSE dashboard!")

# student1=Student("john","john@example.com","1234567890","R12345")
# student1.show_dashboard()


class Administrator(User):
    def __init__(self,name,email,mobile,admin_ID):
        super().__init__(name,email,mobile)
        self.admin_ID=admin_ID
    def show_dashboard(self):
        print(f"Welcome Administrator {self.name} - {self.admin_ID} to SIRI'S PYTHON COURSE dashboard!")

    def view_all_users(self,database):
        print("Viewing all users in the system:")
        found_student=False
    
        for user in database:
            if isinstance(user, Student):
                print(f"Student: {user.name}, Roll No: {user.roll_no}, Email: {user.email}")
                found_student=True
            #print(f"Name: {user.name}, Role: {user.__class__.__name__}")
        if found_student==False:
            print("No users found.")
    def delete_user(self,database,email):
        #target_email = input("Enter the email of the user to delete: ") 
        for user in database:
            if user.email==email:
                database.remove(user)
                print(f"User with email {email} has been deleted.")
                break
        print(f"No user found with email {email}.")
                


                


2 # This will hold all users (students and administrators)

# s1=Student("john","john@example.com","1234567890","R122345")
# s2=Student("Jane","jane@example.com","0987654321","R67890")
# s3=Student("Doe","doe@example.com","1112223333","R99999")
# if s3 not in database:
#     print(f"Student {s3.name} not found in the system. Adding to database.")
#     database.append(s3)
# # s1.show_dashboard()








# --- SYSTEM INITIALIZATION ---
database = [] 

while True:
    print("\n" + "="*30)
    print("SIRI'S PYTHON COURSE SYSTEM")
    print("="*30)
    print("Please select your role:")
    print("1. Student")
    print("2. Administrator")
    print("3. Exit")
    
    role_choice = input("Enter choice (1-3): ")

    if role_choice == "1":
        print("\n1. Signup (New Student)")
        print("2. Login (Existing Student)")
        choice = input("Select option: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            mobile = input("Enter Mobile: ")
            roll = input("Enter Roll No: ")
            
            # Check if already exists
            exists = any(u.email == email for u in database)
            if exists:
                print(f"\nUser {email} already registered! Please login.")
            else:
                database.append(Student(name, email, mobile, roll))
                print(f"\nRegistration Successful for {name}!")

        elif choice == "2":
            email = input("Enter registered email: ")
            found = False
            for user in database:
                if isinstance(user, Student) and user.email == email:
                    user.show_dashboard()
                    found = True
                    break
            if not found:
                print("\nError: Student not found. Please signup.")

    elif role_choice == "2":
        print("\n1. Signup (New Admin)")
        print("2. Login (Existing Admin)")
        choice = input("Select option: ")

        if choice == "1":
            name = input("Enter Admin Name: ")
            email = input("Enter Email: ")
            mobile = input("Enter Mobile: ")
            admin_id = input("Create Admin ID: ")
            database.append(Administrator(name, email, mobile, admin_id))
            print(f"\nAdmin {name} registered successfully!")

        elif choice == "2":
            admin_id = input("Enter Admin ID: ")
            found_admin = None
            for user in database:
                if isinstance(user, Administrator) and user.admin_ID == admin_id:
                    found_admin = user
                    break
            
            if found_admin:
                found_admin.show_dashboard()
                #found_admin.view_all_users(database)
                print("\n1. View All Users")
                print("2. Delete User")
                print("3. Logout")
                admin_choice = input("Select option: ")
                if admin_choice == "1":
                    found_admin.view_all_users(database)
                elif admin_choice == "2":
                    email_to_delete = input("Enter the email of the user to delete: ")
                    found_admin.delete_user(database, email_to_delete)
                elif admin_choice == "3":
                    print("\nLogging out...")

            else:
                print("\nAccess Denied: Invalid Admin ID.")

    elif role_choice == "3":
        print("\nShutting down system...")
        break
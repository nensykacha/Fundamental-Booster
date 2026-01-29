print("Welcome to the student data organizer!")

students=[]
stu_id=1

while True:
    print("\n1.Add Student")
    print("2.Display all Students")
    print("3.Update Student Information")
    print("4.Delete Student")
    print("5.Display subject offered")
    print("6. Exit")
    
    choice=int(input("\nEnter Your Choice: "))  
    
    if choice==1:
        print("\nEnter Student Details:")
        student_dict={
            "id":(stu_id,),
            "name":input("Name: "),
            "age":int(input("Age: ")),
            "grade":input("Grade: "),
            "dob":input("Date of Birth (YYYY-MM-DD): "),
            "subjects":set(input("Subjects (comma-separated): ").split(","))
        }
        
        students.append(student_dict)
        stu_id+=1
        print("Student added successfully!")
        
    
    elif choice==2:
        if not students:
                print("No students found.")
        else:
            print("\n1.Display All Students")
            print("2.Display Student by ID")
            ch=int(input("\nEnter your choice 1 or 2: "))
            
            if ch==1:
                print(f"\n{'ID':<5} {'Name':<10} {'Age':<5} {'Grade':<8} {'DOB':<12} {'Subjects'}")
                print("-"*65) 

                for student in students:
                    sub = ", ".join(student["subjects"])
                    print(f"{student['id'][0]:<5} {student['name']:<10} {student['age']:<5} {student['grade']:<8} {student['dob']:<12} {sub}")

            elif ch==2:
                sid=int(input("Enter Student ID: "))
                
                for student in students:
                    if student["id"][0]==sid:
                        print(f"\n{'ID':<5} {'Name':<10} {'Age':<5} {'Grade':<8} {'DOB':<12} {'Subjects'}")
                        print("-" * 65)
                        sub = ", ".join(student["subjects"])
                        print(f"{student['id'][0]:<5} {student['name']:<10} {student['age']:<5} {student['grade']:<8} {student['dob']:<12} {sub}")
                        break
                else:
                    print("Student not found.")
                    
                    
    elif choice==3:
        if not students:
                print("No students found.")
        else:
            print("\n1.Update student information by ID")
            print("2.Update student information by Name")
            
            up_choice=int(input("\nEnter your choice 1 or 2: "))
            
            if up_choice==1:
                sid=int(input("\nEnter Student ID to update: "))
                for student in students:
                    if student["id"][0]==sid:
                        student["name"]=input("Enter New Name: ")
                        student["age"]=int(input("Enter New Age: "))
                        student["grade"]=input("Enter New Grade: ")
                        student["subjects"]=set(input("Enter New Subjects (comma-separated): ").split(","))
                        print("Student information updated successfully!")
                        break
                else:
                    print("Student not found.")
                    
            elif up_choice==2:
                name=input("\nEnter Student Name to update: ")
                for student in students:
                    if student["name"]==name:
                        student["name"]=input("Enter New Name: ")
                        student["age"]=int(input("Enter New Age: "))
                        student["grade"]=input("Enter New Grade: ")
                        student["subjects"]=set(input("Enter New Subjects (comma-separated): ").split(","))
                        print("Student information updated successfully!")
                        break
                else:
                    print("Student not found.")
                      
    elif choice==4:
        if not students:
                print("No students found.")
        else:
            print("\n1.Delete Student Record By ID")
            print("2.Delet Student Record By Name")
            del_choice=int(input("\nEnter your choice 1 or 2: "))
            
            if del_choice==1:
                sid=int(input("\nEnter Student ID to delete: "))
                i=0
                found=False
                for student in students:
                    if student["id"][0]==sid:
                        del students[i]
                        print("Student deleted successfully!")
                        found=True
                        break
                    i += 1  
                if not found:
                    print("Student not found.")
            
            elif del_choice==2:
                name=input("\nEnter Student Name to delete: ")
                i=0
                found=False
                for student in students:
                    if student["name"]==name:
                        del students[i]
                        print("Student deleted successfully!")
                        found=True
                        break
                    i += 1  
                if not found:
                    print("Student not found.")
                    
    elif choice==5:
        all_sub=set()
        print("\nSubjects offered:")
        print("-"*20)
        for student in students:
            for subject in student["subjects"]:
                if subject not in all_sub:
                    all_sub.add(subject)
                    print(f"{subject}")

    elif choice==6:
        print("\nThank you for using the student data organizer. Goodbye!")
        break

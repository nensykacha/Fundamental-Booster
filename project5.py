class Employee:
    def __init__(self,EmployeeID,name,age,salary):
        self.__EmployeeID=EmployeeID
        self.name=name
        self.age=age
        self.__salary=salary
        
    def __del__(self):
        print(f"Employee {self.name} with ID {self.__EmployeeID} is deleted!")
        
    def get_EmployeeID(self):
        return self.__EmployeeID
    
    def set_EmployeeID(self,EmployeeID):
        self.__EmployeeID=EmployeeID
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self,salary):
        self.__salary=salary
        
    def displayEmployeeDetails(self):
        print(f"Employee_ID: {self.__EmployeeID}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.__salary}")
        
class Manager(Employee):
    def __init__(self,EmployeeID,name,age,salary,department):
        super().__init__(EmployeeID,name,age,salary)
        self.department=department
        
    def displayManagerDetails(self):
        self.displayEmployeeDetails()
        print(f"Department: {self.department}")
        
class Developer(Employee):
    def __init__(self,EmployeeID,name,age,salary,programmingLanguage):
        super().__init__(EmployeeID,name,age,salary)
        self.programmingLanguage=programmingLanguage
        
    def displayDeveloperDetails(self):
        self.displayEmployeeDetails()
        print(f"Programming Language: {self.programmingLanguage}")
        
employee=[]
employeeID=1

while True:
    print("\n1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Display Employee details")
    print("5. Update Salary")
    print("6. Check Position(Employee/Manager/Developer)")
    print("7. Exit")
    
    choice=int(input("Enter your choice: "))
    
    if choice==1:
        name=input("Enter Employee Name : ")
        age=int(input("Enter Employee Age : "))
        salary=float(input("Enter Employee Salary : "))

        employee.append(Employee(employeeID,name,age,salary))
        employeeID+=1
        
        print(f"Employee added Successfully !")
        
    elif choice==2:
        name=input("Enter Manager Name : ")
        age=int(input("Enter Manager Age : "))
        salary=float(input("Enter Manager Salary : "))
        department=input("Enter Manager Department : ")
        
        emp=Manager(employeeID,name,age,salary,department)
        employee.append(emp)
        employeeID+=1
        
        print(f"Manager added Successfully !")
        
    elif choice==3:
        name=input("Enter Developer Name : ")
        age=int(input("Enter Developer Age : "))
        salary=float(input("Enter Developer Salary : "))
        programmingLanguage=input("Enter Developer Programming Language : ")
        
        emp=Developer(employeeID,name,age,salary,programmingLanguage)
        employee.append(emp)
        employeeID+=1
        
        print(f"Developer added Successfully !")
        
    elif choice==4:
        if not employee:
            print("No Employees to display.")
        else:
            print("\n1. Employee Details:")
            print("2. Manager Details:")
            print("3. Developer Details:")
            print("4. All Employee Details:")
            displayChoice=int(input("Enter your choice: "))
            
            if displayChoice==1:
                print("\n1. Display Employee Details By ID")
                print("2. Display All Employee Details")
                empChoice=int(input("Enter your choice: "))
                
                if empChoice==1:
                    empID=int(input("Enter Employee ID to display details: "))
                    found=False
                    for emp in employee:
                        if isinstance(emp, Employee) and emp.get_EmployeeID()==empID:
                            emp.displayEmployeeDetails()
                            print()
                            found=True
                            break
                    if not found:
                        print(f"No Employee found with ID {empID}.")
                        
                elif empChoice==2:
                    for emp in employee:
                        emp.displayEmployeeDetails()
                        print()
                        
            elif displayChoice==2:
                print("\n1. Display Manager Details By ID")
                print("2. Display All Manager Details")
                mgrChoice=int(input("Enter your choice: "))
                
                if mgrChoice==1:
                    mgrID=int(input("Enter Manager ID to display details: "))
                    found=False
                    for emp in employee:
                        if isinstance(emp, Manager) and emp.get_EmployeeID()==mgrID:
                            emp.displayManagerDetails()
                            print()
                            found=True
                            break
                    if not found:
                        print(f"No Manager found with ID {mgrID}.")
                        
            elif displayChoice==3:
                print("\n1. Display Developer Details By ID")
                print("2. Display All Developer Details")
                devChoice=int(input("Enter your choice: "))
                
                if devChoice==1:
                    devID=int(input("Enter Developer ID to display details: "))
                    found=False
                    for emp in employee:
                        if isinstance(emp, Developer) and emp.get_EmployeeID()==devID:
                            emp.displayDeveloperDetails()
                            print()
                            found=True
                            break
                    if not found:
                        print(f"No Developer found with ID {devID}.")
                
            elif displayChoice==4:
                for emp in employee:
                    emp.displayEmployeeDetails()
                    print()
                    
    elif choice==5:
        if not employee:
            print("No Employees to update.")
        else:
            empID=int(input("Enter Employee ID to update salary: "))
            newSalary=float(input("Enter new Salary: "))
            found=False
            for emp in employee:
                if emp.get_EmployeeID()==empID:
                    emp.set_salary(newSalary)
                    print(f"Salary updated successfully for Employee ID {empID}.")
                    found=True
                    break
                
            if not found:
                print(f"No Employee found with ID {empID}.")
                
    elif choice==6:
        if not employee:
            print("No Employees to check position.")
        else:
            empID=int(input("Enter Employee ID to check position: "))
            found=False
            for emp in employee:
                if emp.get_EmployeeID()==empID:
                    if isinstance(emp, Manager):
                        print(f"\nEmployee ID {empID} is a Manager.")
                    elif isinstance(emp, Developer):
                        print(f"\nEmployee ID {empID} is a Developer.")
                    else:
                        print(f"\nEmployee ID {empID} is a Basic Employee.")
                    found=True
                    break
                
            if not found:
                print(f"No Employee found with ID {empID}.")
        
    elif choice==7:
        print("Exiting the program. Goodbye!")
        break
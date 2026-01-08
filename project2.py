print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("""Select an option:
          1. Generate Patterns
          2. Analyze Numbers
          3. Exit""")
    print()
    
    choice=int(input("Enter your choice (1-3):"))
    if choice==1:
        while True:
            print("""select a pattern type:
                1. Right-Angled Star Triangle Pattern
                2. Invwerted Star Triangle Pattern
                3. Number Triangle Pattern
                4. Inverted Number Triangle Pattern
                5. Back to Main Menu
                """)
            pattern=int(input("Enter your Pattern choice (1-5):"))
            
            match pattern:
                case 1:
                    num=int(input("Enter the number of rows for the pattern:"))
                    for i in range(1,num+1):
                        print(i*"*")
                case 2:
                    num=int(input("Enter the number of rows for the pattern:"))
                    for i in range(num,0,-1):
                        print(i*"*")
                case 3:
                    num=int(input("Enter the number of rows for the pattern:"))
                    for i in range(1,num+1):
                        for j in range(1,i+1):
                            print(j,end="")
                        print()
                    print()
                case 4:
                    num=int(input("Enter the number of rows for the pattern:"))
                    for i in range(num,0,-1):
                        for item in range(1,i+1):
                            print(item,end="")              
                        print()
                    print()
                    
                case 5:
                    break
        print()
    
    elif choice==2:
        start=int(input("Enter the start of the range:"))
        end=int(input("Enter the end of the range:"))
        total=0
        for number in range(start,end+1):
            if number%2==0:
                print(f"{number} is an Even Number")
            else:
                print(f"{number} is an Odd Number")
            total=total+number
        print("Sum of numbers in the range is:", total)
        # print("sum of numbers in the range is:", sum(range(start,end+1)))
        
            
        print()
            
    elif choice==3:
        print("Thanks for using the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
    
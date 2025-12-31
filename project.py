print("Welcome to the personal data collection program")

name=input("Please enter your name: ")
age=int(input("Please enter your age: "))
height=float(input("Please enter your height (in meters): "))
number=int(input("Please enter your favorite number: "))

print("""\nThank you !
Here is collected information\n""")

print("Name: ",name,end=" ( ")
print("Type :",type(name),end=", ")
print("Memory Adsress : ",id(name),")")

print("Age: ",age,end=" ( ")
print("Type :",type(age),end=", ")
print("Memory Adsress : ",id(age),")")

print(f"Height: ",height,end=" ( ")
print(f"Type :",type(height),end=", ")
print(f"Memory Adsress : ",id(height),")")

print("Favorite Number: ",number,end=" ( ")
print("Type :",type(number),end=", ")
print("Memory Adsress : ",id(number),")")


byear=2024-age
print(f"\nHello {name}, your age is {age} and You were born in the year {byear}.")

print("""\nThankyou for using personal data collection program. 
Goodbye!""")
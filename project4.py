def display_data():
    """Menu"""
    print("1. Input Data")
    print("2. Display Data Summary(Built-in Functions)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Filter Data By Threshold(Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics(Returning Multiple Values)")
    print("7. Exit")
    
def input_data(arr):
    n=int(input("Enter Total Number of Elements: "))
    for i in range(n):
        element=int(input(f"Enter element {i+1}: ")) 
        arr.append(element)
    print("\nData has been stored successfully.\n")

def display_summary(arr):
    """Data Summary"""
    print(f"\nArray: {arr}")
    print(f"Length of Array Elemnts: {len(arr)}")
    print(f"Maximum in Array: {max(arr)}")
    print(f"Minimum in Array: {min(arr)}")
    print(f"Sum of Array Elements: {sum(arr)}")
    print(f"Average of Array Elements: {sum(arr)/len(arr)}\n")    
    
def factorial(num):
    """Recursion"""
    if num==0 or num==1:
        return 1
    return num*factorial(num-1)

def fatorial_calculation():
    num=int(input("\nEnter a number to calculate factorial: "))
    print(f"Factorial of {num} is {factorial(num)}\n")
    
    
def filter_data(arr):
    ts=int(input("\nEnter Threshold value: "))
    print("\n1. show Threshold Above value : ")
    print("2. show Threshold Below value : \n")    
    choice=int(input("Enter your choice (1-2): "))
    
    if choice==1:
        filter_data=list(filter(lambda x:x>ts,arr))
        print(f"\nFiltered Data (>{ts}): {filter_data}\n")
    elif choice==2:
        filter_data=list(filter(lambda x:x<ts,arr))
        print(f"\nFiltered Data (<{ts}): {filter_data}\n")
    else:
        print("Invalid Choice\n")
    
def sort_data(arr):
    print("\nEnter Sorting Order: ")
    print("1. Ascending")
    print("2. Descending")
    sorting_choice=int(input("\nEnter your choice (1-2): "))
    if sorting_choice==1:
        arr.sort()
    elif sorting_choice==2:
        arr.sort(reverse=True)
    print(f"Sorted Array: {arr}")
        
def dataset_statistics_value(arr):
    """Returning Multiple Values"""
    min_val = min(arr)
    max_val = max(arr)
    sum_val = sum(arr)
    avg_val = sum_val/len(arr)
    return min_val, max_val, sum_val, avg_val

def dataset_statistics(arr):
    min_val, max_val, sum_val, avg_val = dataset_statistics_value(arr)
    print("\nDataset Statistics:")
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")
    print(f"Sum: {sum_val}")
    print(f"Average: {avg_val}\n")
        
def main():
    arr=[]
    
    while True:
        display_data()
        choice=int(input("Enter Your Choice (1-7): "))
        
        if choice==1:
            input_data(arr)
            
        elif choice==2:
            display_summary(arr)
            
        elif choice==3:
            fatorial_calculation()
            
        elif choice==4:
            filter_data(arr)
            
        elif choice==5:
            sort_data(arr)
            
        elif choice==6:
            dataset_statistics(arr)
            
        elif choice==7:
            print("Exiting the Program.")
            break
main()
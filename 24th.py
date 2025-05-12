name = input("Enter your name: ")
salary = input("Enter your salary: ")
def dispay_info(name, salary=9000):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
dispay_info(name, salary)
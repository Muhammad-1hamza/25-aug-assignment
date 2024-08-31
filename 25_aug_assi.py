num_list : list = []
user_name : str = input("Your name:")
print()

for i in range(1,4):
    num = int(input(f"Enter your {i} favorite number: "))
    num_list.append(num)
   
print(f"\nHello, {user_name} Lets explore your favorite number:")

for item in num_list:
    if item % 2 == 0:
        print(f"{item} is even number")
    else:
        print(f"The number {item} is odd ")

for item in num_list:
    print(f"The number {item} and its square:({item}, {item **2})")

sum_of_num: int =sum(num_list)
print(f"Great! The sum of your favorite numbers is: {sum(num_list)} ")    

is_prime = True
if sum_of_num <=1:
    is_prime = False
for x in range (2,sum_of_num):
    if sum_of_num % x ==0:
        is_prime = False

if is_prime:
    print(f"Good! The number {sum_of_num} is a prime!")
else:
    print(f"great job! The number {sum_of_num} is not a prime number.")
# check nuber is even or odd
#print(f"/nHello, {user_name}")
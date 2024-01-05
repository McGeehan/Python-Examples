#Example 1: Variables and Data types:

name = "Alice"

age = 27

height = 5.5

is_student = True

print(name)

print(age)

print(height)

print(is_student)


#example 2: Input and Output

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hello, " + user_name + "!")

print("You are " + str(user_age) + " years old.")

#example 3: conditionals 

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

 
 
#Example 4: LOOPS

counter = 0
while counter < 505: #while loops run forever unless a condition is met
    print("Iteration", counter)
    counter += 1 
    
for i in range(1000):
    print("Iteration", 1)
    
    
    

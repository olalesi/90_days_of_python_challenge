# User inputs numbers
numbers_input = input("Enter numbers seperated by sapces: ")
# Convert the input into a list of integers
numbers = []
for number in numbers:
  total += number 
# calculate the average
average = total / len(numbers)
# print results
print(f"Sum: {total}")
print(f"Average: {average}")

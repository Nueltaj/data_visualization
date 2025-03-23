# Here's a quick exercise to put your memory to work:

# Write a function that takes a list of numbers and returns a new list containing only the even numbers.

# Example:nums = [1, 2, 3, 4, 5, 6]
# even_numbers = get_evens(nums)  # [2, 4, 6]
def get_numbers():
        print("what is the range of number you want to get even numbers from.\n")
        a = int(input("from: "))
        b = int(input("to: ")) 
        number = list(range(a,b+1)) 
        return number 
        
def print_even_numbers(numbers):
    even_number =[]
    for num in numbers:
        if num %2 == 0:
            even_number.append(num)
    return  even_number

numbers =get_numbers()
even_numbers = print_even_numbers(numbers)  # Get even numbers
print("Even numbers:", even_numbers)
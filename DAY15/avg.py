def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0  
    total_sum = calculate_sum(numbers)
    return total_sum / len(numbers)

numbers = [10, 20, 30, 40, 50]
print("Sum:", calculate_sum(numbers))          
print("Average:", calculate_average(numbers)) 

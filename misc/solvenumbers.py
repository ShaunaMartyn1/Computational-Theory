
# Find Solution or Nearest Solution to the Target Number
from itertools import permutations
from operator import add, sub, mul, truediv

def solve_numbers(numbers, target):
    operations = [add, sub, mul, truediv]
    op_symbols = {add: '+', sub: '-', mul: '*', truediv: '/'}
    closest_result = None
    min_difference = float('inf')
    
    #Recursive function to try all combinations of numbers and operations
    def backtrack(current_value, index, expression):
        nonlocal closest_result, min_difference
        
        if index == len(numbers):
            current_diff = abs(current_value - target)
            if current_diff < min_difference:
                closest_result = (expression, current_value)
                min_difference = current_diff
            
            if current_value == target:
                return expression
            else:
                return None

        for i in range(len(operations)):
            next_value = numbers[index]
            if operations[i] == truediv:
                if next_value == 0 or current_value % next_value != 0:
                    continue
            if operations[i] == sub:
                if current_value < next_value:
                    continue
            new_value = operations[i](current_value, next_value)
            new_expression = f"({expression} {op_symbols[operations[i]]} {next_value})"
            result = backtrack(new_value, index + 1, new_expression)
            if result:
                return result

        return None

    #Try every permutation of the numbers
    for perm in permutations(numbers):
        result = backtrack(perm[0], 1, str(perm[0]))
        if result:
            return result
    
    if closest_result:
        return f"Closest solution: {closest_result[0]} = {closest_result[1]}"
    return None

# Example usage
numbers = [25, 10, 2, 8, 1, 5]
target = 340 # Change the target number for finding the nearest solution
solution = solve_numbers(numbers, target)
print("Solution:", solution if solution else "No valid solution found.")

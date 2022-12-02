n,p = map(int,input().split())

numbers = [i-p for i in list(map(int,input().split()))]
def max_subarray(numbers):
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum
print(max_subarray(numbers))
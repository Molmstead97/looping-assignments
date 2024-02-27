def summation_while(n: int) -> int:

    total = 0
    
    num = 1

    while num <= n:
       
       total += num

       num += 1


    return total


def summation_for(n: int) -> int:

    total = 0

    for num in range(1, n + 1):
        total += num

    return total


num = 20
result_while = summation_while(num)
result_for = summation_for(num)


print(f"While total: {result_while}")

print(f"For total: {result_for}")

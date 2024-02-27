def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    
    
    result = []
    i = 0
    
    while i < len(a):
        result.append(a[i] * b[i])
        i += 1
    
    return result

def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    
    result = []
    for i in range(len(a)):
        result.append(a[i] * b[i])
    return result

a = [1, 2, 3, 4]
b = [5, 6, 7, 8] 

print(f"Multiply while: {list_multiply_while(a, b)}")
print(f"Multiply for: {list_multiply_for(a, b)}")



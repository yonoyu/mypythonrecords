def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list)//2
    
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            return recursive_binary_search(list[midpoint+1:], target)
        else: 
            return recursive_binary_search(list[:midpoint-1],target)


def verify(result):
    print('Target found: ', result)


numbers = [0,1,2,3,4,5,6,7,8,9]
three = [1,2,3]

result = recursive_binary_search(three,4)
verify(result)

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)


def binary_search(list, target):
    first = 0
    last = len(list)-1

    while first <= last: 
        midpoint = (first + last)//2
        
        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first= midpoint+1

        else: 
            last= midpoint-1

    return None

def verify2(index):
    if index is not None:
        print('Target is at: ', index)
    else:
        print('Target not found!')

number = [0,1,2,3,4,5,6,7,8,9]
index = binary_search(number, 12)
verify2(index)

index = binary_search(number, 6)
verify2(index)


def check_prime(number):
    
    return number > 1 and all(number % i != 0 for i in range(2, number))
def rotations(num):
    rotated = []

    m = str(num)

    for _ in m:
        rotated.append(int(m))
        m = m[1:] + m[0]

    return rotated


def get_circular_prime_count(limit):
    counter = 0 

    for number in range(1, limit + 1):
        
        if all(check_prime(rotation) for rotation in rotations(number)): 
            counter += 1 

    return counter
print(get_circular_prime_count(1000))

def solution(n, k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def to_base_k(number, base):
        result = ''
        while number > 0:
            result = str(number % base) + result
            number //= base
        return result

    n_base_k = to_base_k(n, k)
    split_numbers = n_base_k.split('0')

    count = 0
    for num in split_numbers:
        if num and is_prime(int(num)):
            count += 1

    return count


# Example Usage
n = 437674
k = 3
result = solution(n, k)
print(result)  # Output: 3
#이건 통째로 다 외우자


def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True


def to_base_k(number, base):
        result = ''
        while number > 0:
            result = str(number % base) + result
            number //= base
        return result

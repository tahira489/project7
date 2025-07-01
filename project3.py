def reverse_bits(n, total_bits=32):
    result = 0
    for i in range(total_bits):
        result <<= 1
        result |= (n & 1)
        n >>= 1
    return result

number = 5  
reversed_number = reverse_bits(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
print("Reversed binary:", bin(reversed_number))
def reverse_used_bits(n):
    result = 0
    num_bits = n.bit_length()  

    for _ in range(num_bits):
        result <<= 1         
        result |= (n & 1)     
        n >>= 1              

    return result

number = 13 
reversed_number = reverse_used_bits(number)

print("Original number:", number)
print("Original binary:", bin(number)[2:])
print("Reversed binary:", bin(reversed_number)[2:])
print("Reversed number:", reversed_number)

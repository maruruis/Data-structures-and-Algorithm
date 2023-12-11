def remove_duplicates(sequence):
    unique_sequence = set()
    result = []

    for num in sequence:
        if num not in unique_sequence:
            unique_sequence.add(num)
            result.append(num)
    
    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)
def find_subsequences(s):
    # Base case: if the string is empty, return a list with the empty string
    if len(s) == 0:
        return [""]

    # Recursive step: exclude the first character and generate subsequences for the rest
    smaller_subsequences = find_subsequences(s[1:])

    # Add the first character to each subsequence generated from the rest
    with_first = [s[0] + subseq for subseq in smaller_subsequences]

    # Return both subsequences: with and without the first character
    return with_first + smaller_subsequences

# Example usage
result = find_subsequences("123456789")
print(result)

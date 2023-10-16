def is_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def min_palindrome_cuts_recursive(s, start, end):
    if start == end or is_palindrome(s, start, end):
        return 0

    min_cuts = float('inf')

    for i in range(start, end):
        if is_palindrome(s, start, i):
            min_cuts = min(min_cuts, 1 + min_palindrome_cuts_recursive(s, i + 1, end))

    return min_cuts

# Example usage:
input_str = "bababcbadcede"
result = min_palindrome_cuts_recursive(input_str, 0, len(input_str) - 1)
print(result)

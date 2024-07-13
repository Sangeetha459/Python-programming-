def is_palindrome(n):
  return str(n)==str(n)[::-1]
def find_largest_palindrome(numbers):
    largest_palindrome = None
    for n in numbers:
        if is_palindrome(n):
            if largest_palindrome is None or n>largest_palindrome:
                largest_palindrome=n
    return largest_palindrome
if __name__=="__main__":
    n=[1,232,54545,999991]
    largest_palindrome=find_largest_palindrome(n)
    if largest_palindrome is not None:
        print(f"The largest palindrome: {largest_palindrome}")
    else:

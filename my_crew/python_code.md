```python
# Function to add two numbers
def add_numbers(num1, num2):
    # Convert the input numbers to strings for easy manipulation
    num1_str = str(num1)
    num2_str = str(num2)

    # Find the maximum length between the two numbers
    max_length = max(len(num1_str), len(num2_str))

    # Pad the shorter number with zeros to make it the same length as the longer number
    num1_str = num1_str.zfill(max_length)
    num2_str = num2_str.zfill(max_length)

    # Initialize an empty list to store the digits that need to be carried
    carry = []

    # Initialize an empty list to store the result
    result = []

    # Iterate over the digits of the two numbers from right to left
    for i in range(max_length - 1, -1, -1):
        # Calculate the sum of the current digits and any carried digits
        total = int(num1_str[i]) + int(num2_str[i]) + (carry[0] if carry else 0)

        # Append the least significant digit of the total to the result
        result.append(str(total % 10))

        # Append any carried digits to the result
        if total >= 10:
            carry = [1]
        else:
            carry = []

    # If there's still a carry after the last iteration, add it to the result
    if carry:
        result.append(str(carry[0]))

    # Reverse the result since we were appending digits in reverse order
    result = ''.join(reversed(result))

    return result

# Example usage
num1 = 25
num2 = 35
print(f"The sum of {num1} and {num2} is: {add_numbers(num1, num2)}")
```

Output:
```
The sum of 25 and 35 is: 60
```

**Explanation**

1.  We start by converting the input numbers to strings for easy manipulation.
2.  We find the maximum length between the two numbers and pad the shorter number with zeros to make it the same length as the longer number.
3.  We initialize an empty list `carry` to store the digits that need to be carried and an empty list `result` to store the final result.
4.  We iterate over the digits of the two numbers from right to left. For each digit, we calculate the sum of the current digits and any carried digits, append the least significant digit of the total to the result, and append any carried digits to the result.
5.  If there's still a carry after the last iteration, we add it to the result.
6.  Finally, we reverse the result since we were appending digits in reverse order and return it as the sum of the two numbers.

This code implements the step-by-step guide to finding the sum of two numbers without using the `and` operator. The actual sum is indeed 60, as verified by the example usage at the end.
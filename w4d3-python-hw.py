# https://www.codewars.com/kata/5a00e05cc374cb34d100000d

# Build a function that returns an array of integers from n to 1 where n>0.

# Example : n=5 --> [5,4,3,2,1]

# Original Solution: O(n)

def reverse_seq(n):
    ans = []
    for i in range(1,n+1):
        ans.append(i)
    ans.reverse()
    return ans

# Refactored Solution: O(1)

def reverse_seq(n):
    return list(range(n, 0, -1))


# https://www.codewars.com/kata/535474308bb336c9980006f2

# Write a method that takes one argument as name and then greets that name, capitalized and ends with an exclamation point.

# Example:

# "riley" --> "Hello Riley!"
# "JACK"  --> "Hello Jack!"

# Original Solution: O(n)

def greet(name): 
    title_cased_name = name.title()
    return f"Hello {title_cased_name}!"

# Refactored Solution: O(1)

def greet(name):
    if name:
        return f"Hello {name[0].upper()}{name[1:]}!"
    else:
        return "Hello!"
    

# https://www.codewars.com/kata/5715eaedb436cf5606000381

# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

# New Codewars problem: O(n)

def positive_sum(arr):
    total = 0
    for num in arr:
        if num > 0:
            total += num
    return total
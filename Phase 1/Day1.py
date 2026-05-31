def mean(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

print(mean([1, 2, 3, 4, 5]))

def largestnumber(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

print(largestnumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(largestnumber([5, 10, 15, 20, 25]))

def pallindrome(word):
    if word == word[::-1]:
        return "The word is a pallindrome."
    else:
        return "The word is not a pallindrome."

print(pallindrome("racecar"))




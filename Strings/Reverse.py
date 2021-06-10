def reverse(s):
    return s[::-1]

def reverse2(s):
    t = ""
    for i in s:
        t = i + t

    return t

s = input("Enter any string to reverse: ")
r = reverse(s)
print("Using Slicing:", r)

q = reverse2(s)
print("Using loop:", q)


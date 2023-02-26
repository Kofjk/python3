def my_function(x):
    if x < 0:
        raise ValueError("Number cannot be negative")
    else:
        print("Number is positive")

try:
    print("start code")
    print("error")
    my_function(-1)
    print("No errors")
except ValueError as e:
    print("We have an error:", e)

print("code after capsule")

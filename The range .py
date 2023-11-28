# def validate_input(num):
#     if 0 <= num <= 100:
#         return True
#     else:
#         return False
# That is how it works And now test it
def validate_input(num):
    return 0 <= num <= 100

num = int(input("Inter a number："))
if validate_input(num):
    print("In the range of 1-100")
else:
    print("Not the range")
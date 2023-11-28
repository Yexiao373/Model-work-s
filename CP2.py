def greet(name: str) -> str:
    name = name.lower().capitalize()
    return f"Hello, {name}! "
test_name = input("what you want input ")
greeting = greet(test_name)
print(greeting)
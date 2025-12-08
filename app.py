def greet(name: str):
    return f"Hello, {name}!"

def add(a:int, b:int):
    return a+b

def mult(a:int, b:int):
    return a*b

def div(a:int, b:int):
    return a/b
if __name__ == "__main__":
    print(greet("Stas"))
    print("2 + 3 =", add(2, 3))
    print("4 * 5 =", mult(4, 5))
    print("10 / 2 =", div(10, 2))
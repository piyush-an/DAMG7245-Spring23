
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def join_str(a:str, b:str):
    return a+'//'+b


print(f"Calling the inc function: {inc(2)}")
print(f"Calling the dec function: {dec(2)}")
print(f"Calling the join_str function: { join_str('2023', 'ABCD') }")

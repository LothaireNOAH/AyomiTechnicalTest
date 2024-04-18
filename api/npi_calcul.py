import sqlite3

conn = sqlite3.connect('expressions.db')
cursor = conn.cursor()

def insert_result(expression : str, result: float):
    cursor.execute("INSERT INTO expressions (expression, result) VALUES (?, ?)", (expression, result))
    conn.commit()

def do_NPI_calcul(expression: str) -> float:
    stack = []
    operators = {'+', '-', '*', '/'}
    tokens = expression.split() 
    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(float(token))
        elif token in operators:
            if len(stack) < 2:
                raise ValueError("Expression invalide")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ValueError("Division par zéro")
                stack.append(a / b)
        else:
            raise ValueError("Token non valide")    
    if len(stack) != 1:
        raise ValueError("Expression invalide")
    insert_result(expression, stack[0])
    return stack[0] 
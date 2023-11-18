import sympy as sym

"""Создадим переменную alpha и beta как alpha и beta с помощью функции 
sym.Symbol(). 
"""
alpha = sym.symbols('alpha')
beta= sym.symbols('beta')
S_lin =(1/4)*(((alpha + beta * 1 - 860) ** 2) +
              ((alpha + beta * 2 - 850) ** 2) +
              ((alpha + beta * 3 - 920) ** 2) +
              ((alpha + beta * 4 - 900) ** 2))
sym.pprint(sym.diff(S_lin, alpha))
sym.pprint(sym.diff(S_lin, beta))
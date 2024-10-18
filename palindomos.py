def es_palindromo(X):
    if X < 1 or X > 10000:
        return False
    
    original = X
    reverso = 0
    
    while X > 0:
        ultimo_digito = X % 10
        reverso = reverso * 10 + ultimo_digito
        X //= 10
    
    return original == reverso


X = 12321
print(es_palindromo(X))  # Debería devolver True

X = 1234
print(es_palindromo(X))  # Debería devolver False
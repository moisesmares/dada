def busqueda_binaria(A, ele, s=0):
    n = len(A)

    
    if n == 1:
        return s if A[0] == ele else -1

    m = n // 2

    
    if A[m] == ele:
        return s + m


    if A[m] > ele:
        return busqueda_binaria(A[:m], ele, s)
    else:
        return busqueda_binaria(A[m + 1:], ele, s + m + 1)


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

element_to_find = 7
print(busqueda_binaria(arr, element_to_find))  # Se debe imprimir: 3

element_to_find = 8
print(busqueda_binaria(arr, element_to_find))  # Se debe imprimir: -1

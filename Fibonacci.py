"""***********************************+++
+++ Francisco Jesús Jiménez Hidalgo   +++
+++ Fundamentos de programación       +++
+++ Fibonacci recursivo con arrays    +++
+++***********************************"""
nFibo = (0, 1)


def fibonacciR(n):
    """int -> int
    ---OBJ: Muestra el término n de la serie de fibonacci
    ---PRE: n natural o 0"""
    global nFibo

    if n > 1:
        nFibo += (nFibo[n-1] + fibonacciR[n-2],)

    return nFibo

print(fibonacciR(3))


def fibonacciI(n):
    """int -> int
        ---OBJ: Muestra el término n de la serie de fibonacci
        ---PRE: n natural o 0"""

    serieFibonacci = (0,1)
    for i in range (2, n+1):
        serieFibonacci += (serieFibonacci[i-1] + serieFibonacci[i-2],)

    return serieFibonacci

print(fibonacciI(10))

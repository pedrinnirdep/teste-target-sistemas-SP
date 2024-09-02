def fibonacci_sequence(number):
    fib_sequence = [0, 1]

    while fib_sequence[-1] < number:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    
    if number in fib_sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."

numero = int(input("Informe um número: "))
resultado = fibonacci_sequence(numero)
print(resultado)
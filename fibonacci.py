# fibonacci.py

def generate_fibonacci(nterms):

    if nterms <= 0:
        return "Please enter a positive integer"
    elif nterms == 1:
        return [0]
    else:
        sequence = []
        n1, n2 = 0, 1
        count = 0
        while count < nterms:
            sequence.append(n1)
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1
        return sequence

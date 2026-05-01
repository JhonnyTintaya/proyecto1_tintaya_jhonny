class BitProcessor:
    """
    Lógica de procesamiento bit a bit.
    Esta clase es independiente de la interfaz (View).
    """

    def operate_binary(self, n1, n2, operation):
        """Realiza operaciones entre dos números."""
        if operation == 'AND':
            return n1 & n2
        elif operation == 'OR':
            return n1 | n2
        elif operation == 'XOR':
            return n1 ^ n2
        return 0

    def operate_unary(self, n, operation, shifts=0):
        """Realiza operaciones de un solo número o desplazamientos."""
        if operation == 'NOT':
            return ~n
        elif operation == 'LEFT_SHIFT':
            # n << shifts
            return n << shifts
        elif operation == 'RIGHT_SHIFT':
            # n >> shifts
            return n >> shifts
        return 0
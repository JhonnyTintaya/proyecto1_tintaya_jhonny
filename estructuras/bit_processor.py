class BitProcessor:
    """Clase encargada de la lógica matemática bitwise."""
    
    def calculate(self, op, a, b=0):
        if op == "AND": return a & b
        if op == "OR":  return a | b
        if op == "XOR": return a ^ b
        if op == "NOT": return ~a
        if op == "L-SHIFT": return a << b
        if op == "R-SHIFT": return a >> b
        return 0

    def to_binary(self, value):
        """Convierte a binario con formato limpio."""
        return bin(value)
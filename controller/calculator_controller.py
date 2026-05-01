from model.bit_processor import BitProcessor

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Conectar el botón de la vista con la lógica
        self.view.btn_calculate.config(command=self.calculate)

    def calculate(self):
        data = self.view.get_data()
        if data:
            n1, n2, op = data
            result = 0
            
            if op == "AND": result = self.model.operate_binary(n1, n2, 'AND')
            elif op == "OR": result = self.model.operate_binary(n1, n2, 'OR')
            elif op == "XOR": result = self.model.operate_binary(n1, n2, 'XOR')
            elif op == "NOT": result = self.model.operate_unary(n1, 'NOT')
            elif op == "LEFT SHIFT": result = self.model.operate_unary(n1, 'LEFT_SHIFT', n2)
            elif op == "RIGHT SHIFT": result = self.model.operate_unary(n1, 'RIGHT_SHIFT', n2)
            
            self.view.set_results(result, bin(result))

    def run(self):
        self.view.mainloop()
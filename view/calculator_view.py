import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Bitwise - Jhonny Tintaya")
        self.geometry("400x450")
        self.configure(padx=20, pady=20)
        
        # Componentes de la interfaz
        self.label_n1 = ttk.Label(self, text="Número Entero 1:")
        self.label_n1.pack(pady=5)
        self.entry_n1 = ttk.Entry(self)
        self.entry_n1.pack(pady=5)

        self.label_n2 = ttk.Label(self, text="Número Entero 2 (o Desplazamiento):")
        self.label_n2.pack(pady=5)
        self.entry_n2 = ttk.Entry(self)
        self.entry_n2.pack(pady=5)

        self.label_op = ttk.Label(self, text="Operación:")
        self.label_op.pack(pady=5)
        self.combo_op = ttk.Combobox(self, values=["AND", "OR", "XOR", "NOT", "LEFT SHIFT", "RIGHT SHIFT"])
        self.combo_op.set("AND")
        self.combo_op.pack(pady=5)

        self.btn_calculate = ttk.Button(self, text="Calcular")
        self.btn_calculate.pack(pady=20)

        # Resultados
        self.result_dec = ttk.Label(self, text="Decimal: -", font=('Arial', 10, 'bold'))
        self.result_dec.pack()
        self.result_bin = ttk.Label(self, text="Binario: -", font=('Arial', 10, 'bold'))
        self.result_bin.pack()

    def get_data(self):
        try:
            n1 = int(self.entry_n1.get())
            op = self.combo_op.get()
            # Si no es NOT, intentamos obtener el segundo número
            n2 = 0
            if op != "NOT":
                n2 = int(self.entry_n2.get())
            return n1, n2, op
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números enteros válidos.")
            return None

    def set_results(self, decimal, binario):
        self.result_dec.config(text=f"Decimal: {decimal}")
        self.result_bin.config(text=f"Binario: {binario}")
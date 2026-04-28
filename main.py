import tkinter as tk
import json
from estructuras.bit_processor import BitProcessor

class BitwiseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Bitwise - Jhonny Tintaya")
        self.processor = BitProcessor()
        
        # UI similar a la anterior
        tk.Label(root, text="Número A:").pack()
        self.ent_a = tk.Entry(root)
        self.ent_a.pack()
        
        tk.Label(root, text="Número B:").pack()
        self.ent_b = tk.Entry(root)
        self.ent_b.pack()
        
        self.lbl_res = tk.Label(root, text="Resultado: ", font=("Arial", 12, "bold"))
        self.lbl_res.pack(pady=10)

        # Botones de operación
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        
        for op in ["AND", "OR", "XOR", "NOT", "L-SHIFT", "R-SHIFT"]:
            btn = tk.Button(btn_frame, text=op, command=lambda o=op: self.run_op(o))
            btn.pack(side=tk.LEFT)

    def run_op(self, op):
        try:
            a = int(self.ent_a.get())
            b = int(self.ent_b.get()) if self.ent_b.get() else 0
            res = self.processor.calculate(op, a, b)
            self.lbl_res.config(text=f"Dec: {res} | Bin: {self.processor.to_binary(res)}")
        except ValueError:
            self.lbl_res.config(text="Error: Ingrese números válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = BitwiseApp(root)
    root.mainloop()
from model.bit_processor import BitProcessor
from view.calculator_view import CalculatorView
from controller.calculator_controller import CalculatorController

if __name__ == "__main__":
    model = BitProcessor()
    view = CalculatorView()
    controller = CalculatorController(model, view)
    controller.run()
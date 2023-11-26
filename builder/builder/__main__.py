from director import Director
from mycomputer_builder import MyComputerBuilder
from budgetbox_builder import BudgetBoxBuilder

computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

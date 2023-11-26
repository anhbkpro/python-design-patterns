from director import Director
from mycomputer_builder import MyComputerBuilder
from budgetbox_builder import BudgetBoxBuilder

# Problems solved:
# - too many parameters in constructor
# - exposing attributes to client
# - encapsulated the attributes
# - enforced assembly order
# - separated assembly from the components
computer_builder = Director(MyComputerBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

computer_builder = Director(BudgetBoxBuilder())
computer_builder.build_computer()
computer = computer_builder.get_computer()
computer.display()

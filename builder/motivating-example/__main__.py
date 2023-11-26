from computer import Computer

# This is a lot of parameters to pass in!
# This is hard to read and maintain, which is mandatory, which is optional?
# this breaks the Open/Closed Principle
computer = Computer(case='Coolermaster N300',
                    mainboard='MSI 970',
                    cpu='Intel Core i7-4770',
                    memory='Corsair Vengeance 16GB',
                    hard_drive='Seagate 2TB',
                    video_card='GeForce GTX 1070')

computer.display()

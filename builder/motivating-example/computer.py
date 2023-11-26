class Computer(object):
  # contructor has a lot of parameters
  def __init__(self, case, mainboard, cpu, memory, hard_drive, video_card):
    self.case = case
    self.mainboard = mainboard
    self.cpu = cpu
    self.memory = memory
    self.hard_drive = hard_drive
    self.video_card = video_card

  def display(self):
    print("Custom Computer Configuration:")
    print(f'\t{"Case":>15}: {self.case}')
    print(f'\t{"Mainboard":>15}: {self.mainboard}')
    print(f'\t{"CPU":>15}: {self.cpu}')
    print(f'\t{"Memory":>15}: {self.memory}')
    print(f'\t{"Hard Drive":>15}: {self.hard_drive}')
    print(f'\t{"Video Card":>15}: {self.video_card}')

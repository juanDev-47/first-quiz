################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class Oven:

  def __init__(self):
    self.ingredients = []
    self.temperature = 0

  def add(self, item):
    self.ingredients.append(item)

  def freeze(self):
    self.temperature = -100
  
  def boil(self, temperature):
    print(temperature)
    if(temperature > 150 and temperature <= 5100):
      self.temperature = 5000
    elif(temperature > 0 and temperature <= 150):
      self.temperature = 150
  
  def wait(self):
    self.temperature = 0
  
  def get_output(self):
    if self.temperature == -100 and "water" in self.ingredients and "air" in self.ingredients:
      return "snow"
    elif self.temperature >= 5000 and "lead" in self.ingredients and "mercury" in self.ingredients:
      return "gold"
    elif self.temperature == 150 and "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
      return "pizza"
    else:
      return "nothing"

def make_oven():
  oven = Oven()
  return oven

def alchemy_combine(oven, ingredients, temperature):
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100:
    oven.boil(temperature)
  else:
    oven.wait()

  return oven.get_output()

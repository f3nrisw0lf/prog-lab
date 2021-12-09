class Person:
  def __init__(self, weight, height):
    self.weight = weight
    self.height = height
    self.bmi = weight / ((height / 100) ** 2)

  def printBMI(self):
    print(f"Your BMI is {self.bmi:.3f}")

  def printBMIClass(self):
    self.printBMI();
    if self.bmi <= 18.5:
      print("You're Underweight!")
    elif 18.5 <= self.bmi and self.bmi <= 24.9:
      print("You're Normal!")
    elif 25 <= self.bmi and self.bmi <= 29.9:
      print("You're Overweight!")
    elif 30 <= self.bmi and self.bmi <= 34.9:
      print("You're Obese Class 2!")
    elif self.bmi >= 40:
      print("You're Obese Class 3!")
  

if __name__ == "__main__":
  height = float(input("Enter Height [CM]: "))
  weight = float(input("Enter Height [KG]: "))

  person = Person(weight, height)

  person.printBMIClass()

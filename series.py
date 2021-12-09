class Calculator:
  def __init__(self):
    self.operation = None;
    self.values = []
    
  def input_values(self):
    choice = None

    while choice not in ['1','2']:
      choice = input('Select Operator \n (1) Add (2) Subtract: ')

    self.operation = '+' if choice == '1' else '-'

    values = input('Enter Series of Numbers (Seperate by Comma ex. 1,2,3): ')
    self.values = values.split(',')

  def checkOperation(self,**kwargs):
    if self.operation == '-':
      kwargs['answer'] -= kwargs['value']
    elif self.operation == '+':
      kwargs['answer'] += kwargs['value']
    
    return kwargs['answer']

  def get_first_value(self):
    first = None
    for i, value in enumerate(self.values):
      try:
        first = float(value)
        return [i, first]
      except:
        continue

    return [0,0]
        

  def calculate(self):
    first = self.get_first_value();

    index_next_to_first = first[0] + 1
    answer = first[1]
    for i in self.values[index_next_to_first:]:
      try:
        character = float(i)
        answer = self.checkOperation(answer=answer, value=character)
      except:
        print(f'{i} cannot be converted')
      
    print(f"Total: {answer}")
  
if __name__ == '__main__':
  calculator = Calculator()

  calculator.input_values()
  calculator.calculate()

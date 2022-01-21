import random

class Cards(): 
  def __init__(self): 
    self.value = 0 
    self.points = 300 
print("")
Print("=========================================================") 
  def card(self): 
    self.cardFace = random.randint(1,13) 
    self.newCard = random.randint(1,13) 
    
    if self.cardFace > self.newCard and self.user == 'h': 
      self.points += 100 
    elif self.cardFace < self.newCard and self.user == 'l':
     self.points += 200 
    else: self.points -= 80 
 print("")
 
class game(): 
  def __init__(self): 
    self.isPlaying = True 
    self.points = 300 
    self.cardFace = random.randint(1,13) 
    def playing(self): 
      while self.isPlaying: 
        self.guess() 
    
    def guess(self): 
      if self.points <= 0: 
        self.isPlaying = False 
print("######################################################################")      
      print(self.cardFace) 
      self.user = input('Is the next card higher or lower? (h/l) : ').lower() 
print("######################################################################")    
Cards() 
game().playing()

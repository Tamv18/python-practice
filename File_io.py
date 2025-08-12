s=""
f = open("hiscore.txt", "w")
f.write(s)
f.close()
#creates a new file named hiscore

import random
def game():
  print("はじめまして。")
  score = random.randint(1, 62)
  with open("hiscore.txt") as f:
      hiscore = f.read()
      if(hiscore != ""):
          hiscore = int(hiscore)
      else:
          hiscore = 0
  print(f"Your score is: {score}")
  if(score>hiscore):
      with open("hiscore.txt", "w") as f:
          f.write(str(score))
      return score
game()
#Body of the code 

with open("hiscore.txt", "r") as f:
    print("Current high score:", f.read())
#reads file 

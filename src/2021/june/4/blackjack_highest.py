# Have the function BlackjackHighest(strArr) take the strArr parameter being passed which will be an array of numbers and letters 
# representing blackjack cards. Numbers in the array will be written out. So for example strArr may be ["two","three","ace","king"]. 
# The full list of possibilities for strArr is: two, three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace. 
# Your program should output below, above, or blackjack signifying if you have blackjack (numbers add up to 21) or not and the highest card in your hand in relation 
# to whether or not you have blackjack. If the array contains an ace but your hand will go above 21, you must count the ace as a 1. You must always try and stay below the 21 mark. 
# So using the array mentioned above, the output should be below king. The ace is counted as a 1 in this example because if it wasn't you would be above the 21 mark.

# Another example would be if strArr was ["four","ten","king"], the output here should be above king. 
# If you have a tie between a ten and a face card in your hand, return the face card as the "highest card". 
# If you have multiple face cards, the order of importance is jack, queen, king.

def blackjack_highest(str):
  dict = { 
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10,
    "ace": 1,
  }
  dictRating = {
    "" : 0,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 11,
    "queen": 12,
    "king": 13,
    "ace": 1,
  }
  
  aceCount = 0
  total = 0
  highest = ""
  abvBlw = ""

  for i in str:
    if(i == "ace"):
      aceCount += 1
      total += dict["ace"]
    else:
      total += dict[i]
    if(dictRating[i] > dictRating[highest]):
      highest = i

  while(total < 12 and aceCount > 0):
    highest = "ace"
    total += 10
    aceCount -= 1

  if(total > 21):
    abvBlw = "above"
  elif(total < 21):
    abvBlw = "below"
  else:
    abvBlw = "blackjack"

  str = abvBlw + " " + highest
  return str

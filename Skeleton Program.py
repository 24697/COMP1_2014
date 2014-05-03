# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
import time
import pickle

NO_OF_RECENT_SCORES = 10

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = time.strptime('01/01/70','%d/%m/%y')

Deck = [None]
Choice = ''
ace_high = 0


def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def options():
    loop = True
    print('OPTIONS MENU')
    print()
    print('1. Set Ace to be HIGH or LOW')
    print('')
    hold = str(input('Select an option from the menu (or enter q to quit): '))
    while loop == True:
        if hold == '1':
            loop_2 = True
            print('Do you want the ace to be (H)igh or (l)ow')
            hold_2 = str(input())
            while loop_2 == True:
                if hold_2 == 'High' or hold_2 == 'high' or hold_2 == 'h' or hold_2 == 'H':
                    ace_high = True
                    print('Aces are now high')
                    loop_2 = False
                elif hold_2 == 'Low' or hold_2 == 'low' or hold_2 == 'L' or hold_2 == 'l':
                    ace_high = False
                    print('Aces ae now low')
                    loop_2 = False
                else:
                    print('Invalid option please re-enter you option')
                    hold_2 = str(input())
            loop = False
        elif hold == 'q':
            loop = False
        else:
            print('Invalid option please re-enter you option')
            hold = str(input())
    return ace_high
        
def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Save recent scores')
  print('6. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  if Choice == 'q' or Choice == 'Q' or Choice == 'Quit' or Choice == 'quit':
    Choice = 'q'
  print()
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

def IsNextCardHigher(LastCard, NextCard,ace_high):
  Higher = False
  if ace_high == False:
    if NextCard.Rank > LastCard.Rank:
      Higher = True
  if ace_high == True:
    if NextCard.Rank == 1:
      NextCard.Rank = 14
    if LastCard.Rank == 1:
      LastCard.Rank = 14
  return Higher

def GetPlayerName():
  print()
  valid = False
  while valid == False:
    PlayerName = input('Please enter your name: ')
    if PlayerName == '':
      print('You must enter something for your name!')
    else:
      valid = True
  print()
  return PlayerName

def GetChoiceFromUser():
  loop = True
  while loop == True:
      Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ')
      if Choice == 'y' or Choice == 'Y' or Choice == 'yes' or Choice == 'Yes':
        Choice = 'y'
        loop = False
      elif Choice == 'n' or Choice == 'N' or Choice == 'no' or Choice == 'No':
        Choice = 'n'
        loop = False
      else:
          print('Invalid input, please re-enter value')
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0
    RecentScores[Count].Date = time.strptime('01/01/70','%d/%m/%y')

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print('{0:<15} {1:>15} {2:>15}'.format('Name:','Score:','Date:'))
  try:
    for Count in range(1, NO_OF_RECENT_SCORES + 1):
      if RecentScores[Count].Name != '':
        print('{0:<15} {1:>5} {2:>11}/{3:>0}/{4:>0}'.format(RecentScores[Count].Name, RecentScores[Count].Score, RecentScores[Count].Date.tm_mday, RecentScores[Count].Date.tm_mon, RecentScores[Count].Date.tm_year))
  except:
    pass
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  loop = True
  while loop == True:
    hold = str(input('Do you want to add you score to the reacent score list (y or n): '))
    if hold == 'y' or hold == 'Y' or hold == 'yes' or hold == 'Yes':
      hold = 'y'
      loop = False
    elif hold == 'n' or hold == 'N' or hold == 'no' or hold == 'No':
      hold = 'n'
      loop = False
    else:
      pass
  if hold == 'y':
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    hold1 = str(input('Please enter a date in the from DD/MM/YY: '))
    hold2 = time.strptime(hold1,'%d/%m/%y')
    RecentScores[Count].Date = hold2
  else:
    pass

def PlayGame(Deck, RecentScores,ace_high):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser()
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    Higher = IsNextCardHigher(LastCard, NextCard, ace_high)
    if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    else:
      GameOver = True
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def bubble_sort_scores(RecentScores):
  Variables_numb = len(RecentScores)
  run = True
  count1 = 1
  count2 = 2
  swap_area = 0
  finished = 0
  while run:
    if finished == Variables_numb-2:
      run = False
    elif RecentScores[count1].Score < RecentScores[count2].Score:
      swap_area = RecentScores[count1]
      RecentScores[count1] = RecentScores[count2]
      RecentScores[count2] = swap_area
      finished = 0
      count1 = 1
      count2 = 2
    elif RecentScores[count1].Score >= RecentScores[count2].Score:
      count1 +=1
      count2 +=1
      finished +=1
  return RecentScores

def save_scores(RecentScores):
  pickle.dump(RecentScores,open('scores.dat','wb'))
  print('Scores saved :) ')

def load_scores():
  RecentScores = pickle.load(open('scores.dat','rb'))
  return RecentScores
  
if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  try:
    RecentScores = load_scores()
  except:
    RecentScores = [None]
    for Count in range(1, NO_OF_RECENT_SCORES + 1):
      RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores,ace_high)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores,ace_high)
    elif Choice == '3':
      RecentScores = bubble_sort_scores(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      save_scores(RecentScores)
    elif Choice == '6':
        ace_high = options()

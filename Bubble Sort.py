def Arrange_scores(RecentScores):
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







#mine
  list_1 = 1
  list_2 = 2
  run = True
  time_to_run = len(RecentScores) - 1
  while run == True:
    if RecentScores[list_1].Score < RecentScores[list_2].Score:
      hold = RecentScores[list_1]
      RecentScores[list_1] = RecentScores[list_2]
      RecentScores[list_2] = hold
      list_1 += 1
      list_2 += 1
      changed = True
    if list_1 == time_to_run:
      if changed == True:
        list_1 = 1
        list_2 = 2
      else:
        run = False
  return RecentScores

def specialSort(toSort): 
  
     count = 0
     evens = []
     odds = [] 
    
     for item in toSort:
          if count % 2 == 0:
               evens.append(item)
          else:
               odds.append(item)

          count += 1

     return evens + odds 

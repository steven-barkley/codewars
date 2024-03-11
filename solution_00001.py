def open_or_senior(data):
  # Handicap 0 to 28 
  # Seniors >=55 and Handicap > 7 
  # All others are Open 
    output = []
    for item in data: 
      output += item
      
  #      output += item 
  # Run a for loop on data (which is a nested list)
  #  if data[0][0] >= 55 and data[0][1] > 7:
  #     output += "Senior"
  # else:
  #     output += "Open"
    return output
    
input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
print(open_or_senior(input))

#junk

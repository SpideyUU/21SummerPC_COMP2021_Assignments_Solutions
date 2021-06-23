import math
sec = 60 * 60 * 24
birth = sec // 7
death = sec // 13
immigrant = sec // 45
daySum = birth + death + immigrant
yearSum = daySum * 365

oneLater = 312032486 + yearSum
twoLater = oneLater + yearSum
threeLater = twoLater + yearSum
fourLater = threeLater + yearSum
fiveLater = fourLater + yearSum
print("There are " + str(format(birth, ',')) + " children are born, and " + str(format(death, ',')) + " people become dead per day" +
      ",\nand there are " + str(format(immigrant, ',')) + " people move to USA per day.\n" +
      "One year later, the population of USA is " + str(format(oneLater, ',')) +
      ",\ntwo years later, the population of USA is " + str(format(twoLater, ',')) +
      ",\nthree years later, the population of USA is " + str(format(threeLater, ',')) +
      ",\nfour years later, the population of USA is " + str(format(fourLater, ',')) +
      ",\nand five years later, the population of USA is " + str(format(fiveLater, ',')))

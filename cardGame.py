#lilly middleman
#card war game

numberCards=[]
for i in range(2,11):
    numberCards.append(i)
    numberCards[i-2]=str(numberCards[1-2])
print(numberCards)
suits=['s', 'c','h','d']
royals=['j','q','k','a']


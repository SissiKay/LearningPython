print("Welcome to the Tip Calcultor!")

total= input("What was the total of your bill?")
print (total)
total2= float(total)

p_tip= input("What percentage tip would you like to give? 10,12, or 15?")

print(p_tip)

p2_tip= (float(p_tip))/100 + 1.00

ppl= input("How many people are splitting the bill?")
print(ppl)

ppl2=int(ppl)

value= float (((total2 / ppl2) *(p2_tip)))
real_value = round(value,3)
value_better= str(real_value)

print("You should each pay: " + value_better)

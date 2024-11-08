weight=input("Enter the weight in pounds: ")
wg = float(weight)
kg_or_lbs=input("Enter the kg or lbs: ")
if(kg_or_lbs=="kg"):
    print(wg*.45)
else:
    print(wg/0.45)
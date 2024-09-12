income = float(input("Enter the monthly income: "))
rent,groceries,utilities,otherexp = float(input("rent ")),float(input("groceries")),float(input("utilities")),float(input("otherexp"))
totalExp = rent + groceries + utilities + otherexp
totalSaving = income - totalExp
percentIncomeSave = float(totalSaving/income * 100)
percentIncomeExp = float(totalExp/income * 100)
print("Total Saving: ",totalSaving)
print("  Percentage of income saving:",round(percentIncomeSave,2))
print("  percentIncomeExp",round(percentIncomeExp,2))
print(f"percentage of saving : {percentIncomeSave:.2f}")
print(f"percentage of expenses : {percentIncomeExp:.2f} ")
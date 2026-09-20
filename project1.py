expenses=[]
print=("welcome user")
while True:
  print=("HOME")
  print=("1.tell me about your expensess")
  print=("2.view all expenses")
  print=("3.view total expenses")
  print=("EXIT")

  choice=input("enter your choice:")
  if (choice==1):
    date=input("date of expense:")
    type=input('type of expense:')
    description=input("any description:")
    amount=input("amount")

  expense={
     'date':date,
     'type':type,
     "description":description,
     "amount":amount,
  }
  expenses.append(expense)
  print("done")
  if (choice==2):
    if(len(expenses==0)):
      print('empty')
    else:
      print("all expenses aare over here")
      count=1
      for eachexpense in expenses: print(f"\nExpense {count}")
      print("Date:", eachexpense["date"])
      print("Type:", eachexpense["type"]) 
      print("Description:", eachexpense["description"])
      print("Amount:", eachexpense["amount"])
      count+=1
  elif choice == "3":
    total = 0 
    for eachexpense in expenses: total += float(eachexpense["amount"])
    print("Total expenses:", total)
  elif choice =="4":
   print("Thank you! Exiting") 
  break 
else: 
  print("Invalid choice. Please")
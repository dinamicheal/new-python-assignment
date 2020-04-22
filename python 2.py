

age =input('Are you a cigarette addict older than 75 years old: [yes , no]?:').lower()

chronic = input('enter if you have severe chronic disease [yes, no]?:').lower()
immune = input('enter if your immune system too weak[yes,no]?: ').lower()

if age == 'yes' :
   age = True
else:
  age = False


if chronic == 'yes':
   chronic = True
else:
   chronic =False

if  immune == 'yes' :
    immune = True
else:
    immune = False

if age or chronic or immune == True   :
   print("you're in risky group")
else:
   print("you're not in risky group")
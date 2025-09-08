#Task 10.1 
def formate_name(f_name,l_name):
    a =f_name.title()
    b =l_name.title()
    output = (a,b)
    return output
print(formate_name("KarIme", "HassaIn"))

# Task 10.2
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) is True and month ==2:
    return 28
  return month_days[month-1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

#Function with output 
def formate_name (f_name, l_name):
  if f_name == "" or l_name=="":
    return "You do not put any valid input"
  format_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{format_f_name} {formated_l_name}"

print(formate_name(input("What is your first name? ", input("What is your last name? "))))

## FInal Project Calculator

def Calculator(num1, oparator, num2):
  print (Calculator)
  if oparator == "add":
    return num1+num2
  if oparator == "substrack":
    return num1-num2
  if oparator == "multiple":
    return num1*num2
  if oparator == "devide":
    return num1/num2


print(Calculator(input("What is your Number 1? "), input("What is your oparator"),  input("What is your 2nd Number? ")))

#Final_taks





#   Thomas Carney
#   CIS261
#   Course Project Phase 4

from datetime import datetime
######## create class definition
class UserInfo:
    def __init__(self):
        self.username = ''
        self.userpwd = ''
        self.userrole = ''
    def set_username(self, un):
        self.username = un
    def set_userpwd(self, pwd):
        self.userpwd = pwd
    def set_userrole(self, role):
        self.userrole = role
################################################################################
def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    ########## Open the file user.txt in append mode and assign to UserFile
     
    while True:
        ########## Write the line of code that will call function GetUserName and assign the return value to username
        username = GetUserName()
        if (username.upper() == "END"):
            break
        ########## Write the line of code that will call function GetUserPassword and assign the return value to userpwd
        userpwd = GetUserPassword()
        ########## Write the line of code that will call function GetUserRole() and assign the return value to userrole
        userrole = GetUserRole()
    ########## Write the lines of code that will create an object of the class, assign values to the properties, and append to list
        user = UserInfo()
        user.username = username
        user.set_userpwd(userpwd)
        user.set_userrole(userrole)
        UserList.append(user)
    printuserinfo()
    

def GetUserName():
    ##### write the code to enter the username or End and return username 
   return input('Enter user name or "End" to quit: ')

def GetUserPassword():
    ##### write the code to enter the pwd and return pwd
    return input('Enter password:  ')

def GetUserRole():
     userrole = input("Enter role (Admin or User): ")
     while True:
         ####### write the if statement that validates that Admin or User has been entered. If true, return userrole.  If false, re-input userrole     
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ") 


def printuserinfo():
# write the code that will loop through the list, assign values to variables from the object
    for user in UserList:
        username = user.username
        userpassword= user.userpwd
        userrole = user.userrole
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)

############################################################################################

def Login():
        # read login information a t storee of code that wil3######## Write the line of code that will open the file Users.txt in read mode
    
    
    UserName = input("Enter User Name: ")
    UserPwd = input("Enter Password: ")
    UserRole = "None"
       ########## Write the lines of code that will loop through the list and compare name and pwd to entry.  
    for user in UserList:
        if user.username == UserName and user.userpwd == UserPwd:
       #### write the lines of code that will assign property to user role if name and pwd match and return the values
            UserRole = user.userrole
            return UserRole, UserName, UserPwd
    return UserRole, UserName, UserPwd
#########################################################################################
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyy: ")
    todate = input("Enter End Date (mm/dd/yyyy: ")
    return fromdate, todate
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(DetailsPrinted):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    EmpFile = open("Employees.txt","r")
    while True:
        rundate = input ("Enter start date for report (MM/DD/YYYY) or All for all data in file: ")
        if (rundate.upper() == "ALL"):
            break
        try:
            rundate = datetime.strptime(rundate, "%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue  # skip next if statement and re-start loop
    while True:
        EmpDetail = EmpFile.readline()
        if not EmpDetail:
            break
        EmpDetail = EmpDetail.replace("\n", "") #remove carriage return from end of line
        EmpList = EmpDetail.split("|")
        fromdate = EmpList[0]
        if (str(rundate).upper() != "ALL"):
            checkdate = datetime.strptime(fromdate, "%m/%d/%Y")
            if (checkdate < rundate):
                continue        
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate  = float(EmpList[4])
        taxrate = float(EmpList[5])
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",  f"{hourlyrate:,.2f}", f"{grosspay:,.2f}",  f"{taxrate:,.1%}",  f"{incometax:,.2f}",  f"{netpay:,.2f}")
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        EmpTotals["TotEmp"] = TotEmployees
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay
        DetailsPrinted = True   
    if (DetailsPrinted):  #skip of no detail lines printed
        PrintTotals (EmpTotals)
    else:
        print("No detail information to print")
def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
if __name__ == "__main__":
    ##################################################
    ########## Write the line of code to call the method CreateUsers
    UserList = []
    CreateUsers()
    print()
    print("##### Data Entry #####")
    ########## Write the line of code to assign UserRole, UserName and UserPwd to the function Login
    UserRole, UserName, UserPwd = Login()
    DetailsPrinted = False  ###
    EmpTotals = {} ###
    ########## Write the if statement that will check to see if UserRole is equal to NONE (NOTE: code will show red error lines until this line is written)
    if UserRole == 'None':
        print(UserName," is invalid.")
    else:
    # only admin users can enter data
        ##### write the if statement that will check to see if the UserRole is equal to ADMIN (NOTE: code will show red error lines until this line is written)
        if UserRole.lower() == 'admin':
            EmpFile = open("Employees.txt", "a+")                
            while True:
                empname = GetEmpName()
                if (empname.upper() == "END"):
                    break
                fromdate, todate = GetDatesWorked()
                hours = GetHoursWorked()
                hourlyrate = GetHourlyRate()
                taxrate = GetTaxRate()
                EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(taxrate) + "\n"  
                EmpFile.write(EmpDetail)
        # close file to save data
            EmpFile.close()    
        printinfo(DetailsPrinted)



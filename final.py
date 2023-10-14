
class Bank:
    users = []
    admin = 'Admin'
    bankBalance = 0
    totalLoan = 0
    loanActive = True
    withdrawActive=True

    def createUser(self, name, email, address, accountType):
        accNo=f'{name}{email}'
        userInfo = User(name, email, address, accountType, self,accNo)
        self.users.append(userInfo)
        return userInfo
    def loginUser(self,username):
        for user in self.users:
            if user.name==username:
              return user
        return None
    
    def depositBankBalance(self, amount):
        self.bankBalance += amount

    def checkBalanceBank(self):
        print('\n---------welcome our bank------------\n')
        print(f'bank total balance : {self.bankBalance} ')
        print('\n-------------------------------------\n')
        return ''

    def withdrawBankBalance(self, amount):
        self.bankBalance -= amount

    def updateTotalLoan(self, amount):
        self.totalLoan += amount

    def showTotalLoan(self):
        print('\n---------welcome our bank------------\n')
        print(f'bank total loan amount : {self.totalLoan}')
        print('\n-------------------------------------\n')

    def showAllAcount(self):
      user_info = set()
      for user in self.users:
        user_info.add((user.name, user.accNo))

      print('\n--------show our all user account ------------\n')
      for name, acco in user_info:
        
        print(f'User: {name}, Account Number: {acco}')
        
      print('\n-------------------------------------\n')
      

    def deleteAccount(self, accNoIn):
        updated_users = [user for user in self.users if user.accNo != accNoIn]

        if updated_users != self.users:
            self.users = updated_users
            print('\n---------welcome our bank------------\n')
            print(f'This account has been deleted successfully')
            print('\n-------------------------------------\n')
        else:
          print(f'{accNoIn} this account does not exist in this bank')

    
        

       
    def loanFetureOnOff(self,value):
        if value ==1:
            self.loanActive=True
            print('\n---------welcome our bank------------\n')    
            print(f'loan feture on secessfully !! ')
            print('\n-------------------------------------\n')
        elif value==0:
            self.loanActive=False
            print('\n---------welcome our bank------------\n')    
            print(f'loan feture off secessfully !! ')
            print('\n-------------------------------------\n')

    def withdrawFetureOnOff(self,value):
        if value ==1:
            self.withdrawActive=True
            print('\n---------welcome our bank------------\n')    
            print(f'withdraw feture on secessfully !! ')
            print('\n-------------------------------------\n')
        
        elif value==0:
            self.withdrawActive=False
            print('\n---------welcome our bank------------\n')    
            print(f'withdraw feture off secessfully !! ')
            print('\n-------------------------------------\n')
        


class User:
    transactionHistory = []
    loanLimit = 2
    balance = 0
    accNo=None

    def __init__(self, name, email, address, accountType, bank,accNo):
        self.name = name
        self.email = email
        self.address = address
        self.accountTupe = accountType
        self.bank = bank
        self.accNo=accNo
        self.bank.users.append(self)
        
        print('\n---------walcome our bank------------\n')
        print(f'your account create secessfully !! your account number : {self.accNo}\n')
        print('-------------------------------------\n')

    def deposit(self, amount):
        if amount < 0:
            print('\n---------welcome our bank------------\n')
            print('invalid amount, please deposit a positive amount\n')
            print('-------------------------------------\n')

        else:
            self.balance += amount
            self.bank.depositBankBalance(amount)
            description = 'deposit'
            info = {description: amount}
            self.transactionHistory.append(info)
            print('\n---------welcome our bank------------\n')
            print(f'your deposit was successful! Your current balance: {self.balance}\n')
            print('-------------------------------------\n')
    def moneyTransferAnotherAccount(self,accountNumber,amount):
        for  user in self.bank.users:
            if user.accNo==accountNumber:
                if amount<=self.balance:
                    user.balance+=amount
                    self.balance-=amount
                    self.bank.bankBalance+=amount
                    des='money transfer'
                    description = f'{des}-account number-{accountNumber}-amount-{amount}'
                    info = {description: amount}
                    self.transactionHistory.append(info)
                    print('\n---------welcome our bank------------\n')
                    print(f'money transfer account number : {accountNumber}--amount--{amount}--successfully !!')
                    print('--------------------------------------')
                    return
                else:
                    print('\n-------------warning------------\n')
                    print('invalid amount \n')
                    print('-------------------------------------\n')
                    return

    
        print('\n-------------warning------------\n')
        print('invalid account number\n')
        print('-------------------------------------\n')
        return



    def withdraw(self, amount):
        if self.bank.withdrawActive:
            if amount <= self.balance:
                self.balance -= amount
                self.bank.withdrawBankBalance(amount)
                description = 'withdraw'
                info = {description: amount}
                self.transactionHistory.append(info)
                print('\n---------welcome our bank------------\n')
                print(f'your withdrawal was successful! Your current balance: {self.balance}')
                print('-------------------------------------\n')

            else:
              print(f'\n---------your current balance  : ({self.balance})------------\n')
              print('invalid amount\n')
              print('-------------------------------------\n')
        else:
             print('\n---------welcome our bank------------\n')
             print('----------the bank is bankrupt--------\n')
             print('-------------------------------------\n')
        

    def getBalance(self):
        print('\n---------your account  balance------------\n')
        print(f'your current balance: {self.balance}')
        print('-------------------------------------\n')

    def getTransactionHistory(self):
        print('\n---------your transaction history------------\n')
        for info in self.transactionHistory:
            for key, value in info.items():
                print(f'{key} --- {value}')
        print('\n-------------------------------------\n')

    def takeLoan(self, amount):
        if self.bank.loanActive:
            if self.loanLimit !=0 :
                self.balance += amount
                self.loanLimit -= 1
                self.bank.updateTotalLoan(amount)
                description = 'take loan'
                info = {description: amount}
                self.transactionHistory.append(info)
                print('\n--------- welcome our bank ------------\n')
                print(f'your loan was successful! Your loan limit: {self.loanLimit} times -- balance: {self.balance}')
                print('\n-------------------------------------\n')
            else:
                print('\n--------- welcome our bank ------------\n')
                print('your loan limit is over')
                print('\n-------------------------------------\n')
        else:
            print('\n--------- welcome our bank ------------\n')
            print('bank loan feature is off. If you want a loan, please contact our admin')
            print('\n-------------------------------------\n')

    def transferTo(self):
        pass


sonali = Bank()

currentUser=None
flag=True
while(flag):
    if currentUser ==None:
            print('\n---are you new in Sonali bank ? please access Adminauthority --\n')
        
            print('1.access admin authority ! please use (Admin) key  word\n')

            authName=input('\ngiven your access name : ')
            if sonali.admin==authName:
                currentUser=authName
            else:
                print('\n--------------warning-----------')
                print('\n invalid key word please wright (Admin) \n')
                print('--------------------------------')
    else:
        if currentUser !='Admin':
            print('chose your option !!\n')
            print('1.deposit \n')          
            print('2.withdraw \n')          
            print('3.check balance \n')          
            print('4.take loan \n')          
            print('5.check transaction history \n')          
            print('6.transfer the amount another user account \n')          
            print('7.user logout \n')          
            
            op=int(input('chose your option : '))
            if op==1:
                amount=int(input('give your deposit amount : '))
                currentUser.deposit(amount)
            elif op==2:
                amount=int(input('give your withdraw amount : '))
                currentUser.withdraw(amount)
            elif op ==3:
                currentUser.getBalance()
            elif op==4:
                 amount=int(input('give your loan amount : '))
                 currentUser.takeLoan(amount)
            elif op==5:
                currentUser.getTransactionHistory()
            elif op ==6:
                accountNumber=input('\nplease wright account number : ')
                amount=int(input('please wright your transection  amount : '))
                currentUser.moneyTransferAnotherAccount(accountNumber,amount)
            elif op==7:
                currentUser='Admin'
        else:
            print('chose your option !!\n')
            print('0.User login   \n')          
            print('1.create an account   \n')          
            print('2.delete user account   \n')          
            print('3.see all user accounts list  \n')          
            print('4.check the total available balance of the bank\n')          
            print('5.check the total loan amount \n')          
            print('6.on or off the loan feature of the bank \n')          
            print('7.on or off the withdraw feature of the bank \n')          
            print('8.admin logout \n')          
            
            op=int(input('chose your option : '))
            if op==0:

                info=input('\naccount holder name : ')
                
                loggedUser=sonali.loginUser(info)
                if loggedUser:
                    currentUser=loggedUser
                else:
                    print('\n--------------warning-----------')
                    print('\ninvalid user')
                    print('--------------------------------')
                    
            elif op==1:
                name=input('wright your name\n')
                email=input('wright your email\n')
                address=input('wright your address\n')
                acctupe=input('wright your account type ? (saving/current)  : ')
                sonali.createUser(name,email,address,acctupe)
            elif op==2:
                info=input('account number : ')
                sonali.deleteAccount(info)
            elif op ==3:
                sonali.showAllAcount()
               
            elif op==4:
                  sonali.checkBalanceBank()
            elif op==5:
                sonali.showTotalLoan()
            elif op ==6:
                value=input('if you loan feture on please wright (on/off) key word: ')
                if value=='on':
                    sonali.loanFetureOnOff(1)

                elif value=='off':
                    sonali.loanFetureOnOff(0)

                else:
                    print('\n--------------warning-----------')
                    print('invalid key word')
                    print('--------------------------------')

            elif op==7:
                value=input('if you withdraw feture on please wright (on/off) key word: ')
                if value=='on':
                    sonali.withdrawFetureOnOff(1)

                elif value=='off':
                    sonali.withdrawFetureOnOff(0)

                else:
                    print('\n--------------warning-----------')
                    print('invalid key word')
                    print('--------------------------------')
            
            elif op==8:
                flag=False


            

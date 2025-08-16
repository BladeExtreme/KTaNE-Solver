from .__basemod__ import BaseSolver
import math

class TaxReturns(BaseSolver):
    NAME = 'Tax Returns'

    def display(self):
        turnovers = []
        expenses = []
        hist = []

        while True:
            for a in range(12-len(hist)):
                self.local_header()
                print(f"Gross Turnovers & Expenses (Format should be `Turnover; Expense 1, Expense 2, Expense 3`. Separated with comma space and semi-colon betwen Turnover and Expense): ")
                for a in range(len(hist)):
                    print(f"> {' | '.join([hist[a][0], ', '.join(hist[a][1])])}")
                temp = input(f"> ").lower().split('; ')

                if len(temp)!=2: break
                elif len(temp[1].split(', '))!=3: break
                elif not temp[0].isdigit() or not all(a.isdigit() for a in temp[1].split(', ')): break
                elif int(temp[0])<0 or any(int(a)<0 for a in temp[1].split(', ')): break
                else:
                    hist.append([temp[0], [a for a in temp[1].split(', ')]])
                    continue
            
            if len(hist)!=12: continue
            else:
                turnovers = [int(a[0]) for a in hist]
                expenses = [sum(int(b) for b in a[1]) for a in hist]
                self.gross_turnover = sum(turnovers)
                self.gross_expense = sum(expenses)
                break

        while True:
            self.local_header()
            print(f"Gross Turnovers: ${str(self.gross_turnover)}")
            print(f"Gross Expenses: ${str(self.gross_expense)}")
            ans = input(f"Surname: ").lower()
            
            if not ans.isalpha(): continue
            else:
                self.surname = ans
                break
        
        while True:
            self.local_header()
            print(f"Gross Turnovers: ${str(self.gross_turnover)}")
            print(f"Gross Expenses: ${str(self.gross_expense)}")
            print(f"Surname: {self.surname.capitalize()}")
            ans = input(f"NI Number: ").lower().split(' ')
            
            if len(ans)!=3: continue
            elif not (ans[0].isalpha() and ans[1].isdigit() and ans[2].isalpha()): continue
            elif len(ans[2])!=1: continue
            else:
                self.NI = ' '.join(ans)
                break
        
        while True:
            self.local_header()
            print(f"Gross Turnovers: ${str(self.gross_turnover)}")
            print(f"Gross Expenses: ${str(self.gross_expense)}")
            print(f"Surname: {self.surname.capitalize()}")
            print(f"NI Number: {self.NI.upper()}")
            ans = input(f"Payroll Number: ").lower()

            if len(ans)!=6: continue
            elif not ans.isdigit(): continue
            else:
                self.payroll = ans
                break
        
    
    def _calculate(self):
        NI = self.NI[-1]

        def pension_table(lit, unlit):
            if lit==0 and unlit==0: return math.floor(0*self.gross_turnover)
            elif lit==unlit: return math.floor(0.15*self.gross_turnover)
            elif lit>unlit: return math.floor(0.05*self.gross_turnover)
            elif unlit>lit: return math.floor(0.1*self.gross_turnover)
        
        tfi_table = 'HBGFACED'
        tfi_bit = []

        if self.surname[0].upper() in 'ABCDEFGHIJKLM': tfi_bit.append('1')
        else: tfi_bit.append('0')

        if int(self.payroll[-1])%2==1: tfi_bit.append('1')
        else: tfi_bit.append('0')
        
        if NI.upper() in 'AC': tfi_bit.append('1')
        else: tfi_bit.append('0')

        self.pension_contributions = pension_table(len(self.eg.litind), len(self.eg.unlitind))
        match tfi_table[int(''.join(tfi_bit), 2)]:
            case 'A': self.tax_free_invesments = 599
            case 'B': self.tax_free_invesments = 1241
            case 'C': self.tax_free_invesments = 478
            case 'D': self.tax_free_invesments = 932
            case 'E': self.tax_free_invesments = 81
            case 'F': self.tax_free_invesments = 736
            case 'G': self.tax_free_invesments = 1647
            case 'H': self.tax_free_invesments = 0
        self.tax_free_invesments *= len(self.eg.uniqueports)
        self.gross_profit = self.gross_turnover - (self.gross_expense + self.pension_contributions + self.tax_free_invesments)
        
        if self.gross_profit>100000: self.AD = math.floor((self.gross_profit-100000)/2)
        else: self.AD = 0

        self.tax_free_allowance = 11850 - self.AD
        self.t_income_tax = self.gross_profit - self.tax_free_allowance

        self.br = math.floor(0.2*(34500 if self.t_income_tax>34500 else self.t_income_tax))
        self.hr = math.floor(0.4*(104000 if self.t_income_tax>138500 else self.t_income_tax-34500 if self.t_income_tax>34500 else 0))
        self.ar = math.floor(0.45*(self.t_income_tax-138500 if self.t_income_tax>138500 else 0))
        self.income_tax = self.br+self.hr+self.ar

        self.t_NIC = (self.gross_turnover - self.gross_expense)
        self.t_NIC -= 8423 if self.t_NIC>8424 else 0
        
        self.sr = math.floor(0.09*(37927 if self.t_NIC>37927 else self.t_NIC))
        self.er = math.floor(0.02*(self.t_NIC-37927 if self.t_NIC>37927 else 0))
        self.NIC = self.sr+self.er

        self.total_tax_bill = self.income_tax + self.NIC
        return self.total_tax_bill

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Gross Turnovers: £{str(self.gross_turnover)}")
        print(f"Gross Expenses: £{str(self.gross_expense)}")
        print(f"Surname: {self.surname.capitalize()}")
        print(f"NI Number: {self.NI.upper()}")
        print(f"Payroll Number: {self.payroll}\n")
        print(f"{self.answer_pretext}Total Tax: {str(sol)}")
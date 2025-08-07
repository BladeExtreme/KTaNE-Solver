from .__basemod__ import BaseSolver
import colorama as c
import requests
import math

c.init(autoreset=True)

class ForeignExchangeRates(BaseSolver):
    NAME = 'Foreign Exchange Rates'
    code = {'036': 'AUD','124': 'CAD','156': 'CNY','191': 'HRK','208': 'DKK','344': 'HKD','348': 'HUF','356': 'INR','360': 'IDR','376': 'ILS','392': 'JPY','410': 'KRW','458': 'MYR','484': 'MXN','554': 'NZD','578': 'NOK','608': 'PHP','643': 'RUB','702': 'SGD','710': 'ZAR','752': 'SEK','756': 'CHF','764': 'THB','826': 'GBP','840': 'USD','946': 'RON','949': 'TRY','975': 'BGN','978': 'EUR','985': 'PLN','986': 'BRL'}
    revcode = {v: k for k, v in code.items()}

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Row (In order from top to bottom row. Seperate with comma space): ").upper().split(', ')

            if len(ans)!=3: continue
            elif not all(a.isdigit() or a.isalpha() for a in ans): continue
            elif not all(a in list(self.code.values()) or a in list(self.code.keys()) for a in ans[:2]): continue
            else:
                self.target = 0; self.base = 0
                if self.eg.batt>=2:
                    self.target = ans[0] if ans[0].isalpha() else self.code[ans[0]]
                    self.base = ans[1] if ans[1].isalpha() else self.code[ans[1]]
                else:
                    self.base = ans[0] if ans[0].isalpha() else self.code[ans[0]]
                    self.target = ans[1] if ans[1].isalpha() else self.code[ans[1]]
                self.value = int(ans[2])
                break
        
        while 1:
            self.local_header()
            print(f"Row: {', '.join([self.base, self.target, str(self.value)])}")
            ans = input(f"Connection [Green, Red]: ").lower()

            if ans not in ['green', 'red']: continue
            else:
                self.state = True if ans=='green' else False
                break
        
        self.local_header()
        print(f"Row: {', '.join([self.base, self.target, str(self.value)])}")
        print(f"Connection: {'Green' if self.state else 'Red'}")
        print(f"Please wait for the result to be calculated...")
    
    def _calculate(self):
        if self.state:
            try:
                link = f"https://fer.eltrick.uk/latest"
                params = {"base":self.base, "symbols": self.target}
                resp = requests.get(link, params)

                resp.raise_for_status()
                data = resp.json()
                conv = math.floor(data["rates"][self.target]*self.value)

                if conv<10: return 0
                return 0 if str(conv)[1]=='0' else int(str(conv)[1])-1
            except:
                while 1:
                    self.local_header()
                    print(f"{c.Fore.RED}UNABLE TO GET API{c.Style.RESET_ALL} - An error occurred during the process of getting the result via API. Please enter this link: \'{'https://fer.eltrick.uk/latest?base='+self.base+'&symbols='+self.target}\' and input the rates below: ")
                    ans = input(f"Rates: ").lower()

                    if not ans.isdigit(): continue
                    else:
                        ans = float(ans)
                        self.rates = ans
                        break
                conv = math.floor(self.rates*self.value)

                if conv<10: return 0
                return 0 if str(conv)[1]=='0' else int(str(conv)[1])-1
        else:
            return int(self.revcode[self.target][1])-1

    def solve(self):
        ans_l = ['Top Left', 'Top Middle', 'Top Right', 'Middle Left', 'Middle', 'Middle Right', 'Bottom Left', 'Bottom Middle', 'Bottom Right']
        sol = self._calculate()
        self.local_header()
        print(f"Row: {', '.join([self.base, self.target, str(self.value)])}")
        print(f"Connection: {'Green' if self.state else 'Red'}")
        print(f"{self.answer_pretext}Press the {ans_l[sol]} button.")
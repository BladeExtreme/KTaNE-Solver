from .other.header import header
import colorama as c #type: ignore

c.init(autoreset=True)

def edgeworkCreate():
    batt, hold, ind = None, None, None

    while 1:
        header()
        batt = input('Total Battery: ')
        if not batt.isdigit(): continue
        elif int(batt)<0: continue
        else:
            batt = int(batt)
            break
    
    while 1:
        header()
        print(f"Total Battery: {batt}")
        hold = input('Total Holder: ')
        if not hold.isdigit(): continue
        elif int(hold)<0: continue
        elif int(hold)>batt: continue
        else:
            hold = int(hold)
            break
    
    while 1:
        header()
        print(f"Total Battery: {batt}")
        print(f"Total Holder: {hold}")
        
        ind = input(f"Indicators (Separators uses comma then space, Asterisk indicates lit state. If no indicators, press enter with no input): ").upper().split(', ')
        if not ind or ind == ['']:
            ind = []
            break
        else:
            formatted_ind = []
            for x in ind:
                clean_indicator = x.replace('*', '')
                if '*' in x:
                    formatted_ind.append(clean_indicator + '*')
                else:
                    formatted_ind.append(clean_indicator)
            litInd = [x for x in formatted_ind if '*' in x]
            unlitInd = [x for x in formatted_ind if '*' not in x]
            all_indicators = litInd + unlitInd

            valid_indicators = ['SND', 'CLR', 'CAR', 'IND', 'FRQ', 'SIG', 'NSA', 'MSA', 'TRN', 'BOB', 'FRK']
            if all(ind.replace('*', '') in valid_indicators for ind in formatted_ind):
                ind = all_indicators
                break
    
    while 1:
        header()
        print(f"Total Battery: {batt}")
        print(f"Total Holder: {hold}")
        print(f"Indicators: {', '.join(ind)}")

        print("Ports (Separator for each port in one plate should be comma space, Separator for each plate should be a newline. If inside a port plate is empty, don't input anything and press enter. `-` to exit port input):")
        print("Confirmed port names are ['PARALLEL', 'SERIAL', 'PS/2', 'RCA', 'DVI-D', 'RJ-45']")

        port_plates = []
        while True:
            p = input("> ").upper()
            if p == '-':
                break
            p = p.split(', ')

            group_1 = ['PARALLEL', 'SERIAL']
            group_2 = ['PS/2', 'RCA', 'DVI-D', 'RJ-45']
            empty = ['']

            valid_ports = [port for port in p if port in group_1 + group_2 + empty]

            if len(valid_ports) == len(p):
                has_group_1 = any(port in group_1 for port in p)
                has_group_2 = any(port in group_2 for port in p)

                if has_group_1 and has_group_2:
                    print(f"{c.Fore.RED}Error:", end=""); print(" A port plate cannot contain ports from both groups (SERIAL & PARALLEL with DVI-D, RCA, RJ-45 & PS/2).")
                    continue
                else:
                    if p!=['']: port_plates.append(p)
                    else: port_plates.append([])
            else:
                print(f"{c.Fore.RED}Error:", end=""); print(" Invalid port(s) entered. Please use valid port names.")
                continue
        break

    while 1:
        header()
        print(f"Total Battery: {batt}")
        print(f"Total Holder: {hold}")
        print(f"Indicators: {', '.join(ind)}")
        print(f"Ports: {'; '.join(['['+', '.join(x)+']' for x in port_plates])}")

        sn = input(f"Serial Number: ").upper()

        if not (any(a.isalpha() for a in sn) and any(a.isdigit() for a in sn)): continue
        elif len(sn)!=6: continue
        break
    
    while 1:
        header()
        print(f"Total Battery: {batt}")
        print(f"Total Holder: {hold}")
        print(f"Indicators: {', '.join(ind)}")
        print(f"Ports: {'; '.join(['['+', '.join(x)+']' for x in port_plates])}")
        print(f"Serial Number: {sn}")

        tm = input(f"Total Modules: ")
        if not tm.isdigit(): continue
        elif int(tm)<=0: continue
        else:
            tm = int(tm)
            break
    
    while 1:
        header()
        print(f"Total Battery: {batt}")
        print(f"Total Holder: {hold}")
        print(f"Indicators: {', '.join(ind)}")
        print(f"Ports: {'; '.join(['['+', '.join(x)+']' for x in port_plates])}")
        print(f"Serial Number: {sn}")
        print(f"Total Modules: {tm}")

        tn = input(f"Total Needies: ")
        if not tn.isdigit(): continue
        elif int(tn)<0: continue
        elif int(tn)>=tm: continue
        else:
            tn = int(tn)
            break

    header()
    print(f"Total Battery: {batt}")
    print(f"Total Holder: {hold}")
    print(f"Indicators: {', '.join(ind)}")
    print(f"Ports: {'; '.join(['['+', '.join(x)+']' for x in port_plates])}")
    print(f"Serial Number: {sn}")
    print(f"Total Modules: {tm}")
    print(f"Total Needies: {tn}")
    print(f"\n{c.Fore.GREEN}SETUP COMPLETE", end=""); print(f" - Edgework Setup Completed. Proceed to menu!")
    input()
    return Edgework(batt, hold, ind, port_plates, sn, tm, tn)

class Edgework:
    def __init__(self, batt:int, hold:int, ind:list[str], ports:list[str], sn:str, modules:int, needy:int):
        self.batt = batt
        self.hold =  hold
        self.ind = ind
        self.litind = [a for a in ind if '*' in a]
        self.unlitind = [a for a in ind if '*' not in a]
        self.ports = ports; self.uniqueports = list(set([a for b in self.ports for a in b]))
        self.sn = sn; self.snletter = [a for a in sn if a.isalpha()]; self.sndigit = [a for a in sn if a.isdigit()]
        self.modules = modules
        self.needy = needy
        self.solves = 0
        self.strikes = 0
    
    def solve(self, N:int=1):
        if self.solves+N<=self.modules and self.solves+N>=0: self.solves+=N
    
    def strike(self, N:int=1):
        if self.strikes+N<=self.modules and self.strikes+N>=0: self.strikes+=N
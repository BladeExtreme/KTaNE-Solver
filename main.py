from ktanesolver.other.header import header
from ktanesolver.other.help import help
from ktanesolver.other.modulelist import modulelist, MODULE_MAP
from ktanesolver.edgework import edgeworkCreate
from ktanesolver.patchnotes import patchnotes
import ktanesolver.modules as m
import colorama as c #type: ignore

HELP_INFO = True
OPTIONS = {
    'fmn': None,
    'bm': None,
    'swan': None,
    'ttks': None,
    'troll': None,
    'dividedsquares': None,
    'autosolve': True,
    'autostrike': True,
    'max_strike': 3,
}
EDGEWORK = None

c.init(autoreset=True)

def menu():
    global HELP_INFO, EDGEWORK, OPTIONS
    while True:
        header()
        
        if EDGEWORK is None:
            print(f"{c.Fore.RED}Edgework not initialized.\n")
        else:
            print(f"{EDGEWORK.batt}b {EDGEWORK.hold}h // {', '.join(EDGEWORK.ind)} // {'; '.join(['['+', '.join(x)+']' for x in EDGEWORK.ports])} // {EDGEWORK.sn}")
            print(f"Modules\t: {EDGEWORK.modules}")
            print(f"Needies\t: {EDGEWORK.needy}\n")
            print(f"Solves\t: {EDGEWORK.solves}\t{c.Fore.GREEN+'[AUTOSOLVE]' if OPTIONS['autosolve'] else ''}")
            print(f"Strikes\t: {EDGEWORK.strikes}\t{c.Fore.RED+'[STRIKE TRACK]' if OPTIONS['autostrike'] else ''}")
            print()
            if OPTIONS['fmn']: print(f"FORGET ME NOT - {c.Fore.YELLOW}ACTIVE")
            if OPTIONS['ttks']: print(f"TURN THE KEYS - {c.Fore.YELLOW}ACTIVE {c.Style.RESET_ALL}| {c.Fore.GREEN if OPTIONS['ttks'].left else c.Fore.RED}Left{c.Style.RESET_ALL}/{c.Fore.GREEN if OPTIONS['ttks'].right else c.Fore.RED}Right")
            if OPTIONS['troll']: print(f"TROLL - STAGE: {OPTIONS['troll'].stage}")
            if OPTIONS['dividedsquares']:
                if isinstance(OPTIONS['dividedsquares'], m.DividedSquares): print(f"DIVIDED SQUARES - HOLD ON {OPTIONS['dividedsquares'].max_solve} SOLVES")
                else: print(f"DIVIDED SQUARES - ACTIVE")
                
            print()

        if HELP_INFO: print("Enter '-help' to get more information.\n")

        op_menu = input("cmd > ").lower()
        
        if op_menu=='-edgework': EDGEWORK = edgeworkCreate()
        elif op_menu=='-help': help()
        elif op_menu=='-exit':
            print(f"{c.Fore.BLUE}PROGRAM TERMINATED:{c.Style.RESET_ALL} Thank you for using this program!")
            break
        elif op_menu=='-modulelist': modulelist()
        
        elif op_menu=='-autosolve': OPTIONS['autosolve'] = not OPTIONS['autosolve']
        elif op_menu=='-autostrike': OPTIONS['autostrike'] = not OPTIONS['autostrike']

        elif op_menu=='-turnthekeys':
            if OPTIONS['ttks'] is None: OPTIONS['ttks'] = m.TurnTheKeys()
            else: OPTIONS['ttks'] = None
        elif op_menu=='-turnthekeys left' and OPTIONS['ttks']: OPTIONS['ttks'].left = not OPTIONS['ttks'].left
        elif op_menu=='-turnthekeys right' and OPTIONS['ttks']:
            if OPTIONS['ttks'].left: OPTIONS['ttks'].right = not OPTIONS['ttks'].right
        
        elif op_menu[:len('-troll')] == '-troll':
            temp_l = op_menu.split(' ')
            if len(temp_l) == 3:
                try:
                    amount = int(temp_l[1])
                    unsolve = int(temp_l[2])
                    if amount >= EDGEWORK.modules: pass
                    else:
                        OPTIONS['troll'] = m.Troll(EDGEWORK, 0, amount, unsolve)
                except ValueError: pass
            elif len(temp_l) == 1:
                if OPTIONS['troll'] is None: OPTIONS['troll'] = m.Troll(EDGEWORK, 0)
                else: OPTIONS['troll'] = None

        elif op_menu == '-patchnotes': patchnotes()

        elif op_menu == '-dividedsquares':
            if OPTIONS['dividedsquares']: OPTIONS['dividedsquares'] = None
            else: OPTIONS['dividedsquares'] = True
        
        elif EDGEWORK:
            v = None

            if op_menu[:len('-strike')] == '-strike':
                temp_l = op_menu.split(' ')
                if len(temp_l) == 2:
                    try:
                        strike_value = int(temp_l[1])
                        if strike_value > OPTIONS['max_strike']: pass
                        else:
                            EDGEWORK.strike(strike_value)
                            if OPTIONS['autostrike'] and strike_value>0: EDGEWORK.solve(strike_value*-1)
                    except ValueError: pass
                elif len(temp_l) == 1:
                    EDGEWORK.strike()
                    if OPTIONS['autostrike']: EDGEWORK.solve(-1)
            elif op_menu[:len('-solve')] == '-solve':
                temp_l = op_menu.split(' ')
                if len(temp_l) == 2:
                    try:
                        solve_value = int(temp_l[1])
                        if solve_value > EDGEWORK.modules: pass
                        else:
                            EDGEWORK.solve(solve_value)
                    except ValueError: pass
                elif len(temp_l)==1:
                    EDGEWORK.solve()
            
            elif op_menu=='-forgetmenot':
                if OPTIONS['fmn'] is None: OPTIONS['fmn'] = m.ForgetMeNot(EDGEWORK)
                else: OPTIONS['fmn'] = None
            elif op_menu=='-binarymemory':
                if OPTIONS['bm'] is None: OPTIONS['bm'] = m.BinaryMemory(EDGEWORK)
                else: OPTIONS['bm'] = None

            elif op_menu in MODULE_MAP: 
                if OPTIONS['ttks']:
                    if (op_menu in OPTIONS['ttks'].FORBIDDEN_MOD['left'] and not OPTIONS['ttks'].left) or (op_menu in OPTIONS['ttks'].FORBIDDEN_MOD['right'] and not OPTIONS['ttks'].right): continue
                
                if op_menu=='troll' and OPTIONS['troll'] is None: continue
                elif op_menu=='troll' and OPTIONS['troll']:
                    OPTIONS['troll'].solve()
                    if OPTIONS['troll'].state!=3: continue
                elif OPTIONS['troll']:
                    if OPTIONS['troll'].state==2 and op_menu!='troll': continue

                elif op_menu=='forgetmenot':
                    if OPTIONS['fmn'] is None: continue
                    elif len(OPTIONS['fmn'].number)<3:
                        OPTIONS['fmn'].error()
                        continue
                    else: v = OPTIONS['fmn'].solve()

                elif op_menu=='binarymemory':
                    if OPTIONS['bm'] is None: continue
                    else: v = OPTIONS['bm'].solve()

                else:
                    v = MODULE_MAP[op_menu](EDGEWORK)
                    EDGEWORK.solved_modules.append(v)
                    if op_menu=='dividedsquares' and OPTIONS['dividedsquares']==True:
                        OPTIONS['dividedsquares'] = v
                        if OPTIONS['dividedsquares'].max_solve<EDGEWORK.solves:
                            OPTIONS['dividedsquares'] = True
                        continue

            if v and OPTIONS['autosolve']: EDGEWORK.solve()
            if v and OPTIONS['fmn']: OPTIONS['fmn'].display()
            if v and OPTIONS['bm']: OPTIONS['bm'].display()
            if v and OPTIONS['troll']: 
                if OPTIONS['troll'].state==1: OPTIONS['troll'].moduleSolve()
                elif OPTIONS['troll'].state==3: OPTIONS['troll'] = None
            if v and OPTIONS['dividedsquares']:
                OPTIONS['dividedsquares'].moduleSolve()
                if OPTIONS['dividedsquares'].max_solve==EDGEWORK.solves: OPTIONS['dividedsquares'] = None
        HELP_INFO = False

if __name__=="__main__":
    menu()
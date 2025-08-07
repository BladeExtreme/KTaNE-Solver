from ktanesolver.other.header import header
from ktanesolver.other.help import help
from ktanesolver.other.modulelist import modulelist, MODULE_MAP
from ktanesolver.edgework import edgeworkCreate
from ktanesolver.patchnotes import patchnotes
import colorama as c #type: ignore

HELP_INFO = True
OPTIONS = {
    'fmn': False,
    'swan': False,
    'autosolve': True,
    'autostrike': True,
    'max_strike': 3
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
            print(f"Strikes\t: {EDGEWORK.strikes}\t{c.Fore.RED+'[STRIKE TRACK]' if OPTIONS['autostrike'] else ''}\n")

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
        
        elif op_menu == '-patchnotes':
            patchnotes()
        
        elif EDGEWORK is not None:
            v = False

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

            if op_menu in MODULE_MAP: v = MODULE_MAP[op_menu](EDGEWORK)
            if v and OPTIONS['autosolve']: EDGEWORK.solve()
        HELP_INFO = False

if __name__=="__main__":
    menu()
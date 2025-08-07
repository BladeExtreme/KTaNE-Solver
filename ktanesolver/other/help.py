from .header import header
from ..__version__ import __version__
import colorama as c #type: ignore

def help():
    header()
    instructions = f'''Welcome to BladeExtreme's KTaNE Solver {__version__}!

Before diving into the solver, you'll first need to define your edgework. To do this, simply enter the command `edgework`. Once you've set up your edgework, you can begin solving by typing the module's full name — without any apostrophes, the word "The", or spaces. Make sure to include any symbols if the module name contains them. If you ever need a list of all available module names, simply type the command `-modulelist`. 

To let the solver know that the "Forget Me Not" module is present, use the command `-forgetmenot` to toggle it on or off. When you're ready to enter or solve the module, just type `forgetmenot`.

Similarly, if you have "The Swan" module, use `-swan` to toggle it on or off. When you're ready to enter or solve "The Swan", simply type `swan`.

If you ever need notes to the recent changes of this solver program, type the comand `-patchnotes` to view all of the patch notes.

---

{c.Back.WHITE+c.Fore.BLACK}Strike and Solve Management{c.Style.RESET_ALL}
- If you've struck the bomb at any point, enter `-strike` or `-strike N` (where N is the number of strikes you want to add). By default, N is set to 1, but you can also use negative numbers, though the total strikes will never go below 0.
  
- If you've solved a module, enter `-solve` or `-solve N` (where N is the number of modules you want to add to your solved counter). Again, by default, N is 1, but you can adjust the number as needed. Negative numbers are allowed, but the total solves will never go below 0.

{c.Back.WHITE+c.Fore.BLACK}Auto-Tracking Options{c.Style.RESET_ALL}
- If you'd prefer not to manually track the number of modules solved, you can enable the `-autosolve` toggle. When on, a green indicator will appear beside the solve counter, and each module completed will automatically update the count.

- Similarly, if you'd rather not manually adjust your solve counter after a mistake or error, use the `-autostrike` toggle. When enabled, every time you enter `-strike N`, the solver will automatically subtract the same number of solves, assuming the solution was incorrect. This ensures the solve counter is adjusted automatically when errors occur.
'''
    print(instructions)
    input()
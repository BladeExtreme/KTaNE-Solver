from .__basemod__ import BaseSolver

class WhosOnFirst(BaseSolver):
    NAME = 'Who\'s on First'
    displist = [
        ['ur'],
        ['first', 'okay', 'c'],
        ['yes', 'nothing', 'led', 'they are'],
        ['blank', 'read', 'red', 'you', 'your', "you're", 'their'],
        ['', 'reed', 'leed', "they're"],
        ['display', 'says', 'lead', 'hold on', 'you are', 'there', 'see', 'cee']
    ]
    wordlist = {
        "blank": ["wait", "right", "okay", "middle", "blank"],
	    "done": ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"],
	    "first": ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"],
	    "hold": ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"],
	    "left": ["right", "left"],
	    "like": ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"],
	    "middle": ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"],
	    "next": ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"],
	    "no": ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"],
	    "nothing":["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"],
	    "okay": ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"],
	    "press": ["right", "middle", "yes", "ready", "press"],
	    "ready": ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"],
	    "right": ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"],
	    "sure": ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"],
	    "u": ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"],
	    "uh uh": ["ur", "u", "you are", "you're", "next", "uh uh"],
	    "uhhh": ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"],
	    "ur": ["done", "u", "ur"],
	    "wait": ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"],
	    "what": ["uhhh", "what"],
	    "what?": ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"],
	    "yes": ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"],
	    "you are":["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"],
	    "you": ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"],
	    "your": ["uh uh", "you are", "uh huh", "your"],
	    "you're": ["you", "you're"]
    }


    def __init__(self, edgework):
        self.stage = 1
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def display(self):
        while 1:
            self.local_header()
            print(f"STAGE {self.stage} OF 3")
            
            ans = input("Display (With apostrophe. If it's empty, enter with no input): ").lower()
            
            if not ans.isalpha() and ans!='': continue
            elif not any([ans in a for a in self.displist]): continue
            else:
                self.dispword = ans
                break
        
        while 1:
            self.local_header()
            print(f"STAGE {self.stage} OF 3")
            print(f"Display: {self.dispword.capitalize()}")

            ans = input("Buttons (With apostrophe. Each word is seperated with comma space): ").lower().split(', ')
            if len(ans)!=6: continue
            elif not all([a in self.wordlist.keys() for a in ans]): continue
            elif len(set(ans))!=6: continue
            else:
                self.buttonword = ans
                break
    
    def _calculate(self):
        to_look = ''
        for a in range(len(self.displist)):
            if self.dispword in self.displist[a]:
                to_look = self.buttonword[a]
                break
        
        return [a for a in self.wordlist[to_look] if a in self.buttonword][0]
    
    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"STAGE {self.stage} OF 3")
        print(f"Display: {self.dispword.capitalize()}")
        print(f"Buttons: {', '.join([a.capitalize() for a in self.buttonword])}")
        print(f"{self.answer_pretext}Words: {sol.capitalize()}")
        input()
        self.stage+=1

        while self.stage!=4:
            self.display()
            
            sol = self._calculate()
            self.local_header()
            print(f"STAGE {self.stage} OF 3")
            print(f"Display: {self.dispword.capitalize()}")
            print(f"Buttons: {', '.join([a.capitalize() for a in self.buttonword])}")
            print(f"{self.answer_pretext}Words: {sol.capitalize()}")
            self.stage+=1
            
            if self.stage==4: continue
            input()
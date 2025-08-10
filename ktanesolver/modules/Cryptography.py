from .__basemod__ import BaseSolver

class Cryptography(BaseSolver):
    NAME = 'Cryptography'
    sentences = [
      "AFROSTYIMEWNHDBC", "ASQUEZINGWRCHPLTOVD", "ITWASLHEMO", "ITWASHEVRYNGLKD", "NOWIDTHABLESRFGMUPY", "TOEDGHISWAYLNCRPFUMK", "HEICDSOFNTGAY", "OFCURSEHDI", "NOWARMTHCULDIYE", "HECARIDSOWNLTMPUYB", "BUTHEWASIGFDNROC", "THEFIRMWASKNOCGDLY",
      "BUTWHADISCROGE", "ANDWHETYSIMCOGULRP", "ANDTHEWOULGIRSYBVKM", "THECOLDWINMFRZSAUPVKG", "HOWCULDITBERS", "ANDITHWOEGRCSM", "THEMNIOFARLYSUBGCKPD", "THEAVISRNDOWLCUBFGMYP", "MADEHISYRTNLPBUOKWGVC", "HARDNSPFLITOMWCEVUKG", "EVNTHBLIDMSOGAPRKW",
      "THISMUBEDNCLYROGWFA", "WHENILYOUCMTS", "THEYOFNCAMDWSLRGVI", "FOULWEATHRDINKVM", "THERISNODUBAMLYW", "THERISODYAFWBVUCGNML", "SECRTANDLFOIY", "NOBDYEVRSTPHIMAWGLKCU", "SCROGEANDHWPTFIKMY", "SCROGEWAHILXUTDMNYF", "SCROGEKNWHAD", "SCROGENVPAITDULMY", "EXTRNALHDCOIFUSG", "SOMETIPLNWHBUCADRGY"
    ]
    lettcount = [
        [1, 6, 4, 3], [1, 9, 9, 8], [2, 3, 3, 3], [2, 3, 3, 4], [2, 4, 4, 4], [2, 4, 3, 3], [2, 4, 3, 6], [2, 6, 2, 3], [2, 6, 5, 4], [2, 7, 3, 3], [3, 2, 3, 1],
        [3, 4, 3, 5], [3, 4, 3, 7], [3, 4, 4, 3], [3, 4, 5, 3], [3, 4, 6, 3], [3, 5, 2, 2], [3, 5, 4, 2], [3, 7, 2, 7], [3, 8, 4, 3], [4, 3, 4, 3], [4, 3, 5, 2],
        [4, 3, 5, 4], [4, 4, 2, 10], [4, 4, 3, 4], [4, 5, 4, 4], [4, 7, 5, 4], [5, 2, 2, 5], [5, 2, 5, 5], [6, 3, 13, 3], [6, 4, 7, 3], [7, 3, 2, 4], [7, 3, 3, 4],
        [7, 4, 2, 3], [7, 5, 7, 3], [8, 4, 3, 4], [9, 6, 3, 2]
    ]

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Display (First four words, each word separated by space): ").lower().split(' ')

            if len(ans)<4: continue
            elif not any(b in [len(a) for a in ans] for b in self.lettcount): continue
            else:
                self.disp = ans[0:4]
                break
        
        while 1:
            self.local_header()
            print(f"Display: {' '.join(map(lambda x: x.upper(), self.disp))}")
            ans = input(f"Buttons (Letters separated by comma space): ").lower().split(', ')

            if len(ans)!=5: continue
            elif not all(a.isalpha() for a in ans): continue
            elif len(set(ans))!=5: continue
            else:
                self.button = ans
                break
    
    def _calculate(self):
        return tuple([a.lower() for a in self.sentences[self.lettcount.index(list(map(lambda x: len(x), self.disp)))] if a.lower() in self.button])

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Display: {' '.join(map(lambda x: x.upper(), self.disp))}")
        print(f"Buttons: {', '.join(map(lambda x: x.upper(), self.button))}")
        print(f"{self.answer_pretext}Order press: {', '.join(sol)}")
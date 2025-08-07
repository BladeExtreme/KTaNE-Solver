from .__basemod__ import BaseSolver

class ColourFlash(BaseSolver):
    NAME = 'Colour Flash'

    class colorclass:
        def __init__(self,w,c):
            self.label = w
            self.color = c

    def display(self):
        self.words = []; self.colors = []
        while 1:
            self.local_header()
            ans = input(f'Words [Red, Yellow, Green, Blue, Magenta, White] (Seperated by comma space): ').lower().split(', ')

            if not all(a.isalpha() for a in ans): continue
            elif not all(a in ['red', 'yellow', 'green', 'blue', 'magenta', 'white'] for a in ans): continue
            elif len(ans)!=8: continue
            else:
                self.words = ans
                break

        while 1:
            self.local_header()
            print(f"Words: {', '.join([a.capitalize() for a in self.words])}")
            ans = input(f'Colors [Red, Yellow, Green, Blue, Magenta, White] (Seperated by comma space): ').lower().split(', ')

            if not all(a.isalpha() for a in ans): continue
            elif not all(a in ['red', 'yellow', 'green', 'blue', 'magenta', 'white'] for a in ans): continue
            elif len(ans) != len(self.words): continue
            else:
                self.colors = ans
                break

        self.list = [self.colorclass(self.words[a], self.colors[a]) for a in range(len(self.words))]    
    
    def _calculate(self):
        final = self.list[-1].color

        match final:
            case 'red':
                if [a.color for a in self.list].count('green')>=3: return [a for a in range(len(self.list)) if 'green' in [self.list[a].color, self.list[a].label]][2], 'yes'
                elif [a.color for a in self.list].count('blue')>=1: return [a for a in range(len(self.list)) if self.list[a].label=='magenta'][0], 'no'
                else: return [a for a in range(len(self.list)) if 'white' in [self.list[a].color, self.list[a].label]][-1], 'yes'
            case 'yellow':
                if len([a for a in self.list if a.color=='green' and a.label=='blue'])>0: return [a for a in range(len(self.list)) if self.list[a].color=='green'][0], 'yes'
                elif len([a.color for a in self.list if a.label=='white' and (a.color=='white' or a.color=='red')])>0: return [a for a in range(len(self.list)) if self.list[a].label!=self.list[a].color][1], 'yes'
                else: return (len([a for a in self.list if a.label=='magenta' or a.color=='magenta'])-len([a for a in self.list if a.label=='magenta' and a.color=='magenta']))-1, 'no'
            case 'green':
                if [a for a in range(len(self.list)-1) if self.list[a].label==self.list[a+1].label and self.list[a].color!=self.list[a+1].color]!=[]: return 4, 'no'
                elif [a.color for a in self.list].count('magenta')>=3: return [a for a in range(len(self.list)) if 'yellow' in [self.list[a].color, self.list[a].label]][0], 'no'
                else: return [a for a in range(len(self.list)) if self.list[a].color==self.list[a].label][0], 'yes'
            case 'blue':
                if len([a for a in range(len(self.list)) if self.list[a].color!=self.list[a].label])>=3: return [a for a in range(len(self.list)) if self.list[a].color!=self.list[a].label][0], 'yes'
                elif [a for a in self.list if (a.label=='red' and a.color=='yellow') or (a.label=='yellow' and a.color=='white')]!=[]: return [a for a in range(len(self.list)) if self.list[a].label=='white' and self.list[a].color=='red'][0], 'no'
                else: return [a for a in range(len(self.list)) if 'green' in [self.list[a].color, self.list[a].label]][-1], 'yes'
            case 'magenta':
                if [a for a in range(len(self.list)-1) if self.list[a].label!=self.list[a+1].label and self.list[a].color==self.list[a+1].color]!=[]: return 2, 'yes'
                elif len([a for a in self.list if a.label=='yellow'])>len([a for a in self.list if a.color=='blue']): return [a for a in range(len(self.list)) if self.list[a].label=='yellow'][0], 'no'
                else: return [a for a in range(len(self.list)) if self.list[6].label], 'no'
            case 'white':
                if self.list[2].color in [self.list[3].label, self.list[4].label]: return [a for a in range(len(self.list)) if self.list[a].color==self.list[a].label][0], 'no'
                elif self.colorclass(c='red', w='yellow') in self.list: return [a for a in range(len(self.list)) if self.list[a].color=='blue'][-1], 'yes'
                else:  return 0, 'no'

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Words: {', '.join([a.capitalize() for a in self.words])}")
        print(f"Colors: {', '.join([a.capitalize() for a in self.colors])}")
        print(f"{self.answer_pretext}Press on {str(sol[0]+1)+('st' if sol[0]==0 else 'nd' if sol[0]==1 else 'rd' if sol[0]==2 else 'th' if sol[0]==3 else 'fifth' if sol[0]==4 else 'sixth' if sol[0]==5 else 'seventh')} button ({sol[1]})")
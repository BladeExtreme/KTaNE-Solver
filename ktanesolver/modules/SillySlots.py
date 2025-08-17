from .__basemod__ import BaseSolver

class SillySlots(BaseSolver):
    NAME = 'Silly Slots'

    def display(self):
        self.history = []
        while True:
            self.local_header()
            print(f"Symbol and Color (Separated with a comma space): "); a = 0
            for _ in range(len(self.history)):
                print(f" {'Left  : ' if a==0 else 'Middle: ' if a==1 else 'Right : '}{self.history[a]}")
                a+=1
            ans = input(f" {'Left  : ' if a==0 else 'Middle: ' if a==1 else 'Right : '}").lower().split(', ')

            if len(ans)!=2: continue
            elif not all(a.isalpha() for a in ans): continue
            elif not all(a[0] in ['red','blue','green'] for a in ans): continue
            elif not all(a[1] in ['cherry','bomb','grape','coin'] for a in ans): continue
            else:
                self.history.append(ans)
                break   
        pass
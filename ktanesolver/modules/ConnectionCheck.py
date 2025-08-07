from .__basemod__ import BaseSolver

class ConnectionCheck(BaseSolver):
    NAME = 'Connection Check'
    table = [
        ['23','13','12','67','67','45','45',''],
        ['246','134','2','127','6','1578','468','67'],
        ['236','16','146','35678','467','12345','458','47'],
        ['27','17','48','38','67','57','1256','34'],
        ['23','147','157','2678','367','458','2345','46'],
        ['2368','146','14678','23567','478','1234','3458','1357'],
        ['248','1367','2467','135','468','2357','2368','157'],
        ['267','1378','2568','578','3467','1357','124568','2347']
    ]

    def display(self):
        self.pair = []
        while 1:
            self.local_header()
            for a in range(len(self.pair)):
                print(f"{'First' if a==0 else 'Second' if a==1 else 'Third' if a==2 else 'Fourth'} Pair: {' '.join(list(map(lambda x: str(x), self.pair[a])))}")
            ans = input(f"{'First' if len(self.pair)==0 else 'Second' if len(self.pair)==1 else 'Third' if len(self.pair)==2 else 'Fourth'} Pair [1-8] (Connection seperated with space): ").lower().split(' ')

            if len(ans)!=2: continue
            if not all(a.isdigit() for a in ans): continue
            if not all(int(a) in range(1, 9) for a in ans): continue
            if ans[0] == ans[1]: continue
            else:
                self.pair.append(list(map(lambda x: int(x), ans)))
                if len(self.pair)==4: break
    
    def _calculate(self):
        rowbook = ['7HPJ','34XYZ','SLIM','15BRO','20DGT','8CAKE','9QVN','6WUF']
        connection = []
        flat = [a for b in self.pair for a in b]
        pos = -1
        
        if len(set(flat))==8: pos = -1
        elif flat.count(1)>=2: pos = 0
        elif flat.count(7)>=2: pos = -1
        elif flat.count(2)>=3: pos = 1
        elif flat.count(5)==0: pos = 4
        elif flat.count(8)==2: pos = 2
        elif self.eg.batt in range(1, 6): pos = self.eg.batt - 1
        
        tblrow = [a for a in range(len(rowbook)) if self.eg.sn[pos].upper() in rowbook[a]][0]

        for a in self.pair:
            if str(a[1]) in self.table[tblrow][a[0]-1]: connection.append(True)
            else: connection.append(False)
        
        return connection

    def solve(self):
        sol = self._calculate()
        self.local_header()
        for a in range(len(self.pair)):
            print(f"{'First' if a==0 else 'Second' if a==1 else 'Third' if a==2 else 'Fourth'} Pair: {' '.join(list(map(lambda x: str(x), self.pair[a])))}")
        print()
        print(f"{self.answer_pretext}Good Connection: ")
        for x in range(4):
            if sol[x]:
                print(f"{'First' if x==0 else 'Second' if x==1 else 'Third' if x==2 else 'Fourth'} Pair - {' '.join(list(map(lambda x: str(x), self.pair[x])))}")
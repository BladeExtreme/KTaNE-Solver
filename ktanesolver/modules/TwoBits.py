from .__basemod__ import BaseSolver

class TwoBits(BaseSolver):
    NAME = 'Two Bits'
    querybank = [
        ['kb','dk','gv','tk','pv','kp','bv','vt','pz','dt'],
        ['ee','zk','ke','ck','zp','pp','tp','tg','pd','pt'],
        ['tz','eb','ec','cc','cz','zv','cv','gc','bt','gt'],
        ['bz','pk','kz','kg','vd','ce','vb','kd','gg','dg'],
        ['pb','vv','ge','kv','dz','pe','db','cd','td','cb'],
        ['gb','tv','kk','bg','bp','vp','ep','tt','ed','zg'],
        ['de','dd','ev','te','zd','bb','pc','bd','kc','zb'],
        ['eg','bc','tc','ze','zc','gp','et','vc','tb','vz'],
        ['ez','ek','dv','cg','ve','dp','bk','pg','gk','gz'],
        ['kt','ct','zz','vg','gd','cp','be','zt','vk','dc']
      ]

    def __init__(self, edgework):
        self.stage = 0; self.query_list = []
        self.eg = edgework
        self.display()
        self.solve()
        input()

    def _calculate(self):
        n = ord(self.eg.snletter[0]) - ord('A') + 1 if len(self.eg.snletter) > 0 else 0
        n += int(self.eg.sndigit[-1])*self.eg.batt
        if 'STEREO RCA' in self.eg.uniqueports and 'RJ-45' not in self.eg.uniqueports: n*=2
        n = str(n%100) if n>99 else '0'+str(n) if n<10 else str(n)
        
        return int(n[0]), int(n[1])

    def display(self):
        r,c = self._calculate()

        self.local_header()
        print(f"{self.answer_pretext}Query: {self.querybank[r][c]}")
        respond = [self.querybank[r][c]]
        self.stage += 1
        input()

        while 1:
            self.local_header()
            print(f"Response List:")
            for a in respond:
                print(f" - {a}")
            print()
            ans = input(f"Response Code: ").lower()

            if not ans.isdigit(): continue
            elif int(ans) not in range(100): continue
            else:
                if self.stage<3:
                    print(f"{self.answer_pretext}Query: {self.querybank[int(ans[0])][int(ans[1])]}")
                    respond.append(self.querybank[int(ans[0])][int(ans[1])])
                    input()
                    self.stage+=1
                else:
                    print(f"{self.answer_pretext}Submit: {self.querybank[int(ans[0])][int(ans[1])]}")
                    break
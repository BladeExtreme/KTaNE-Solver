from .__basemod__ import BaseSolver

class Plumbing(BaseSolver):
    NAME = 'Plumbing'

    def _calculate(self):
        flatports = [a for b in self.eg.ports for a in b]
        inputred = (1 if '1' in self.eg.sndigit else 0)+(1 if 'RJ-45' in self.eg.uniqueports else 0)+(-1 if any(flatports.count(a)>=2 for a in self.eg.uniqueports) else 0)+(-1 if len(set(self.eg.sn))!=len(self.eg.sn) else 0)
        inputyellow = (1 if '2' in self.eg.sndigit else 0)+(1 if flatports.count('STEREO RCA')>=1 else 0)+(-1 if any(flatports.count(a)==1 for a in self.eg.uniqueports) else 0)+(-1 if any(a in self.eg.snletter for a in '1L') else 0)
        inputgreen = (1 if len(self.eg.sndigit)>=3 else 0)+(1 if self.eg.batt==1 else 0)+(-1 if not inputred else 0)+(-1 if not inputyellow else 0)
        inputblue = (99 if all(a<0 for a in [inputred, inputyellow, inputgreen]) else 0)+(1 if len(self.eg.uniqueports)>=4 else 0)+(1 if self.eg.batt>=4 else 0)+(-1 if len(flatports)==0 else 0)+(-1 if self.eg.batt==0 else 0)
        inputs = [inputred, inputyellow, inputgreen, inputblue]; inputs = list(map(lambda x: x>=1, inputs))

        outputred = (1 if flatports.count('SERIAL')>=1 else 0)+(1 if self.eg.batt==1 else 0)+(-1 if len(self.eg.sndigit)>2 else 0)+(-1 if len([a for a in [inputred, inputblue, inputgreen, inputyellow] if a>0])>2 else 0)
        outputyellow = (1 if any(flatports.count(a)>=2 for a in self.eg.uniqueports) else 0)+(1 if any(a in '48' for a in self.eg.sndigit) else 0)+(-1 if '2' not in self.eg.sndigit else 0)+(-1 if inputgreen else 0)
        outputgreen = (1 if len([a for a in [inputred, inputblue, inputgreen, inputyellow] if a>0])==3 else 0)+(1 if len(flatports)==3 else 0)+(-1 if len(flatports)<3 else 0)+(-1 if len(self.eg.sndigit)<3 else 0)
        outputblue = (99 if all(a<0 for a in [outputred, outputgreen, outputyellow]) else 0)+(1 if all(inputs) else 0)+(1 if any(a<0 for a in [outputred, outputgreen, outputyellow]) else 0)+(1 if self.eg.batt<2 else 0)+(1 if 'PARALLEL' not in self.eg.uniqueports else 0)
        outputs = [outputred, outputyellow, outputgreen, outputblue]; outputs = list(map(lambda x: x>=1, outputs))

        return inputs, outputs

    def solve(self):
        sol = self._calculate()
        self.local_header()
        colors = ['Red', 'Yellow', 'Green', 'Blue']
        print(f"{self.answer_pretext}Pipes:\n * Input: {', '.join(colors[a] for a in range(len(sol[0])) if sol[0][a])}\n * Output: {', '.join(colors[a] for a in range(len(sol[1])) if sol[1][a])}")
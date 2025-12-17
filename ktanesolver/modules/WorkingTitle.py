from .__basemod__ import BaseSolver

class WorkingTitle(BaseSolver):
    NAME = 'Working Title'
    bank = {
        'foo': 'A', 'foobar': 'A', 'quuz': 'A', 'garply': 'A', 'plugh': 'A','wibble': 'A', 'flob': 'A', 'fuga': 'A', 'toto': 'A', 'tutu': 'A','eggs': 'A', 'alice': 'A', 'lorem ipsum': 'A', 'widget': 'A', 'eek': 'A','bat': 'A', 'haystack': 'A', 'blarg': 'A', 'kalaa': 'A', 'sub': 'A','momo': 'A', 'change this': 'A', 'hi': 'A', 'thing': 'A', 'xyz': 'A','bar': 'B', 'qux': 'B', 'corge': 'B', 'waldo': 'B', 'xyzzy': 'B', 'wobble': 'B', 'hoge': 'B', 'hogera': 'B', 'tata': 'B', 'spam': 'B', 'raboof': 'B', 'bob': 'B', 'do stuff': 'B', 'bla': 'B', 'moof': 'B', 'shme': 'B', 'beekeeper': 'B', 'dothestuff': 'B', 'mum': 'B', 'temp': 'B', 'var': 'B', 'placeholder': 'B', 'hello': 'B', 'stuff': 'B', 'text': 'B', 'baz': 'C', 'quux': 'C', 'grault': 'C', 'fred': 'C', 'thud': 'C', 'wubble': 'C', 'piyo': 'C', 'hogehoge': 'C', 'titi': 'C', 'ham': 'C', 'fruit': 'C', 'john doe': 'C', 'data': 'C', 'gadget': 'C', 'gleep': 'C', 'needle': 'C', 'blah': 'C', 'grault': 'C', 'puppu': 'C', 'test': 'C', 'change': 'C', 'null': 'C', 'hey': 'C', 'something': 'C', 'abc': 'C'
    }

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Word: ").lower()
            
            if ans not in self.bank.keys(): continue
            else:
                self.word = ans
                break
    
    def _calculate(self):
        return self.bank[self.word]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Word: {self.word}")
        print(f"{self.answer_pretext}{sol}")
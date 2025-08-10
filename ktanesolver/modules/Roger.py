from .__basemod__ import BaseSolver

class Roger(BaseSolver):
    NAME = 'Roger'

    def display(self):
        while 1:
            self.local_header()
            ans = input(f"Manual's Code: ").lower()

            if not ans.isdigit(): continue
            elif len(ans)!=4: continue
            else:
                self.code = ans
                break
    
    def _calculate(self):
        # Pad with Zero
        message = 'Roger '+self.code
        message = [bin(ord(a))[2:].zfill(8) for a in message]
        original = len(''.join(message))
        message += ['1']
        message += ['0' for a in range(448-len(''.join(message)))]
        message += [bin(original)[2:].zfill(64)]
        message = ''.join(message)

        # Constant & Functions Definitions
        H0 = int('9559b62d', 16)
        H1 = int('71884793', 16)
        H2 = int('1bb72471', 16)
        H3 = int('deadbeef', 16)
        H4 = int('f1ea5eed', 16)
        A,B,C,D,E = ['0'*8 for a in range(5)]

        A = H0; B = H1; C = H2; D = H3; E = H4

        def K(t) -> int:
            if t in range(20):
                return int('00196883', 16)
            elif t in range(20, 40):
                return int('01200145', 16)
            elif t in range(40, 60):
                return int('009080a2', 16)
            elif t in range(60, 80):
                return int('383f8128', 16)


        def f(t,b,c,d) -> int:
            if t in range(20):
                return (b & c) | (~b & d)
            elif t in range(20, 40) or t in range(60, 80):
                return b ^ c ^ d
            elif t in range(40, 60):
                return (b & c) | (b & d) | (c & d)

        def S(X,n) -> int:
            return ((X << n) | (X >> 32-n)) & int('ffffffff', 16)

        # Construct Word for W[0] - W[79]
        W = []
        for a in range(0, len(message), 32):
            W.append(int(message[a:a+32], 2))

        for t in range(16, 80):
            W.append(S(W[t-3] ^ W[t-8] ^ W[t-14] ^ W[t-16], 1))

        # Hashing
        for t in range(80):
            TEMP = (S(A, 5) + f(t, B, C, D) + E + W[t] + K(t)) & int('ffffffff', 16)
            E = D; D = C; C = S(B, 30); B = A; A = TEMP

        H0 = (H0 + A) & int('ffffffff', 16)
        H1 = (H1 + B) & int('ffffffff', 16)
        H2 = (H2 + C) & int('ffffffff', 16)
        H3 = (H3 + D) & int('ffffffff', 16)
        H4 = (H4 + E) & int('ffffffff', 16)

        # Post-Processing
        decoded = ''.join(hex(a)[2:].zfill(8) for a in [H0, H1, H2, H3, H4])
        decoded = ''.join([a for a in decoded if a.isdigit()])

        return decoded[:4]

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"{self.answer_pretext}Query: {sol}")
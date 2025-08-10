from .__basemod__ import BaseSolver
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
import colorama as c

class CruelPianoKeys(BaseSolver):
    NAME = c.Fore.RED+'Cruel '+c.Style.RESET_ALL+'Piano Keys'
    music_list = [
        'flat', 'common time', 'sharp', 'natural', 'fermata', 
        'cut time', 'turn', 'clef', 'mordent', '16th rest', 
        'breve', 'double sharp', 'down bow', 'quarter rest', 'turn'
    ]

    def display(self):
        rcParams['toolbar'] = 'none'

        if not hasattr(self, 'loaded_images'):
            self.loaded_images = {}
            for name in self.music_list:
                key = name.lower().replace(' ', '_')
                path = f"ktanesolver/resources/PianoKeys/{key}.png"
                self.loaded_images[key] = mpimg.imread(path)

        while True:
            images = list(map(lambda x: x.lower().replace(' ', '_'), self.music_list))
            fig, axs = plt.subplots(4, 4, figsize=(6, 6))
            axs = axs.flatten()

            for i, key in enumerate(images):
                ax = axs[i]
                img = self.loaded_images[key]
                ax.imshow(img)
                ax.set_title(self.music_list[i].capitalize(), fontsize=8)
                ax.axis('off')
                ax.set_navigate(False)

            for j in range(i + 1, len(axs)):
                axs[j].axis('off')

            self.local_header()
            plt.tight_layout()
            plt.show(block=False)

            ans = input("Symbols (Separate with comma space): ").lower().split(', ')
            music_lookup = list(map(lambda x: x.lower(), self.music_list))

            if len(ans) != 3:
                plt.close(fig)
                continue
            elif not all(a in music_lookup for a in ans):
                plt.close(fig)
                continue
            else:
                self.symbols = ans
                plt.close(fig)
                break
    
    def inverse(self, tone:list[str]):
        sequence = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        
        for a in range(1, len(tone)+1):
            tone[a] = sequence[(sequence.index(tone[a-1])+(-1*(sequence.index(tone[a])-sequence.index(tone[a-1]))))%12]
        return tone

    def retrogade(self, tone:list[str]):
        return list(reversed(tone))

    def transpose(self, tone:list[str], x:int):
        sequence = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        x = x%12

        for a in range(len(tone)):
            tone[a] = sequence[(sequence.index(tone[a])+x)%12]
        return tone


    def _calculate(self):
        tone_seq = [
            ['F','D','F#','G#','C','B','A#','C#','G','E','D#','A'],
            ['A#','A','C','E','C#','D','D#','G','B','F#','G#','F'],
            ['F#','B','A','G#','D','C','G','C#','F','D#','E','A#'],
            ['E','D#','D','F#','F','A#','G#','C#','C','B','G','A'],
            ['D','E','A','A#','C','B','C#','G#','F','F#','D#','G'],
            ['C','D#','F#','D','F','C#','B','A','G','A#','E','G#'],
            ['G#','C','A#','C#','E','G','B','D#','A','D','F','F#'],
            ['E','A','C#','B','G','G#','A#','D#','F#','F','C','D'],
            ['G#','D#','D','E','A#','C#','F#','G','F','A','C','B'],
            ['D#','G#','C','B','D','C#','F#','A#','F','G','A','E']
        ]
        if all(a in self.symbols for a in ['breve', 'turn']) and len(self.eg.ind)>=2:
            lookup = tone_seq[int(self.eg.sndigit[0])]
            return self.retrogade(self.inverse(lookup))
        elif any(a in self.symbols for a in ['sharp', 'double sharp']) and [] in self.eg.ports:
            lookup = tone_seq[self.eg.hold%10]
            while 1:
                self.local_header()
                ans = input(f"Minutes Left: ").lower()

                if not ans.isdigit(): continue
                elif int(ans) < 0: continue
                else:
                    x = int(ans)
                    break
            return self.transpose(lookup, x)
        elif any(a in self.symbols for a in ['fermata', 'down bow']) and any([a for b in self.eg.ports for a in b].count(z)>=2 for z in self.eg.uniqueports):
            lookup = tone_seq[self.eg.solves%10]
            return self.inverse(lookup)
        elif all(a in self.symbols for a in ['clef', '16th rest']) and len(self.eg.ports)>=2:
            lookup = tone_seq[(9-len(self.eg.unlitind))%10]
            return self.retrogade(lookup)
        elif any(a in self.symbols for a in ['cut time', 'common time']) and len(a for a in self.eg.snletter if a in 'AIUEO')>=1:
            lookup = tone_seq[self.eg.strikes%10]
            return self.transpose(self.retrogade(lookup), 3)
        elif any(a in self.symbols for a in ['natural', 'mordent']) and self.eg.batt%2==0: 
            if 'DVI-D' in self.eg.uniqueports: lookup = tone_seq[7]
            else: lookup = tone_seq[3]
            return self.transpose(lookup, len(a for b in self.eg.ports for a in b))
        elif any(a in self.symbols for a in ['flat','quarter rest']) and any(True for a in self.eg.ind if not any(b in 'AIUEO' for b in a)):
            lookup = tone_seq[8]
            return self.inverse(lookup)
        elif any(a in self.symbols for a in ['down bow', '16th rest']) and len(a for b in self.eg.ports for a in b)<2:
            lookup = tone_seq[4]
            return self.retrogade(lookup)
        elif any(a in self.symbols for a in ['double sharp', 'breve']):
            lookup = tone_seq[5]
            return lookup

        if 'flat' in self.symbols and int(self.eg.sndigit[-1])%2 == 0: return ['A#','A#','A#','A#','F#','G#','A#','G#','A#']
        elif ('common time' in self.symbols or 'sharp' in self.symbols) and self.eg.hold >= 2: return ['D#','D#','D','D','D#','D#','D','D#','D#','D','D','D#']
        elif ('natural' in self.symbols and 'fermata' in self.symbols): return ['E','F#','F#','F#','F#','E','E','E']
        elif ('cut time' in self.symbols or 'turn' in self.symbols) and any('STEREO RCA' in a for a in self.eg.uniqueports): return ['A#','A','A#','F','D#','A#','A','A#','F','D#']
        elif ('clef' in self.symbols) and any('SND*'in a for a in self.eg.litind): return ['E','E','E','C','E','G','G']
        elif ('mordent' in self.symbols or 'fermata' in self.symbols or 'common time' in self.symbols) and self.eg.batt >= 3: return ['C#','D','E','F','C#','D','E','F','A#','A']
        elif ('flat' in self.symbols and 'sharp' in self.symbols): return ['G','G','C','G','G','C','G','C']
        elif ('cut time' in self.symbols or 'mordent' in self.symbols) and any(numb in self.eg.sndigit for numb in ['3', '7', '8']): return ['A','E','F','G','F','E','D','D','F','A']
        elif ('flat' in self.symbols or 'turn' in self.symbols or 'clef' in self.symbols): return ['G','G','G','D#','A#','G','D#','A#','G']
        else: return ['B','D','A','G','A','B','D','A']

    def solve(self):
        sol = self._calculate()
        print(f"Symbols: {', '.join([a.capitalize() for a in self.symbols])}")
        print(f"{self.answer_pretext}Music: {', '.join(sol)}")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams
from .__basemod__ import BaseSolver

class PianoKeys(BaseSolver):
    NAME = 'Piano Keys'
    music_list = [
        'flat', 'common time', 'sharp', 'natural', 'fermata',
        'cut time', 'turn', 'clef', 'mordent'
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
            images = [name.lower().replace(' ', '_') for name in self.music_list]
            fig, axs = plt.subplots(5, 5, figsize=(6, 6))
            axs = axs.flatten()

            for i, key in enumerate(images):
                ax = axs[i]
                img = self.loaded_images[key]
                ax.imshow(img)
                ax.set_title(f"{self.music_list[i].capitalize()}", fontsize=8)
                ax.axis('off')
                ax.set_navigate(False)

            for j in range(i + 1, len(axs)):
                axs[j].axis('off')

            self.local_header()
            plt.tight_layout()
            plt.show(block=False)

            ans = input("Symbols (separate with comma space): ").lower().split(', ')
            music_lookup = [name.lower() for name in self.music_list]

            if len(ans) != 3:
                plt.close(fig)
                continue
            elif not all(a in music_lookup for a in ans):
                plt.close(fig)
                continue
            elif len(set(ans)) != 3:
                plt.close(fig)
                continue
            else:
                self.symbols = ans
                plt.close(fig)
                break
    
    def _calculate(self):
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
        
        self.local_header()
        print(f"Symbols: {', '.join([a.capitalize() for a in self.symbols])}")
        print(f"{self.answer_pretext}Music: {', '.join(sol)}")
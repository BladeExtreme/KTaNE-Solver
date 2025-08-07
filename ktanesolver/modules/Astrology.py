from .__basemod__ import BaseSolver
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams

class Astrology(BaseSolver):
    NAME = 'Astrology'
    table = [
        [
            [0, 0, 1, -1, 0, 1, -2, 2, 0, -1],
            [-2, 0, -1, 0, 2, 0, -2, 2, 0, 1],
            [-1, -1, 0, -1, 1, 2, 0, 2, 1, -2],
            [-1, 2, -1, 0, -2, -1, 0, 2, -2, 2]
        ],[
            [1, 0, -1, 0, 0, 2, 2, 0, 1, 0, 1, 0],
            [2, 2, -1, 2, -1, -1, -2, 1, 2, 0, 0, 2],
            [-2, -1, 0, 0, 1, 0, 1, 2, -1, -2, 1, 1],
            [1, 1, -2, -2, 2, 0, -1, 1, 0, 0, -1, -1]
        ],[
            [-1, -1, 2, 0, -1, 0, -1, 1, 0, 0, -2, -2],
            [-2, 0, 1, 0, 2, 0, -1, 1, 2, 0, 1, 0],
            [-2, -2, -1, -1, 1, -1, 0, -2, 0, 0, -1, 1],
            [-2, 2, -2, 0, 0, 1, -1, 0, 2, -2, -1, 1],
            [-2, 0, -1, -2, -2, -2, -1, 1, 1, 1, 0, -1],
            [-1, -2, 1, -1, 0, 0, 0, 1, 0, -1, 2, 0],
            [-1, -1, 0, 0, 1, 1, 0, 0, 0, 0, -1, -1],
            [-1, 2, 0, 0, 1, -2, 1, 0, 2, -1, 1, 0],
            [1, 0, 2, 1, -1, 1, 1, 1, 0, -2, 2, 0],
            [-1, 0, 0, -1, -2, 1, 2, 1, 1, 0, 0, -1]
      ]
    ]
    elements_list = ['Fire', 'Water', 'Earth', 'Air']
    planets_list = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    zodiacs_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']

    def display(self):
        rcParams['toolbar'] = 'none'

        while 1:
            images = ['e_fire.png', 'e_water.png', 'e_earth.png', 'e_air.png']

            fig = plt.figure(figsize=(4, 4))

            for i, img_path in enumerate(images):
                img = mpimg.imread(f"ktanesolver/resources/Astrology/{img_path}")
                ax = fig.add_subplot(2, 2, i + 1)
                ax.imshow(img)
                ax.set_title(self.elements_list[i])
                ax.set_xticks([])
                ax.set_yticks([])
                ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
                ax.set_navigate(False)

            self.local_header()
            plt.tight_layout()
            plt.show(block=False)
            ans = input("Element [Fire, Water, Earth, Air]: ").lower()
            if ans not in list(map(lambda x: x.lower(), self.elements_list)):
                plt.close(fig)
                continue
            else:
                self.elem = list(map(lambda x: x.lower(), self.elements_list)).index(ans)
                plt.close(fig)
                break
        
        while 1:
            images = ['p_sun.png', 'p_moon.png', 'p_mercury.png', 'p_venus.png', 'p_mars.png', 'p_jupiter.png', 'p_saturn.png', 'p_uranus.png', 'p_neptune.png', 'p_pluto.png']

            fig = plt.figure(figsize=(4, 6))

            for i in range(9):
                img = mpimg.imread(f"ktanesolver/resources/Astrology/{images[i]}")
                ax = fig.add_subplot(4, 3, i + 1)
                ax.imshow(img)
                ax.set_title(self.planets_list[i])
                ax.set_xticks([])
                ax.set_yticks([])
                ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
                ax.set_navigate(False)

            img = mpimg.imread(f"ktanesolver/resources/Astrology/{images[9]}")
            ax = fig.add_subplot(4, 3, 11)
            ax.imshow(img)
            ax.set_title(self.planets_list[9], fontsize=8)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
            ax.set_navigate(False)

            fig.add_subplot(4, 3, 10).axis('off')
            fig.add_subplot(4, 3, 12).axis('off')

            self.local_header()
            print(f"Element: {self.elements_list[self.elem]}")
            plt.tight_layout()
            plt.show(block=False)
            ans = input("Planet [Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto]: ").lower()
            planet_names_lower = list(map(lambda x: x.lower(), self.planets_list))
            if ans not in planet_names_lower:
                plt.close(fig)
                continue
            else:
                self.planet = planet_names_lower.index(ans)
                plt.close(fig)
                break
        
        while 1:
            images = ['a_aries.png', 'a_taurus.png', 'a_gemini.png', 'a_cancer.png', 'a_leo.png', 'a_virgo.png', 'a_libra.png', 'a_scorpio.png', 'a_sagittarius.png', 'a_capricorn.png', 'a_aquarius.png', 'a_pisces.png']

            fig = plt.figure(figsize=(6, 6))

            for i in range(12):
                img = mpimg.imread(f"ktanesolver/resources/Astrology/{images[i]}")
                ax = fig.add_subplot(3, 4, i + 1)
                ax.imshow(img)
                ax.set_title(self.zodiacs_list[i], fontsize=9)
                ax.set_xticks([])
                ax.set_yticks([])
                ax.grid(True, color='gray', linestyle='--', linewidth=0.5)
                ax.set_navigate(False)

            self.local_header()
            print(f"Element: {self.elements_list[self.elem]}")
            print(f"Planet: {self.planets_list[self.planet]}")

            plt.tight_layout()
            plt.show(block=False)

            ans = input("Zodiac [Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces]: ").lower()
            zodiac_names_lower = list(map(str.lower, self.zodiacs_list))
            if ans not in zodiac_names_lower:
                plt.close(fig)
                continue
            else:
                self.zodiac = zodiac_names_lower.index(ans)
                plt.close(fig)
                break
    
    def _calculate(self):
        scores = 0

        scores += self.table[0][self.elem][self.planet]
        scores += self.table[1][self.elem][self.zodiac]
        scores += self.table[2][self.planet][self.zodiac]

        if any([a in self.elements_list[self.elem].upper() for a in self.eg.snletter]): scores+=1
        else: scores-=1

        if any([a in self.planets_list[self.planet].upper() for a in self.eg.snletter]): scoers+=1
        else: scores-=1

        if any([a in self.zodiacs_list[self.zodiac].upper() for a in self.eg.snletter]): scores+=1
        else: scores-=1
        return ('Good' if scores>0 else 'Bad' if scores<0 else 'No')+f' Omen in {str(abs(scores))}'

    def solve(self):
        sol = self._calculate()
        self.local_header()
        print(f"Element: {self.elements_list[self.elem]}")
        print(f"Planet: {self.planets_list[self.planet]}")
        print(f"Zodiac: {self.zodiacs_list[self.zodiac]}")
        print(f"{self.answer_pretext}{sol}")
        pass
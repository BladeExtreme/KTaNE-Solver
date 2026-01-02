from ..tools.image import img_close, img_open, img_initialize
from .__basemod__ import BaseSolver
import math

class Constellations(BaseSolver):
    NAME = 'Constellations'
    constellations_names = [
        ['Canis Minor'],
        ['Coma Berenices','Equuleus','Pictor','Pyxis','Triangulum'],
        ['Antlia','Apus', 'Aries', 'Caelum','Crux', 'Fornax', 'Mensa', 'Norma','Scutum', 'Sextans', 'Triangulum Australe'],
        ['Cancer', 'Canes Venatici', 'Cassiopeia', 'Circinus', 'Corvus', 'Delphinus', 'Indus', 'Leo Minor', 'Microscopium', 'Octans', 'Sagitta'],
        ['Chamaeleon', 'Columba', 'Corona Australis', 'Dorado', 'Hydrus', 'Lyra', 'Musca', 'Reticulum', 'Telescopium', 'Tucana', 'Volans'],
        ['Auriga', 'Cepheus', 'Corona Borealis', 'Horologium', 'Monoceros', 'Piscis Austrinus', 'Ursa Minor', 'Vulpecula'],
        ['Ara', 'Camelopardalis', 'Crater', 'Lynx', 'Sculptor', 'Vela'],
        ['Aquila', 'Cygnus', 'Lacerta', 'Leo', 'Libra', 'Lupus', 'Puppis'],
        ['Capricornus', 'Grus'],
        ['Bootes', 'Carina', 'Lepus', 'Pavo'],
        ['Canis Major', 'Sagittarius'],
        ['Aquarius', 'Draco', 'Phoenix', 'Serpens'],
        ['Cetus', 'Taurus', 'Virgo'],
        ['Orion', 'Pegasus'],
        ['Andromeda'],
        ['Perseus', 'Scorpius'],
        ['Gemini'],
        ['Hercules', 'Pisces', 'Ursa Major'],
        ['Centaurus', 'Hydra'],
        ['Ophiuchus'],
        ['Eridanus']
    ]
    constellations_starcount = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,31]
    sky_quadrants = [
        ['Andromeda', 'Aries', 'Cassiopeia', 'Orion', 'Perseus', 'Pisces', 'Taurus', 'Triangulum'],
        ['Auriga', 'Camelopardalis', 'Cancer', 'Canis Minor', 'Gemini', 'Leo', 'Leo Minor', 'Lynx', 'Monoceros', 'Ursa Major'],
        ['Bootes', 'Canes Venatici', 'Coma Berenices', 'Corona Borealis', 'Draco', 'Hercules', 'Serpens', 'Ursa Minor'],
        ['Aquila', 'Cepheus', 'Cygnus', 'Delphinus', 'Equuleus', 'Lacerta', 'Lyra', 'Pegasus', 'Sagitta', 'Vulpecula'],

        ['Caelum', 'Cetus', 'Columba', 'Dorado', 'Eridanus', 'Fornax', 'Horologium', 'Hydrus', 'Lepus', 'Mensa', 'Phoenix', 'Pictor', 'Reticulum', 'Sculptor'],
        ['Antlia', 'Canis Major', 'Carina', 'Chamaeleon', 'Crater', 'Hydra', 'Puppis', 'Pyxis', 'Sextans', 'Vela', 'Volans'],
        ['Apus', 'Ara', 'Centaurus', 'Circinus', 'Corvus', 'Crux', 'Libra', 'Lupus', 'Musca', 'Norma', 'Ophiuchus', 'Scorpius', 'Triangulum Australe', 'Virgo'],
        ['Aquarius', 'Capricornus', 'Corona Australis', 'Grus', 'Indus', 'Microscopium', 'Octans', 'Pavo', 'Piscis Austrinus', 'Sagittarius', 'Scutum', 'Telescopium', 'Tucana']
    ]

    def factor_grid(self, n: int) -> tuple[int, int]:
        """
        Returns (rows, cols) such that:
        - rows * cols >= n
        - grid is as close to square as possible
        """
        root = int(math.sqrt(n))
        for r in range(root, 0, -1):
            if n % r == 0:
                return r, n // r
        return 1, n

    def display(self):      
        while True:
            self.local_header()
            ans = input(f"How many stars in the constellation: ")

            if not ans.isdigit(): continue
            elif int(ans) not in self.constellations_starcount: continue
            else:
                self.star_count = int(ans)
                break
        
        if len(self.constellations_names[self.star_count])==1:
            self.constellation = self.constellations_names[self.star_count][0]
        else:
            while True:
                self.local_header()
                rows, cols = self.factor_grid(len(self.constellations_names[self.constellations_starcount.index(self.star_count)]))
                img_initialize(self.NAME, self.constellations_names[self.constellations_starcount.index(self.star_count)], rows, cols)
                img_open()
                print(f"STAR COUNT: {self.star_count}")
                print(f"List of Constellations:")
                for a in range(len(self.constellations_names[self.constellations_starcount.index(self.star_count)])):
                    print(f"{a+1}. {self.constellations_names[self.constellations_starcount.index(self.star_count)][a]}")
                ans = input(f"\nConstellation Number: ")

                if not ans.isdigit():
                    img_close()
                    continue
                elif int(ans)-1 not in range(len(self.constellations_names[self.constellations_starcount.index(self.star_count)])):
                    img_close()
                    continue
                else:
                    self.constellation = self.constellations_names[self.constellations_starcount.index(self.star_count)][int(ans)-1]
                    img_close()
                    break

    def _calculate(self):
        sky = [a for a in self.sky_quadrants if self.constellation in a][0]
        rows, cols = [[3,3],[4,3],[3,3],[4,3],[4,4],[4,3],[4,4],[4,4]][self.sky_quadrants.index(sky)]
        while True:
            img_initialize(self.NAME, sky, rows, cols, 'ktanesolver/resources/Constellations/symbols')
            img_open()
            self.local_header()
            print(f"List of Constellations that is in one sky with {self.constellation}: ")
            for a in range(len(sky)):
                print(f"{a+1}. {sky[a]}")
            ans = input(f"\nConstellation Numbers: ").lower()

            if not ans.isdigit():
                img_close()
                continue
            elif int(ans)-1 not in range(len(sky)):
                img_close()
                continue
            else:
                img_close()
                return sky[int(ans)-1]

    def solve(self):
        sol = self._calculate()
        print(f"{self.answer_pretext}Module has been solved with {sol} as the answer.")
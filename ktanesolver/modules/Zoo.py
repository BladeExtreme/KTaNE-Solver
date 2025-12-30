from .__basemod__ import BaseSolver

class Zoo(BaseSolver):
    NAME = 'Zoo'
    startinglist = {
        'gazelle': ['bear','v'],
        'caracal': ['spider','v'],
        'cheetah': ['pig','v'],
        'ocelot': ['cat','v'],
        'sheep': ['cow','v'],
        'caterpillar': ['tyrannosaurus rex','v'],
        'groundhog': ['rabbit','v'],
        'armadillo': ['horse','v'],
        'orca': ['flamingo','v'],
        'plesiosaur': ['flamingo','d'],
        'penguin': ['hyena','d'],
        'baboon': ['dimetrodon','d'],
        'whale': ['dromedary','d'],
        'squid': ['warthog','d'],
        'coyote': ['swallow','d'],
        'ram': ['starfish','d'],
        'deer': ['gorilla','d'],
        'crocodile': ['salamander','d']
    }
    board = [
        ['','','','','cow','','','',''],
        ['','','','cat','','tyrannosaurus rex','','',''],
        ['','','pig','','bat','','rabbit','',''],
        ['','spider','','owl','','ant','','horse',''],
        ['bear','','goose','','rhinoceros','','fly','','flamingo'],
        ['','dragonfly','','snail','','tortoise','','llama',''],
        ['ferret','','butterfly','','monkey','','sea horse','','hyena'],
        ['','lion','','fox','','wolf','','camel',''],
        ['stegosaurus','','squirrel','','dolphin','','kangaroo','','dimetrodon'],
        ['','pterodactyl','','giraffle','','eagle','','lobster',''],
        ['elephant','','cobra','','koala','','porcupine','','dromedary'],
        ['','rooster','','hippopotamus','','crab','','otter',''],
        ['mouse','','woodpecker','','triceratops','','frog','','warthog'],
        ['','seal','','apatosaurus','','duck','','swallow',''],
        ['','','skunk','','beaver','','starfish','',''],
        ['','','','viper','','gorilla','','',''],
        ['','','','','salamander','','','','']
    ]

    def display(self):
        while 1:
            self.local_header()
            total = list(self.startinglist.keys())
            for y in range(7):
                for x in range(5):
                    try:
                        text = f"{str((y+1)+(x*7)).zfill(2)}. {total[(y+1)+(x*7)].capitalize()}"
                        print(text, end=" "*(23-len(text)))
                    except: pass
                print()
            print()
            ans = input("Animals in Crate (numbers obtained from list above, seperate with comma space): ").lower().split(', ')

            if len(ans)!=2: continue
            elif not all(a.isdigit() for a in ans): continue
            elif ans[0]==ans[1]: continue
            elif self.startinglist[total[int(ans[0])]][1]==self.startinglist[total[int(ans[1])]][1]: continue

            conv = [int(a) for a in ans]
            if conv[0]<=4 and conv[1]<13-conv[0]: continue
            elif not all(int(a) in range(1,len(total)) for a in ans): continue
            else:
                self.animals = [total[int(a)] for a in ans]
                break
    
    def _calculate(self):
        starting_animals = {a:self.startinglist.get(a)[0] for a in self.animals}
        directions = {a:self.startinglist.get(a)[1] for a in self.animals}
        xy = {a:[] for a in self.animals}

        for a in starting_animals:
            for x in self.board:
                if starting_animals[a] in x:
                    xy[a] = ([self.board.index(x), x.index(starting_animals[a])])
                    break
        
        for a in self.animals:
            if directions[a] == 'v':
                starting_animals[a] = [self.board[b][xy[a][1]] for b in range(len(self.board)) if self.board[b][xy[a][1]]!='']
            elif directions[a] == 'd':
                temp = []
                for b in range(len(self.board)):
                    if self.board[xy[a][0]-b][xy[a][1]-b]!='': temp.append(self.board[xy[a][0]-b][xy[a][1]-b])
                    else: break
                starting_animals[a] = temp

        midpoint_animal = list(set(starting_animals[self.animals[0]]).intersection(set(starting_animals[self.animals[1]])))[0]
        midpoint_coord = []
        midpoint_direction = ''

        for a in self.board:
            if midpoint_animal in a: midpoint_coord = [self.board.index(a), a.index(midpoint_animal)]
        
        score = [[x for y in self.eg.ports for x in y].count(a) for a in ['DVI-D','RCA','SERIAL','PS/2','RJ-45','PARALLEL']]
        dir_list = ['N','NE','SE','S','SW','NW']
        validity = ['' for a in dir_list]
        
        dir_list = [dir_list[a] for a in range(len(score)) if score[a]==max(score)]
        validity = [validity[a] for a in range(len(score)) if score[a]==max(score)]

        for a in range(len(dir_list)):
            if dir_list[a]=='N': validity[a] = 'v' if midpoint_coord[1]-8>=0 else 'd'
            elif dir_list[a]=='NE': validity[a] = 'v' if midpoint_coord[0]+8<len(self.board[0]) and midpoint_coord[1]-8>=0 else 'd'
            elif dir_list[a]=='NW': validity[a] = 'v' if midpoint_coord[0]-8>=0 and midpoint_coord[1]-8>=0 else 'd'
            elif dir_list[a]=='S': validity[a] = 'v' if midpoint_coord[1]+8<len(self.board) else 'd'
            elif dir_list[a]=='SE': validity[a] = 'v' if midpoint_coord[0]+8<len(self.board[0]) and midpoint_coord[1]+8<len(self.board) else 'd'
            elif dir_list[a]=='SW': validity[a] = 'v' if midpoint_coord[0]-8>=0 and midpoint_coord[1]+8<len(self.board) else 'd'
        
        dir_list2 = [dir_list[a] for a in range(len(validity)) if validity[a]=='v']
        validity2 = [validity[a] for a in range(len(validity)) if validity[a]=='v']

        if len([a for a in score if a!=max(score)])!=1:
            for a in range(len(dir_list)):
                x_dir = 0; y_dir = 0; special_direction = ''
                match dir_list[a]:
                    case 'N': y_dir = -16
                    case 'NE': y_dir = -8; x_dir = 8
                    case 'NW': y_dir = -8; x_dir = -8
                    case 'S': y_dir = 16
                    case 'SE': y_dir = 8; x_dir = 8
                    case 'SW': y_dir = 8; x_dir = -8
                if midpoint_coord[0]+y_dir not in range(0,len(self.board)) or midpoint_coord[1]+x_dir not in range(0,len(self.board[0])): continue
                elif self.board[midpoint_coord[0]+y_dir][midpoint_coord[1]+x_dir]=='': continue
                else:
                    special_direction = dir_list[a]
                    break
            x_dir = 0; y_dir = 0
            match special_direction:
                case 'N': y_dir = -2
                case 'NE': y_dir = -1; x_dir = 1
                case 'NW': y_dir = -1; x_dir = -1
                case 'S': y_dir = 2
                case 'SE': y_dir = 1; x_dir = 1
                case 'SW': y_dir = 1; x_dir = -1
            animals = [self.board[midpoint_coord[0]][midpoint_coord[1]]]
            for a in range(1,5):
                animals.append(self.board[midpoint_coord[0]+(2*a*y_dir)][midpoint_coord[1]+(2*a*x_dir)])
            return animals if len(set(animals))>1 else None
        else:
            x_dir = 0; y_dir = 0
            match dir_list2[0]:
                case 'N': y_dir = -2
                case 'NE': y_dir = -1; x_dir = 1
                case 'NW': y_dir = -1; x_dir = -1
                case 'S': y_dir = 2
                case 'SE': y_dir = 1; x_dir = 1
                case 'SW': y_dir = 1; x_dir = -1
            
            animals = [self.board[midpoint_coord[0]][midpoint_coord[1]]]
            for a in range(1,5):
                animals.append(self.board[midpoint_coord[0]+(a*y_dir)][midpoint_coord[1]+(a*x_dir)])
            return animals

    def solve(self):
        sol = None
        while sol is None:
            sol = self._calculate()
            self.local_header()
            print(f"{self.answer_pretext if sol is not None else self.fail_pretext}{(', '.join(a.capitalize() for a in sol)) if sol is not None else 'Failed to find answer, enter different Animals.'}")
            if sol is None:
                input()
                self.display()
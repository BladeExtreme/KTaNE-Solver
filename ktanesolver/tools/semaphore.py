semadict = {
    tuple(sorted({'S','SW'})): ['A','1'],
	tuple(sorted({'S','W'})): ['B', '2'],
	tuple(sorted({'S','NW'})): ['C', '3'],
	tuple(sorted({'S','N'})): ['D', '4'],
	tuple(sorted({'S','NE'})): ['E', '5'],
	tuple(sorted({'S','E'})): ['F', '6'], 
	tuple(sorted({'S','SE'})): ['G', '7'], 
	tuple(sorted({'SW','W'})): ['H', '8'],
	tuple(sorted({'SW','NW'})): ['I', '9'],
	tuple(sorted({'N','E'})): ['J', None],
	tuple(sorted({'SW','N'})): ['K', '0'],
	tuple(sorted({'SW','NE'})): ['L', None],
	tuple(sorted({'SW','E'})): ['M', None],
	tuple(sorted({'SW','SE'})): ['N', None],
	tuple(sorted({'W','NW'})): ['O', None],
	tuple(sorted({'W','N'})): ['P', None],
	tuple(sorted({'W','NE'})): ['Q', None],
	tuple(sorted({'W','E'})): ['R', None],
	tuple(sorted({'W','SE'})): ['S', None],
	tuple(sorted({'NW','N'})): ['T', None],
	tuple(sorted({'NW','NE'})): ['U', None],
	tuple(sorted({'N','SE'})): ['V', None],
	tuple(sorted({'NE','E'})): ['W', None],
	tuple(sorted({'NE','SE'})): ['X', None],
	tuple(sorted({'E','NW'})): ['Y', None],
	tuple(sorted({'E','SE'})): ['Z', None],
	tuple(sorted({'N','NE'})): [None, None]
}

def sematranslate(a, state):
    if state not in range(2): return -1
    return semadict[a][state]
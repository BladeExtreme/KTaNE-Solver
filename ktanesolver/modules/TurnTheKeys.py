from .__basemod__ import BaseSolver

class TurnTheKeys(BaseSolver):
    NAME = 'Turn The Keys'

    FORBIDDEN_MOD = {
        'left': [
            'maze',
            'memory',
            'complicatedwires',
            'wiresequence',
            'cryptography',
        ],
        'right': [
            'semaphore',
            'combinationlock',
            'simonsays',
            'astrology',
            'switches',
            'plumbing'
        ]
    }

    def __init__(self):
        self.left = False
        self.right = False
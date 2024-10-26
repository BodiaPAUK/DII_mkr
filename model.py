input_lvs = [
    {
        'X': (0, 300, 1),
        'name': 'Distance',
        'terms': {
            'short': ('trapmf', 0, 0, 30, 70),
            'average': ('trapmf', 50, 75, 120, 150),
            'long': ('trapmf', 100, 150, 300, 300),
        }
    },

    {
        'X': (-1, 1, 0.01),
        'name': 'State',
        'terms': {
            'approaches': ('trapmf', -1, -1, -0.15, -0.01),
            'stays in place': ('trimf', -0.1, 0, 0.1),
            'moves away': ('trapmf', 0.01, 0.15, 1, 1),
        }
    },
]

output_lv = {
    'X': (0, 20, 1),
    'name': 'Speed',
    'terms': {
        'stay still': ('trimf', 0, 0, 2),
        'slowly move away': ('trapmf', 1, 3, 7, 10),
        'quickly move away': ('trapmf', 9, 12, 20, 20),
    }
}


rule_base = [
    (('short', 'approaches'), 'quickly move away'),
    (('short', 'stays in place'), 'quickly move away'),
    (('short', 'moves away'), 'slowly move away'),
    (('average', 'approaches'), 'quickly move away'),
    (('average', 'stays in place'), 'slowly move away'),
    (('average', 'moves away'), 'stay still'),
    (('long', 'approaches'), 'slowly move away'),
    (('long', 'stays in place'), 'stay still'),
    (('long', 'moves away'), 'stay still'),
]
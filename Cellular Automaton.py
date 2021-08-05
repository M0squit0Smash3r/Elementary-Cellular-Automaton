from time import sleep


def get_rule(n: int) -> list:
    rule_core = str(bin(n))[2:]
    if len(rule_core) >= 8:
        return [int(i) for i in list(rule_core[len(rule_core)-8:])]
    rule = '0' * (8-len(rule_core)) + rule_core
    return [int(i) for i in list(rule)]


def get_neighbors() -> list:
    neighbors = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                neighbors.append([a, b, c])
    return neighbors[::-1]


def cellular_automaton(rule_n: int):
    size = (157, 40)
    slp_t = 0.1
    if 0 > rule_n > 255:
        return 'Please enter a valid rule number'
    rule = get_rule(rule_n)
    configs = get_neighbors()
    state = ['.', '#']
    base_gen = [0 if i != ((size[0] + 1) // 2) - 1 else 1 for i in range(size[0])]
    to_print = ''
    for i in range(size[0]):
        to_print += state[base_gen[i]]
    print(to_print)
    sleep(slp_t)
    while True:
        to_print = ''
        next_gen = []
        for i in range(size[0]):
            if i == 0:
                check = [base_gen[-1]] + base_gen[:2]
            elif i == size[0]-1:
                check = base_gen[size[0]-2:] + [base_gen[0]]
            else:
                check = base_gen[i-1:i+2]
            check = rule[configs.index(check)]
            to_print += state[check]
            next_gen.append(check)
        print(to_print)
        sleep(slp_t)
        base_gen = next_gen


cellular_automaton(169)
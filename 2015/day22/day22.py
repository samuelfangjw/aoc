import math

min_cost = math.inf
part2 = False

def simulate(state, turn):
    global min_cost, part2
    cost, hp, mana, ehp, shield, poison, recharge = state
    
    if cost > min_cost:
        return

    if shield > 0:
        armor = 7
    else:
        armor = 0

    if poison > 0:
        ehp -= 3

    if recharge > 0:
        mana += 101
    
    if turn == 'player' and part2:
        hp -= 1

    shield -= 1
    poison -= 1
    recharge -= 1

    if hp <= 0:
        return
    if ehp <= 0:
        min_cost = min(min_cost, cost)
        return

    if turn == 'player':
        if mana < 53:
            return
        simulate((cost+53, hp, mana-53, ehp-4, shield, poison, recharge), 'boss')
        if mana >= 73:
            simulate((cost+73, hp+2, mana-73, ehp-2, shield, poison, recharge), 'boss')
        if mana >= 113:
            simulate((cost+113, hp, mana-113, ehp, 6, poison, recharge), 'boss')
        if mana >= 173:
            simulate((cost+173, hp, mana-173, ehp, shield, 6, recharge), 'boss')
        if mana >= 229:
            simulate((cost+229, hp, mana-229, ehp, shield, poison, 5), 'boss')
    else: # Boss turn
        simulate((cost, hp-9+armor, mana, ehp, shield, poison, recharge), 'player')

simulate((0, 50, 500, 58, 0, 0, 0), 'player')
print(min_cost)

min_cost = math.inf
part2 = True
simulate((0, 50, 500, 58, 0, 0, 0), 'player')
print(min_cost)

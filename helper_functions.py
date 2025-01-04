def calculate_profit(units, multiplier, outcome):
    
    if outcome == 1 or outcome == 'Won':
        profit = units*multiplier - units
    else:
        profit = units*-1
    
    return profit
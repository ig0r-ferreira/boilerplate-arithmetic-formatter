def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    import re
    
    onlydigits = re.compile(r'^\d+$')
    lines = [[] for _ in range(3 + solve)]
    
    for problem in problems:
        number1, operator, number2 = re.match(r'(.*)\s(\W)\s(.*)', problem).groups()
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

        if not onlydigits.match(number1) or not onlydigits.match(number2):
            return 'Error: Numbers must only contain digits.'
        
        max_width = max(len(number1), len(number2))

        if max_width > 4:
            return 'Error: Numbers cannot be more than four digits.'

        max_width += 2
        
        lines[0] += [f'{number1:>{max_width}}']
        lines[1] += [f'{operator} {number2:>{max_width - 2}}']
        lines[2] += [('-' * max_width)]
        
        if solve:
            lines[3] += [f'{int(number1) + (int(number2) * (-1) ** (operator == "-")):>{max_width}}']

    return '\n'.join([(' ' * 4).join(line) for line in lines])
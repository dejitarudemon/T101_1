def parse_rules(rules) -> list:
    result = []
    for rule in rules:
        oper = ''.join(rule['if'].keys())
        result.append([oper, set(rule['if'][oper]), rule['then']])
    result.sort()
    return result


def check_validate_rules(rules: list) -> list:
    rules = parse_rules(rules)
    correct_rules = list()
    for i in range(len(rules) - 1):
        for j in range(i + 1, len(rules) - 1):
            if rules[i][1] == rules[j][1]:  # check "if and/or A then B -> if not A then B"
                if ('and' == rules[i][0] and 'not' == rules[j][0]) or ('and' == rules[j][0] and 'not' == rules[i][0]):
                    if rules[i][2] == rules[j][2]:
                        rules[j].clear()
                        rules[i].clear()
                if ('or' == rules[i][0] and 'not' == rules[j][0]) or (
                        'or' == rules[j][0] and 'not' == rules[i][0]):
                    if rules[i][2] == rules[j][2]:
                        rules[j].clear()
                        rules[i].clear()
            if 'not' == rules[i][0] == rules[i][1]:
                if rules[i][2] in rules[j][1]:
                    rules[i].clear()
                    rules[j].clear()

    for rule in rules:
        if rule:
            correct_rules.append(rule)
    return correct_rules


def check_facts(rules: list, facts: list) -> set:
    facts = set(facts)
    last_move = 0
    while True:
        result = set()
        for rule in rules:
            if rule[0] == 'or' and any([z in facts for z in rule[1]]):
                result.add(rule[2])
                rules.remove(rule)
                continue
            if rule[0] == 'and' and all([z in facts for z in rule[1]]):
                result.add(rule[2])
                rules.remove(rule)
                continue
            if rule[0] == 'not' and not all([z in facts for z in rule[1]]):
                result.add(rule[2])
                rules.remove(rule)
                continue
        facts = facts.union(result)
        if last_move == len(rules): break
        last_move = len(rules)

    return facts

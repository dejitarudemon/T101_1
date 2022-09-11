def parse_rules(rules) -> list:
    result = []
    for rule in rules:
        oper = ''.join(rule['if'].keys())
        result.append([oper, set(rule['if'][oper]), rule['then']])
    result.sort()
    return result


def check_validate_rules(rules) -> list:
    rules = parse_rules(rules)
    for i in range(0, len(rules) - 1):
        for j in range(i + 1, len(rules)):
            if rules[i][0] == rules[j][0] and rules[i][1] == rules[j][1] and rules[i][2] != rules[j][2]:
                rules[i][2] = rules[j][2] = -1

    return rules


def check_facts(rules, facts) -> list:
    result = []
    for rule in rules:
        if rule[0] == 'or':
            result.append(rule[2] if any([z in facts for z in rule[1]]) else 0)
        if rule[0] == 'and':
            result.append(rule[2] if all([z in facts for z in rule[1]]) else 0)
        if rule[0] == 'not':
            result.append(rule[2] if not any([z in facts for z in rule[1]]) else 0)

    return result

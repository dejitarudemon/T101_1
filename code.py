def parse_rules(rules) -> list:
    result = []
    for rule in rules:
        for oper in ('or', 'and', 'not'):
            incoming = rule['if'].get(oper)
            if incoming:
                result.append([oper, set(incoming), rule['then']])
                break

    result.sort()
    return result


def check_facts(rules, facts) -> dict:
    result = {}
    for i, rule in enumerate(rules):
        if rule[0] == 'or':
            result[i] = False
            for num in rule[1]:
                result[i] = result[i] or num in facts

    return result
def parse_rules(rules) -> dict:
    result = {'and': [], 'or': [], 'not': []}
    for rule in rules:
        for oper in ('and', 'or', 'not'):
            incoming = rule['if'].get(oper)
            if incoming:
                result[oper].append([set(incoming), rule['then']])
                break

    return result


def check_validate_rules(rules) -> dict:
    rules = parse_rules(rules)
    opers = ('and', 'or', 'not')
    for oper in opers:
        rule = rules[oper]
        for i in range(0, len(rule) - 1):
            for j in range(i + 1, len(rule)):
                if rule[i][0] == rule[j][0] and rule[i][1] != rule[j][1]:
                    rule[i][1] = rule[j][1] = 'Unknown'

    return rules


def check_facts(rules, facts) -> list:
    result = []
    opers = ('and', 'or', 'not')
    for oper in opers:
        rule = rules[oper]
        for r in rule:
            if oper == 'or':
                if any([z in facts for z in r[0]]):
                    result.append(r[1])
            if oper == 'and':
                if all([z in facts for z in r[0]]):
                    result.append(r[1])
            if oper == 'not':
                if not any([z in facts for z in r[0]]):
                    result.append(r[1])

    return result

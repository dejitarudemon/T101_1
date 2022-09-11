from lab1 import generate_simple_rules, generate_rand_facts


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
    opers = ('and', 'or', 'not')
    for oper in opers:
        rule = rules[oper]
        for i in range(0, len(rule) - 1):
            for j in range(i + 1, len(rule)):
                if rule[i][0] == rule[j][0]:
                    rule[i][1] = rule[j][1] = ['Unknown']

    return rules


def check_facts(rules, facts) -> dict:
    result = {}
    for i, oper in enumerate(rules):
        if oper == 'or':
            result[i] = any([z in facts for z in rule[1]])

        if rule[0] == 'and':
            result[i] = all([z in facts for z in rule[1]])

        if rule[0] == 'not':
            result[i] = not any([z in facts for z in rule[1]])

    return result


a = generate_simple_rules(10, 4, 4)
f = generate_rand_facts(10, 10)
b = parse_rules(a)
print(a)
print(b)
print(f)
# print(check_facts(b, f))

from lab1 import generate_simple_rules, generate_rand_facts


def parse_rules(rules) -> list:
    result = []
    for rule in rules:
        for oper in ('or', 'and', 'not'):
            incoming = rule['if'].get(oper)
            if incoming:
                result.append([oper, incoming, rule['then']])
                break

    result.sort()
    return result


def check_facts(rules, facts) -> dict:
    result = {}
    for i, rule in enumerate(rules):
        if rule[0] == 'or':
            result[i] = any([z in facts for z in rule[1]])

        if rule[0] == 'and':
            result[i] = all([z in facts for z in rule[1]])

        if rule[0] == 'not':
            result[i] = not all([z in facts for z in rule[1]])

    return result


a = generate_simple_rules(10, 4, 4)
f = generate_rand_facts(10, 10)
b = parse_rules(a)
print(a)
print(b)
print(f)
print(check_facts(b, f))

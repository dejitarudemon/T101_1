from lab1 import generate_simple_rules, generate_rand_facts
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

        if rule[0] == 'and':
            result[i] = rule[1].issubset(facts)

    return result

a = generate_simple_rules(10, 4, 4)
f = generate_rand_facts(10, 10)
b = parse_rules(a)
print(a)
print(b)
print(f)
print(check_facts(b, f))
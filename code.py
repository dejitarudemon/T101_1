from lab1 import generate_simple_rules

def parse_rule(rules) -> list:
    result = []
    for rule in rules:
        for oper in ('or', 'and', 'not'):
            incoming = rule['if'].get(oper)
            if incoming:
                result.append([oper, incoming, rule['then']])
                break

    return result


a = generate_simple_rules(100, 4, 10)
b = parse_rule(a)

print(a)
print(b)
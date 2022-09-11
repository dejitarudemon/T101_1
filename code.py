from lab1 import generate_simple_rules


def parse_rules(rules) -> list:
    result = []
    for rule in rules:
        for oper in ('or', 'and', 'not'):
            incoming = rule['if'].get(oper)
            if incoming:
                result.append([oper, set(incoming), rule['then']])
                break

    return result

def sort_rules(rules) -> list:


a = generate_simple_rules(10, 4, 5)
b = parse_rules(a)

print(a)
print(b)

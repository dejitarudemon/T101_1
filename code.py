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


def check_facts(rules, facts) -> list:

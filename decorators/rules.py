_rules = set()


def rule(f):
    _rules.add(f)
    return f


def run_all(data):
    for f in list(_rules):
        print(f(data))

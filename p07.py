import re

from aocd import data


supernet_pattern = re.compile(r'(?:^|(?<=\]))\w+')
hypernet_pattern = re.compile(r'\[(\w+)]')
abba_pattern = re.compile(r'(\w)(?!\1)(\w)\2\1')
aba_pattern = re.compile(r'(?=(\w)(?!\1)(\w\1))')

support_TLS = 0
support_SSL = 0

for ip in data.splitlines():
    supernets = supernet_pattern.findall(ip)
    hypernets = hypernet_pattern.findall(ip)

    if (any(abba_pattern.search(supernet) for supernet in supernets)
            and not any(abba_pattern.search(hypernet) for hypernet in hypernets)):
        support_TLS += 1

    abas = set()
    for supernet in supernets:
        abas.update(set(aba_pattern.findall(supernet)))

    for aba in abas:
        bab = aba[1] + aba[1][0]
        if any(bab in hypernet for hypernet in hypernets):
            support_SSL += 1
            break

print('Part 1:', support_TLS)
print('Part 2:', support_SSL)

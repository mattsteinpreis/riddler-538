import collections


def unique_sum(sd, pd, ad):
    remaining = collections.defaultdict(list)
    for key, value in ad.items():
        sum_i = value['s']
        prod_i = value['p']
        if len(sd[sum_i]) == 1:
            _ = sd[sum_i].pop()
            _ = pd[prod_i].pop(pd[prod_i].index(key))
        else:
            remaining[key] = value
    return remaining

def unique_product(sd, pd, ad):
    remaining = collections.defaultdict(list)
    for key, value in ad.items():
        sum_i = value['s']
        prod_i = value['p']
        if len(pd[prod_i]) == 1:
            _ = pd[prod_i].pop()
            _ = sd[sum_i].pop(sd[sum_i].index(key))
        else:
            remaining[key] = value
    return remaining


sum_dict = collections.defaultdict(list)
product_dict = collections.defaultdict(list)
remaining = collections.defaultdict(list)

for i in range(1, 10):
    for j in range(i, 10):
        s = i + j
        sum_dict[s].append((i, j))
        p = i * j
        product_dict[p].append((i, j))
        remaining[(i, j)] = {'s': s, 'p': p}

# For each turn, remove all pairs that have a unique product/sum, as those are disqualified based on the fact
# that neither Pete or Susan is sure yet. I.E. if only one pair of numbers had the product/sum they were holding,
# they would know the answer for sure.

print('Remaining pairs:')
print('  Initial: ', len(remaining))
for i in range(4):
    remaining = unique_product(sum_dict, product_dict, remaining)
    print('  Pete, Turn 1: ', len(remaining))
    remaining = unique_sum(sum_dict, product_dict, remaining)
    print('  Susan, Turn 1: ', len(remaining))

print('All pairs with unique product after 4 turns: ')
for key, value in product_dict.items():
    if len(value) == 1:
        print(value[0])

# If Pete would've said no...
remaining = unique_product(sum_dict, product_dict, remaining)
print('All pairs with unique sum after 4 turns: ')
for key, value in sum_dict.items():
    if len(value) == 1:
        print(value[0])

print('Remaining pairs: ')
for item in sum_dict.items():
    if len(item[1]) > 0:
        print(item)
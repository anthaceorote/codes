def flatten_list(l, ans=[]):
    for elem in l:
        if isinstance(elem, (list, tuple)):
            # yield from flatten_list(elem, ans)
            flatten_list(elem, ans)
        else:
            # yield elem
            ans.append(elem)
    return ans


def flatten_list_iterative(items, seqtypes=(list, tuple)):
    for i, x in enumerate(items):
        while i < len(items) and isinstance(items[i], seqtypes):
            items[i:i + 1] = items[i]
    return items


def main():
    a = [1, [2], [3, [4, 5], [6]], [[[[]]]], 7, 8, [[[9]], [10]]]
    b = ['y', 'e', ['lp', 'i'], [[['n', 't']], ['er']], ['v', 'i', 'e'], 'w']

    assert flatten_list(a, []) == list(range(1, 10 + 1))
    assert ''.join(flatten_list(b, [])) == 'yelpinterview'


if __name__ == '__main__':
    main()

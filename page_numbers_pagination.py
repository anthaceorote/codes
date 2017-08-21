'''
Write a function that outputs a string that shows pagination information for a website. The string must show the current page, lowest page index, highest page index, with some "padding" around the current page.
Example output:
"1 ... 4 5 (6) 7 8 ... 30" for a site with 30 pages where the user is on page 6
"1 (2) 3 4 ... 30"
'''

def print_str(page, min_page, max_page):
    if min_page == page:
        op = ['({})'.format(min_page)]
    else:
        op = [min_page]
    for pg in range(min_page + 1, max_page):
        if pg == page:
            op.append('({})'.format(page))
        elif abs(pg - page) <= 2 or max_page - pg < 2 or pg - min_page < 2:
            op.append(pg)
        elif op[-1] == '...':
            continue
        else:
            op.append('...')
    if max_page == page:
        op.append('({})'.format(max_page))
    else:
        op.append(max_page)
    return ' '.join(map(str, op))


for i in range(1, 30 + 1):
    print(print_str(i, 1, 30))

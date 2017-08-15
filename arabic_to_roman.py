def toRoman(data):
    ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))
    ans = []
    
    for roman, val in ROMANS:
        while data >= val:
            data -= val
            ans.append(roman)

    return ''.join(ans)


if __name__ == '__main__':
    assert toRoman(6) == 'VI', '6'
    assert toRoman(76) == 'LXXVI', '76'
    assert toRoman(499) == 'CDXCIX', '499'
    assert toRoman(3888) == 'MMMDCCCLXXXVIII', '3888'
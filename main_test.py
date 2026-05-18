import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # data1: 30 male, 40 female, 30 others -> Male:30.00% Female:40.00% Others:30.00%
    content = open('result1.txt').read()
    print(content)
    regex_test([r'30\.00', r'40\.00', r'30\.00'], content)

@pytest.mark.T2
def test_main_2():
    # data2: 50 male, 25 female, 25 others -> Male:50.00% Female:25.00% Others:25.00%
    content = open('result2.txt').read()
    print(content)
    regex_test([r'50\.00', r'25\.00', r'25\.00'], content)

@pytest.mark.T3
def test_main_3():
    # data3: 10 male, 80 female, 10 others -> Male:10.00% Female:80.00% Others:10.00%
    content = open('result3.txt').read()
    print(content)
    regex_test([r'10\.00', r'80\.00', r'10\.00'], content)

@pytest.mark.T4
def test_main_4():
    # data4: 60 male, 20 female, 20 others -> Male:60.00% Female:20.00% Others:20.00%
    content = open('result4.txt').read()
    print(content)
    regex_test([r'60\.00', r'20\.00', r'20\.00'], content)

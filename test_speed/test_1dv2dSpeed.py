from rx_tools import RxTools

letters = list(set('abcdefghijklmnopqrstuvwxyz'))
nums = range(100)
dd = {(letter, num) for letter in letters for num in nums}

@RxTools.Wrappers.calc_time_wrapper
def isin1(letter, num):
    return letter in letters and num in nums

@RxTools.Wrappers.calc_time_wrapper
def isin2(letter, num):
    return (letter, num) in dd


isin1('a', 2)
isin2('a', 2)
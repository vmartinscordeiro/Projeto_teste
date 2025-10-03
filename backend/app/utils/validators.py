import re

def only_digits(s: str) -> str:
    return re.sub(r"\D", "", s or "")

def _all_equal(d: str) -> bool:
    return d == d[0] * len(d)

def is_valid_cpf(cpf: str) -> bool:
    d = only_digits(cpf)
    if len(d) != 11 or _all_equal(d):
        return False
    nums = list(map(int, d))
    s1 = sum((10-i) * nums[i] for i in range(9))
    r1 = (s1 * 10) % 11
    if r1 == 10: r1 = 0
    s2 = sum((11-i) * nums[i] for i in range(10))
    r2 = (s2 * 10) % 11
    if r2 == 10: r2 = 0
    return nums[9] == r1 and nums[10] == r2

def is_valid_cnpj(cnpj: str) -> bool:
    d = only_digits(cnpj)
    if len(d) != 14 or _all_equal(d):
        return False
    nums = list(map(int, d))
    w1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    w2 = [6]+w1
    r1 = sum(x*y for x,y in zip(nums[:12], w1)) % 11
    dv1 = 0 if r1 < 2 else 11 - r1
    r2 = sum(x*y for x,y in zip(nums[:13], w2)) % 11
    dv2 = 0 if r2 < 2 else 11 - r2
    return nums[12] == dv1 and nums[13] == dv2

def normalize_cpf_cnpj(value: str) -> str:
    d = only_digits(value)
    if len(d) == 11 and is_valid_cpf(d):
        return d
    if len(d) == 14 and is_valid_cnpj(d):
        return d
    raise ValueError("CPF/CNPJ inválido.")

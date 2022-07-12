# With long division approach
def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator%denominator==0:
        return str(numerator//denominator)
    sign='' if numerator*denominator>=0 else '-'
    numerator, denominator = abs(numerator), abs(denominator)
    result=sign+str(numerator//denominator)+'.'
    iteration=0
    recurring_decimal_part=''
    numerator=numerator%denominator
    remainder_in_iteration={numerator:iteration}
    while numerator%denominator:
        iteration+=1
        numerator=numerator*10
        remainder=numerator%denominator
        recurring_decimal_part+=str(numerator//denominator)
        if remainder in remainder_in_iteration:
            recurring_decimal_part=recurring_decimal_part[:remainder_in_iteration[remainder]]+"("+recurring_decimal_part[remainder_in_iteration[remainder]:]+")"
            return result + recurring_decimal_part
        remainder_in_iteration[remainder]=iteration
        numerator=remainder
    return result + recurring_decimal_part

res=fractionToDecimal(int(input()),int(input()))
print(res)
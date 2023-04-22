def convert_binary(n):
    result = ''
    temp = n
    if temp == 0: result = '000000'
    else:
        while temp > 0:
            if temp % 2 == 0: 
                result = '0' + result
                temp //= 2
            else: 
                result = '1' + result
                temp //= 2
    while n > 0:
        if len(result) < 6:
            result = '0' * (6 - len(result)) + result
            n //= 2
        else:
            n //= 2
    return result
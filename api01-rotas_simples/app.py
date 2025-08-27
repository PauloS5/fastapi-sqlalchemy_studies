async def test():
    res = 0
    for i in range(1_000_000):
        res += i
    return res


res = test()
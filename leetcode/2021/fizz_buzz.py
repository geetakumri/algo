def fizzbuzz(intr)
if num is None:
            raise TypeError('num cannot be None')
        if num < 1:
            raise ValueError('num cannot be less than one')
        results = []
        for i in range(1, num + 1):
            res = ""
            if i % 3 == 0:
                res +='Fizz'
            if i % 5 == 0:
                res +='Buzz'
            if res == '':
                res = str(i)
            results.append(res)
        return results
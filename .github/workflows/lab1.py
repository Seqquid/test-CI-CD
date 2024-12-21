class Lab:

    def selection_sort(self, alist):
        for i in range(0, len(alist) - 1):
            smallest = i
            for j in range(i + 1, len(alist)):
                if alist[j] < alist[smallest]:
                    smallest = j
            alist[i], alist[smallest] = alist[smallest], alist[i]
        return alist

    def is_palindrome(self, s):
        if len(s) == 0:
            raise ValueError("Ошибка")
        s_lower = s.lower()
        a = s_lower[::-1]
        if s_lower == a:
            return True
        else:
            return False

    def fac(self, n):
        if n < 0:
            raise ValueError("Ошибка")
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

    def fibonachi(self, n):
        if n < 0:
            raise ValueError("Ошибка")
        if n == 0:
            raise ValueError("Ошибка")

        fib1 = 1
        fib2 = 1

        i = 0
        while i < n - 2:
            fib_sum = fib1 + fib2
            fib1 = fib2
            fib2 = fib_sum
            i = i + 1
        return (fib2)

    def string_search(self, string_n, full_string_n):
        if string_n in full_string_n:
            return True
        else:
            return False

    def simple_int(self, a):
        a = abs(a)
        if a == 0:
            raise ValueError("Ошибка")
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True


    def reverse_32(self, x):
        if x < 0:
            s = str(-x)
            s = '-' + s[::-1]
        else:
            s = str(x)[::-1]
        res = int(s)
        if res < -231 or res > 231 - 1:
            return 0
        else:
            return res

    def integer_to_roman(self, num):
        if num == 0:
            raise ValueError("Ошибка")
        if num < 0:
            raise ValueError("Ошибка")
        symbols = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        roman = ''
        for value, symbol in symbols:
            while num >= value:
                roman += symbol
                num -= value

        return roman
# В данной задаче мы просим вас реализовать класс multifilter,
# который будет выполнять ту же функцию, что и стандартный класс filter, но будет использовать не одну функцию, а несколько.


class Multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        return pos >= 1

    # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        return neg == 0

    # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge


    # iterable - исходная последовательность
    # funcs - допускающие функции
    # judge - решающая функция

    def __iter__(self):
        for elem in self.iterable:
            positive = 0
            negative = 0
            for f in self.funcs:
                if f(elem):
                    positive += 1
                else:
                    negative += 1
            if self.judge(positive, negative):
                yield elem


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(Multifilter(a, mul2, mul3, mul5)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_half)))
print(list(Multifilter(a, mul2, mul3, mul5, judge=Multifilter.judge_all)))

import math


class Integral:
    function = 0
    low = 0
    high = 0
    is_neg = 0
    accuracy = 0
    answer = 0

    def __init__(self, function):
        self.function = function

    def convergence(self):
        if self.function == 1:
            if (self.low < 0) & (self.high > 0):
                self.answer = 2
        elif self.function == 4:
            if (self.low < 0) & (self.high > 0):
                self.answer = 1
        elif self.function == 5:
            if (self.low <= 0) | (self.high <= 0):
                self.answer = 3

    def set_limits(self, low, high):
        self.low = low
        self.high = high
        if self.low > self.high:
            self.is_neg = 1
            self.low, self.high = self.high, self.low
        self.convergence()

    def set_accuracy(self, accuracy):
        self.accuracy = accuracy

    def solve(self):
        if self.answer == 2:
            return [2]
        if self.answer == 3:
            return [3]
        h = (self.high - self.low)
        difference = self.accuracy + 1
        i = 1
        current_value = self.trapezoid_method(h)
        while 1:
            i += 1
            if (self.accuracy >= difference) | ((self.high - self.low) / h > 2000):
                break
            last_value = current_value
            h /= 2
            current_value = self.trapezoid_method(h)
            difference = abs(last_value - current_value) / 3
        if self.is_neg == 1:
            current_value *= -1
        return [int(self.answer), current_value, int((self.high - self.low) / h), difference]

    def trapezoid_method(self, h):
        result = h
        mid = 0
        for i in range(1, int((self.high - self.low) / h)):
            mid += self.get_integral(self.low + i * h)
        result *= (((self.get_integral(self.low) + self.get_integral(self.high)) / 2) + mid)
        return result

    def get_integral(self, x):
        try:
            if self.function == 1:
                return 1 / x
            elif self.function == 2:
                return math.pow(x, 2)
            elif self.function == 3:
                return 8 * x + math.pow(x, 2) - math.pow(x, 3) / 3
            elif self.function == 4:
                return math.sin(x) / x
            elif self.function == 5:
                return math.sqrt(x)
        except ZeroDivisionError:
            return 1


def set_function(f, limits, accuracy):
    integral = Integral(f)
    integral.set_limits(float(limits[0]), float(limits[1]))
    integral.set_accuracy(accuracy)
    return integral.solve()

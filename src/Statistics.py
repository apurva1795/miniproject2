from Calculator import Calculator
import collections

def pop_mean(list):
    num_sum = sum(list)
    answer = Calculator.divide(self, num_sum , len(list))
    return answer

def median(list):
    list.sort()
    if len(list) % 2 == 0:
        first_median = num_list[len(list) // 2]
        second_median = num_list[len(list) // 2 - 1]
        answer = (first_median + second_median) / 2
    else:
        answer = num_list[len(num_list) // 2]
    return answer

def mode(list):
    data = collections.Counter(list)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    if len(mode_val) == len(list):
        answer = 0
    else:
        answer=  join(map(str, mode_val))
    return answer

def pop_variance(list):
    mu = pop_mean(list)
    answer =  Calculator.divide(self,sum(Calculator.square(self, Calculator.subtract(self, number, mu))), (len(list)-1))
    return answer

def pop_standard_deviation(list):
    answer =  Calculator.squareRoot(self, Calculator.divide(self,sum(Calculator.square(self, Calculator.subtract(self, number, mu))), len(list)))
    return answer

def standardized_score(list):
    mu = pop_mean(list)
    sd = pop_standard_deviation(list)
    answer =  Calculator.divide(self, Calculator.subtract(self, number, mu), SD)
    return answer

def sample_mean(list):
    num_values = len(list)
    total =0
    for number in data:
        total = Calculator.add(self, total, number)
    answer =  Calculator.divide(self, total, num_values)
    return answer

def sample_standard_deviation(list):
    score =0
    mu = pop_mean(list)
    for number in list:
        score = sum(Calculator.square(self,Calculator.subtract(self, number, mu)))
    answer =  Calculator.squareRoot(self, Calculator.divide(self,score,(len(list)-1)))
    return answer

def sample_variance (list):
    mu = pop_mean(list)
    answer =  Calculator.divide(self,sum(Calculator.square(self, Calculator.subtract(self, number, mu))), len(list))
    return answer

def z_score (list):
    mu = pop_mean(list)
    sd = pop_standard_deviation(list)
    sm = sample_mean(list)
    answer = Calculator.divide(self,Calculator.subtract(self,sm,mu), Calculator.divide(self,sd,Calculator.squareRoot(self,len(list))))
    return answer



class Statistics(Calculator):
    result = 0

    def __init__(self):
        pass

    def pop_mean(self, list):
        self.result = pop_mean(list)
        return self.result

    def pop_variance(self, list):
        self.result = pop_variance(list)
        return self.result

    def pop_standard_deviation(self, list):
        self.result = pop_standard_deviation(list)
        return self.result

    def standardized_score(self, list):
        self.result = standardized_score(list)
        return self.result

    def median(self, list):
        self.result = median(list)
        return self.result

    def mode(self, list):
        self.result = mode(list)
        return self.result

    def sample_mean(self, list):
        self.result = sample_mean(list)
        return self.result

    def sample_standard_deviation(self, list):
        self.result = sample_standard_deviation(list)
        return self.result

    def sample_variance(self, list):
        self.result = sample_variance(list)
        return self.result

    def z_score (self, list):
        self.result = z_score(list)
        return self.result

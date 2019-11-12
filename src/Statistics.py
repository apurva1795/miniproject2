from Calculator import Calculator

def mean(list):
    num_sum = sum(list)
    answer = num_sum / len(list)
    return answer

class Statistics(Calculator):
    result = 0

    def __init__(self):
        pass

    def mean(self,list):
        self.result = mean(list)
        return self.result


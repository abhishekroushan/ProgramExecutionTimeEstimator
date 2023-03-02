from methods.for_loop import *
import time

class Estimator():
    def __init__(self):
        pass
    def estimate(self):
        pass

class Executor():
    def __init__(self, operation:str):
        self.operation = operation
    def exec(self):
        result = None
        end_time = 0
        start_time = time.time()
        if self.operation == "addition":
            result = forLoopAddition()
            end_time = time.time()
        if self.operation == "multiplication":
            result = forLoopMultiplication()
            end_time = time.time()
        return end_time - start_time


# main
operation = "addition"
#e = Estimator()
#timeEstimated = e.estimate()
a = Executor(operation)
timeActual = a.exec()
print("for operation : ", operation, 
      ",actual time taken", timeActual, " seconds")

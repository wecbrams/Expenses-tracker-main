from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed Value: ",x)

        @abstractmethod
        def task(self):
            print("We ar in abstract task")

class test_class(Absclass):
    def task(self):
            print("We ar in task_class task")
t=test_class()
t.task()
t.print(100)
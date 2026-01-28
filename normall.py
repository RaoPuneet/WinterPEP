from dataclasses import dataclass


@dataclass
class Marks:
    firstmarks:int
    secondmarks:int
    thirdmarks:int

    def total(self) -> int:
        return self.firstmarks + self.secondmarks + self.thirdmarks

@dataclass
class Person:
    name: str
    age: int
    marks: Marks

marks1=Marks(20, 20, 20)
person1=Person("Krish", 31, marks1)

marks2=Marks(50, 20, 30)
person2=Person("rahul", 31, marks2)
marks3=Marks(0, 0, 0)

person3=Person("daku", 31, marks3)

class ResultCalculator:
    def calculate_result(self, person):
        
        total = person.marks.firstmarks + person.marks.secondmarks + person.marks.thirdmarks

        if total == 0:
            print(person.name, "is Absent")

        elif total >= 70:
            print(person.name, "is Pass")
            print("Total Marks =", total)

        else:
            print(person.name, "is Fail")
            print("Total Marks =", total)

result_calculator = ResultCalculator()
result_calculator.calculate_result(person1)
result_calculator.calculate_result(person2)
result_calculator.calculate_result(person3)


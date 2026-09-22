class ClasseB:
    def __init__(self, b1: int = 0, b2: float = 0.0):
        self.__B1 = b1
        self.__B2 = b2

    # Getters e Setters
    def getB1(self) -> int:
        return self.__B1

    def setB1(self, b1: int):
        self.__B1 = b1

    def getB2(self) -> float:
        return self.__B2

    def setB2(self, b2: float):
        self.__B2 = b2

    # Métodos da classe
    def MB1(self):
        print("MB1")

    def MB2(self):
        print("MB2")

    def MB3(self):
        print("MB3")


if __name__ == "__main__":
    obj = ClasseB(20, 2.71)
    obj.MB1()
    obj.MB2()
    obj.MB3()
    print(f"B1 = {obj.getB1()}, B2 = {obj.getB2()}")
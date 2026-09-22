class ClasseA:
    def __init__(self, a1: int = 0, a2: float = 0.0):
        self.__A1 = a1
        self.__A2 = a2

    # Getters e Setters
    def getA1(self) -> int:
        return self.__A1

    def setA1(self, a1: int):
        self.__A1 = a1

    def getA2(self) -> float:
        return self.__A2

    def setA2(self, a2: float):
        self.__A2 = a2

    # Métodos da classe
    def MA1(self):
        print("MA1")

    def MA2(self):
        print("MA2")

    def MA3(self):
        print("Alteração a classe A partir do clone")


if __name__ == "__main__":
    obj = ClasseA(10, 3.14)
    obj.MA1()
    obj.MA2()
    obj.MA3()
    print(f"A1 = {obj.getA1()}, A2 = {obj.getA2()}")
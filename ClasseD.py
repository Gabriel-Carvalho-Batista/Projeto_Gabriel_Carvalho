class ClasseD:
    def __init__(self, d1: int = 0, d2: float = 0.0):
        self.__D1 = d1
        self.__D2 = d2

    # Getters e Setters
    def getD1(self) -> int:
        return self.__D1

    def setD1(self, d1: int):
        self.__D1 = d1

    def getD2(self) -> float:
        return self.__D2

    def setD2(self, d2: float):
        self.__D2 = d2

    # Métodos da classe
    def MD1(self):
        print("MD1")

    def MD2(self):
        print("MD2")


if __name__ == "__main__":
    obj = ClasseD(7, 9.5)
    obj.MD1()
    obj.MD2()
    print(f"D1 = {obj.getD1()}, D2 = {obj.getD2()}")

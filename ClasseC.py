class ClasseC:
    def __init__(self, c1: str = "", c2: int = 0):
        self.__C1 = c1
        self.__C2 = c2

    # Getters e Setters
    def getC1(self) -> str:
        return self.__C1

    def setC1(self, c1: str):
        self.__C1 = c1

    def getC2(self) -> int:
        return self.__C2

    def setC2(self, c2: int):
        self.__C2 = c2

    # Métodos da classe
    def MC1(self):
        print("MC1")

    def MC2(self):
        print("MC2")


if __name__ == "__main__":
    obj = ClasseC("texto exemplo", 42)
    obj.MC1()
    obj.MC2()
    print(f"C1 = {obj.getC1()}, C2 = {obj.
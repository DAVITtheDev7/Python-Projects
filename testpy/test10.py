class Currency:
    rates = {"GEL": 1, "USD": 2.7, "EUR": 3}

    def __init__(self, value, unit="GEL"):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}.00 {self.unit}"

    def changeTo(self, new_unit):
        if new_unit == "USD":
            dolari = self.value / 2.2
            a = Currency(dolari)
            return  a.value
        else:
            return self.value

    def __add__(self, other):
        if isinstance(other, Currency):
            converted_other = other.changeTo(self.unit)
            return Currency(self.value + converted_other.value, self.unit)
        else:
            raise TypeError("Cannot add non-Currency object to Currency")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Currency(self.value * other, self.unit)
        else:
            raise TypeError("გამრავლების ოპერაცია უნდა შესრულდეს მხოლოდ მთელ ან ათწილად რიცხვზე")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __gt__(self, other):
        other.value = other.changeTo(other.unit)
        if other.value > self.value:
            print(f"{other.value}>{self.value}")
        elif other.value < self.value:
            print(f"{other.value}<{self.value}")
c1 = Currency(100, "USD")
print(c1)
c2 = c1.changeTo("EUR")
print(c2)

c3 = Currency(200, "EUR")
c4 = c1 + c3
print(c4)

c5 = c1 * 3
print(c5)
c6 = Currency(300, "GEL")
c1.__gt__(c6)
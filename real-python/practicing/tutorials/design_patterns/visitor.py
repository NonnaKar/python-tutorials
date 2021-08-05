
# * Behavioral patterns
# * Visitor example
class House(object):
    def accept(self, visitor):
        visitor.visit(self)

    def work_on_hvac(self, hvac_specialist):
        print(self, f"worked on by {hvac_specialist}")

    def work_on_electricity(self, electician):
        print(self, f"worked on by {electician}")

    def __str__(self):
        return self.__class__.__name__


class Visitor(object):
    def __str__(self):
        return self.__class__.__name__


class HvacSpecialist(Visitor):
    def visit(self, house):
        house.work_on_hvac(self)


class Electician(Visitor):
    def visit(self, house):
        house.work_on_electricity(self)


hv = HvacSpecialist()
e = Electician()
home = House()
home.accept(hv)
home.accept(e)

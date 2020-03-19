class Layout:
    vias = ['v1', 'v2', 'v3']

    def __init__(self, layers):
        self.layers = layers

    def calculateCost(self):
        return 1000 + len(self.layers) * 5

    @classmethod
    def getVias(cls):
        return cls.vias

    @staticmethod
    def calculate(p, q):
        return p * 2 + q * 3


l1 = Layout(['A', 'B', 'C', 'D', 'Z'])
l2 = Layout(['P', 'Q', 'R'])
print(l1.calculateCost())
print(l1.getVias(), l2.getVias(), Layout.getVias())
print(Layout.calculate(3, 5), l1.calculate(4, 6))
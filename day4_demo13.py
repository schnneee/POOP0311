class Layout:
    vias = ['v1', 'v2', 'v3']

    def __init__(self, layers):
        self.layers = layers
        pass

    pass


l1 = Layout([1, 2, 3, 4])
l2 = Layout([1, 3, 5, 7])
print(l1.layers, l2.layers)
#print(Layout.layers)
print(Layout.vias, l1.vias, l2.vias)
Layout.vias.append('v4')
print(Layout.vias, l1.vias, l2.vias)
l1.layers.append(5)
print(l1.layers, l2.layers)
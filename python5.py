class ParentClass1:
    def __init__(self):
        self.parent1_attr = 'Parent 1 attribute'

    def parent1_method(self):
        print('Parent 1 method')

class ParentClass2:
    def __init__(self):
        self.parent2_attr = 'Parent 2 attribute'

    def parent2_method(self):
        print('Parent 2 method')

class ChildClass(ParentClass1, ParentClass2):
    def __init__(self):
        ParentClass1.__init__(self)
        ParentClass2.__init__(self)
        self.child_attr = 'Child attribute'

    def child_method(self):
        print('Child method')

# Приклад використання
child = ChildClass()
print(child.parent1_attr)
print(child.parent2_attr)
child.parent1_method()
child.parent2_method()
child.child_method()

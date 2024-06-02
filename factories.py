from abc import ABC, abstractmethod
from Component import TreeContainer, TreeLeaf, RectangleContainer, RectangleLeaf

"""
1. 工厂方法模式（Factory Method）：
   - 通过定义一个创建对象的接口，让子类决定实例化哪一个类。
   - 在 factories.py 中，TreeFactory 和 RectangleFactory 定义了 create_container 和 create_leaf 方法，
     使用这些方法在 Builder 类中创建具体的容器和叶子组件。

2. 抽象工厂模式（Abstract Factory）：
   - 提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
   - AbstractFactory 是一个抽象类，定义了创建容器和叶子的方法接口。TreeFactory 和 RectangleFactory
     是其具体实现，用于创建树形和矩形结构的组件。
"""


class AbstractFactory(ABC):
    @abstractmethod
    def create_container(self, name, icon='', level=0):
        pass

    @abstractmethod
    def create_leaf(self, name, icon='', level=0):
        pass


class TreeFactory(AbstractFactory):
    def create_container(self, name, icon='', level=0):
        return TreeContainer(name=name, icon=icon, level=level)

    def create_leaf(self, name, icon='', level=0):
        return TreeLeaf(name=name, icon=icon, level=level)


class RectangleFactory(AbstractFactory):
    def create_container(self, name, icon='', level=0):
        return RectangleContainer(name=name, icon=icon, level=level)

    def create_leaf(self, name, icon='', level=0):
        return RectangleLeaf(name=name, icon=icon, level=level)

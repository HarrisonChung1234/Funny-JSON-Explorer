import copy
from abc import ABC, abstractmethod

"""
组合模式（Composite）：
   - 将对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。
   - Component 是一个抽象基类，定义了 Container 和 Leaf 的公共接口。Container 可以包含子组件，
     而 Leaf 则是终端组件。
"""


class Component(ABC):
    def __init__(self, name, icon='', level=0):
        self.name = name
        self.icon = icon
        self.level = level

    @abstractmethod
    def render(self, args=None):
        pass


class Container(Component):
    def __init__(self, name, icon='', level=0):
        super().__init__(name, icon, level)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def render(self, args=None):
        raise NotImplementedError("This method should be implemented by subclasses")


class Leaf(Component):
    def render(self, args=None):
        raise NotImplementedError("This method should be implemented by subclasses")


class TreeContainer(Container):
    def render(self, args=None):
        is_last = args['is_last']
        prefix = ''.join(['   ' if last else '│  ' for last in is_last])
        prefix = prefix[:-3] if self.level > 0 else prefix
        prefix += '└─ ' if is_last[-1] else '├─ '
        prefix = prefix[:-1]
        print(prefix + str(self.icon) + str(self.name))
        for i, child in enumerate(self.children):
            is_last_child = copy.deepcopy(is_last)
            is_last_child.append((i == len(self.children) - 1))
            child_args = {'is_last': is_last_child, 'is_first': False}
            child.render(child_args)


class TreeLeaf(Leaf):
    def render(self, args=None):
        is_last = args['is_last']
        name = self.name.split(":")[0] if 'None' in self.name else self.name
        prefix = ''.join(['   ' if last else '│  ' for last in is_last])
        prefix = prefix[:-3] if self.level > 0 else prefix
        prefix += '└─ ' if is_last[-1] else '├─ '
        prefix = prefix[:-1]
        print(prefix + str(self.icon) + str(name))


class RectangleContainer(Container):
    def render(self, args=None):
        is_first = args['is_first']
        max_len = args['max_len']
        is_last = args['is_last']
        if is_first:
            print(f"┌─{self.icon}{self.name} ─"f"{'─' * (max_len - len(str(self.name)) - len(self.icon))}┐")
        else:
            print(f"{'│  ' * (self.level - 1)}├─{self.icon}{self.name} ─"
                  f"{'─' * (max_len - len(str(self.name)) - 3 * (self.level - 1) - len(self.icon))}|")
        for i, child in enumerate(self.children):
            child.level = self.level + 1
            is_last_child = copy.deepcopy(is_last)
            last_child = (i == len(self.children) - 1)
            is_last_child.append(last_child)
            child_args = {'is_last': is_last_child, 'is_first': False, 'max_len': max_len}
            child.render(child_args)


class RectangleLeaf(Leaf):
    def render(self, args=None):
        is_last = args['is_last']
        max_len = args['max_len']
        name = self.name.split(":")[0] if 'None' in self.name else self.name
        label = all(is_last)
        if label:
            prefix = '└──' + '┴──' * max(0, self.level - 2) + ('┴─' if self.level > 1 else '')
            suffix = '─' * (max_len - 3 * (self.level - 1) - len(name)) + '┘'
        else:
            prefix = '│  ' * (self.level - 1) + '├─'
            suffix = '─' * (max_len - 3 * (self.level - 1) - len(name)) + '|'
        print(f"{prefix}{self.icon}{name} {suffix}")

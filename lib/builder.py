"""
建造者模式（Builder）：
   - 将一个复杂对象的构建过程与它的表示分离，使得同样的构建过程可以创建不同的表示。
   - Builder 类负责解析JSON数据并使用工厂方法创建组件。它管理构建过程并将组件组装成最终的层次结构。
"""


class Builder:
    def __init__(self, factory, icon_family):
        self.factory = factory
        self.icon_family = icon_family
        self.max_level = 0
        self.max_name_len = 0
        self.root = None

    def build(self, json_data):
        self.root = self.parse(json_data, 'root', level=0)
        max_len = self.max_level * 3 + self.max_name_len + 5
        return self.root, max_len

    def parse(self, data, name, level=0):
        self.max_level = max(self.max_level, level)
        if isinstance(data, dict):
            container = self.factory.create_container(name, icon=self.icon_family['container'], level=level)
            self.max_name_len = max(self.max_name_len, len(name))
            for key, value in data.items():
                if isinstance(value, dict):
                    container.add(self.parse(value, key, level=level + 1))
                else:
                    container.add(
                        self.factory.create_leaf(f"{key}: {value}", icon=self.icon_family['leaf'], level=level + 1))
                    self.max_name_len = max(self.max_name_len, len(f"{key}: {value}"))
            return container
        else:
            self.max_name_len = max(self.max_name_len, len(f"{name}: {data}"))
            return self.factory.create_leaf(f"{name}: {data}", icon=self.icon_family['leaf'], level=level)

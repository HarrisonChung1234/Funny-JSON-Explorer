from builder import Builder
from ..Component import Container


class FunnyJsonExplorer:
    def __init__(self, factory, icon_family=None):
        self.root = None
        self.factory = factory
        self.max_len = 0
        if icon_family is None:
            icon_family = {'container': ' ', 'leaf': ' '}
        self.icon_family = icon_family

    def _load(self, json_data):
        builder = Builder(self.factory, self.icon_family)
        self.root, self.max_len = builder.build(json_data)

    def show(self, json_data):
        self._load(json_data)
        if self.root and isinstance(self.root, Container):
            for i, child in enumerate(self.root.children):
                is_last = [(i == len(self.root.children) - 1), ]
                args = {'is_first': (i == 0), 'is_last': is_last, 'max_len': self.max_len}
                child.render(args=args)

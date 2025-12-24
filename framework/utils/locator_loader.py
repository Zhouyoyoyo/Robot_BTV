import yaml


class LocatorLoader:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, page: str, name: str):
        """
        return: { by: id/xpath/css, value: xxx }
        """
        return self.data[page][name]

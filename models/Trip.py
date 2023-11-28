class Trip:
    def __init__(self, param=None, parent=None, urls=None, words=False):
        self.words = words
        self.param = param
        self.urls = [] if urls is None else urls
        self.parent = parent

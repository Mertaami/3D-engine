def init(self, **kwargs):
    for attr, value in kwargs.items():
        if hasattr(self, attr):
            setattr(self, attr, value)

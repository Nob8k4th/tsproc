class TimeSeries:
    def __init__(self, items):
        self.items = dict(items)
    def get(self, ts):
        return self.items[ts]

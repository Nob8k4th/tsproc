class Resampler:
    def aggregate(self, values, method='mean'):
        if method=='sum': return sum(values)
        if method=='max': return max(values)
        if method=='min': return min(values)
        return sum(values)/len(values)

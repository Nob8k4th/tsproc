class Smoother:
    def sma(self, data, window):
        return [sum(data[i:i+window])/window for i in range(len(data)-window)]
    def ema(self, data, alpha):
        out=[]
        prev=0
        for x in data:
            prev = alpha*x + (1-alpha)*prev
            out.append(prev)
        return out

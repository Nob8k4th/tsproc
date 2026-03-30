import math
class Detector:
    def threshold_detect(self, data, t):
        return [i for i,x in enumerate(data) if x>t]
    def zscore_detect(self, data, z=2.0):
        mean=sum(data)/len(data)
        var=sum((x-mean)*(x-mean) for x in data)/len(data)
        std=math.sqrt(var)
        return [i for i,x in enumerate(data) if abs((x-mean)/std)>z]

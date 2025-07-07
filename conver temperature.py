class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        k=273.15 + celsius 
        F=1.8*celsius + 32
        return [k,F]

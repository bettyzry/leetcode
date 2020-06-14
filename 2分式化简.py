class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        down = cont[-1]
        up = 1
        for i in reversed(cont[:-1]):
            up = i*down + up
            re = down
            down = up
            up = re
        hcf = self.hcf(down, up)
        down = down/hcf
        up = up/hcf
        answer = [int(down), int(up)]
        return answer
    
    def hcf(self, x, y):
        if x > y:
            smaller = y
        else:
            smaller = x
 
        for i in range(1,smaller + 1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf

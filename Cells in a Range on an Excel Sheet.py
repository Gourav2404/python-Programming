class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        listt=list(s)
        firstchar=ord(listt[0])
        secondchar=ord(listt[3])
        secondrange=int(listt[4])
        ret=[]
        for i in range(secondchar-firstchar+1):
            firstrange=int(listt[1])
            while firstrange<=(secondrange):
                ret.append(chr(firstchar+i)+str(firstrange))
                firstrange+=1
        return ret
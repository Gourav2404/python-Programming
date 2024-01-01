class Solution:
    def sortSentence(self, s: str) -> str:
        final=""
        x = s.split()
        d = {}
        for i in x :
            d[i[-1]] = i[:-1]
        for i,j in sorted(d.items()):
            if final != "":
                final+=" "+ j
            else:
                final+= j
        return (final)
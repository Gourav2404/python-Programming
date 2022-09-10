class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count=0
        if ruleKey=="type":
            check=0
        elif ruleKey=="color":
            check=1
        else:
            check=2
        for item in items:
            if item[check]==ruleValue:
                count+=1
        return count
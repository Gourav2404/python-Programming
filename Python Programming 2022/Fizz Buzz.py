class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(n):
            x=i+1
            if (x%3==0) and (x%5==0):
                ans.append("FizzBuzz")
            elif x%3==0:
                ans.append("Fizz")
            elif x%5==0:
                ans.append("Buzz")
            else:
                y=str(x)
                ans.append(y)
        return ans
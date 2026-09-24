class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        l = []
        for i in range(1,n+1):
            if (i%3 == 0 and i%5 == 0):
                l+=['FizzBuzz']
            elif (i % 3 == 0):
                l+=["Fizz"]
            elif (i % 5 == 0):
                l+=["Buzz"]            
            else:
                l+=[str(i)]
        return l

        
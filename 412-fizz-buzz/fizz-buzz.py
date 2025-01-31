class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [0] * (n + 1)
        
        for i in range(1,n +1):
            if i % 15 == 0:
                answer[i] = "FizzBuzz"
            elif i % 5 == 0:
                 answer[i] = "Buzz"
            elif i % 3 == 0:
                 answer[i] = "Fizz"
            else:
                 answer[i] = str(i)
        return answer[1:]

        
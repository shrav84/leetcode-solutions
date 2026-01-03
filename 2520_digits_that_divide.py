class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        divisors = []
        while temp > 0:
            divisors.append(temp % 10)
            temp //= 10

        for i in divisors:
            if num % i == 0:
                count += 1

        return count

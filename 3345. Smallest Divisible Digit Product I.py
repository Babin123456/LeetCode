class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num: int) -> int:
            product = 1
            for digit in str(num):
                product *= int(digit)
            return product
        
        curr = n
        while True:
            if get_digit_product(curr) % t == 0:
                return curr
            curr += 1
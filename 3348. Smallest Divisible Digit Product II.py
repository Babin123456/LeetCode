class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Factorize t into prime factors 2, 3, 5, 7
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in (2, 3, 5, 7):
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"

        def get_min_digits(c2, c3, c5, c7):
            """Returns the smallest list of digits needed to form 2^c2 * 3^c3 * 5^c5 * 7^c7."""
            digits = []
            digits.extend(['5'] * c5)
            digits.extend(['7'] * c7)
            
            digits.extend(['9'] * (c3 // 2))
            c3 %= 2
            
            digits.extend(['8'] * (c2 // 3))
            c2 %= 3
            
            if c2 == 2:
                digits.append('4')
                c2 = 0
            
            if c2 == 1 and c3 == 1:
                digits.append('6')
                c2 = c3 = 0
            elif c2 == 1:
                digits.append('2')
            elif c3 == 1:
                digits.append('3')
                
            return digits

        def build_suffix(length, c2, c3, c5, c7):
            req_digits = get_min_digits(c2, c3, c5, c7)
            if len(req_digits) > length:
                return None
            
            res = []
            digit_factors = {
                1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
                4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
                7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
            }
            
            rem_len = length
            for _ in range(length):
                for d in range(1, 10):
                    f2, f3, f5, f7 = digit_factors[d]
                    nc2, nc3 = max(0, c2 - f2), max(0, c3 - f3)
                    nc5, nc7 = max(0, c5 - f5), max(0, c7 - f7)
                    if len(get_min_digits(nc2, nc3, nc5, nc7)) <= rem_len - 1:
                        res.append(str(d))
                        c2, c3, c5, c7 = nc2, nc3, nc5, nc7
                        rem_len -= 1
                        break
            return "".join(res)

        n = len(num)
        
        first_zero = num.find('0')
        limit = n if first_zero == -1 else first_zero
        
        pref = [(counts[2], counts[3], counts[5], counts[7])] * (n + 1)
        cur2, cur3, cur5, cur7 = counts[2], counts[3], counts[5], counts[7]
        
        digit_factors = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }

        for i in range(limit):
            d = int(num[i])
            f2, f3, f5, f7 = digit_factors[d]
            cur2, cur3 = max(0, cur2 - f2), max(0, cur3 - f3)
            cur5, cur7 = max(0, cur5 - f5), max(0, cur7 - f7)
            pref[i + 1] = (cur2, cur3, cur5, cur7)

        if first_zero == -1 and pref[n] == (0, 0, 0, 0):
            return num

        for i in range(limit, -1, -1):
            c2, c3, c5, c7 = pref[i]
            
            start_d = int(num[i]) + 1 if i < n else 1
            for d in range(start_d, 10):
                f2, f3, f5, f7 = digit_factors[d]
                nc2, nc3 = max(0, c2 - f2), max(0, c3 - f3)
                nc5, nc7 = max(0, c5 - f5), max(0, c7 - f7)
                
                rem_len = n - 1 - i
                suf = build_suffix(rem_len, nc2, nc3, nc5, nc7)
                if suf is not None:
                    return num[:i] + str(d) + suf

        # Repeatedly increment total_len until a valid string is formed
        total_len = n + 1
        while True:
            suf = build_suffix(total_len, counts[2], counts[3], counts[5], counts[7])
            if suf is not None:
                return suf
            total_len += 1
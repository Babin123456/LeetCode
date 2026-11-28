class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        min_price = items[0][1]

        for factor, price in items:
            freq[factor] += 1
            if price < min_price:
                min_price = price

        factor_gain = [0] * (n + 1)
        for f in range(1, n + 1):
            if freq[f] == 0:
                continue
            cnt = 0
            for mult in range(f, n + 1, f):
                cnt += freq[mult]
            factor_gain[f] = cnt - 1

        boosted = []
        for factor, price in items:
            g = factor_gain[factor]
            if g > 0:
                boosted.append((price, g))
        boosted.sort()

        pref_cost = [0] * (len(boosted) + 1)
        pref_items = [0] * (len(boosted) + 1)
        for idx, (price, g) in enumerate(boosted):
            pref_cost[idx + 1] = pref_cost[idx] + price * g
            pref_items[idx + 1] = pref_items[idx] + 2 * g

        best = budget // min_price

        for idx, (price, g) in enumerate(boosted):
            prev_cost = pref_cost[idx]
            if prev_cost > budget:
                break
            max_units = (budget - prev_cost) // price
            used_units = g if g < max_units else max_units
            total_cost = prev_cost + used_units * price
            rem = budget - total_cost
            candidate = pref_items[idx] + 2 * used_units + (rem // min_price)
            if candidate > best:
                best = candidate

        rem_all = budget - pref_cost[-1]
        if rem_all >= 0:
            candidate = pref_items[-1] + (rem_all // min_price)
            if candidate > best:
                best = candidate

        return best
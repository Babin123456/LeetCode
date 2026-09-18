class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {c: i for i, c in reversed(list(enumerate(s)))}
        last = {c: i for i, c in enumerate(s)}
        
        valid_intervals = []

        for c, start in first.items():
            end = last[c]
            i = start
            valid = True
            
            while i <= end:
                if first[s[i]] < start:
                    valid = False
                    break
                end = max(end, last[s[i]])
                i += 1
            
            if valid:
                valid_intervals.append((start, end))

        valid_intervals.sort(key=lambda x: x[1])
        
        ans = []
        prev_end = -1
        for start, end in valid_intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans
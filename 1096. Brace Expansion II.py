class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr: str) -> set[str]:
            groups = []  
            cur_product = {""}  
            
            i = 0
            n = len(expr)
            
            while i < n:
                ch = expr[i]
                
                if ch == '{':
                    j = i
                    brace_count = 0
                    while j < n:
                        if expr[j] == '{':
                            brace_count += 1
                        elif expr[j] == '}':
                            brace_count -= 1
                            if brace_count == 0:
                                break
                        j += 1
                    
                    inner_set = parse(expr[i + 1:j])
                    
                    cur_product = {a + b for a in cur_product for b in inner_set}
                    i = j + 1
                    
                elif ch.isalpha():
                    cur_product = {a + ch for a in cur_product}
                    i += 1
                    
                elif ch == ',':
                    groups.append(cur_product)
                    cur_product = {""}
                    i += 1
            
            groups.append(cur_product)
            
            res = set()
            for group in groups:
                res.update(group)
            return res

        return sorted(list(parse(expression)))
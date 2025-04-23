from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def dfs():
            pass

        number_set = set()
        equation_dict = defaultdict(int) 
        graph = defaultdict(list)
        for i, pair in enumerate(equations):
            x, y = pair
            number_set.add(x)
            number_set.add(y)
            graph[x].append(y)
            graph[y].append(x)
            equation_dict[ (x, y) ] = values[i]
            equation_dict[ (y, x) ] = 1/values[i]
        
        result = []
        print("equation_dict")
        for k in equation_dict:
            print(k, equation_dict[k])
        print("graph")
        for k in graph:
            print(k, graph[k])

        for query in queries:
            x, y = query
            if x not in number_set or y not in number_set:
                result.append(-1.0)
            elif x==y:
                result.append(1.0)
            elif (x, y) in equation_dict:
                result.append(equation_dict.get((x, y)))
            else:
                print("stack is required")
                stack=[(x, [x])]
                visited = set()
                visited.add(x)
                real_path = None
                while stack:
                    print(stack)
                    top, path = stack.pop()
                    for neighbor in graph[top]:
                        if neighbor == y:
                            path.append(y)
                            real_path = path
                            break
                        elif neighbor not in visited:
                            visited.add(neighbor)
                            new_path = path + [neighbor]
                            stack.append( (neighbor, new_path) )
                
                print(real_path)
                if real_path is None:
                    result.append(-1.0)
                else:
                    calc = 1
                    print("calculating...")
                    for idx in range(0, len(real_path)-1):
                        print(equation_dict.get((real_path[idx], real_path[idx+1])))
                        calc *= equation_dict.get((real_path[idx], real_path[idx+1]))

                    result.append(calc)
        
        return result

                        
                            
            

        
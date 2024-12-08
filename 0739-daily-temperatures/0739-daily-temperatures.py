class Solution(object):
    def dailyTemperatures(self, temperatures):
        st = []
        results = [0] * len(temperatures)
        
        for i in range(len(temperatures)-1, -1, -1):
            while st and temperatures[st[-1]] <= temperatures[i]:
                st.pop()
            if st and temperatures[st[-1]] > temperatures[i]:
                results[i] = st[-1] - i
            st.append(i)
            
        
        return results
        


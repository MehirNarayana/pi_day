class Solution:
    def __init__(self):
        
        self.sum = 1

    def solve(self, iterations):
        self.iterations = iterations
        for i in range(1, self.iterations):
            if i % 2 != 0:
                self.sum -= 1/ (2*i + 1)
                
            else:
                self.sum += 1/ (2*i + 1)
            
        self.sum*=4
    
    def return_solution(self):
        return self.sum

    

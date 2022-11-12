class Number:
    def __init__(self, number):
        self.number = number
        
    def __str__(self):
        return f"{self.number}"
        
    @property
    def double(self):
        self.number *= 2
        return self
    
if __name__ == "__main__":
    n = Number(5)
    print(n.double.double)
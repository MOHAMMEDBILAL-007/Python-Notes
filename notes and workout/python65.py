class math:
    def __init__(self,num):
        self.num = num
    def addn_to_num(self,n):
        self.num = n + self.num
    @staticmethod
    def eqn(a,b):
        return (a+b)*b-a+a*(a/b)+a**b
    
a =math(23)
a.addn_to_num(12)
print(a.num)
print(a.eqn(a.num,21))
print(a.eqn(2,4))

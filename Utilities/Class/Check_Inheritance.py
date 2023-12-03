class MultiFalafel(Falafel): 
    def __init__(self,num=1,num_to_eat=1):
        self.number = num
        self.number_eat = num_to_eat
        if self.number_eat > self.number:
            print('Reset the number of falafels eaten '+str(num_to_eat)+' to the total number of falafels '+str(num))
            self.number_eat = num
        Falafel.__init__(self)
        print(str(num)+' falafel(s) created')
    def eat(self):
        print(str(self.number_eat)+' falafel(s) got eaten')
        self.remaining = self.number - self.number_eat

def inspect_falafel_class(c):
    if issubclass(c, Falafel):
        print(f"{c.__name__} inherits from the Falafel class")
    else:
        print(f"{c.__name__} does not inherit from the Falafel class")

inspect_falafel_class(MultiFalafel)
# MultiFalafel inherits from the Falafel class

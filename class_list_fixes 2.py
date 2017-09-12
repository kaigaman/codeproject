class MyPc:
    def __init__(self, pc_owner, pc_model, OS):
        self.pc_owner = pc_owner
        self.OS = OS
        self.pc_model = pc_model

    # There are two magic methods that do similar things but have slightly different
    # functionality: __repr__ and __str__. What's the difference?
    # 
    # Create your own __str__ magic method. Change your __repr__ magic method as needed.
    # Use both correctly from your test code.

    def __repr__(self):
        return " pc_owner: %s\n pc_model: %s\n OS: %s\n " % (self.pc_owner, self.pc_model ,self.OS)

    def __str__(self):
        return " pc_owner: %s\n pc_model: %s\n OS: %s\n " % (self.pc_owner, self.pc_model,self.OS)
        
if __name__ == '__main__':
   

    pcs = []
    pcs.append(MyPc('zerox', 'dell', 'windows'))
    pcs.append(MyPc('noris', 'dell', 'linux'))
    pcs.append(MyPc('kaiga', 'dell', 'linux'))

    pc_nz = raw_input("who is the pc owner ?: ")
    pc_modelz = raw_input("What is the machine model? ")
    pc_OSz = raw_input("what is the operating system ? ")

    
    pcz = MyPc(pc_nz,pc_modelz,pc_OSz)

    pcs.append(pcz)

    for pcz in pcs:
        print pcs
        print

class MyPc:
    def __init__(self, pc_owner, pc_model, OS,pc_descrip):
        self.pc_owner = pc_owner
        self.OS = OS
        self.pc_model = pc_model
        self.pc_descrip = pc_descrip
 

    def __repr__(self):
        return " pc_owner: %s\n pc_model: %s\n OS: %s\n pc_descrip: %s\n " % (self.pc_owner, self.pc_model ,self.OS,self.pc_descrip)


        
if __name__ == '__main__':
   

    pcs = []
    pcs.append(MyPc('zerox', 'dell', 'windows','Black. Dented. Still works fine, but it LOOKS awful!'))
    pcs.append(MyPc('noris', 'dell', 'linux','Gray. Brand new. Still in original box!'))
    pcs.append(MyPc('kaiga', 'dell', 'linux','black. Brand new. Still in original box!'))

    pc_nz = raw_input("who is the pc owner ?: ")
    pc_modelz = raw_input("What is the machine model? ")
    pc_OSz = raw_input("what is the operating system ? ")
    pc_Descrip = raw_input("Describe the pc ? ")

    
    pcz = MyPc(pc_nz,pc_modelz,pc_OSz,pc_Descrip)

    pcs.append(pcz)

    for pcz in pcs:
        print pcs
        print

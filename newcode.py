''' importing the class mypc'''
import Mypc

def readline():
	''' now this will print the pc information base on pc per line in a list format'''
    f = open('pc_info.txt','r')
    for line in f.readlines():
		print line
		f.close()

if __name__ == '__main__':
    readline()
    



 

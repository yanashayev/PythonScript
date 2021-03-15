import os
import subprocess

"""
****os****
"""

# 
os.system("ls") #output when everything is ok its return 0

# os.popen will take the command as an input and return an open file object - you can do function on this object like read(), write().. 
os.popen("ls").read() #output result of the command 'a.txt\ntest.py\n'

print (os.popen("ls").read()) # will print it nicely not as a string 
# spawn has multiplay name with different variation(type of arguments that can  be passed )
os.spawnl(so.P_NOWAIT,"/usr/sh", "ls") #returns Process ID


"""
****subprocess modle****
"""


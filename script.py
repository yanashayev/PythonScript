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
    #output CompletedProcess(args='ls',returncode=0, stdout=b'a.txt\ntest.py\n')
    result=subprocess.run("ls",stdout=subprocess.PIPE )
    result.stdout # returns a bytes stream !!!!!!
    #output b'a.txt\ntest.py\n'
    result.stdout.decode() # return a string
    #output b'a.txt\ntest.py\n'
    print(result.stdout.decode()) # return a string
    #output a.txt
     #      test.py


subprocess.run(["python3","test.py"])
subprocess.run("ls",stdout=subprocess.PIPE)
result=subprocess.run("ls",stdout=subprocess.PIPE)
print(result.stdout.decode())

subprocess.run(["rm","xyz"],stdout=subprocess.PIPE,stderr=subprocess.PIPE) # return what the error if there is one

subprocess.run(["rm","xyz"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT) # return what the error in one field

subprocess.run(["rm","xyz"],capture_output=True)

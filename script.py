import os
import subprocess
import shlex

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
    result = subprocess.run("ls",stdout=subprocess.PIPE )
    result.stdout # returns a bytes stream !!!!!!
    #output b'a.txt\ntest.py\n'
    result.stdout.decode() # return a string
    #output b'a.txt\ntest.py\n'
    print(result.stdout.decode()) # return a string
    #output a.txt
     #      test.py

p1=subprocess.run(['ls','-la'])
print(p1.args) # will give the args
print(p1.returncode) #will return the return code - 0 if succsess, 1 if faile
print(p1.stdout) # will return None

p2=subprocess.run(['ls','-la'], capture_output=True)
print(p2.stdout) #will print with bytes
print(p2.stdout.decode()) #will print as string 

p3=subprocess.run(['ls','-la'], capture_output=True, text=True)
print(p3.stdout) #will print as string 
 
"""
we can also redirect thr standardout to other places as well 
for example let's say that we wanted to redirect that to a file instead (could be used for logging )
we can open up a file and redirect it to there
"""
with open('output.txt','w') as f: #name file and the mode of the file as f its means file objecty
    p4=subprocess.run(['ls','-la'], stdout=f, text=True)




#when we get an error python do not throw an exaption, instead its just returns a nonzero error code  we can check that:
p5=subprocess.run(['ls','-la','dne'], capture_output=True, text=True)
print(p5.returncode) #if there is an error it will pront a nonzero value
if(p5.returncode!=0)
    print(p5.stderr) # print the erorr if there is one 

#if we want to throw exaption if there is a error we need to add a ardument check=true
p6=subprocess.run(['ls','-la','dne'], capture_output=True, text=True,check=True)
print(p6.returncode)

#we3 can ignore our errors by
p7=subprocess.run(['ls','-la','dne'],stderr=subprocess.DEVNULL)
print(p7.returncode) #will print None 

"""
we can change the input that different commands receive as well 
take the output from one command and have that be the input to another
cat on a file- which is a linux command that will just print the content of a file if it 
just have one file as the input and for he second command i"m just doing to use  the output of that first command
to greb that file. grep can be used to search the file for certain contents and again these are linux 
"""
p8=subprocess.run(['ls','test.txt'],capture_output=True)
print(p8.stdout) #will print in bytes 

p9=subprocess.run(['ls','test.txt'],capture_output=True,text=True)
print(p9.stdout) #will print in string

#we want to use the output of this as an input: -n gives as the line number that finds a match


p10=subprocess.run(['grep','-n','test'],capture_output=True,text=True,input=p9.stdout)
print(p10.stdout) #line 4 find test 

subprocess.run(["python3","test.py"])
subprocess.run("ls",stdout=subprocess.PIPE)
result=subprocess.run("ls",stdout=subprocess.PIPE)
print(result.stdout.decode())

subprocess.run(["rm","xyz"],stdout=subprocess.PIPE,stderr=subprocess.PIPE) # return what the error if there is one

subprocess.run(["rm","xyz"],stdout=subprocess.PIPE,stderr=subprocess.STDOUT) # return what the error in one field

subprocess.run(["rm","xyz"],capture_output=True)

#we can run comands in string by this:
subprocess.run("ls -a",shell=True)
#output CompletedProcess(args='ls -a',returncode=0)

#take the comand in a.txt and execute it -very unsave !! the txt file can contain shell injection 
user_input="a.txt"
command="cat {}".format(user_input)
subprocess.run(command, shell=True, capture_output=True)

#example for shell injection code - pwd return the present working directory 
user_input2="a.txt ; pwd"
command2="cat {}".format(user_input2)
subprocess.run(command2, shell=True, capture_output=True)

#example for shell injection code - rm -rf * delete everything in your present directory
user_input3="a.txt ; rm -rf *"
command2=3="cat {}".format(user_input3)
subprocess.run(command3, shell=True, capture_output=True)

#shlex can protect you from injection !!
user_input4="a.txt ; pwd"
command4="cat {}".format(shlex.quote(user_input4))
subprocess.run(command4, shell=True, capture_output=True)
shlex.split("cat a.txt ; pwd")
#output ['cat','a.txt ',';','pwd']
shlex.split("cat 'abc def' >> a.txt")
#output ['cat','abc def','>>','a.txt']

"""
run command and pass input
"""
subprocess.run(["python3","text.py"], capture_output=True,input="abc\mdef".encode()) #send to bytes tream
#output CompletedProcess(args=['python3','text.py'],returncode=0, stdout=b'abc def', stderr=b'')

#the two next example are the same:
subprocess.run(["python3","text.py"], capture_output=True,input="abc\mdef", universal_newlines=True) ##accapt string
#output CompletedProcess(args=['python3','text.py'],returncode=0, stdout=b'abc def', stderr=b'')

subprocess.run(["python3","text.py"], capture_output=True,input="abc\mdef", text=True) ##accapt string since python3.7
#output CompletedProcess(args=['python3','text.py'],returncode=0, stdout=b'abc def', stderr=b'')

subprocess.run(["python3","text.py"], capture_output=True,stdin=open("a.txt",'r')) #take from file a.txt 'r' is read mode
#output CompletedProcess(args=['python3','text.py'],returncode=0, stdout=b'abc def', stderr=b'')

"""
run command with timeout
"""
subprocess.run(["sleep","3"],timeout=5)
#output CompletedProcess(args=['sleep','3'],returncode=0)

"""
run command and throw error if fail
"""
try
    subprocess.run(["rm", "xyz"], check=True)
except subprocess.CalledProcessError:
    print("FAILED") #will print it if there is un exaption
Running Shell Commands using Python
=======

Python Script execute commands in Terminal.

os
===

*os.system(command )*

on *Unix* the return value is the exit status of the process
- 0 value means that everything went fine- there were no errors
- other values means that somthing bad happend- the command didnt run successfully 
 os.system will take the command as an input and return the value of the exit status

exemple:
```
    os.system("ls")
```
*os.popen(command)*

os.popen will take the command as an input and return an open file object - you can do function on this object like read(), write().. 

exemple:

```
    os.popen("ls").read()
    output 'a.txt\ntest.py\n'
    print (os.popen("ls").read())
    output a.txt
           test.py
```
*os.spawn(mode, path, command)* 

executes the program path that you pass in a new process
mode- has 2 vaules - P_NOWAIT/P_WAIT 
P_NOWAIT - not wait for the completion of your command execution and return the ID of the process
P_WAIT - wait for the command to execute completely, and if the it done seccessfuly -exit code, else (not good) return the signal that kill the process
path- path of the program- path of thee command line interpreter "/usr/sh"
command- what to write in the command line 
spawn has multiplay name with different variation(type of arguments that can  be passed )

exemple:
```
    os.spawnl(so.P_NOWAIT,"/usr/sh", "ls") 
```

subprocess
===
*provides more powerful ways to manage and communicate with the subprocesses which are resposible for executing our shell commands*

the main ARI of subprocess module is that it has a function:

*run()* (function)(only in python3.5)

responsible for running any shell command, waits for it to complete, then it will return 'CompletedProcess' instance- args- what we write, return code- value

class subprocess.CompletedProcess
The return value from run(), representing a process that has finished.

args
The arguments used to launch the process. This may be a list or a string.

returncode
Exit status of the child process. Typically, an exit status of 0 indicates that it ran successfully.

A negative value -N indicates that the child was terminated by signal N (POSIX only).

exemple:
```
    subprocess.run("ls")
    output CompletedProcess(args='ls',returncode=0)
    subprocess.run(["python","test.py"]) // more then one word
    
```

*run command and read output*
subprocess.run("ls",subprocess.PIPE )
subprocess.PIPE opens a pipe to the standarfd stream which simply means that whatever output is being produced by that particular process that will be avialible to you program  

```
subprocess.PIPE   open a pipe to the standard stream
*stdout=subprocess.PIPE
*stderr=subprocess.PIPE
*stderr=subprocess.STDOUT
*capyure_output=true (in python3.7)
```

example 

```
    subprocess.run("ls",stdout=subprocess.PIPE )
    output CompletedProcess(args='ls',returncode=0, stdout=b'a.txt\ntest.py\n')
    result=subprocess.run("ls",stdout=subprocess.PIPE )
    result.stdout // returns a bytes stream !!!!!!
    output b'a.txt\ntest.py\n'
    result.stdout.decode() // return a string
    output b'a.txt\ntest.py\n'
    print(result.stdout.decode()) // return a string
    output a.txt
           test.py
     result=subprocess.run("ls",captue_output=Ture )


```

*Popen()* (Class)

A class for flexibly executing a command in a new process



https://www.youtube.com/watch?v=IIiKVaxHCX0
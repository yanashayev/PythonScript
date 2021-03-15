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
provides more powerful ways to manage and communicate with the subprocesses which are resposible for executing our shell commands

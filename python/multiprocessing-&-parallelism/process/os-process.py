import os
import subprocess

# Using os module to create a child process
pid = os.fork()

if pid == 0:
    print("This is the child process with PID: ", os.getpid())
else:
    print("This is the parent process with PID: ", os.getpid())

# Using subprocess module to run a system command
result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True)
print(result.stdout.decode())
import paramiko

# set login credentials
host = "hostname"
port = 22
username = "username"
password = "password"

# set command to run
command = "powershell.exe ls"

# use paramiko to ssh into remote machine
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
print(lines)

# export output to file
with open("output.txt", "w") as f:
    for line in lines:
        f.write(line)
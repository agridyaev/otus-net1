import paramiko
import os


HOST = "192.168.0.107"

with paramiko.SSHClient() as client:
    # Load host key from ~/.ssh/known_hosts
    # client.load_host_keys(filename=os.path.expanduser("~/.ssh/known_hosts"))

    # Add missing host key to the local HostKeys object
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Login using password
    # client.connect(HOST, username="agr",
    #                password=f'{os.getenv("SSH_PASSWD")}')

    # Login using public key
    client.connect(HOST, username="agr")

    stdin, stdout, stderr = client.exec_command("ls -la")
    # stdin, stdout, stderr = client.exec_command("touch file.py")
    print(stdout.read().decode("utf-8"))

    # Interactive shell example
    # ssh = client.invoke_shell()
    # ssh.send("cat\n")
    # ssh.send("Hello OTUS!\n")
    # print(ssh.recv(3000).decode("utf-8"))
    # ssh.send("^D")

    # sftp = client.open_sftp()

    # Download via ssh
    # sftp.get("/home/agr/ssh.txt", "ssh.txt")

    # Upload via ssh
    # sftp.put("config.yml", "/home/agr/config.yml")

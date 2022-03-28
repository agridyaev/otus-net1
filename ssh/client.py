import paramiko
import time


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
    # https://github.com/paramiko/paramiko/issues/1617#issuecomment-712703486
    # stdin.close()
    print(stdout.read().decode("utf-8"))

    # Interactive shell example
    # channel = client.invoke_shell()
    # while not channel.recv_ready():
    #     time.sleep(1)
    # print(channel.recv(3000).decode("utf-8"))
    #
    # channel.send("cat\n")
    # channel.send("Hello OTUS!\n")
    # while not channel.recv_ready():
    #     time.sleep(1)
    # print(channel.recv(3000).decode("utf-8"))
    # channel.send("^D")

    # sftp = client.open_sftp()

    # Download via ssh
    # sftp.get("/home/agr/ssh.txt", "ssh.txt")

    # Upload via ssh
    # sftp.put("config.yml", "/home/agr/config.yml")

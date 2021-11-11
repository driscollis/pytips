import paramiko

def main():
    host = "myserver"
    port = 22
    username = "mike"
    password = "dingbat!"
    
    local_path = '/home/mld/projects/ssh/random_file.txt'
    remote_path = '/home/mdriscoll/random_file.txt'
    
    transport = paramiko.Transport((host, port))
    transport.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, remote_path)
    
    transport.close()
    
main()
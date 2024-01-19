import socket
import concurrent.futures

def scan_port(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        print(f'[+] Port {port} is open')
        s.close()
    except (socket.timeout, socket.error):
        pass

def portscan(ip, start_port, end_port):
    print(f'[*] Starting portscan on {ip}')
    with concurrent.futures.ThreadPoolExecutor(max_workers=worker) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}

        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            try:
                future.result()
            except Exception as e:
                print(f'[-] Port {port} scan failed: {e}')

if __name__ == "__main__":
    ip = input('[*] Enter the IP you want to scan: ')
    start_port = int(input('[*] Enter the starting port: '))
    end_port = int(input('[*] Enter the ending port: '))
    worker = int(input('[*] Enter the number of workers: '))

    portscan(ip, start_port, end_port)

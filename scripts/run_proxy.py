import sys
import os

# Ensure the root directory is in the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from proxy.proxy_server import ProxyServer

if __name__ == '__main__':
    proxy = ProxyServer()
    proxy.run()
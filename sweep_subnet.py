import subprocess  #module to run system commands
import platform    #module to detect host os

from pythonping import ping

def ping_host(host):
    response = ping(host, count= 1, timeout= 1)
    return response.success()



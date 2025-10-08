#!/usr/bin/env python3

import socket
import time
import psutil
import emails

def cpu_state():
    print("-Checking CPU state...")
    if psutil.cpu_percent(interval=1) > 80:
        return "Error - CPU usage is over 80%"
    print("\tCPU state OK.")
    return None

def disk_space():
    print("-Checking disk space...")
    if psutil.disk_usage("/").free / psutil.disk_usage("/").total * 100 < 20.0:
        return "Error - Available disk space is less than 20%"
    print("\tDisk space OK.")
    return None

def memory_space():
    print("-Checking memory space...")
    if psutil.virtual_memory().available / (1024**2) < 100:
        return "Error - Available memory is less than 100MB"
    print("\tMemory space OK")
    return None

def localhost_resolved():
    try:
        print("-Checking availability of localhost")
        if socket.gethostbyname("localhost") != "127.0.0.1":
            return "Error - localhost cannot be resolved to 127.0.0.1"
        print("\tlocalhost available.")
        return None
    except socket.gaierror:
        return "Error - localhost cannot be resolved to 127.0.0.1"



def check_health():
    checks = [cpu_state,
              disk_space,
              memory_space,
              localhost_resolved]
    
    for function_check in checks:
        result = function_check()
        if result is not None:
            message = emails.generate_email(sender="automation@example.com",
                                            to="student@example.com",
                                            subject=result,
                                            body="Please check your system and resolve the issue as soon as possible.")
            emails.send_email(message)

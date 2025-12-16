import os
import subprocess

def run_command(cmd):
    # Command injection
    os.system(cmd)

def execute_shell(cmd):
    # Command injection
    subprocess.call(cmd, shell=True)

def run_subprocess(cmd):
    # Command injection
    os.popen(cmd).read()

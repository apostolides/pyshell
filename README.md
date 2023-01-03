# Demo Python Remote Access Scripts for Windows.  

A sample implementation of "reverse shell"-like remote access utility aimed for windows hosts. The executable deployed on victim machine listens for commands issued on attacker server side, spawns a new powershell process and passes the desired commands as arguments.         


## Server side setup.
On attacker server side start listener with:

```bash
python3 listener.py
```

## Building Executables for victim hosts.
Edit the "HOST" field in shell.py to match the attacker listening server IP.  

 
Use [PyInstaller](https://pyinstaller.org/en/stable/installation.html) to build executables for target systems. Install with:

```bash
python3 -m pip install pyinstaller
```

With src directory as the root folder, build the executable with:
```bash
pyinstaller --onefile shell.py
```
or with:
```bash
python3 -m PyInstaller --onefile .\shell.py
```

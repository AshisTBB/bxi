import os, platform
os.system('xdg-open https://www.facebook.com/profile.php?id=100080255766329/')
bit = platform.architecture()[0]
if bit == '64bit':
    import bxi
else:
    exit('\033[1;31msorry not support 32bit')

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["numpy"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
exe =Executable(script="rpcstart.py", base=base,targetName="RPC_Generator.exe",icon="icon.ico")

setup(  name = "RPC Generator",
        version = "2.0",
        description = "Generates Rational Polynomial Coefficients in the desired format",
        options={"build_exe": build_exe_options},
        executables = [exe])
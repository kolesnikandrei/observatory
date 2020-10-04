import subprocess
import sys
import pickle
from p2 import get_path

strings = ["Bob"]
with subprocess.Popen([sys.executable, get_path()], stdin=subprocess.PIPE) as p:
    p.communicate(input=pickle.dumps(strings), timeout=15)

#  Popen(["/usr/bin/git", "commit", "-m", "Fixes a bug."])

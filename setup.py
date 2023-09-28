import subprocess

print("Setup is starting...")

subprocess.call(["pip", "install", "simplejson"], shell=True)
subprocess.call(["pip", "install", "argparse"], shell=True)
subprocess.call(["pip", "install", "pynput"], shell=True)
subprocess.call(["pip", "install", "Crypto"], shell=True)
subprocess.call(["pip", "install", "datetime"], shell=True)
subprocess.call(["pip", "install", "pillow"], shell=True)
subprocess.call(["pip", "install", "opencv-python"], shell=True)
print("Setup completed successfully.")

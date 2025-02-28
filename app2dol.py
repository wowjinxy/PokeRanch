#!/usr/bin/env python3
import subprocess

# Define input and output paths
app_path = "orig/WBME/00000001.app"
dol_path = "orig/WBME/00000001.dol"

# Define the path to dtk.exe
dtk_path = "./dtk.exe"  # Assumes dtk.exe is in the same directory as this script

# Run the decompression command
subprocess.run(
    [dtk_path, "nlzss", "decompress", app_path, "-o", dol_path],
    check=True
)

print(f"Decompressed {app_path} to {dol_path}")

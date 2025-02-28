#!/usr/bin/env python3
import subprocess

# Define input and output paths
app_path = "orig/WBME_1/00000001.app"
dol_path = "orig/WBME_1/00000001.dol"
# app_path2 = "orig/WBME_256/00000001.app"
# dol_path2 = "orig/WBME_256/00000001.dol"
# app_path3 = "orig/WBME_1/00000001.app"
# dol_path3 = "orig/WBME_1/00000001.dol"
app_path4 = "orig/WBMJ_258/00000001.app"
dol_path4 = "orig/WBMJ_258/00000001.dol"

# Define the path to dtk.exe
dtk_path = "./dtk.exe"  # Assumes dtk.exe is in the same directory as this script

# Run the decompression command
subprocess.run(
    [dtk_path, "nlzss", "decompress", app_path, "-o", dol_path],
    check=True
)

# subprocess.run(
    # [dtk_path, "nlzss", "decompress", app_path2, "-o", dol_path2],
    # check=True,
# )
    
# subprocess.run(
    # [dtk_path, "nlzss", "decompress", app_path3, "-o", dol_path3],
    # check=True
# )

subprocess.run(
    [dtk_path, "nlzss", "decompress", app_path4, "-o", dol_path4],
    check=True
)

print(f"All apps have been decompressed")

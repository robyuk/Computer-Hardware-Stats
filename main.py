#! /usr/bin/env /usr/bin/python3
"""
Examples how to get CPU, RAM, Disk stats

For more information on the psutil library go to:
https://psutil.readthedocs.io/en/latest

Note: Using this on replit will get the stats for the repl

Install the psutil library
pip install psutil
"""

import psutil

# Get CPU statistics
print(psutil.cpu_count())      # Virtual CPU count
print(psutil.cpu_count(logical=False))  #pyhysical CPU count

print(psutil.cpu_percent(interval=1))

print(psutil.cpu_times())
print(psutil.cpu_stats())
print(psutil.cpu_freq())

# RAM stats 
print(psutil.virtual_memory())
print(psutil.swap_memory())

# Disk stats
print(psutil.disk_usage('/'))  #Named tuple of disks stats
print(psutil.disk_partitions())


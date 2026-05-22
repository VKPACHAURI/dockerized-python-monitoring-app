import psutil

cpu = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()

disk = psutil.disk_usage('/')


print(f"cpu usage: {cpu}%")
print(f"memory utlization :{memory.percent}%")
print(f"disk usage:{disk}")



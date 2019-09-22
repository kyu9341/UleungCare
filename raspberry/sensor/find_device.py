import subprocess


def find_dev():
	cmd = ['ls', '/sys/bus/usb-serial/devices/']
	#ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"

	fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	fd_popen.close()

	print(data.decode('utf-8'))
	return(data.decode('utf-8'))

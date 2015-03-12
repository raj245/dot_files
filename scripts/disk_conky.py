#!/usr/bin/env python
import os

io_list = ['/dev/sda', '/dev/sdb', '/dev/sde', '/dev/sdh']

# folder in /media
# for device in os.listdir("/media/"):
#    if (not device.startswith("cdrom")) and (os.path.ismount('/media/' + device)):
#        mountpoint = '/media/' + device
#        io_list.append(mountpoint)

for mountpoint in io_list:
    if os.path.exists(mountpoint):
        print '%s ${goto 80} ${diskio_read %s} ${goto 150} ${diskio_write %s}' % (os.path.basename(mountpoint), mountpoint, mountpoint)

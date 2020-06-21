sudo apt-get install hfsprogs
sudo mkdir /media/tmp
sudo mount -t hfsplus -o force,rw /dev/sdb2 /media/tmp


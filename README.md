Very simple python script to check websites every minute  and send emails if they are down.

**Requires Python 2**
*Tested using Python 2.7*

Instructions:

Download site-check.py and put it some where (I use /opt)

```bash
sudo chown root:root site-check.py
```

```bash
sudo chmod 755 site-check.py
```

Now you want to edit the text file (as root since only root can write) and change everything that has /path/to/x.txt and "#change this" next to it (later this will be a settings file)

Open crontab

```bash
crontab -e
```

Add the following line at the bottom

```bash
* * * * * python /opt/site-check.py
```

Make sure to change the path to where you put the program.


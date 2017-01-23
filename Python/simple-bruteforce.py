import os
import signal
import sys

for w in range(0, 10):
	for x in range(0, 10):
		for y in range(0, 10):
			for z in range(0, 10):
				if os.system('echo "{}" | gpg --passphrase-fd 0 {}'.format((str(w) + str(x) + str(y) + str(z)), sys.argv[1])) == 0:
					os.system('figlet Cracked!')
					print("The passphrase was {}".format(str(w) + str(x) + str(y) + str(z)))
					print()
					os.kill(os.getpid(), signal.SIGINT)
				else:
					print("Cracking... {}".format(str(w) + str(x) + str(y) + str(z)))
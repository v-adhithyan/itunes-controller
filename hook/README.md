# itunes-controller -  hook directory

hook directory contains files that connect iTunes with itunescontroller utility.

There are 2 files in this directory
  * iTunesHook.scpt - Applescript
  * plist

plist helps to run applescript continuosly in background.

Applescript checks if iTunes is running. If iTunes is running, then it calls the itunescontroller utility. From the result of itunescontroller utility, iTunes is controlled.

The 2 files in this directory is copied to user's home directory to .itunescontroller folder which is created after setup. After copying 2 files, using launchctl plist is added as system process which helps to continuosly run itunescontroller utility in the background.

For convenience, the content of these 2 files is included in setup.py file, so that after setup() function completes, the contents are copied as mentioned above.

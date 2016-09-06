import os
import platform
import sys
from setuptools import setup

# check os: If it's not macOS (darwin), then err and exit

if platform.system() != "Darwin":
    print("This utility runs only on macOS")
    sys.exit(1)

# check opencv (cv2): if not present, prompt to install cv2.
# if user chose not to install cv2, then exit setup

try:
    import cv2
except:
    install = raw_input("Open CV is required to run this utility. Enter yes to install:")
    if install == "yes":
        os.system("brew install opencv")
    else:
        print("Setup terminated because this utility requires Open CV and you don't want to install it")
        sys.exit(1)

# if the above checks don't fail, proceed with installation
setup(
    name = "itunescontroller",
    packages = ["itunescontroller"],
    package_data = {'itunescontroller' : ['data/*.xml']},
    include_package_data = True,
    version = "1",
    description = "Control iTunes using hand gestures.",
    url = "https://github.com/v-adhithyan/itunes-controller",
    author = "Adhithyan Vijayakumar",
    author_email = "pollachi.developer@gmail.com",
    license = "MIT",
    classifiers = [
        "Intended Audience :: End Users, Developers",
        "License :: MIT",
        "Operating System :: macOS",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords = "itunes, control, hand, gestures",
    entry_points = {
        'console_scripts' : [
            'itunescontroller=itunescontroller:main'
        ],
    },
)


# function to save applescript and plist to file
def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

# create a hidden folder named itunescontroller in User home.
home_dir = os.getenv('HOME') + os.path.sep
dirname = home_dir + ".itunescontroller"
launch_agent_dir = home_dir + "Library/LaunchAgents/"

if not os.path.exists(dirname):
    print("Creating directory ~/.itunescontroller ...")
    os.makedirs(dirname)
    print("Directory created ....")

script_file = dirname + os.path.sep + "iTuneshook.applescript"
plist_file = launch_agent_dir + "iTunescontroller.plist"

applescript = '''-- This function returns true, if iTunes is running.
on iTunesRunning()
	tell application "System Events" to (name of processes) contains "iTunes"
end iTunesRunning

(* Check if iTunes is running.
If iTunes is running, then run the itunescontroller python utility.
If no face is detected, then probably the mac user is away, so pause playback.
If a face is detected, then mac user is in front of the screen, so now if the playback is paused then start playing. *)

set playing to iTunesRunning()
if playing then
	set away to do shell script "itunescontroller"

	if ((away as string) contains "no face") then
		tell application "iTunes" to pause
	else if ((away as string) contains "face") then
		tell application "iTunes"
			set playerState to player state as string
			if playerState is "paused" or playerState is "stopped" then
				play
			end if
		end tell
	end if
end if
'''

plist = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
<key>Disabled</key>
<false/>
<key>Label</key>
<string>iTunescontroller</string>
<key>Program</key>
<string>/usr/bin/osascript</string>
<key>ProgramArguments</key>
<array>
	<string>osascript</string>
	<string>{script}</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>StartInterval</key>
<integer>15</integer>
</dict>
</plist>
'''.format(script = script_file)

#copy the applescript and plist content to above created folder.
print("Copying config files to ~/.itunescontroller")
write_to_file(script_file, applescript)
write_to_file(plist_file, plist)
print("Files copied.")
print("Installation success ..")

# load plist, now so that controller starts immediately
os.system("launchctl load " + plist_file)

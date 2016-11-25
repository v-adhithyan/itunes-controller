from glob import glob
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

data = glob("data/*.xml")

# if the above checks don't fail, proceed with installation
setup(
    name = "itunescontroller",
    packages = ["itunescontroller"],
    package_data = {'itunescontroller' : data},
    include_package_data = True,
    version = "0.5",
    description = "Play/Pause iTunes with face.",
    url = "https://github.com/v-adhithyan/itunes-controller",
    author = "Adhithyan Vijayakumar",
    author_email = "pollachi.developer@gmail.com",
    license = "MIT",
    classifiers = [
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
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
# try to use os.path.expanduser here.
home_dir = os.getenv('HOME') + os.path.sep
dirname = home_dir + ".itunescontroller"
launch_agent_dir = "/Library/LaunchAgents/"

if not os.path.exists(dirname):
    print("Creating directory ~/.itunescontroller ...")
    os.makedirs(dirname)
    print("Directory created ....")

script_file = dirname + os.path.sep + "iTuneshook.applescript"
plist_file = launch_agent_dir + "me.adhithyan.iTunescontroller.plist"

applescript = ""
with open("itunesHook.applescript", "r") as f:
    applescript = f.read()

plist = ""
with open("me.adhithyan.iTunescontroller.plist", "r") as f:
    plist = f.read()
plist.format(script = script_file)

#copy the applescript and plist content to above created folder.
print("Copying config files to ~/.itunescontroller")
write_to_file(script_file, applescript)
write_to_file(plist_file, plist)
print("Files copied.")
print("Installation success ..")

# load plist, now so that controller starts immediately
os.system("launchctl load " + plist_file)

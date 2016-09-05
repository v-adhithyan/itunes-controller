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

# itunes-controller
![pip](https://img.shields.io/pypi/v/pip.svg)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/v-adhithyan/itunes-controller/blob/master/LICENSE)


  Play/Pause itunes with face.

## Motivation

  One fine day, I was hearing songs with my headphones on and suddenly I wanted to go bathroom. A good song was playing and I needed to pause it in iTunes before going to bathroom. So, i thought what if iTunes plays only if a person is in front of the system. Then i hunted for the software. I was unable to find one. So i made this.

## Installation

  Package is available via pip. Please install as sudo. Otherwise it won't work.

  ```
  $ sudo pip install itunescontroller
  ```

  * **Runs only on macOS**.

## Screenshots

  * When you are away, you will get a notification indicating itunes has paused.
  ![pause](https://raw.githubusercontent.com/v-adhithyan/itunes-controller/master/screenshots/pause.png)

  * When you are back, you will get a notification indicating itunes has started playing.
  ![play](https://raw.githubusercontent.com/v-adhithyan/itunes-controller/master/screenshots/play.png)

## Working

  The package is a combination of python, plist and applescript.

  * [itunescontroller](https://github.com/v-adhithyan/itunes-controller/blob/master/itunescontroller/__init__.py) utility just detects face using **open cv haarcascade classifer** and says **"face"** if a face is detected and **"no face"** if a face is not detected.

  * On installation using pip, a folder .itunescontroller is created in user home and a applescript is copied to that folder. The applescript checks if itunes is running. If itunes is running, it calls itunescontroller utility for face detection. If result is no face and if itunes is playing, it will be paused and if the result is face and if itunes is not playing, it will start playing.

  * After installation, a [**plist**](https://github.com/v-adhithyan/itunes-controller/blob/master/hook/me.adhithyan.iTunescontroller.plist) is created in **/Library/LaunchAgents** which invokes applescript which controls iTunes.

  * The utility will continuosly run in background for every 15 seconds.


## To do

- [ ] Check whether it is working in Python 3.

## License

  Released under MIT license.

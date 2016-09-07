# itunes-controller

  Play/Pause itunes with face.

## Motivation

  One fine day, I was hearing songs with my headphones on and suddenly I wanted to go bathroom. A good song was playing and I needed to pause it in iTunes before going to bathroom. So, i thought what if iTunes plays only if a person is in front of the system. Then i hunted for the software. I was unable to find one. So i made this.

## Installation

  Package is available via pip. Please install as sudo. Otherwise it won't work.

  ```
  $ sudo pip install itunescontroller
  ```

  * **Runs only on macOS**.

## Working

  The package is a combination of python, plist and applescript.

  * [itunescontroller](https://github.com/v-adhithyan/itunes-controller/blob/master/itunescontroller/__init__.py) utility just detects face using **open cv haarcascade classifer** and says **"face"** if a face is detected and **"no face"** if a face is not detected.

  * On installation using pip, a folder .itunescontroller is created in user home and a applescript is copied to that folder. The applescript checks if itunes is running. If itunes is running, it calls itunescontroller utility for face detection. If result is no face and if itunes is playing, it will be paused and if the result is face and if itunes is not playing, it will start playing.

  * After installation, a [**plist**](https://github.com/v-adhithyan/itunes-controller/blob/master/hook/me.adhithyan.iTunescontroller.plist) is created in **/Library/LaunchAgents** which invokes applescript which controls iTunes.

  * The utility will continuosly run in background for every 15 seconds.

 For more details, see [setup.py](https://github.com/v-adhithyan/itunes-controller/blob/master/setup.py) file, [init.py](https://github.com/v-adhithyan/itunes-controller/blob/master/itunescontroller/__init__.py) file and [hook](https://github.com/v-adhithyan/itunes-controller/tree/master/hook) directory.

 ## Contributing

 - [ ] Check whether it is working in python 3.

Any suggestions are welcome.

## License

  MIT.

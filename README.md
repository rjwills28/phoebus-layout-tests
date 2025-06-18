# phoebus-layout-tests
Scripts to test displaying Phoebus screens

This app will test opening:
- Standalone displays
- Saved mementos

## Installation
- Clone the repo:
  
  `git clone git@github.com:rjwills28/phoebus-layout-tests.git`
- cd:
  
  `cd phoebus-layout-tests/`

## Setup
- First modify the Python helper script (`scripts/phoebusHelper.py`) to point to your instance of Phoebus and `settings.ini` file, e.g.:
  ```
  phoebusInstance = "/home/user/software/phoebus/phoebus-product/phoebus.sh"
  phoebusSettings = " -settings /home/user/software/phoebus/phoebus_settings.ini"
  ```
- Create the require `memento` file based on your path:

  `python scripts/createMementos.py`

  Files will be placed in the `mementos/` directory
- Start the demo IOC in another terminal:

  `softIoc -d ioc/test.db`
- Note: if you do not have the Python package `psutil` installed natively then you will need to create a virtual environment to install it:
  ```
  python3 -m venv venv
  source venv/bin/activate
  pip install psutil
  ```

## Run
- Start the top up display:

  `python scripts/topup.py`

- Start the diagnostics overview

  `python scripts/diagostics.py`

  - Click on `Fans` to open a display from here

- Start the standalone window:

  `python scripts/standalone1.py`

# Democracy Works Practical: Upcoming Elections

This is a Flask application that accepts a user address and returns information about upcoming elections.

## Installation

### Requirements
This app requires a virtual environment (details to install below) as well as a requirements.txt file with all needed libraries.

### Dependencies

To install the dependencies, run the following commands:

```sh
## Create a virtual Python environment in the `.venv` directory
python3 -m venv .venv

## Ensure you have pip installed. For help see:
## https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/
python3 -m pip install --user --upgrade pip

## Enter the virtual environment: you'll need to do this in your environment to
## run commands at command line.
source .venv/bin/activate

## Install the requirements
pip install -r requirements.txt
```

When you are done with the virtual environment, use `deactivate` to exit it and
return to your normal shell, or quit your terminal program. 


## Usage

### Running

To run the application, use the following commands:

```sh
## OPTIONAL: If you haven't done this yet
source .venv/bin/activate

export FLASK_APP=elections
export FLASK_ENV=development
flask run
```

Once the app is running, check the terminal for the http address/port and copy address into browser.

When the address is searched in the browser, the search page will appear. The application accepts a full address, but only the city and state are required.

As of October 5, these are some city/states that will return elections:
Homestead, FL
Binger, OK
Arvada, CO
Seattle, WA
Philadelphia, PA

And some city/states that will not return elections:
Los Angeles, CA
Burlingon, VT
Bladensburg, MD

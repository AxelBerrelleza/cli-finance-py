- To get an BMV API token go to https://databursatil.com/

### Setup development proyect
- activate virtual env
- install packages
- optional: install the command `pip install -e .`, this way you can start using the bmv command

### Intalling the bmv cli app
1. git clone the repository
2. change to that directory
3. create a virtual environment e.g.: `virtualenv .venv`
4. thell pip to perform the installation from project: `pip install --editable .`
5. the above step just create a file in .venv/bin/ named bmv, 
and it is need to change the first line (shebang) with the route of your python installation. deactivate your venv to get it.
6. once the shebang is placed as indicated, the step left is to copy the bmv file into one directory of the PATH, e.g. /usr/local/bin/. `sudo cp .venv/bin/bmv /usr/local/bin/`
7. then you ready to go `bmv --help`


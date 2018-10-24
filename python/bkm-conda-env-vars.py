#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Will create <path_to_conda_env_/etc/conda/(de-)activate.d/<env_name>_env_vars.bat
"""

import argparse
import os
import pathlib
import platform
import re
import subprocess

PLATFORM = platform.system()

def get_default_conda_env_path():
    """
    Get the system's default conda environment path.

    :returns: Returns either the path as a string or "0" in case no path was found.
    """
    tmp = subprocess.Popen("conda info", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out = tmp.communicate()[0].decode('utf-8')
    dirs = re.findall("envs directories : (.*)", out)
    if dirs:
        return dirs[0].strip()
    else:
        return "0"

def create_env_dirs(path, name):
    """
    Creates paths for scripts that get automatically executed when the environment gets
    de-/activated. Use these scripts to set/unset environment variables when the conda env is
    de./activated.

    :param path: Path to the conda environment.
    :param name: Name of the conda environment.
    :returns: The path to the folder which contains the de-/activate scripts as a string.
    """
    # TODO 2018-10-22 Add Linux
    if not os.path.split(path)[1] == name:
        path = os.path.join(path, name)

    tmp = os.path.join(path, 'etc', 'conda')
    activate_path = os.path.join(tmp, 'activate.d')
    deactivate_path = os.path.join(tmp, 'deactivate.d')

    pathlib.Path(activate_path).mkdir(parents=True, exist_ok=True) 
    pathlib.Path(deactivate_path).mkdir(parents=True, exist_ok=True) 

    with open(os.path.join(activate_path, name + '_env_vars.bat'), 'w') as f:
        f.write("set MY_KEY='secret-key-value'\nset MY_FILE=C:\\path\\to\\my\\file")

    with open(os.path.join(deactivate_path, name + '_env_vars.bat'), 'w') as f:
        f.writelines("set MY_KEY=\nset MY_FILE=")

    return str(tmp)

def main():
    """
    Usage: python3 bkm-conda-env-vars.py <name_of_conda_env>
    """
    # TODO 2018-10-22 Add option to run "conda install autopep8 flake8 pyflakes pylint rope"
    # TODO 2018-10-22 Add option to install Kivy

    parser = argparse.ArgumentParser(description='Create conda env vars files.')
    parser.add_argument('env_name', type=str, metavar='NAME', help='Name of the conda environment')
    args = parser.parse_args()
    print(create_env_dirs(get_default_conda_env_path(), args.env_name))

    # TODO 2018-10-22 Print created paths/files

if __name__ == '__main__':
    main()
import sys
import os
import platform
import tempfile
import shutil
import argparse
import subprocess
import site
from importlib import reload

os.chdir(os.path.dirname(__file__))

#region: Check python version
pythonVersion = platform.python_version_tuple()
if (int(pythonVersion[0]) != 3) or (int(pythonVersion[1]) < 8):
    print('Error: Install requires python version 3.8 or newer.')
    print("The latest version of python can be downloaded "
          + "using the following link: https://www.python.org")
    print('')
    print('Install unsuccessful.')
    quit()
#endregion

#region: Check if QUARC is installed
try:
    import quanser
except ImportError:
    print('Error: Before running this installer, you must first install QUARC.')
    quit()
#endregion

#region: Parse Command Line Arguments
parser = argparse.ArgumentParser()

parser.add_argument(
    "-i",
    "--install_dir",
    help="path to where QAL should be installed",
    action="store"
)
parser.add_argument(
    "-d",
    "--ignore_dependencies",
    help="skip installing required python packages",
    action="store_true"
)
parser.add_argument(
    "-e",
    "--skip_envvar_setup",
    help="skip setting up required environment variables",
    action="store_true"
)

args = parser.parse_args()
#endregion

#region: Determine Install Location
if args.install_dir is not None:
    install_dir = args.install_dir # XXX Strip Quotes
else:
    # Default install location is Quanser folder in home directory
    if (os.name == 'nt'):
        install_dir = os.environ['USERPROFILE'] + '/Documents/Quanser/'
    elif (os.name == 'posix'):
        install_dir = os.environ['HOME'] + '/Quanser/'
    else:
        print('Error: Unsupported OS')
        print('Install unsuccessful.')
        quit()

install_dir = os.path.normpath(install_dir)

if 'QAL_DIR' in os.environ:
    if install_dir != os.environ['QAL_DIR']:
        print('Error: QVL already installed in a different location.')
        print('Current location: ' + os.environ['QAL_DIR'])
        print('Attempted new location: ' + install_dir)
        print('Install unsuccessful.')
        quit()

    print('')
    confirmation = input(
        'Warning: QVL is already installed at "' + os.environ['QAL_DIR'] + '". '
        + 'Continuing with this installer will overwrite files from the '
        + 'current installation. Are you sure you want to continue? (y,[n])'
        )
    if 'y' not in confirmation.lower():
        print('Installation cancelled.')
        quit()

# Create install directory if it doesn't already exist
if not os.path.isdir(install_dir):
    try:
        os.mkdir(install_dir)
    except:
        print('Error: Invalid install location.')
        print('Install unsuccessful.')
        quit()
#endregion

#region: Install Dependencies
if not args.ignore_dependencies:
    print('Installing required python packages...')
    packages = [
        'numpy',
        'opencv-python',
        'PyQt6',
        'pyqtgraph',
        'pygit2',
    ]

    try:
        subprocess.check_call([sys.executable,'-m','pip','install'] + packages)
        reload(site)
        import pygit2 # < must be placed here since it gets installed earlier in script
    except:
        print('Error: Failed to install required python packages '
            + '(Note: this requires a valid internet connection).'
        )
        confirmation = input(
            'Would you like to skip installing dependencies for now '
            + 'and finish with the rest of the installation? (y,[n])'
        )
        if 'y' not in confirmation.lower():
            print('Installation cancelled.')
            quit()
#endregion

#region: Install files from GitHub
print('Installing Quanser virtual libraries...')
try:
    import pygit2
    tmpdir = tempfile.TemporaryDirectory()
    pygit2.clone_repository(
        'https://github.com/quanser/Quanser_Interactive_Labs_Resources.git',
        tmpdir.name
    )
    shutil.copytree(
        tmpdir.name + '/python/qvl/',
        os.path.join(install_dir,'libraries/python/qvl'),
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns('.*')
    )
    try:
        tmpdir.cleanup()
    except:
        pass
except:
    print('Error: Failed to install files from GitHub '
        + '(Note: this requires a valid internet connection).'
    )
    confirmation = input(
        'Would you like to skip this part for now '
        + 'and finish with the rest of the installation? (y,[n])'
    )
    if 'y' not in confirmation.lower():
        print('Installation cancelled.')
        quit()
#endregion

#region: Setup Environment Variables
environmentVariablesSet = False
if not args.skip_envvar_setup:

    pythonPath = os.path.normpath(install_dir + '/libraries/python/')

    if os.name == 'nt':
        if not('PYTHONPATH' in os.environ):
            os.system('setx PYTHONPATH "' + pythonPath + '"')
            environmentVariablesSet = True

        elif not(pythonPath in os.environ['PYTHONPATH']):
            pythonPath = os.environ['PYTHONPATH'] + ';' + pythonPath
            os.system('setx PYTHONPATH "' + pythonPath + '"')
            environmentVariablesSet = True

        if not('QAL_DIR' in os.environ):
            os.system('setx QAL_DIR "' + install_dir + '"')
            environmentVariablesSet = True
    elif os.name == 'posix':
        shell = os.environ.get('SHELL')
        if shell and 'bash' in shell:
            shellConfigFile = '.bashrc'
        elif shell and 'zsh' in shell:
            shellConfigFile = '.zshrc'
        else:
            print('Error: Unsupported shell interface. '
                +'Only bash and zsh supported.'
            )
            quit()
        configFilePath = os.path.join(os.environ['HOME'], shellConfigFile)

        alreadySetup = False
        if os.path.exists(configFilePath):
            with open(configFilePath, 'r') as config_file:
                for line in config_file.readlines():
                    if 'QAL_DIR' in line.strip():
                        alreadySetup = True
                        break

        if not alreadySetup:
            msg = (
                '\n# Environment variables for Quanser Application Libraries'
                + '\nexport QAL_DIR="' + install_dir + '"'
                + '\nexport PYTHONPATH="${PYTHONPATH}:'+ pythonPath + '"'
            )
            with open(configFilePath, 'a') as config_file:
                config_file.write(msg)
            environmentVariablesSet = True
    else:
        print('Error: unrecognized OS.')
        quit()
#endregion


print('')
print('Install Successful!')
print('Location: ' + install_dir)
print('')
if environmentVariablesSet:
    if (os.name == 'nt'):
        print('Windows must be reset in order '
            + 'to finish setup of environment variables.'
        )
    elif (os.name == 'posix'):
        print('Close this terminal and open a new one '
            + 'to finish setup of environment variables.'
        )
print('')
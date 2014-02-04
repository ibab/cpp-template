
import sys
import os

# Python 2 compatibility
try:
    input = raw_input
except NameError:
    pass

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":True,   "y":True,  "ye":True,
             "no":False,     "n":False}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")

name = input("Please enter a name for your project [default]: ")
version = input("Please enter an initial version [0.0.0.0]: ")
brief = input("Please enter a description [No description]: ")

if not name.strip():
    name = "default"
if not version.strip():
    version = "0.0.0.0"
if not brief.strip():
    brief = "No description"

use_git = query_yes_no("Do you want to initialize git?", default="no")
git_url = ""
if use_git:
    git_url = input("Please enter the url of your git repository: ").strip()

def template(name, target, **kwargs):
    f = open(name)
    text = f.read()
    f.close()
    for k, v in kwargs.items():
        text = text.replace('{{' + k + '}}', v)
    f = open(target, 'w')
    f.write(text)
    f.close()

kwargs = dict(project_name = name, project_version=version, project_brief=brief)

print('Creating CMake files...')
template('cmake/template.txt', 'CMakeLists.txt', **kwargs)
template('cmake/template_src.txt', 'src/CMakeLists.txt', **kwargs)
template('cmake/template_test.txt', 'test/CMakeLists.txt', **kwargs)

if git_url.strip():
    print('Initializing git...')
    os.system('git remote rm origin > /dev/null 2>&1 || git init > /dev/null 2>&1')
    os.system('git remote add origin ' + git_url)


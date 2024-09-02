# Create a virtual environment
# python -m venv myenv
# Activate the virtual environment (Linux/macOS)
# source myenv/bin/activate
# Activate the virtual environment (Windows)
# myenv\Scripts\activate.bat

'''Once the virtual environment is activated, any packages 
that you install using pip will be installed in the 
virtual environment, rather than in the global Python 
environment. This allows you to have a separate set of 
packages for each project, without affecting the packages 
installed in the global environment.'''


# Deactivate the virtual environment
# deactivate

''' To create a requirements.txt file, you can use 
the ### pip freeze ### command, which outputs a list of 
installed packages and their versions. For example:
'''
# Output the list of installed packages and their versions to a file
# pip freeze > requirements.txt

''' To install the packages listed in the requirements.txt 
file, you can use the pip install command with the -r flag:'''

# Install the packages listed in the requirements.txt file
# pip install -r requirements.txt

''' Using a virtual environment and a requirements.txt 
file can help you manage the dependencies for your 
Python projects and ensure that your projects are 
portable and can be easily set up on a new machine.'''
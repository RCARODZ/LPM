from distutils.core import setup

REQUIERED = {
    #Required packages for LPM
}

setup(
    name='LPMcli',
    version='0.4dev',
    license='MIT License',
    long_description=open('../README.md').read(),
    author='Ricardo Castro',
    packages=[
          'virtualenv',
          'requests',
      ],
)
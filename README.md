# LPM

Local Password Manager is a tool design to generate and store passwords in a safer way. 

## To Do:

* Working on Python 3 implementation

Create an API for a more modular environment.

Create an integration with a database. (maybe)

Create easy user interaction. (add, remove, modify)

Redesing Class Implementations

Create user accounts within LPM. (Figure out how to do this...)

## FIX:

+ Add more comments in the code.


## LPM API

+ End-to-end encrypted to proctect user account.
+ The comms will be decrypted by LPM
+ What methods will be implemented in the API:
    - get_userinfo()
        * This will respond with the user information
    - get_accountinfo()
        * Respond with account information
    - get_accountpsswds()
        * Respond with every account and every password that corresponds to the account.


### User stuff:

User must be able to add multiple accounts

User will be able to generate a random password

Dig into what more will i need... 

### Some helpful links:

* [django password manager](https://pypi.python.org/pypi/django-password-manager/0.0.1) 
* [to read](http://charlesleifer.com/blog/creating-a-personal-password-manager/)

## Getting Started

To get started activate virtualevn (must have it installed beforehand):

```
git clone https://github.com/RCARODZ/LPM.git

source LPM/bin/activate #Activates virtual environment
```

### C Version
```
pgenerator.c account password
```

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python 2.7
```

### Installing

#### Developing Setup.py

```
python setup.py install
```

+ Install LPM Dependencies
+ Setup Database
+ What more? 

## Running the tests

```
python main.py -t 
```

### Break down into end to end tests

Explain what these tests test and why

```
python main.py -t
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org) - Python 2.7


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Ricardo Castro** - *Initial work* - [RCARODZ](https://github.com/RCARODZ)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

## Project

The objective of this project is to generate test files for pure function
 
## Setup

clone repo:

```shell
git clone https://github.com/Theodrem/tdd-architecture-python.git
```

go to the project, then create virtualenv with:

```shell
python3 -m venv env
```

```
source env/bin/activate
```

run the command to install the project:
```shell
python3 setup.py install
```

## CREATE YOUR TESTS

**Now you have to go to the project where you want to create your tests**

Create a json configuration, you have an example for this project. All tests in this project has been generated.

**Now execute the command:**

```shell
management cmd-create-test <path your json config>
```

## project testing
```shell
 pytest -s src/ns_architecture/tests
```
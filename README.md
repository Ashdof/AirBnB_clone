# AirBnB clone - The console

## Description
This project is part of the AirBnB clone project, which aims to create a command-line interpreter (CLI) to manage AirBnB objects. The CLI provides users with a text-based interface to interact with the system, allowing them to perform various tasks and operations such as creating, updating, and deleting objects such as Users, States, Cities, and Places. This serves as a crucial foundation for the subsequent development of a full-fledged web application.

## Command Interpreter

The command interpreter, also known as the console or shell, is a program that allows users to interact with the AirBnB system using text-based commands. It provides a command-line interface where users can input commands to perform specific tasks or operations on AirBnB objects.

### How To Run The Command Line Interpreter
To start the AirBnB clone command interpreter, Run the command `./console.py` .

### Using the Interpreter
Once the command interpreter is running, you can use various commands to manage AirBnB objects. The available commands include:

**create**: Create a new object.

**show**: Display details of a specific object.

**destroy**: Delete a specified object.

**all**: List all available objects.

**update**: Update attributes of a specified object.



## Examples of Usage

**create**: Create a new object (e.g., User, State, City, Place).

`(hbnb) create User`

__show__: Retrieve information about a specific object.

`(hbnb) show User 1234-5678`

__destroy__: Delete a specified object.


`(hbnb) destroy User 1234-5678`

__all__: Display all instances of a specific class or all objects.

`(hbnb) all`

`(hbnb) all User`

__update__: Update attributes of a given object.

`(hbnb) update User 1234-5678 name "John Doe"`

__quit/EOF__: Exit the command interpreter.


`(hbnb) quit`


## Execution

The shell works like this in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
## Authors

- [Dave Bryan Tamakloe](https://www.github.com/davebryan001)
- [Emmanuel Enchill](https://www.github.com/ashdof)


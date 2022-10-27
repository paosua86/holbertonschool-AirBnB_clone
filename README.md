# AirBnB Clone - The Console
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.8.5)

## Installation
* Clone this repository: `https://github.com/paosua86/holbertonschool-AirBnB_clone.git`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the entry point of the command interpreter.
List of commands this console current supports:
* `EOF` - exits console
* `quit` - exits console
* `<emptyline>` - overwrites default emptyline method and does nothing
* `create` - Creates a new instance of`BaseModel`, saves it (to the JSON file) and prints the id
* `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
* `show` - Prints the string representation of an instance based on the class name and id.
* `all` - Prints all string representation of all instances based or not on the class name.
* `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class from which future classes will be derived
* `def __init__(self, *args, **kwargs)` - Initialization of the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JASON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* `def reload(self)` -  deserializes the JSON file to __objects

#### `/Running the tests`
All our tests are executed by using this command in the root directory of the project: <code>python3 -m unittest discover tests</code>


## Examples of use
```
$./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) all Mymodel
** class doesn't exist **
(hbnb) create BaseModel
bbd5eb79-4e24-404f-93f8-53c9c10de9e2
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel bbd5eb79-4e24-404f-93f8-53c9c10de9e2
[BaseModel] (bbd5eb79-4e24-404f-93f8-53c9c10de9e2) {'id': 'bbd5eb79-4e24-404f-93f8-53c9c10de9e2', 'created_at': datetime.datetime(2022, 10, 27, 18, 14, 2, 909876), 'updated_at': datetime.datetime(2022, 10, 27, 18, 14, 2, 909999)}
(hbnb) create User
409fa35a-db20-450e-84ee-d510c1b6cf9a
(hbnb) User.create()
f8d260fe-c93b-4ffa-9048-a80734fc91b4
(hbnb) all User
["[User] (409fa35a-db20-450e-84ee-d510c1b6cf9a) {'id': '409fa35a-db20-450e-84ee-d510c1b6cf9a', 'created_at': datetime.datetime(2022, 10, 27, 18, 14, 32, 759811), 'updated_at': datetime.datetime(2022, 10, 27, 18, 14, 32, 759877)}", "[User] (f8d260fe-c93b-4ffa-9048-a80734fc91b4) {'id': 'f8d260fe-c93b-4ffa-9048-a80734fc91b4', 'created_at': datetime.datetime(2022, 10, 27, 18, 14, 43, 358151), 'updated_at': datetime.datetime(2022, 10, 27, 18, 14, 43, 358225)}"]
(hbnb) User.count()
2
(hbnb) Place.create()
ac2e852a-e309-41d2-b551-57f2a65f6b48
(hbnb) show Place ac2e852a-e309-41d2-b551-57f2a65f6b48
[Place] (ac2e852a-e309-41d2-b551-57f2a65f6b48) {'id': 'ac2e852a-e309-41d2-b551-57f2a65f6b48', 'created_at': datetime.datetime(2022, 10, 27, 18, 15, 26, 418437), 'updated_at': datetime.datetime(2022, 10, 27, 18, 15, 26, 418496)}
(hbnb) destroy Place ac2e852a-e309-41d2-b551-57f2a65f6b48
(hbnb) quit
```

## Bugs
No known bugs at this time.

## Authors
Paola Suarez - [Github](https://github.com/paosua86)
Jesus Macias - [Github](https://github.com/Ragnar9902)

## License
Public Domain. No copy write protection.

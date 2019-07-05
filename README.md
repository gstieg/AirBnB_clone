![AirBnB Clone - The Console](hbnb.png)

# **AirBnB Clone - The Console**

  * Holberton project making a clone of the AirBnB web application
  * The Console:
	* create your data model
	* manage (create, update, destroy, etc) objects via a console / command interpreter
	* store and persist objects to a file (JSON file)

# **Breakdown of the Console**

Each task is linked and will help you to:

     * put in place a parent class (called BaseModel) to take care of the
      initialization, serialization and deserialization of your future instances
     * create a simple flow of serialization/deserialization:
     Instance <-> Dictionary <-> JSON string <-> file
     * create all classes used for AirBnB (User, State, City, Place…) that
     inherit from BaseModel
     * create the first abstracted storage engine of the project: File storage.
     * create all unittests to validate all our classes and storage engine


# **Resources**

	* cmd module
	* packages
	* uuid module
	* datetime
	* unittest module
	* args/kwargs
	* Python test cheatsheet

# **General**

	* How to create a Python package
        * How to create a command interpreter in Python using the cmd module
        * What is Unit testing and how to implement it in a large project
        * How to serialize and deserialize a Class
        * How to write and read a JSON file
        * How to manage datetime
        * What is an UUID
        * What is *args and how to use it
        * What is **kwargs and how to use it
        * How to handle named arguments in a function

# **Command Interpreter**

This command interpreter has a few different uses including:

        * Create a new object (ex: a new User or a new Place)
        * Retrieve an object from a file, a database etc…
        * Do operations on objects (count, compute stats, etc…)
        * Update attributes of an object
        * Destroy an object


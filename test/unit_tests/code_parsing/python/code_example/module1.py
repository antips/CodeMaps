# Define a variable with unspecified type
module_variable_unspecified = None


# Define a function with type hinting
def module_function(parameter: str):
    print("This is a module-level function.")
    print("Parameter:", parameter)


# Define a class with attributes of different data types and type hinting
class ModuleClass:
    def __init__(self, name: str, age: int, city: str, salary: float, interests: list):
        self.name = name  # A string attribute
        self.age = age  # An integer attribute
        self.city = city  # A string attribute
        self.salary = salary  # A floating-point attribute
        self.interests = interests  # A list attribute

    def greet(self) -> str:
        return f"Hello, I'm {self.name} from {self.city}!"


# Define a custom class with an unspecified type attribute
class CustomClass:
    def __init__(self, data):
        self.data = data  # An attribute of unspecified type

    def display(self) -> str:
        return f"CustomClass data: {self.data}"


# You can include additional code below if needed.

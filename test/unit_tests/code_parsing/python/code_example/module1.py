"""Module that contains the most current Python symbols.
Used to test the CodeMapper program and extension.
"""

# Define a variable with unspecified type
MODULE_VARIABLE_UNSPECIFIED = None


# Define a function with type hinting
def module_function(parameter: str) -> None:
    """Module function

    Args:
        parameter (str): parameter
    """
    print("This is a module-level function.")
    print("Parameter:", parameter)


# Define a custom class with an unspecified type attribute
class CustomClass:
    """CustomClass docstring."""

    def __init__(self, data):
        self.data = data  # An attribute of unspecified type

    def display(self) -> str:
        """Displays the custom class data.

        Returns:
            str: the formatted data message.
        """
        message_to_display: str = f"CustomClass data: {self.data}"
        return message_to_display


# Define a class with attributes of different data types and type hinting
class ModuleClass:
    """ModuleClass docstring."""

    def __init__(
        self,
        name: str,
        age: int,
        city: str,
        salary: float,
        interests: list,
        custom_data: CustomClass,
    ):
        self.name = name  # A string attribute
        self.age = age  # An integer attribute
        self.city = city  # A string attribute
        self.salary = salary  # A floating-point attribute
        self.interests = interests  # A list attribute
        self.custom_data = custom_data

    def greet(self) -> str:
        """Greets in console.

        Returns:
            str: the greeting message
        """
        greeting: str = f"Hello, I'm {self.name} from {self.city}!"
        return greeting

    def print_custom_data(self) -> None:
        """Prints the custom data of its class"""
        display_message: str = self.custom_data.display()
        print(display_message)


# You can include additional code below if needed.

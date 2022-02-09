class MyClass:

    class_attribute = "my class attr"

    def __init__(self):
        self.attr = "instance attribute"

        print(f"{self.attr=}")
        print(f"{MyClass.class_attribute=}")

        # This shadows or hides the class attribute MyClass.class_attribute
        self.class_attribute = "another instance attribute"
        print(f"{self.class_attribute}")
        print(f"{MyClass.class_attribute=}")

mc = MyClass()
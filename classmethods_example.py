class Vehicle:

    @classmethod
    def create_empty(cls, name):
        return cls(name, veh_type="", contents=[])

    @classmethod
    def create_with_contents(cls, name, contents):
        return cls(name, veh_type="", contents=list(contents))

    def __init__(self, name: str, veh_type: str, contents: list):
        self.name = name
        self.veh_type = veh_type
        self.contents = contents

if __name__ == "__main__":
    v = Vehicle.create_empty(name="Car")
    print(f"{v.name=}")
    v2 = Vehicle.create_with_contents("Truck", {"boxes", "tools"})
    print(f"{v2.name= } {v2.contents=}")
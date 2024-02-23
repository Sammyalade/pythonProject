class Gun:
    def __init__(self, capacity: int, model: str, serial_no: str):
        self.gun_name = None
        self.capacity = capacity
        self.model = model
        self.manufacturer = "Femzy"
        self.serial_no = serial_no
        self.safety_indicator = True
        self.cock = False
        self.number_of_bullet_left = self.capacity

    def fire(self):
        fire_condition: bool = not self.safety_indicator and self.cock
        if self.safety_indicator:
            return "Safety indicator is engaged, cannot fire"
        elif not self.cock:
            return "Please cock before you shoot"
        elif self.number_of_bullet_left <= 0:
            return "Please reload before you fire"
        elif fire_condition:
            if self.number_of_bullet_left > 0:
                self.number_of_bullet_left -= 1
                return "One shot fired"

    def check_number_of_bullet_left(self):
        return self.number_of_bullet_left

    def reload(self):
        self.number_of_bullet_left = self.capacity
        return "Reloaded"

    def toggle_safety_indicator(self):
        self.safety_indicator = not self.safety_indicator

    def register_gun_name(self, owner):
        self.gun_name = owner

    def toggle_cock_gun(self):
        self.cock = not self.cock

    def __str__(self):
        return f'{self.model} - {self.serial_no} - {self.owner} - {self.manufacturer} - {self.capacity}'


if __name__ == "__main__":
    my_gun = Gun(30, "37878782", "832HFUYW7737")
    my_gun.toggle_cock_gun()
    print(my_gun.cock)
    my_gun.toggle_safety_indicator()
    print(my_gun.safety_indicator)
    my_gun.fire()
    print(my_gun.fire())
    print(my_gun.number_of_bullet_left)
    my_gun.reload()
    print(my_gun.reload())
    print(my_gun.number_of_bullet_left)
    print(my_gun.__str__())

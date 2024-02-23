from gun import Gun


class TestGun:
    def test_that_gun_can_fire(self):
        gun_capacity = 30
        my_gun = Gun(gun_capacity, "12345", "gayety377273278")

        my_gun.toggle_safety_indicator()
        my_gun.toggle_cock_gun()
        my_gun.fire()

        expected_capacity = 29
        assert my_gun.check_number_of_bullet_left() == expected_capacity

    def test_that_gun_cannot_fire_when_safety_is_on(self):
        gun_capacity = 30
        my_gun = Gun(gun_capacity, "12345", "gayety377273278")

        my_gun.toggle_cock_gun()
        my_gun.fire()

        expected_capacity = 30
        assert my_gun.check_number_of_bullet_left() == expected_capacity

    def test_that_gun_cannot_fire_when_gun_is_not_cocked(self):
        gun_capacity = 30
        my_gun = Gun(gun_capacity, "12345", "gayety377273278")

        my_gun.toggle_safety_indicator()
        my_gun.fire()

        expected_capacity = 30
        assert my_gun.check_number_of_bullet_left() == expected_capacity

    def test_that_gun_can_be_reloaded(self):
        gun_capacity = 30
        my_gun = Gun(gun_capacity, "12345", "gayety377273278")

        my_gun.toggle_safety_indicator()
        my_gun.toggle_cock_gun()
        my_gun.fire()
        my_gun.fire()
        assert my_gun.check_number_of_bullet_left() == 28
        my_gun.reload()

        expected_capacity = 30
        assert my_gun.check_number_of_bullet_left() == expected_capacity

    def test_that_gun_can_be_named(self):
        gun_capacity = 30
        my_gun = Gun(gun_capacity, "12345", "gayety377273278")
        my_gun.register_gun_name("AK47")

        assert my_gun.gun_name == "AK47"

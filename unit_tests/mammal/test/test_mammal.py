from unittest import main, TestCase
from mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_mammal_init(self):

        self.assertEqual('name',self.mammal.name)
        self.assertEqual('mammal_type', self.mammal.type)
        self.assertEqual('sound',self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_should_return_proper_string(self):
        make_sound = self.mammal.make_sound()
        self.assertEqual("name makes sound",make_sound)

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(),'animals')

    def test_info(self):
        self.assertEqual(self.mammal.info(),f"name is of type mammal_type")

if __name__ == "__main__":
    main()
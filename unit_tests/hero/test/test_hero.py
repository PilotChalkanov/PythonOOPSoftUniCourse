from unittest import main,TestCase
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Test', 10, 100, 10)
        self.enemy_hero = Hero('Babun', 5, 50, 5)

    def test_hero_init(self):
        self.assertEqual('Test', self.hero.username)
        self.assertEqual(10,self.hero.level)
        self.assertEqual(100,self.hero.health)
        self.assertEqual(10,self.hero.damage)

    def test_battle_raise_excep_when_enemy_name_is_equal_to_self_name(self):
        self.enemy_hero.username = 'Test'
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception) )

    def test_raise_excep_when_health_less_or_equal_to_zero(self):
        self.enemy_hero.username = 'Babun'
        self.hero.health = 0

        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_if_raise_excep_when_enemy_health_less_or_equal_zero(self):
        self.enemy_hero.health = 0
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(context.exception))

    def test_if_health_decreases(self):
        self.enemy_hero.health = 120
        self.hero.health = 100
        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, 75)

    def test_battle_if_draw(self):
        self.enemy_hero.damage = 10
        self.enemy_hero.level = 10
        self.assertEqual("Draw",self.hero.battle(self.enemy_hero))

    def test_if_hero_wins_the_battle(self):
        self.enemy_hero.level = 1
        self.enemy_hero.damage = 1
        self.enemy_hero.health = 50

        self.assertEqual("You win",self.hero.battle(self.enemy_hero))

    def test_if_health_damage_level_increase_after_won(self):
        self.enemy_hero.level = 1
        self.enemy_hero.damage = 1
        self.enemy_hero.health = 50
        self.hero.battle(self.enemy_hero)
        self.assertEqual(self.hero.health, 104)
        self.assertEqual(self.hero.damage,15)
        self.assertEqual(self.hero.level,11)

    def test_if_hero_loses_the_battle(self):
        self.hero.level = 1
        self.hero.damage =1
        self.enemy_hero.level = 10
        self.enemy_hero.damage = 10
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))

    def test_enemy_params_increase_if_enemy_wins(self):
        self.hero.level = 1
        self.hero.damage = 1
        self.enemy_hero.level = 10
        self.enemy_hero.damage = 10
        self.enemy_hero.health = 120
        self.hero.battle(self.enemy_hero)

        self.assertEqual(self.enemy_hero.level,11)
        self.assertEqual(self.enemy_hero.health,124)
        self.assertEqual(self.enemy_hero.damage,15)

    def test_if_str_repr_returns_correct(self):
        str_repr = str(self.hero)
        self.assertEqual(f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n",
                str_repr)


if __name__ == "__main__":
    main()
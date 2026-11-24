from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    username = "Hero"
    health = 50.6
    damage = 24.6
    level = 30

    def setUp(self) -> None:
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init_type(self):
        self.assertIsInstance(self.hero.username, str)
        self.assertIsInstance(self.hero.health, float)
        self.assertIsInstance(self.hero.damage, float)
        self.assertIsInstance(self.hero.level, int)

    def test_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(50.6, self.hero.health)
        self.assertEqual(24.6, self.hero.damage)
        self.assertEqual(30, self.hero.level)

    def test_battle_some_usernames(self):
        enemy = Hero("Hero", 1, 1, 1)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_without_health(self):
        enemy = Hero("Enemy", 1, 1, 1)

        with self.assertRaises(Exception) as ex:
            self.hero.health = 0
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.hero.health = -1
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_zero_health(self):
        enemy = Hero("Enemy", 1, 0, 1)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_battle_enemy_negative_health(self):
        enemy = Hero("Enemy", 1, -1, 1)

        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy = Hero("Enemy", 30, 50.6, 24.6 )
        result = self.hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_battle_hero_win(self):
        enemy = Hero("Enemy", 1, 1, 1)
        result = self.hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(54.6, self.hero.health)
        self.assertEqual(29.6, self.hero.damage)
        self.assertEqual(31, self.hero.level)

    def test_battle_hero_lose(self):
        self.hero.damage = 1
        enemy = Hero("Enemy", 100, 100, 100)
        result = self.hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(75, enemy.health)
        self.assertEqual(1, self.hero.damage)
        self.assertEqual(30, self.hero.level)

    def test_str(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected, str(self.hero))


if __name__ == "__main__":
    main()
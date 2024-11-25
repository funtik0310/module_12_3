import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
             return method(self, *args, **kwargs)
    return wrapper


class Runnertest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner_1 = Runner('Леша')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner_2 = Runner('Егор')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner_3 = Runner('Илья')
        runner_4 = Runner('Андрей')
        for i in range(10):
            runner_3.walk()
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)

if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @skip_if_frozen
    def setUp(self):
        self.usain = Runner("Усейн", 10)
        self.andrey = Runner("Андрей", 9)
        self.nick = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    @skip_if_frozen
    def test_usain_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @skip_if_frozen
    def test_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @skip_if_frozen
    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.andrey, self.usain, self.nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")


if __name__ == '__main__':
    unittest.main()
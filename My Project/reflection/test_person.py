from person import Person
from problem import Problem
from type import Type
import pytest


class TestPerson:
    def test_add_problem(self):
        my_person: Person = Person()
        my_person.add_problem(Problem("Money", Type.FINANCIAL))
        assert my_person.problem_list is not None

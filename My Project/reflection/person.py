from problem import Problem


class Person:
    def __init__(self):
        self.problem_list = []

    def add_problem(self, problem_to_add: Problem):
        self.problem_list.append(problem_to_add)

    def solve_problem(self, problem_to_solve):
        if problem_to_solve in self.problem_list:
            self.problem_list.remove(problem_to_solve)
            return "Problem solved"
        return "problem not in the list of problems"

    def display_problems(self):
        return self.problem_list


import constant
import itertools


def main(kol):
    project = []
    for index in range(2, int(kol) + 1):
        project.append(constant.set_book[str(index)])

    project = list(itertools.chain.from_iterable(project))
    return project

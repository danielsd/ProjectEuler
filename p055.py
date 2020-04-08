

def solve_problem_055():
    return sum(is_lychrel(i) for i in range(10_000))


def is_lychrel(number: int) -> bool:
    for _ in range(50):
        number = number + int(str(number)[::-1])

        if str(number) == str(number)[::-1]:
            return False

    return True

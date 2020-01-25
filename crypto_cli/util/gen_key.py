import click

# from pprint import pprint
import random


@click.command()
@click.argument("n", type=int)
def gen_command(n):
    result = gen_latin_square(n)
    for row in result:
        for cel in row:
            print(chr(cel + ord("a")), end="")
        print("")


def gen_latin_square(n: int) -> list:
    assert n > 0

    random.seed()

    square = [[-1 for _ in range(n)] for _ in range(n)]
    stack = [(0, 0, set())]

    while len(stack) <= n ** 2:
        top = stack[0]
        (row, col, tried) = top
        # print(f"{len(stack)} {top}")

        if not tried:
            unusable = set()
            # find unusable digits
            # in row
            for item in square[row]:
                if item >= 0:
                    unusable.add(item)
            # in col
            for idx in range(n):
                item = square[idx][col]
                if item >= 0:
                    unusable.add(item)

            tried.update(unusable)

        # list items havent tried
        to_try = []
        for i in range(n):
            if i not in tried:
                to_try.append(i)

        if to_try:
            # have item to be tried
            item_put = random.choice(to_try)
            square[row][col] = item_put
            tried.add(item_put)

            if row == col == (n - 1):
                # last cell, it's a success then
                break
            else:
                # not last cell, go to next cell
                next_row, next_col = row, col
                if col == (n - 1):
                    next_row += 1
                    next_col = 0
                else:
                    next_col += 1
                stack.insert(0, (next_row, next_col, set()))
        else:
            # no item could be tried
            # set current cell to -1
            # pop stack to backtrack
            square[row][col] = -1
            stack.pop(0)
            pass

    return square


if __name__ == "__main__":
    gen_command()

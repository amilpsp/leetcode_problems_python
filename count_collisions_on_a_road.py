#LINK TO PROBLEM -----> https://leetcode.com/problems/count-collisions-on-a-road/


def solution_to_learn_from(directions: str) -> int:
    return sum(d != 'S' for d in directions.lstrip('L').rstrip('R'))

# .lstrip('L') does the same as my whole first paragraph
# .rstrip('R') does the same as my whole second paragraph

    # Key factor I missed in my analysis =
    # all non 'S' intrinsically augment count by 1.
    # 'R' and 'L' being next to each other doesn't really matter.

def countCollisions(directions: str) -> int:
    if len(directions)<2:
        return 0
    # remove escaping cars from the left
    while directions.startswith('L'):
        directions = directions[1:]
    while directions.startswith('S'):
        if directions[1] == 'S':
            directions = directions[1:]
        elif directions[1] == 'R':
            directions = directions[1:]
        else:
            break

    # removing the escaping cars from the right
    while directions.endswith('R'):
        directions = directions[:-1]
    while directions.endswith('S'):
        if directions[-2] == 'S':  # Necesary?
            directions = directions[:-1]  # Necesary?
        elif directions[-2] == 'L':
            directions = directions[:-1]
        else:
            break

    if len(directions)<2:
        return 0


    count = 0
    for i, item in enumerate(directions):
        if i == len(directions) - 1:
            break
        if item == 'R':
            if directions[i + 1] == 'L':
                count += 2
                continue
            else:
                count += 1
                continue
        elif item == 'S':
            if directions[i + 1] == 'L':
                count += 1
                continue
            else:
                continue
        else:  # item is 'L'
            if directions[i + 1] == 'L':
                count += 1
                continue
            else:
                continue
    return count

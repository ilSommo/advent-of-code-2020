"""Day 4: Passport Processing"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

import string


def main():
    """Solve day 4 puzzles."""
    with open("inputs/day_4.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    passports = get_passports(puzzle_input)

    return sum(len(passport.keys() - {"cid"}) == 7 for passport in passports)


def star_2(puzzle_input):
    """Solve second puzzle."""
    passports = get_passports(puzzle_input)

    return sum(is_valid(passport) for passport in passports)


def get_passports(puzzle_input):
    """Get passports from input."""
    passports = [{}]

    for line in puzzle_input:
        if not line:
            passports.append({})

        else:
            for entry in line.split():
                passports[-1][entry.split(":")[0]] = entry.split(":")[1]

    return tuple(passports)


def check_byr(passport):
    """Check byr validity."""
    byr = passport["byr"]

    return byr.isdigit() and 1920 <= int(byr) <= 2002


def check_ecl(passport):
    """Check ecl validity."""
    ecl = passport["ecl"]

    return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def check_eyr(passport):
    """Check eyr validity."""
    eyr = passport["eyr"]

    return eyr.isdigit() and 2020 <= int(eyr) <= 2030


def check_hcl(passport):
    """Check hcl validity."""
    hcl = passport["hcl"]

    return hcl[0] == "#" and all(char in string.hexdigits for char in hcl[1:])


def check_hgt(passport):
    """Check hgt validity."""
    hgt = passport["hgt"]

    if not hgt[:-2].isdigit() or hgt[-2:] not in ("cm", "in"):
        return False

    if ("cm" in hgt and 150 <= int(hgt[:-2]) <= 193) or (
        "in" in hgt and 59 <= int(hgt[:-2]) <= 76
    ):
        return True

    return False


def check_iyr(passport):
    """Check iyr validity."""
    iyr = passport["iyr"]

    return iyr.isdigit() and 2010 <= int(iyr) <= 2020


def check_pid(passport):
    """Check pid validity."""
    pid = passport["pid"]

    return pid.isdigit() and len(pid) == 9


def is_valid(passport):
    """Check passport validity."""
    if len(passport.keys() - {"cid"}) != 7:
        return False

    return (
        check_byr(passport)
        and check_iyr(passport)
        and check_eyr(passport)
        and check_hgt(passport)
        and check_hcl(passport)
        and check_ecl(passport)
        and check_pid(passport)
    )


if __name__ == "__main__":
    main()

"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - It has blank lines that do not contain names.
# - Some names have leading spaces.
# - Capitalization is inconsistent: some names are lowercase, some uppercase, and some
#   have mixed-case surnames.
# - One surname has two parts ("van rossum"), so treating the final word as the whole
#   surname would split that name inconsistently.
#
# 1. In: one name per line in names.txt, with inconsistent spaces and capitalization.
# 2. Process, problem by problem:
#    - Skip blank lines because they are not name records.
#    - Strip spaces from both ends of every nonblank line.
#    - Convert each word to title case for consistent display and sorting.
#    - Treat the final word as the last name for sorting; keep the full cleaned name
#      together in the output. This convention sorts "Guido van Rossum" under Rossum.
# 3. Out: names_sorted.txt, one cleaned name per line, with no blank lines.
# 4. I use the last word as the last name because the file has no separate first-name
#    and last-name fields. This is a practical rule for this exercise; it does not
#    correctly represent every multiword surname.

from pathlib import Path

INPUT_FILE = Path(__file__).with_name("names.txt")
OUTPUT_FILE = Path(__file__).with_name("names_sorted.txt")


def main():
    names = []
    with INPUT_FILE.open("r", encoding="utf-8") as input_file:
        for line in input_file:
            cleaned_name = " ".join(line.split()).title()
            if cleaned_name:
                names.append(cleaned_name)

    names.sort(key=lambda name: (name.split()[-1].casefold(), name.casefold()))

    with OUTPUT_FILE.open("w", encoding="utf-8", newline="\n") as output_file:
        for name in names:
            output_file.write(name + "\n")

    print(f"Cleaned and sorted {len(names)} names into {OUTPUT_FILE.name}.")


if __name__ == "__main__":
    main()

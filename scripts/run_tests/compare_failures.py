# Run Tests
import sys


if __name__ == "__main__":
    failed = False
    with open(sys.argv[3], "w") as f_write:
        with open(sys.argv[2], "r") as f_main:
            main_failures = f_main.readlines()
            with open(sys.argv[1], "r") as f:
                for line in f:
                    if line not in main_failures:
                        f_write.write(line)

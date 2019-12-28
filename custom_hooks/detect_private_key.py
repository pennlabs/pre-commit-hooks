# Copied from https://github.com/pre-commit/pre-commit-hooks/blob/master/pre_commit_hooks/detect_private_key.py
import argparse
import sys


BLACKLIST = [
    b"BEGIN RSA PRIVATE KEY",
    b"BEGIN DSA PRIVATE KEY",
    b"BEGIN EC PRIVATE KEY",
    b"BEGIN OPENSSH PRIVATE KEY",
    b"BEGIN PRIVATE KEY",
    b"PuTTY-User-Key-File-2",
    b"BEGIN SSH2 ENCRYPTED PRIVATE KEY",
    b"BEGIN PGP PRIVATE KEY BLOCK",
]


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check")
    args = parser.parse_args(argv)

    private_key_files = []

    for filename in args.filenames:
        with open(filename, "rb") as f:
            content = f.read()
            if any(line in content for line in BLACKLIST):
                private_key_files.append(filename)

    if private_key_files:
        for private_key_file in private_key_files:
            print("Private key found: {}".format(private_key_file))
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())

from argparse import ArgumentParser, RawTextHelpFormatter

if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "path",
        metavar="path",
        type=str,
        help="Path of the file to be executed.",
    )
    args = parser.parse_args()

    exec(compile(open(args.path, "rb").read(), args.path, "exec"))

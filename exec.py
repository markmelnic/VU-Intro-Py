from argparse import ArgumentParser, RawTextHelpFormatter

if __name__ == "__main__":
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument(
        "module",
        metavar="Py assignment module",
        type=str,
        help="What module is the file located in.",
    )
    parser.add_argument(
        "folder",
        metavar="Py file folder",
        type=str,
        help="What folder is the file located in.",
    )
    parser.add_argument(
        "filename",
        metavar="Py filename",
        type=str,
        help="What file would you like to run.",
    )
    args = parser.parse_args()

    file_path = args.module + "/" + args.folder + "/" + args.filename
    exec(compile(open(file_path, "rb").read(), file_path, "exec"))

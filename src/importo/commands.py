def command_atual(args):
    pass


def add_atual(sub_parser):
    atual_parser = sub_parser.add_parser("atual", help="dispoe o ultimo estado disponivel.")
    atual_parser.set_defaults(command=command_atual)

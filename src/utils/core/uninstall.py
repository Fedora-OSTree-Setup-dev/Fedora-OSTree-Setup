def uninstall_apps(prog_arr: list[str]) -> list[list[str]]:
    """Uninstall preinstalled flatpak applications.

    Args:
        prog_arr -- list of apps to uninstall
        flatpak_cmd_list -- all commands related to flatpak

    Returns:
        An array of the appropriate uninstall commands
    """

    t_fcmd: list[list[str]] = []

    prog: str
    for prog in prog_arr:
        uninstall_cmd: list[str] = [
                "flatpak",
                "uninstall",
                prog,
                "--delete-data",
                "--system",
                "--assumeyes"
            ]
        t_fcmd.append(uninstall_cmd)

    return t_fcmd

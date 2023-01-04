def uninstall_apps(app_list: list[str]) -> list[list[str]]:
    """Uninstall preinstalled flatpak applications.

    Args:
        app_list -- list of apps to uninstall
        flatpak_cmd_list -- all commands related to flatpak

    Returns:
        An array of the appropriate uninstall commands
    """

    uninstall_cmds: list[list[str]] = []

    app: str
    for app in app_list:
        uninstall_cmd: list[str] = [
                "flatpak",
                "uninstall",
                app,
                "--delete-data",
                "--system",
                "--assumeyes"
            ]
        uninstall_cmds.append(uninstall_cmd)

    return uninstall_cmds

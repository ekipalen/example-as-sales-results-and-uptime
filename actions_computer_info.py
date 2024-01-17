"""
AI Action for getting the uptime of users computer. 
"""

import datetime
import platform
import re
import subprocess

from robocorp.actions import action


@action
def computer_info() -> str:
    """
    Get uptime information from users computer. Action takes no input arguments.

    Args:

    Returns:
        str: String containing computer uptime (how long it has been running).
    """
    os_name = platform.system()

    if os_name == "Windows":
        uptime = get_windows_uptime()

    elif os_name == "Darwin":
        uptime = get_macos_uptime()

    else:
        return "Unsupported Operating System"

    print(uptime)
    return uptime


def format_timedelta(td):
    days = td.days
    hours, remainder = divmod(td.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"


def get_windows_uptime():
    try:
        output = subprocess.check_output(
            "wmic os get lastbootuptime", shell=True
        ).decode()
        last_boot = re.search(r"(\d+)", output).group(0)

        last_boot_time = datetime.datetime.strptime(last_boot, "%Y%m%d%H%M%S")

        uptime = datetime.datetime.now() - last_boot_time
        uptime = format_timedelta(uptime)
        output = f"Your computer has been running for: '{uptime}'"
        return output
    except Exception as e:
        return f"Failed to get uptime: {str(e)}"


def get_macos_uptime():
    try:
        uptime_str = subprocess.check_output("uptime", shell=True).decode()
        output = f"Your computer uptime details: '{uptime_str}'"
        return output
    except Exception as e:
        return f"Failed to get uptime: {str(e)}"

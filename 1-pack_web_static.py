#!/usr/bin/python3
"""
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    """
    try:
        current_date = datetime.now().strftime("%Y%m%d%H%M%S")
        zipper = "versions/web_static_{}.tgz".format(current_date)
        local("sudo mkdir -p versions | sudo tar -cvzf {} web_static".format(
            zipper))
        return zipper
    except Exception:
        return None

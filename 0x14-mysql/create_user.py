#!/usr/bin/env python3
# To be ran on both web servers web-01 and web-02

import subprocess

# MySQL credentials
MYSQL_USER = "root"

# MySQL commands
MYSQL_COMMANDS = """
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
"""

# Execute MySQL commands using subprocess
try:
    subprocess.run(
        ["mysql", "-u", MYSQL_USER, "-p", "-e", MYSQL_COMMANDS],
        encoding="utf-8",
        check=True,
    )
    print("MySQL user 'holberton_user' created successfully.")
except subprocess.CalledProcessError as e:
    print("Error:", e)

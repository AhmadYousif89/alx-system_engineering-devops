#!/usr/bin/env python3
# To be ran on web-01 server

import subprocess

# MySQL credentials
MYSQL_USER = "root"

# MySQL commands
MYSQL_COMMANDS = """
CREATE USER 'replica_user'@'%' IDENTIFIED BY '';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
"""

# Execute MySQL commands using subprocess
try:
    subprocess.run(
        ["mysql", "-u", MYSQL_USER, "-p", "-e", MYSQL_COMMANDS],
        encoding="utf-8",
        check=True,
    )
    print("MySQL user 'replica_user' created successfully.")
except subprocess.CalledProcessError as e:
    print("Error:", e)

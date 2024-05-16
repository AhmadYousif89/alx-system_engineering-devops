#!/usr/bin/env python3
# To be ran on both web servers web-01 and web-02

import subprocess

# MySQL credentials
MYSQL_USER = "root"

# MySQL commands
MYSQL_COMMANDS = """
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    model VARCHAR(255),
    manufacture_date DATE
);
INSERT INTO nexus6 (name, model, manufacture_date) VALUES ('Nexus 6', 'Nexus', '2024-05-14');
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
"""

# Execute MySQL commands using subprocess
try:
    subprocess.run(
        ["mysql", "-u", MYSQL_USER, "-p", "-e", MYSQL_COMMANDS],
        encoding="utf-8",
        check=True,
    )
    print("MySQL DataBase 'tyrell_corp' created successfully.")
except subprocess.CalledProcessError as e:
    print("Error:", e)

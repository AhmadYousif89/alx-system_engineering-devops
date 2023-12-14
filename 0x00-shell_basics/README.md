# Shell Basics

This section covers fundamental shell scripts that introduce you to basic commands and operations in a Unix-like environment.

## Table of content:

**1. [Mandatory Scripts](#Mandatory-Scripts)**

**2. [Advanced Scripts](#Advanced-Scripts)**
<br>
<br>

### Mandatory Scripts:

<hr>

#### [0-current_working_directory](0-current_working_directory)

- This script prints the current working directory using the **`pwd`** command.

```bash
#!/bin/bash
pwd
```

#### [1-listit](1-listit)

- This script lists the contents of the current directory using the **`ls`** command.

```bash
#!/bin/bash
ls
```

#### [2-bring_me_home](2-bring_me_home)

- This script changes the current directory to the home directory using the **`cd`** command.

```bash
#!/bin/bash
cd
```

#### [3-listfiles](3-listfiles)

- This script lists the files in the current directory with detailed information using the **`ls -l`** command.

```bash
#!/bin/bash
ls -l
```

#### [4-listmorefiles](4-listmorefiles)

- This script lists all files (including hidden ones) in the current directory with detailed information using the **`ls -la`** command.

```bash
#!/bin/bash
ls -la
```

#### [5-listfilesdigitonly](5-listfilesdigitonly)

- This script lists the files in the current directory with numeric user and group IDs using the **`ls -an`** command.

```bash
#!/bin/bash
ls -an
```

#### [6-firstdirectory](6-firstdirectory)

- This script creates a directory named "my_first_directory" in the /tmp directory using the **`mkdir`** command.

```bash
#!/bin/bash
mkdir /tmp/my_first_directory
```

#### [7-movethatfile](7-movethatfile)

- This script moves a file named "betty" from /tmp to /tmp/my_first_directory using the **`mv`** command.

```bash
#!/bin/bash
mv /tmp/betty /tmp/my_first_directory
```

#### [8-firstdelete](8-firstdelete)

- This script deletes the file "betty" from /tmp/my_first_directory using the **`rm`** command.

```bash
#!/bin/bash
rm /tmp/my_first_directory/betty
```

#### [9-firstdirdeletionschool.mg](9-firstdirdeletionschool.mg)

- This script recursively deletes the entire directory /tmp/my_first_directory using the **`rm -r`** command.

```bash
#!/bin/bash
rm -r /tmp/my_first_directory
```

#### [10-back](10-back)

- This script changes the current directory to the previous directory using the **`cd -`** command.

```bash
#!/bin/bash
cd -
```

#### [11-lists](11-lists)

- This script lists files and directories in the current directory, parent directory, and /boot directory using the **`ls -al . .. /boot`** command.

```bash
#!/bin/bash
ls -al . .. /boot
```

#### [12-file_type](12-file_type)

- This script determines and displays the type of file "/tmp/iamafile" using the **`file`** command.

```bash
#!/bin/bash
file /tmp/iamafile
```

#### [13-symbolic_link](13-symbolic_link)

- This script creates a symbolic link named "\_\_ls\_\_" to the **/bin/ls** directory using the **`ln -s`** command.

```bash
#!/bin/bash
ln -s /bin/ls __ls__
```

#### [14-copy_htm](14-copy_htm)

- This script copies all HTML files in the current directory to the parent directory using the **`cp -u`** command.

```bash
#!/bin/bash
cp -u *.html ..
```

<br>
<br>

### Advanced Scripts

<hr>

#### [100-lets_move](100-lets_move)

- This script moves files starting with uppercase letters to the "/tmp/u" directory using the **`mv`** command.

```bash
#!/bin/bash
mv [[:upper:]]* /tmp/u
```

#### [101-clean_emacs](101-clean_emacs)

- This script removes all Emacs backup files (files ending with "~") in the current directory using the **`rm`** command.

```bash
#!/bin/bash
rm *~
```

#### [102-tree](102-tree)

- This script creates a directory structure "welcome/to/school" using the **`mkdir -p`** command.

```bash
#!/bin/bash
mkdir -p welcome/to/school
```

#### [103-commas](103-commas)

- This script lists the files in the current directory in comma format, including hidden files, using the **`ls -ap --format`** command with specific options.

```bash
#!/bin/bash
ls -ap --format=comma
```

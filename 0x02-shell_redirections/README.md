# Shell Redirections

This section provides a collection of basic and advanced shell scripts for performing various file and text manipulations using redirections in an Ubuntu Linux system.

## Table of contents:

**1. [Mandatory Scripts](#Mandatory-Scripts)**

**2. [Advanced Scripts](#Advanced-Scripts)**
<br>
<br>

### Mandatory Scripts:

<hr>

#### [0-hello_world](0-hello_world)

- This script output the classic "Hello, World" message using the **`echo`** command.

```bash
#!/bin/bash
echo "Hello, World"
```

#### [1-confused_smiley](1-confused_smiley)

- This script print a confused smiley face using the **`echo`** command.

```bash
#!/bin/bash
echo "\"(Ôo)'"
```

#### [2-hellofile](2-hellofile)

- This script display the contents of the /etc/passwd file using the **`cat`** command.

```bash
#!/bin/bash
cat /etc/passwd
```

#### [3-twofiles](3-twofiles)

- This script concatenate the contents of /etc/passwd and /etc/hosts files using the **`cat`** command.

```bash
#!/bin/bash
cat /etc/passwd /etc/hosts
```

#### [4-lastlines](4-lastlines)

- This script print the last 10 lines of the /etc/passwd file using the **`cat | tail`** command with the arg **`-n`**.

```bash
#!/bin/bash
cat /etc/passwd | tail -n 10
```

#### [5-firstlines](5-firstlines)

- This script display the first lines of the /etc/passwd file using the **`cat | head`** commands.

```bash
#!/bin/bash
cat /etc/passwd | head
```

#### [6-third_line](6-third_line)

- This script output the third line from the file named "iacta. using the **`cat | head | tail`** commands with the arg **`-n`**.

```bash
#!/bin/bash
cat iacta | head -n 3 | tail -n 1
```

#### [7-file](7-file)

- This script create a file named **`"*\"'"Best School"\'"\*$\?\*\*\*\*\*:)"`** with the content "Best School" using the **`echo`** command and the STDOUT redirect flag **`>`**.

```bash
#!/bin/bash
echo "Best School" > \\\*\\\\"'\"Best School\"\\'"\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)
```

#### [8-cwd_state](8-cwd_state)

- This script list the detailed contents of the current directory and saves it to a file named "ls_cwd_content" using the **`ls`** command with the args **`-la`** and the STDOUT redirect flag **`>`**.

```bash
#!/bin/bash
ls -la > ls_cwd_content
```

#### [9-duplicate_last_line](9-duplicate_last_line)

- This script append the last line of the "iacta" file to the end of the same file using the **`tail >>`** commands and with the args **`-n 1`** and the STDOUT redirect flag **`>>`**.

```bash
#!/bin/bash
tail -n 1 iacta >> iacta
```

#### [10-no_more_js](10-no_more_js)

- This script delete all files with a ".js" extension in the current directory and its subdirectories using the **`find`** command and some specific flags.

```bash
#!/bin/bash
find . -type f -name '*.js' -delete
```

#### [11-directories](11-directories)

- This script count and prints the number of directories in the current directory using the **`find | wc`** commands and some specific flags.

```bash
#!/bin/bash
find . -mindepth 1 -type d -print | wc -l
```

#### [12-newest_files](12-newest_files)

- This script list the names of the newest files in the current directory. using the **`ls | head`** command and the **`-cflag `**.

```bash
#!/bin/bash
ls -c | head
```

#### [13-unique](13-unique)

- This script sort and outputs unique lines from standard input using the **`sort | uniq`** commands and the **`-uflag `**.

```bash
#!/bin/bash
sort | uniq -u
```

#### [14-findthatword](14-findthatword)

- This script searche for lines containing the word "root" in the /etc/passwd file using the **`cat | grep`** commands.

```bash
#!/bin/bash
cat /etc/passwd | grep "root"
```

#### [15-countthatword](15-countthatword)

- This script count and prints the number of lines containing the word "bin" in the /etc/passwd file using the **`cat | grep | wc`** commands.

```bash
#!/bin/bash
cat /etc/passwd | grep "bin" | wc -l
```

#### [16-whatsnext](16-whatsnext)

- This script display three lines after each line containing the word "root" in the /etc/passwd file using the **`grep`** command with the args **`-A 3`**.

```bash
#!/bin/bash
grep -A 3 root /etc/passwd
```

#### [17-hidethisword](17-hidethisword)

- This script exclude lines containing the word "bin" from the /etc/passwd file using the **`grep`** command with the **`-vflag `**.

```bash
#!/bin/bash
grep -v bin /etc/passwd
```

#### [18-letteronly](18-letteronly)

- This script print lines from the /etc/ssh/sshd_config file that start with an alphabet letter using Regex and the **`grep`** command.

```bash
#!/bin/bash
grep ^[[:alpha:]] /etc/ssh/sshd_config
```

#### [19-AZ](19-AZ)

- This script translate characters 'A' and 'C' to 'Z' and 'E,' respectively using the **`tr`** command.

```bash
#!/bin/bash
tr [A,c] [Z,e]
```

#### [20-hiago](20-hiago)

- This script remove occurrences of the characters 'C' and 'c' from the input using the **`tr`** command with the **`-dflag `**.

```bash
#!/bin/bash
tr -d [C,c]
```

#### [21-reverse](21-reverse)

- This script reverse the input lines using the **`rev`** command.

```bash
#!/bin/bash
rev
```

#### [22-users_and_homes](22-users_and_homes)

- This script extract and sorts user names and home directories from the /etc/passwd file using the **`cut | sort`** commands with some specific flags.

```bash
#!/bin/bash
cut -d ":" -f 1,6 /etc/passwd | sort
```

<br>
<br>

### Advanced Scripts:

<hr>

#### [100-empty_casks](100-empty_casks)

- This script find and list the names of empty files or directories in the current directory.

```bash
#!/bin/bash
find -empty | rev | cut -d / -f 1 | rev
```

#### [101-gifs](101-gifs)

- This script find and list the unique names (excluding extensions) of all GIF files in the current directory.

```bash
#!/bin/bash
find -name "*.gif" -type f -printf "%f\n" | rev | cut -d . -f 2- | rev | LC_ALL=C sort -f
```

#### [102-acrostic](102-acrostic)

- This script create an acrostic from the first character of each line in the input.

```bash
#!/bin/bash
cut -c 1 | paste -s -d ""
```

#### [103-the_biggest_fan](103-the_biggest_fan)

- This script analyze a log data to output the user the most occurrences, excluding the first line.

```bash
#!/bin/bash
tail -n +2 | cut -f1 | sort | uniq -c | sort -nrk 1 | head -11 | tr -s " " | cut -d " " -f3
```

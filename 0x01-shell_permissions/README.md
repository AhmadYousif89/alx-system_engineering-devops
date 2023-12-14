# Shell Permissions

This section focuses on shell scripts related to file and directory permissions in Unix-like systems.

## Table of content:

**1. [Mandatory Scripts](#Mandatory-Scripts)**

**2. [Advanced Scripts](#Advanced-Scripts)**
<br>
<br>

### Mandatory Scripts:

<hr>

#### [0-iam_betty](0-iam_betty)

This script switches the current user to "betty" using the **`su`** command.

```bash
#!/bin/bash
su betty
```

#### [1-who_am_i](1-who_am_i)

- This script prints the current username using the **`whoami`** command.

```bash
#!/bin/bash
whoami
```

#### [2-groups](2-groups)

- This script displays the groups to which the current user belongs using the **`groups`** command.

```bash
#!/bin/bash
groups
```

#### [3-new_owner](3-new_owner)

- This script changes the owner of the file "hello" to "betty" using the **`sudo chown`** command.

```bash
#!/bin/bash
sudo chown betty hello
```

#### [4-empty](4-empty)

- This script creates an empty file named "hello" using the **`touch`** command.

```bash
###
#!/bin/bash
touch hello
```

#### [5-execute](5-execute)

- This script adds execute permission for the owner of the file "hello" using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod u+x hello
```

#### [6-multiple_permissions](6-multiple_permissions)

- This script sets specific permissions (754) for the file "hello" using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod 754 hello
```

#### [7-everybody](7-everybody)

- This script grants execute permission to everyone for the file "hello" using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod ugo+x hello
```

#### [8-James_Bond](8-James_Bond)

- This script sets specific permissions (007) for the file "hello" using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod 007 hello
```

#### [9-John_Doe](9-John_Doe)

- This script sets specific permissions (753) for the file "hello" using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod 753 hello
```

#### [10-mirror_permissions](10-mirror_permissions)

- This script copies permissions from the file "olleh" to "hello" using the **`sudo chmod --reference`** command.

```bash
#!/bin/bash
sudo chmod --reference=olleh hello
```

#### [11-directories_permissions](11-directories_permissions)

- This script adds execute permissions to all files and directories in the current directory using the **`sudo chmod`** command.

```bash
#!/bin/bash
sudo chmod +X *
```

#### [12-directory_permissions](12-directory_permissions)

- This script creates a directory named "my_dir" with specific permissions (751) using the mkdir **`--mode`** command.

```bash
#!/bin/bash
mkdir --mode=751 my_dir
```

#### [13-change_group](13-change_group)

- This script changes the group of the file "hello" to "school" using the **`sudo chgrp`** command.

```bash
#!/bin/bash
sudo chgrp school hello
```

<br>
<br>

### Advanced Scripts:

<hr>

#### [100-change_owner_and_group](100-change_owner_and_group)

- This script changes the owner to "vincent" and the group to "staff" for all files in the current directory using the **`sudo chown`** command.

```bash
#!/bin/bash
sudo chown vincent:staff *
```

#### [101-symbolic_link_permissions](101-symbolic_link_permissions)

- This script changes the owner and group of the symbolic link "\_hello" to "vincent:staff" using the chown **`-h`** command.

```bash
#!/bin/bash
chown -h vincent:staff _hello
```

#### [102-if_only](102-if_only)

- This script changes the owner of the file "hello" from "guillaume" to "betty" using the sudo chown **`--from`** command.

```bash
#!/bin/bash
suo chown --from=guillaume betty hello
```

#### [103-Star_Wars](103-Star_Wars)

- This script plays an ASCII Star Wars episode in the terminal using the telnet command.

```bash
#!/bin/bash
telnet towel.blinkenlights.nl
```

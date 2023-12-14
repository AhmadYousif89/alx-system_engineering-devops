# Shell Variables Expansions

This section provides a collection of shell scripts that demonstrate various aspects of variable expansions and manipulations in UNIX like systems.

## Table of contents:

**1. [Mandatory Scripts](#Mandatory-Scripts)**

**2. [Advanced Scripts](#Advanced-Scripts)**
<br>
<br>

### Mandatory Scripts:

<hr>

#### [0-alias](0-alias)

- This script create an alias named **`ls`** using the **`alias`** command to forcefully remove all files.

```bash
#!/bin/bash
alias ls='rm *'
```

#### [1-hello_you](1-hello_you)

- This script print a personalized greeting using the **`echo`** command and the **`USER`** environment variable.

```bash
#!/bin/bash
echo "hello $USER"
```

#### [2-path](2-path)

- This script append a new directory "/action" to the **`PATH`** environment variable using the **`export`** command.

```bash
#!/bin/bash
export PATH="$PATH:/action"
```

#### [3-paths](3-paths)

- This script display the number of directories in the **`PATH`** environment variable using the **`echo | tr | wc`** commands.

```bash
#!/bin/bash
echo "$PATH" | tr ":" "\n" | wc -l
```

#### [4-global_variables](4-global_variables)

- This script print all global environment variables using the **`env`** command.

```bash
#!/bin/bash
env
```

#### [5-local_variables](5-local_variables)

- This script print all local environment variables using the **`set`** command.

```bash
#!/bin/bash
set
```

#### [6-create_local_variable](6-create_local_variable)

- This script create a local variable named **`BEST`** with the value **`School`**.

```bash
#!/bin/bash
BEST=School
```

#### [7-create_global_variable](7-create_global_variable)

- This script create a global variable named **`BEST`** with the value **`School`** using the **`export`** command.

```bash
#!/bin/bash
export BEST=School
```

#### [8-true_knowledge](8-true_knowledge)

- This script perform arithmetic expansion and echoes the result of summing the value of the environment variable **`TRUEKNOWLEDGE`** and the number **`128`**.

```bash
#!/bin/bash
echo $((128+($TRUEKNOWLEDGE)))
```

#### [9-divide_and_rul](9-divide_and_rul)

- This script perform arithmetic expansion and echoes the result of dividing the values of the environment variables **`POWER`** by **`DIVIDE`**.

```bash
#!/bin/bash
echo $(($POWER/$DIVIDE))
```

#### [10-love_exponent_breath](10-love_exponent_breath)

- This script perform arithmetic expansion and echoes the result of raising the value of **`BREATH`** to the power of the value of **`LOVE`**.

```bash
#!/bin/bash
echo $(($BREATH**$LOVE))
```

#### [11-binary_to_decimal](11-binary_to_decimal)

- This script convert a binary number (stored in env named **`BINARY`**) to decimal and echoes the result.

```bash
#!/bin/bash
echo $((2#$BINARY))
```

#### [12-combinations](12-combinations)

- This script print combinations of letters **`a to z`**, excluding those containing **`oo`**.

```bash
#!/bin/bash
echo {a..z}{a..z} | tr ' ' '\n' | grep -v 'oo'
```

#### [13-print_float](13-print_float)

- This script print the value of the env **`NUM`** formatted as a floating-point number with two decimal places.

```bash
#!/bin/bash
printf "%.2f\n" $NUM
```

<br>
<br>

### Advanced Scripts:

<hr>

#### [100-decimal_to_hexadecimal](100-decimal_to_hexadecimal)

- This script convert a decimal number (stored in the env **`DECIMAL`**) to hexadecimal and prints the result using the **`printf`** command.

```bash
#!/bin/bash
printf "%x\n" $DECIMAL
```

#### [101-rot13](101-rot13)

- This script applie the **`ROT13`** transformation to some input text usint the **`tr`** command.

```bash
#!/bin/bash
tr a-zA-Z n-za-mN-ZA-M
```

#### [102-odd](102-odd)

- This script print the first field of each line in a given text, assuming the input is in pairs, separated by a comma using the commands **`paste | cut`** with some specific flags.

```bash
#!/bin/bash
paste -d, - - | cut -d, -f1
```

#### [103-water_and_stir](103-water_and_stir)

- This script convert the value of the env variables **`WATER`** and **`STIR`** to octal, adds them, and then converts the result back to text.

```bash
#!/bin/bash
printf "%o\n" $(( $((5#$(echo $WATER | tr water 01234))) + $((5#$(echo $STIR | tr stir. 01234))) )) | tr 01234567 bestchol
```

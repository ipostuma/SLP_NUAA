# BASH scripting

By the end of this hands-on class, you will be able to:

* Understand the basics of Bash scripting
* Write simple Bash scripts
* Use Bash scripts to manage big data
* Perform simple image manipulation

## Basic Bash syntax

### Variables

In Bash, you can declare variables without specifying a data type. Variables can store various types of data, such as strings, numbers, or arrays. To assign a value to a variable, you use the `=` operator with no spaces on either side. For example: `variable_name=value`. To access the value stored in a variable, you prefix the variable name with a `$` symbol, like this: `$variable_name`. Variable names are case-sensitive and can consist of letters, numbers, and underscores but must start with a letter.

```
name="John"
age=30
echo "$name is $age years old"
```

### Control flow structures

Bash supports various control flow structures, including if, else, elif, for, while, and case. if statements are used for conditional branching. for and while loops allow you to perform repetitive tasks.

#### if

```
if [ condition ]; then
    # code to execute if the condition is true
else
    # code to execute if the condition is false
fi
```

#### for

```
for i in {1..5}; do
    echo "Iteration $i"
done
```

### Functions

Functions in Bash are defined using the function keyword or simply by providing a name and parentheses. Functions can take parameters and return values.

```
function greet {
    echo "Hello, $1!"
}
```

using the function:

```
greet "Alice"
```

### Input and Output

Bash scripts can read input from users or files and display output. The `read` command is used to read user input. 

```
echo "What's your name?"
read name
```

Standard input (stdin) can be redirected using `<`, and standard output (stdout) can be redirected using `>`.


```
echo "Hello, world!" > output.txt
```

You can also use pipes (|) to pass output from one command to another.

```
command1 | command2
```

### Command-line arguments

In Bash scripting, you can use command-line arguments to pass information to your script when you run it. These arguments allow you to customize the behavior of your script without modifying its code. Command-line arguments are accessed in your Bash script using special variables:

* **$0**: The name of the script itself.
* **$1**, **$2**, **$3**, ...: Represent the first, second, third, and so on, arguments passed to the script.
* **$#**: represents the number of arguments passed to the script.
* **$@** represents all arguments as a list.

For example, if you run your script with `./myscript.sh arg1 arg2`, then:

* **$0** will be `./myscript.sh`.
* **$1** will be `arg1`.
* **$2** will be `arg2`.

#### Optional Arguments with getopts

If you want to implement more complex argument parsing, especially for scripts that require optional flags and values, you can use the getopts command. Here's a simplified example:

```
#!/bin/bash
# This script demonstrates the use of getopts for parsing options

while getopts ":a:b:" opt; do
case $opt in
    a) arg_a="$OPTARG";;
    b) arg_b="$OPTARG";;
    \?) echo "Invalid option: -$OPTARG" >&2;;
esac
done

echo "Option a: $arg_a"
echo "Option b: $arg_b"
```

In this script, you define the options you expect (in this case, -a and -b) and their corresponding arguments. Then, the getopts loop processes these options and assigns their values to variables.

Example usage: `./options_demo.sh -a value1 -b value2`.

Using command-line arguments in your Bash scripts allows you to make your scripts more flexible and versatile by providing different input parameters without modifying the script's code.

### Special parenthesis

#### `(( ))` in Bash
The `(( ))` syntax in Bash is used for arithmetic evaluation on integers. It allows you to perform arithmetic operations and logical comparisons within a script. Inside `(( ))`, variables can be used without the `$` prefix.

##### Key Features:
1. **Arithmetic Operations**: You can perform addition, subtraction, multiplication, division, and modulus operations.
2. **Increment and Decrement**: You can use `++` and `--` operators.
3. **Logical Comparisons**: You can perform comparisons like `<`, `<=`, `>`, `>=`, `==`, and `!=`.
4. **Exit Status**: The `(( ))` construct returns an exit status of 0 (true) if the expression evaluates to a non-zero value, and 1 (false) otherwise.

##### Example:
```bash
#!/bin/bash

a=5
b=3

# Arithmetic operations
(( sum = a + b ))
echo "Sum: $sum"  # Output: Sum: 8

# Increment and decrement
(( a++ ))
echo "Incremented a: $a"  # Output: Incremented a: 6

(( b-- ))
echo "Decremented b: $b"  # Output: Decremented b: 2

# Logical comparison
if (( a > b )); then
    echo "a is greater than b"
else
    echo "a is not greater than b"
fi
# Output: a is greater than b
```

#### `$()` in Bash
The `$()` syntax in Bash is used for command substitution. It allows you to capture the output of a command and use it as part of another command or assign it to a variable. The output is executed in a subshell and returned as a string.

##### Key Features:
1. **Command Execution**: Executes the command inside the parentheses and captures its output.
2. **Nesting**: You can nest command substitutions.
3. **Cleaner Syntax**: Preferred over the older backticks (``) for readability and ease of nesting.

##### Example:
```bash
#!/bin/bash

# Command substitution
current_date=$(date)
echo "Current date and time: $current_date"  # Output: Current date and time: (current date and time)

# Using command substitution in another command
files_list=$(ls)
echo "Files in the current directory: $files_list"

# Nested command substitution
nested_output=$(echo "Today's date is $(date +%F)")
echo "$nested_output"  # Output: Today's date is (current date in YYYY-MM-DD format)
```

#### Summary:
- **`(( ))`**: Used for arithmetic evaluation and logical comparisons. It evaluates the expression and can be used for both calculations and conditional statements.
- **`$()`**: Used for command substitution. It captures the output of a command and can be used within another command or assigned to a variable.

### Exercises

Start by opening a text editor of your choice, such as nano, vim, or gedit. Use the following script:

```
#!/bin/bash
# This is a simple Bash script to compare two numbers

num1=10
num2=20

if [ $num1 -eq $num2 ]; then
    echo "Both numbers are equal."
elif [ $num1 -lt $num2 ]; then
    echo "$num1 is less than $num2."
else
    echo "$num1 is greater than $num2."
fi
```

Once it is clear how the script works, modify it so that:

* num1 and num2 are passed through arguments;
* find a way to check if the arguments are numbers.

<details>
  <summary>Answer</summary>

```
#!/bin/bash
# This is a simple Bash script to compare two numbers

is_number() {
    [[ $1 =~ ^-?[0-9]+([.][0-9]+)?$ ]]
}

arg1=$1
arg2=$2

if is_number "$arg1" && is_number "$arg2"; then
    echo "Both arguments are numbers."
else
    echo "One or both arguments are not numbers."
    exit 1
fi

if [ $num1 -eq $num2 ]; then
    echo "Both numbers are equal."
elif [ $num1 -lt $num2 ]; then
    echo "$num1 is less than $num2."
else
    echo "$num1 is greater than $num2."
fi
```

</details>

## Backup script

Go through the `backup_script.sh` file. Try to understand each line of code. With `echo` you can print the state of a variable at a certain line of code, by printing this information you may better understand what is happening during the execution of the code.

Once you went through the code, try to understand:

* What would happen if the output\_folder does not exist ?
* Can you compress the current folder and save the result in it ?
    * why ?
* how to add a new option to define the output file name which overwrites the default name.
* how to use getopts.

<details>
  <summary>Answer</summary>

```
#!/bin/bash

# Function to display help message
display_help() {
    echo "Usage: $0 [-o OUTPUT_FOLDER] [-i FILE_NAME] [-h] FOLDER_OR_FILE_TO_BACKUP"
    echo "Options:"
    echo "  -o OUTPUT_FOLDER  Specify the output folder for the backup. If not provided, the backup will be saved in the current folder."
    echo "  -i FILE_NAME      Specify the name of the compressed backup file. When used, the date will not be appended."
    echo "  -h                Display this help message."
    exit 1
}

# Initialize variables with default values
output_folder="."
use_date=true
backup_name=""

# Parse command-line options
while getopts "o:i:h" opt; do
    case $opt in
        o)
            output_folder="$OPTARG"
            ;;
        i)
            use_date=false
            backup_name="$OPTARG"
            ;;
        h)
            display_help
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            display_help
            ;;
    esac
done

# Shift the options so that "$1" is now the first non-option argument (the source path)
shift "$((OPTIND-1))"

# Check if a source path is provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a folder or file to backup."
    display_help
fi

# Check if the source path exists
source_path="$1"
if [ ! -e "$source_path" ]; then
    echo "Error: The specified source folder or file does not exist."
    exit 1
fi

# Check if output path exists
if [ ! -e "$output_folder" ]; then
    echo "Error: The specified outpu folder"
    exit 2
fi

# Determine the backup file name
if [ "$use_date" = true ]; then
    date_today=$(date +%Y%m%d)
    backup_name="backup_$date_today.tar.gz"
fi

# Create the backup
backup_path="$output_folder/$backup_name"
tar -czvf "$backup_path" "$source_path"

echo "Backup completed. The backup is saved as $backup_path"
```

</details>

## Data analysis

The Iris dataset is one of the most well-known and frequently used datasets in machine learning and statistics. It's commonly used for classification and clustering tasks and is included in the scikit-learn library in Python. The dataset consists of measurements of various features of iris flowers and their corresponding species labels. 

The Iris dataset contains data from three different species of iris flowers: Setosa, Versicolor, and Virginica. There are typically 150 samples in the dataset, with 50 samples from each of the three species. The following features are available:

*   Sepal Length (cm): The length of the iris flower's sepal (the outermost part of the flower).
*   Sepal Width (cm): The width of the iris flower's sepal.
*   Petal Length (cm): The length of the iris flower's petal (the inner part of the flower).
*   Petal Width (cm): The width of the iris flower's petal.

Download the data by using wget:

```
wget https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data
```

#### Exercise

* use gnuplot to plot sepal length and width (first two columns) of the three iris types: Setosa, Versicolor, and Virginica. Each type has to have its own maker
* compute mean and standard deviation for each of the four features.

<details>
  <summary>TIP</summary>

GNUPLOT provides a command-line interface for generating 2D and 3D plots of data. Here are some key features and characteristics of Gnuplot:

1. Plot Types: Gnuplot supports a wide range of plot types, including line plots, scatter plots, bar charts, histograms, contour plots, and 3D surface plots. This flexibility allows users to visualize data in various ways.

2. Data Sources: Gnuplot can read data from various sources, such as plain text files, CSV files, and even directly from calculations and functions. This makes it adaptable to a variety of data formats.

3. Scripting Language: Gnuplot uses its own scripting language to create plots. Users write scripts that specify data sources, plot types, labels, titles, axis settings, and other plot attributes. This scripting language allows for fine-grained control over plot customization.

4. Interactive and Non-Interactive Mode: Gnuplot can be used both interactively, where users enter commands and see plots immediately, and in non-interactive mode, where scripts are executed to generate plots without user intervention. This makes it suitable for automated data analysis and report generation.

5. Platform Compatibility: Gnuplot is platform-independent and can run on various operating systems, including Linux, macOS, and Windows.

6. Extensibility: Gnuplot can be extended and customized through the use of external scripts and plugins. Users can enhance its capabilities to suit specific requirements.

7. Output Formats: Gnuplot supports a wide range of output formats for saving plots, including PNG, JPEG, PDF, SVG, PostScript, and more. This makes it suitable for including plots in documents, presentations, and publications.

8. Integration: Gnuplot can be integrated with other tools and programming languages, such as Python, MATLAB, and LaTeX, allowing users to embed plots within larger workflows and documents.

9. Community and Documentation: Gnuplot has an active user community and extensive documentation, including manuals and tutorials, making it accessible to both beginners and experienced users.

10. Licensing: Gnuplot is distributed under an open-source license (GPL), which means it is free to use, modify, and distribute.

There is a gnuplot script example `iris.gpl` which can be used by:

```
gnuplot -p -e "setosa='setosa.csv'" -e "versicolor='versicolor.csv'" -e "virginica='virginica.csv'" iris.gpl 
```

</details>

<details>
  <summary>ANSWER</summary>

```
#!/bin/bash

# Split the dataset into three files, one for each iris type
cat iris.csv| grep "Iris-setosa" > setosa.csv
cat iris.csv| grep "Iris-versicolor" > versicolor.csv
cat iris.csv| grep "Iris-virginica" > virginica.csv

# Plot the sepal length and width of each iris type
gnuplot -p -e "setosa='setosa.csv'" -e "versicolor='versicolor.csv'" -e "virginica='virginica.csv'" iris.gpl

# to ensure that awk reads decimals correctly
LC_NUMERIC=en_US.UTF-8

# Compute the mean and standard deviation for all available columns for each iris type
for iris_type in setosa versicolor virginica; do
  echo "Iris type: $iris_type"
  echo "----------"

  # Compute the mean and standard deviation for each column
  for column in 1 2 3 4; do
    mean=$(awk -F, '{sum+=$'$column'; count++} END {print sum / count}' "$iris_type".csv)
    standard_deviation=$(awk -F, '{sum_of_squares+=($'$column' - '$mean')^2; count++} END {print sqrt(sum_of_squares / (count - 1))}' "$iris_type".csv)

    echo "Column $column: mean = $mean, standard deviation = $standard_deviation"
  done
   echo ""
done
```

</details>

## Writing Bash Scripts for Image Processing

To automate image processing tasks, you can write Bash scripts that use ImageMagick commands. Here's a simple example of a Bash script that resizes a batch of images in a directory:

```
#!/bin/bash

# Specify the input and output directories
input_dir="input_images"
output_dir="output_images"

# Create the output directory if it doesn't exist
mkdir -p "$output_dir"

# Loop through all files in the input directory
for file in "$input_dir"/*; do
    # Get the file name without the path
    filename=$(basename "$file")
    
    # Resize each image to a specified dimension
    convert "$file" -resize 800x600 "$output_dir/$filename"
done

echo "Image processing complete."
```

Make sure to make this script executable with chmod +x script_name.sh, and then you can run it to resize all images in the input_images directory and save the resized images in the output_images directory.

This is a simple example, but you can create more complex Bash scripts for various image processing tasks by combining ImageMagick commands with loops, conditionals, and other features of Bash scripting.

A more advance use of ImageMagick can be done by creating a custom kernel (filter) in a text file and then use the `-convolve `option to apply this kernel to an image. To do this create a text file, e.g., `custom_kernel.txt`, and define your custom convolutional kernel inside it. The kernel should be a matrix of numbers separated by spaces or tabs. For example, a simple 3x3 kernel with all 1s and 0s might look like this:

```
1 0 1
0 1 0
1 0 1
```

This kernel can be used for simple edge detection. Now use the `convert`` command along with the `-convolve`` option to apply the custom kernel to an image. Here's the command:

```
convert input.jpg -define convolve:scale='!' -convolve `cat custom_kernel.txt` output.jpg
```

* `input.jpg` is the input image you want to process.
* `-define convolve:scale='!'` is used to ensure that the kernel is applied without any scaling.
* `-convolve` specifies the convolution operation.
* `cat custom_kernel.txt` reads the kernel from the custom_kernel.txt file.
* `output.jpg` is the resulting image.

This command will apply your custom convolutional filter to the input image and save the result as output.jpg.

You can create various custom kernels with different patterns of 1s and 0s to achieve different image processing effects, such as blurring, sharpening, or edge detection. The flexibility of ImageMagick allows you to experiment and create custom filters to suit your specific image processing needs.

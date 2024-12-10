#!/bin/bash

# Function to list all files in the current directory
list_files() {
    echo "Listing all files in the present working directory:"
    ls -l
}

# Function to display today's date and time
display_date_time() {
    echo "Today's date and time: $(date)"
}

# Function to check if a file is a directory or a regular file
check_file_type() {
    read -p "Enter the file name to check: " filename
    if [ -d "$filename" ]; then
        echo "$filename is a directory."
    elif [ -f "$filename" ]; then
        echo "$filename is a regular file."
    else
        echo "$filename does not exist or is not a valid file."
    fi
}

# Function to create a backup of a file using tar
create_backup() {
    read -p "Enter the file name to backup: " filename
    if [ -f "$filename" ]; then
        tar -cvf "${filename}.tar" "$filename"
        echo "Backup of $filename created as ${filename}.tar"
    else
        echo "File $filename not found."
    fi
}

# Function to compress the tar file
compress_tar() {
    read -p "Enter the tar file name to compress: " tarfile
    if [ -f "$tarfile" ]; then
        gzip "$tarfile"
        echo "Compressed $tarfile to $tarfile.gz"
    else
        echo "File $tarfile not found."
    fi
}

# Function to start an FTP session
start_ftp() {
    read -p "Enter the domain name or IP address to start FTP session: " domain
    ftp "$domain"
}

# Function to start LED control program (assuming it's in Desktop)
start_led_control() {
    LED_PROGRAM_PATH="/home/pi/Desktop/lab2_LED.py"  # Adjust the path if needed
    if [ -f "$LED_PROGRAM_PATH" ]; then
        echo "Starting LED control program..."
        python3 "$LED_PROGRAM_PATH"   # Use python3 to run the script
    else
        echo "LED control program not found at $LED_PROGRAM_PATH"
    fi
}

# Function to display network interfaces and their configurations (ifconfig)
show_ifconfig() {
    echo "Displaying network interface configuration (ifconfig):"
    ifconfig
}

# Function to display disk usage (df)
show_disk_space() {
    echo "Displaying disk space usage (df):"
    df -h
}

# Main menu loop
while true; do
    # Display menu options
    echo "Menu:"
    echo "a. List all files in the present working directory"
    echo "b. Display today's date and time"
    echo "c. Display whether a file is a 'simple' file or a 'directory'"
    echo "d. Create a backup for a file using the 'tar' command"
    echo "e. Compress the tar file"
    echo "f. Start an FTP session"
    echo "g. Start your LED control program"
    echo "h. Display network interface configuration (ifconfig)"
    echo "i. Display disk space usage (df)"
    echo "x. Exit"
    
    # Prompt for user input
    read -p "Enter your choice: " choice
    
    case $choice in
        a)
            list_files
            ;;
        b)
            display_date_time
            ;;
        c)
            check_file_type
            ;;
        d)
            create_backup
            ;;
        e)
            compress_tar
            ;;
        f)
            start_ftp
            ;;
        g)
            start_led_control
            ;;
        h)
            show_ifconfig
            ;;
        i)
            show_disk_space
            ;;
        x)
            echo "Exiting the program."
            break
            ;;
        *)
            echo "Invalid choice, please try again."
            ;;
    esac
done

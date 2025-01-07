#!/bin/bash

# Check if username is already saved
if [ ! -f "$HOME/.user_name" ]; then
    echo "Enter your name:"
    read username
    echo $username > $HOME/.user_name
else
    username=$(cat $HOME/.user_name)
fi

# Path to the python script
SCRIPT_PATH="$HOME/Termux-baner-/logo_animation.py"

# Check if the Python script exists
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Python script not found! Make sure logo_animation.py is in the repository directory."
    exit 1
fi

# Add the command to .bashrc if it's not already there
if ! grep -q "python3 $SCRIPT_PATH" ~/.bashrc; then
    echo "Adding Python script to .bashrc"
    echo "python3 $SCRIPT_PATH" >> ~/.bashrc
    echo "Setup complete. The script will now run on Termux startup."
else
    echo "Python script is already set to run at startup."
fi

# Make the Python script executable
chmod +x "$SCRIPT_PATH"

echo "Setup finished! Close and reopen Termux to see the T-header in action."

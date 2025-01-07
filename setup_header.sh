# Check if username is already stored
if [ ! -f "$HOME/.username" ]; then
    echo "Enter your name:"
    read username
    echo $username > "$HOME/.username"  # Store username in a file
else
    username=$(cat "$HOME/.username")  # Retrieve stored username
fi

# Display the banner with the stored username
echo -e "\n=== E G A L E X 5 ==="
echo -e "    --- Hacking is not a crime, it's skills ---\n"
echo "============================================================"
echo "Welcome to Hacking World $username!"
echo "============================================================"

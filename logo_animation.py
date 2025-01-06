import time
import os
import shutil

# ANSI color codes for styling
GREEN = "\033[1;32m"
RESET = "\033[0m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
YELLOW = "\033[1;33m"

def print_logo_stage(stage, terminal_width, username="User"):
    """Prints different stages of the logo based on the animation step and centers it."""
    logo = ""

    if stage == 1:
        # Stage 1: Initial form (Starting small)
        logo = f"{GREEN}\n        {username[0]}\n       {username[1]} X\n     {username[2]} L E{RESET}"
    elif stage == 2:
        # Stage 2: Some progress
        logo = f"{CYAN}\n     {username[0]} G A\n    X 5 L E\n   A L E X 5{RESET}"
    elif stage == 3:
        # Stage 3: Almost complete
        logo = f"{GREEN}\n     {username[0]} G A L\n    X 5 X E G\n   A L E X 5{RESET}"
    elif stage == 4:
        # Stage 4: Final complete logo with username
        logo = f"{RED}\n   === {username} ===\n    --- Hacking is not a crime, it's skills ---\n    --- Welcome, {username}! ---{RESET}"

    # Center the logo based on terminal width
    padding = (terminal_width - len(max(logo.splitlines(), key=len))) // 2
    for line in logo.splitlines():
        print(" " * padding + line)  # Center each line of the logo

def animate_logo(username):
    """Simulate the opening animation of the logo."""
    terminal_width = shutil.get_terminal_size().columns  # Get the current terminal width

    for stage in range(1, 5):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
        print_logo_stage(stage, terminal_width, username)
        time.sleep(0.5)  # Delay for animation effect

def display_logo(username):
    """Function to display the final logo header without animation."""
    terminal_width = shutil.get_terminal_size().columns  # Get terminal width
    print_logo_stage(4, terminal_width, username)  # Display final logo without animation

def main():
    """Main function to initiate the logo animation."""
    username = input(f"{YELLOW}Enter your name: {RESET}")  # Prompt for name
    animate_logo(username)  # Run animation
    display_logo(username)  # Display final logo

    # Proceed with the rest of the script
    print("\n" + "="*60)
    print(f"{RED}Welcome to Hacking World, {username}!{RESET}")
    print("="*60)

# Run the script directly
if __name__ == "__main__":
    main()

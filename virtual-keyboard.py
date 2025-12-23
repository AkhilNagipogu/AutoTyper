import pyautogui
import sys
import time


def type_payload(payload):
 
    for char in payload:

        # If the character is a newline,
        # press the Enter key
        if char == "\n":
            pyautogui.press("enter")
        else:
            # Otherwise, press the actual key
            pyautogui.press(char)



def main():

    print("=== Virtual Keyboard Typer ===")

    print("Paste or type payload below.")
    print("End input with a single line containing: EOF")
    print()

    lines = []  # This list will store each line of input

    # Read input line-by-line from terminal
    while True:
        line = sys.stdin.readline()

        if not line:
            break

        # If user types 'EOF', stop collecting input
        if line.strip() == "EOF":
            break

        # Store the line (including newline)
        lines.append(line)

    payload = "".join(lines)

    #Gives you time to switch tabs.
    print("\nFocus the TARGET input field (browser/editor).")
    print("Typing starts in 5 seconds...")
    time.sleep(5) #Change this to increase delay time

    # Start typing the payload using virtual keyboard
    type_payload(payload)

    print("\n[+] Done typing.")


if __name__ == "__main__":
    main()
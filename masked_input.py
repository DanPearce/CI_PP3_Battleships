"""Password prompt that shows a mask character for each key typed (standard library only).

Replaces the maskpass package, which depends on pynput and evdev (a desktop keyboard and Linux kernel headers) even
though only its askpass() was used.
"""
import sys


def _getch():
    """Read one key press without echo."""
    try:
        import termios
        import tty
    except ImportError:  # Windows
        import msvcrt
        return msvcrt.getwch()
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


def askpass(prompt="Password: ", mask="*"):
    """Ask for a password, echoing `mask` for each character. Backspace works; Ctrl+C stops the game."""
    sys.stdout.write(prompt)
    sys.stdout.flush()
    chars = []
    while True:
        key = _getch()
        if key in ("\r", "\n"):
            sys.stdout.write("\r\n")
            sys.stdout.flush()
            return "".join(chars)
        if key == "\x03":  # Ctrl+C
            raise KeyboardInterrupt
        if key in ("\x7f", "\b"):  # Backspace
            if chars:
                chars.pop()
                sys.stdout.write("\b \b")
        elif key.isprintable():
            chars.append(key)
            sys.stdout.write(mask)
        sys.stdout.flush()

class _Getch:
    """
    Gets a single character from standard input. Does not echo to the screen.

    Reference:
        - http://code.activestate.com/recipes/134892-getch-like-unbuffered-character-reading-from-stdin/
    """
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        stdin_file_descriptor = sys.stdin.fileno()
        old_settings = termios.tcgetattr(stdin_file_descriptor)
        try:
            tty.setraw(stdin_file_descriptor)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(stdin_file_descriptor, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()
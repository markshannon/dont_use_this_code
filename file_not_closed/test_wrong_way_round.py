
import sys

def write_to_file_or_stdout(txt, filename=None):
    if filename is None:
        out = sys.stdout
    else:
        out = open(filename)
    try:
        out.write(txt)
    finally:
        if filename is not None:
            out.close()

def back_to_front(txt, filename=None):
    if filename is None:
        out = sys.stdout
    else:
        out = open(filename)
    try:
        out.write(txt)
    finally:
        if filename is None:
            out.close()


        
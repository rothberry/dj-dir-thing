from py_term_helpers import *
from ipdb import set_trace
import os
from dotenv import load_dotenv
import glob
from pprint import pp
import eyed3


def analyze_filename(fn):

    set_trace()


if __name__ == "__main__":
    top_wrap('DJ FINDO')
    load_dotenv()
    eyed3.log.setLevel("ERROR") # `Lame tag CRC check failed` work around?
    
    MUSIC_DIR = os.getenv("MUSIC_DIR")
    WHITE_DIR = os.getenv("WHITE_DIR")
    DIR_TEST = os.getenv("DIR_TEST")

    # test_files = os.getcwd() + "/music-files"
    # music_files = os.listdir(test_files)
    white_list = os.listdir(WHITE_DIR)

    # pp(music_files)
    set_trace()
    for filename in white_list:
        cur_file = WHITE_DIR + filename
        analyze_filename(cur_file)

    set_trace()

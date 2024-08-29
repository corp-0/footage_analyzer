from pathlib import Path
from footage_analyzer.analyzer import Analyzer

#################################################
##########     Configuration     ################
########## edit bellow this      ################
#################################################

# path to the folder containing your videos
ROOT_DIR = "C:\\"

# always use lowercase
ALLOWED_EXTENSIONS = ["mp4", "avi", "mov", "mkv", "mts"]

# name of the output file, you can open this with Excel or google sheets
OUTPUT_FILENAME = "footage.csv"

#################################################
##########      End of Configuration     ########
########## do not edit anything below this ######
#################################################

def main():
    analyzer = Analyzer(Path(ROOT_DIR), ALLOWED_EXTENSIONS, OUTPUT_FILENAME)
    analyzer.analyze()

if __name__ == "__main__":
    main()
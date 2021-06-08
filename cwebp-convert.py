import glob
import os

directory = input("Directory >>> \n")
quality = input("Quality (0 to 100) >>> \n")
extentions = ['.png', '.jpeg', '.jpg', '.JPG']

for ext in extentions:
    for filepath in glob.iglob(directory + '/*' + ext):
        print(filepath)
        filename_long = os.path.basename(filepath).split(".")
        filename = filename_long[len(filename_long) - 2]
        os.system("cwebp -q " + quality + " " + filepath + " -o " + directory + "/" + filename + ".webp")
        
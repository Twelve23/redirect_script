#!/usr/bin/python
import os

OUTPUT_FILE = "output.txt"

def main():
    with open(OUTPUT_FILE, 'w') as out_file:
        for f in os.listdir("csvs"):
            file_path = "csvs/{0}".format(f)
            with open(file_path) as in_file:
                for line in in_file:
                    parts = line.split(",")
                    url = parts[0]
                    dest = parts[1]
                    if url.startswith("http"):
                        result = "Redirect 301 {0} {1}\n".format(url, dest)
                        out_file.write(result)
            out_file.write("\n")



if __name__ == "__main__":
    main()
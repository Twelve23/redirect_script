#!/usr/bin/python
import os

def main():
    for f in os.listdir("output"):
        output_filepath = "fixed/{0}-fix.csv".format(f[:-4])
        if not os.path.exists(os.path.dirname(output_filepath)):
            os.makedirs(os.path.dirname(output_filepath))
        with open(output_filepath, 'w') as out_file:
            file_path = "output/{0}".format(f)
            with open(file_path) as in_file:
                for line in in_file:
                    parts = line.strip().split(",")
                    # Check for a redirect loop
                    # I.E. when the first half is the same as the second.
                    if(parts[0] == parts[1]):
                        print "Loop found! Removing: {0}".format(line)
                    else:
                        out_file.write(line)

if __name__ == "__main__":
    main()
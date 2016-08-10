#!/usr/bin/python
import os
from urlparse import urlparse

def main():
    for f in os.listdir("csvs"):
        output_filepath = "output/{0}-output.txt".format(f.strip(".csv"))
        output_alt_filepath = "output-special/{0}-special.txt".format(f.strip(".csv"))
        if not os.path.exists(os.path.dirname(output_filepath)):
            os.makedirs(os.path.dirname(output_filepath))
        if not os.path.exists(os.path.dirname(output_alt_filepath)):
            os.makedirs(os.path.dirname(output_alt_filepath))
        with open(output_filepath, 'w') as out_file:
            with open(output_alt_filepath, 'w') as alt_file:
                file_path = "csvs/{0}".format(f)
                with open(file_path) as in_file:
                    for line in in_file:
                        parts = line.strip().split(",")
                        url = parts[0]
                        dest = parts[1]
                        parsed = urlparse(url)
                        if parsed.netloc.startswith("www"):
                            # Skip all www redirects as these should already redirect to just the base domain
                            print "Skipping domain with www... {0}".format(url)
                            continue
                        new_url = parsed.path
                        if parsed.params:
                            new_url += parsed.params
                        if parsed.query:
                            new_url += "?" + parsed.query
                        if parsed.fragment:
                            new_url += "#" + parsed.fragment

                        if url.startswith("http"):
                            if parsed.path.endswith("php"):
                                result = "Redirect 301 {0} {1}\n".format(parsed.path, dest)
                                alt_file.write(result)
                            else:
                                result = "{0},{1}\n".format(url, dest)
                                out_file.write(result)



if __name__ == "__main__":
    main()
import os
import time
import subprocess
from modules import file_metadata
from modules import text_format
from modules import math_format
from modules import code_format
from modules import blockquote_format
from modules import image_format

PATH_INPUT = "./markdown/" # Directory for all source files in markdown
PATH_OUTPUT = "./html/" # Directory for all generated html
TEMPLATE_HTML = "./template.html"


def generate_html_file(md_file):
    html_content = ""
    with open(TEMPLATE_HTML, "r") as template:
        html_content = template.read() # Copy html boilerplate from template file
    
    html_file = open(PATH_OUTPUT + md_file.replace(".md", ".html"), "w") # Create new or overwrite old file

    output = subprocess.run(
        ["pandoc", PATH_INPUT + md_file],
        capture_output = True,
        text = True
    )

    # Fill out placeholders
    html_content = html_content.replace("[title]", file_metadata.get_file_name(md_file))
    html_content = html_content.replace("[content]", output.stdout)
    html_content = html_content.replace("[created]", file_metadata.get_file_creation_date(md_file))
    html_content = html_content.replace("[updated]", file_metadata.get_file_modified_date(md_file))
    
    html_file.write(html_content) # Write the formatted content to html file

    return md_file.replace(".md", ".html")


def main():
    # Generate html (to ./output) for every markdown file (in ./input)
    for md_file in os.listdir(PATH_INPUT):
        if (md_file.endswith(".md") == False):
            continue # Ignore any files that aren't markdown
        
        print("Parsing " + md_file + "...")
        generate_html_file(md_file)


if __name__=="__main__":
    main()
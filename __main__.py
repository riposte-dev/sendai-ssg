import os
import subprocess
from modules import file_metadata

PATH_INPUT = "./input/" # Directory for all source files in markdown
PATH_OUTPUT = "./output/" # Directory for all generated html
TEMPLATE_HTML = "./template.html"

def generate_html_file(md_file):
    html_content = ""
    with open(TEMPLATE_HTML, "r") as template:
        html_content = template.read() # Copy html from template file

    # Fill out placeholders
    html_content = html_content.replace("[title]", md_file.replace(".md", ""))
    html_content = html_content.replace("[created]", file_metadata.get_file_creation_date(md_file))
    html_content = html_content.replace("[updated]", file_metadata.get_file_modified_date(md_file))

    # Insert content parsed from markdown to html
    output = subprocess.run(
        ["pandoc", PATH_INPUT + md_file],
        capture_output = True,
        text = True
    ).stdout

    html_content = html_content.replace("[content]", output)

    with open(PATH_OUTPUT + md_file.replace(".md", ".html"), "w") as html_file:
        html_file.write(html_content) # Write the formatted content to html file


def main():
    # Generate html (to ./output) for every markdown file (in ./input)
    for md_file in os.listdir(PATH_INPUT):
        if (md_file.endswith(".md") == False):
            continue # Ignore any files that aren't markdown
        
        print("Parsing " + md_file + "...")
        generate_html_file(md_file)


if __name__=="__main__":
    main()
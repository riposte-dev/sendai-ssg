import os
import time

PATH_INPUT = "./input/" # Directory for all source files in markdown
PATH_OUTPUT = "./output/" # Directory for all generated html
DATE_FORMAT = "%Y.%m.%d" # Default format for get_file_creation_date() and get_file_modified_date()
MAX_RECENT_POSTS = 5 # Maximum number of recent posts to show

def get_file_modified_seconds(file):
    return os.path.getmtime(PATH_INPUT + file) # Return seconds since modified


def get_recent_posts():
    recent_posts = []

    for md_file in os.listdir(PATH_INPUT):
        if (md_file.endswith(".md") == False):
            continue # Ignore any files that aren't markdown

        recent_posts.append(md_file)

    recent_posts.sort(key=get_file_modified_seconds) # Sort by modified seconds (Least to greatest)
    recent_posts.reverse() # Sort by modified seconds (Greatest to least)

    return recent_posts


def get_recent_posts_to_show():
    recent_posts = get_recent_posts()

    recent_posts_shown = [] # Recent posts that will be shown

    for i in range(0, MAX_RECENT_POSTS - 1, 1):
        recent_posts_shown.append(recent_posts[i])
    
    return recent_posts_shown


print(get_recent_posts_to_show())
import os

# each website you crawl is a separate project(folder)
# new folder = new project


def create_project_dir(directory):
    # if the folder (project)does not  already exist

    if not os.path.exists(directory):
        print("Creating project "+directory)
        os.makedirs(directory)

# create queue and crawl files (if not created)
# the base_url is needed to give our spider a starting point


""" So the stating point is gonna be our url and its gonna start 
gathering all the urls  , litteraly any url is gonna be added to a waiting
list (BFS search of urls)"""


def create_data_files(project_name, base_url):
    # create a list of links waiting to be crawled
    # create a list of crawled links

    queue = project_name+'/queue.txt'
    crawled = project_name+'/crawled.txt'

    if not os.path.isfile(queue):
        # are queue list should not be empty because if it start and find nothing to crawl :// haha
        write_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_file(crawled, '')


# create a new file
def write_file(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()


# add data onto an existing file (each link on a new line)
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data+'\n')

# delete the content of a file(clear)


def clear_file(path):
    with open(path, 'w'):
        # do nothing
        pass

# read a file and convert each line to set items


def convert_file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results

# iterate through a set , each item of a set will be a new line in a file


def convert_set_to_file(set_links, file_name):
    clear_file(file_name)
    # instead of just storing we can sort the links to have an alphabetical order (wich is better)
    for link in sorted(set_links):
        append_to_file(file_name, link)

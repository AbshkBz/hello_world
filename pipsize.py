'''
program to list all pip packages along with the size they occupy on the disk. Copied from the following stackoverflow
https://stackoverflow.com/questions/34266159/how-to-see-pip-package-sizes-installed
'''

# dependencies
import os
import pkg_resources

def calc_container(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size



dists = [d for d in pkg_resources.working_set]

for dist in dists:
    try:
        path = os.path.join(dist.location, dist.project_name)
        size = calc_container(path)
        if size/1e3 > 1.0:
            print (f"{dist}: {size/1e3} KB")
            print("-"*40)
    except OSError:
        '{} no longer exists'.format(dist.project_name)
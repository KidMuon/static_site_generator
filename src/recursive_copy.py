import os, shutil

def recursive_copy(src, dest):
    if os.path.exists(os.path.join(os.getcwd(), dest)):
        shutil.rmtree(os.path.join(os.getcwd(), dest))
        os.makedirs(dest)

    src_files = get_file_list(os.path.join(os.getcwd(), src))

    for file in src_files:
        shutil.copy(os.path.join(os.getcwd(), src, file), os.path.join(os.getcwd(), dest))

    return None

def get_file_list(path):
    file_list = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_list.append(file)
        else:
            file_list.extend(get_file_list(os.path.join(path, file)))
    return file_list
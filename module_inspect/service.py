import os

from module_inspect.entity.FileStructureEntity import RudiInspectorFileEntity


def build_entity_structure(path=r'/Users/rudi/Project/rudi/rudi_map'):
    def calc_suffixes(data):
        try:
            if data == "__init__.py":
                return 0
            if data[-3:] == ".py":
                return 1
        except Exception as e:
            return 0

    dict_path_file = {}

    for fpath, dirname, fnames in os.walk(path):
        files = filter(lambda i: calc_suffixes(i), os.listdir(fpath))
        files = list(files)
        if len(files) > 0:
            dict_path_file[fpath] = files

    file_entitys = []
    for k, v in dict_path_file.items():
        for _v in v:
            file_entitys.append(RudiInspectorFileEntity(os.path.join(k, _v), path))
    return file_entitys

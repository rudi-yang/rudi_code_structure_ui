import os


class RudiInspectorFileEntity:
    def __init__(self, path, base_path):
        self._base_path = base_path
        self._path, self._fname = os.path.split(path)
        self._path = str(self.path).replace(base_path, "")
        self._desc, self._desc_task, self.desc_input, self._max_l, self._content = self.set_attr(path)

    @property
    def base_path(self):
        return self._base_path

    @property
    def path(self):
        return self._path

    @property
    def max_l(self):
        return self._max_l

    @property
    def fname(self):
        return self._fname

    @property
    def desc_task(self):
        return self._desc_task

    @property
    def content(self):
        return self._content

    def set_attr(self, path):
        desc_input = []
        desc_task = []
        descs = []
        with open(path)  as f:
            line = f.readline
            while line:
                l = str(line).strip(' ')
                if l.startswith("# desc "):
                    desc = l[7:].strip("\n")
                    descs.append(desc)
                if l.startswith("# task "):
                    desc = l[7:].strip("\n")
                    desc_task.append(desc)
                if l.startswith("# input "):
                    desc = l[8:].strip("\n")
                    desc_input.append(desc)
                line = f.readline()
                desc = ""
        max_l = max(len(desc_input), len(desc_task), len(descs))

        with open(path) as f:
            content = f.read()
        return descs, desc_task, desc_input, max_l, content


class RudiInspectorFileManager:
    def __init__(self, entitys):
        self.entitys = entitys
        self.sort()

    def show(self):
        res = []
        for entity in self.entitys:
            res.append([[entity.path], [entity.fname], entity.desc])
        return res

    def sort(self):
        self.entitys.sort(key=lambda i: os.path.join(i.path, i.fname))

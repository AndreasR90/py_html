from .core import htmlObject


class Layout:
    def __init__(self, html_objects: htmlObject):
        self.html_objects = html_objects
        self.idx_dict = self.get_index_dict()

    def get_index_dict(self):
        idx_dict = {}
        for obj in self.html_objects:
            if obj.id is not None:
                if obj.id in idx_dict.keys():
                    raise ValueError(obj.id + " is already in index array")
                else:
                    idx_dict[obj.id] = obj
        return idx_dict

    def __str__(self):
        html_string = ""
        for obj in self.html_objects:
            html_string += obj.__str__()
        return html_string

    def get_object_by_id(self, id):
        return self.idx_dict.get(id, None)

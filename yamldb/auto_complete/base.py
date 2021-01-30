# -*- coding: utf-8 -*-

import jsonpatch


class AutoCompleteContext:
    def __init__(self, data):
        self.data = data
        self.current_index = None
        self.current_datum = None

    def __iter__(self):
        for i, item in enumerate(self.data):
            self.current_index = i
            self.current_datum = item
            yield i, item
        self.current_index = None
        self.current_datum = None


class AutoCompleteRunner:
    def __init__(self, tasks):
        self.tasks = tasks
        self.history = []

    def apply(self, data):
        context = AutoCompleteContext(data)
        result = []
        for i, item in context:
            patches = []
            for task in self.tasks:
                if not task.match(item):
                    continue
                patches.append(task.make_patch(item, context))
            if not patches:
                result.append(item)
                continue

            result.append(jsonpatch.apply_patch(item, patches))
        return result

    def add_patch(self, at, patch):
        self.history.append({
            "at": at,
            "patch": patch,
        })


class AutoCompleteTaskBase:
    def match(self, item):
        raise NotImplementedError

    def make_patch(self, item, context):
        raise NotImplementedError

    def add(self, path, value):
        """
        :param path: update path
        :param value: update value
        """
        return {
            "op": "add",
            "path": path,
            "value": value,
        }

    def remove(self, path):
        """
        :param path: remove path
        """
        return {
            "op": "remove",
            "path": path,
        }

    def replace(self, path, value):
        """
        :param path: replace path
        :param value: replace value
        """
        return {
            "op": "replace",
            "path": path,
            "value": value,
        }

    def move(self, from_path, to_path):
        """
        :param from_path: path of src
        :param to_path: path of dest
        """
        return {
            "op": "move",
            "from": from_path,
            "path": to_path,
        }

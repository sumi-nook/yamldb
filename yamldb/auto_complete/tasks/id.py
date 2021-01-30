import uuid

from ..base import AutoCompleteTaskBase


class AutoCompleteIDTask(AutoCompleteTaskBase):
    def match(self, item):
        return "id" not in item

    def make_patch(self, item, context):
        return self.add("/id", str(uuid.uuid4()))

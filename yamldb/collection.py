# -*- coding: utf-8 -*-

import copy

from jsonpath_ng import jsonpath
from jsonpath_ng import parse as jsonpath_parse
import yaml

from .base import QueryBase
from .serializer import ordered_dict as _


class CollectionQuery(QueryBase):
    def __init__(self, items):
        self.items = items
        self.exprs = []
        for path, op, value in items:
            self.exprs.append((
                jsonpath_parse(path),
                op,
                value,
            ))

    def filter(self, rows):
        result = []
        for row in rows:
            for expr, op, value in self.exprs:
                for m in expr.find(row):
                    if self.evaluate_operator(m.value, op, value):
                        result.append(copy.deepcopy(row))
                        break
        return result


class Collection:
    def __init__(self, data, header=None):
        self.data = data
        self.header = [] if header is None else header

    def insert(self, row):
        self.data.append(row)

    def select(self, query):
        return query.filter(self.data)

    @staticmethod
    def load(fileobj, header=None):
        return Collection(yaml.safe_load(fileobj), header=header)

    def save(self, fileobj):
        yaml.dump(self.data, fileobj, default_flow_style=False)

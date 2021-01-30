# -*- coding: utf-8 -*-ß

class QueryBase:
    BINARY_OPERATORS = [
        "==",
        "!=",
        "<",
        "<=",
        ">",
        ">=",
    ]
    UNARY_OPERATORS = [
        "+",
        "-",
        "*",
        "/",
        "%",
    ]

    @classmethod
    def evaluate_operator(cls, lhs, op, rhs):
        if op in cls.BINARY_OPERATORS:
            return cls.binary_operate(lhs, op, rhs)
        elif op in cls.UNARY_OPERATORS:
            return cls.unary_operate(lhs, op, rhs)
        return None

    @classmethod
    def binary_operate(cls, lhs, op, rhs):
        #assert op in cls.BINARY_OPERATORS
        if op == "==":
            return lhs == rhs
        elif op == "!=":
            return lhs != rhs
        elif op == "<":
            return lhs < rhs
        elif op == "<=":
            return lhs <= rhs
        elif op == ">":
            return lhs > rhs
        elif op == ">=":
            return lhs >= rhs

    @classmethod
    def unary_operate(cls, lhs, op, rhs):
        #assert op in cls.UNARY_OPERATORS
        if op == "+":
            return lhs + rhs
        elif op == "-":
            return lhs - rhs
        elif op == "*":
            return lhs * rhs
        elif op == "/":
            return lhs / rhs
        elif op == "%":
            return lhs % rhs

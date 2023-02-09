from dataclasses import dataclass

from .operator import Operator


class Expression:
    # TODO: もしかしてProtocolが向く？
    ...


@dataclass
class BinaryExpression(Expression):
    operator: "Operator"
    lhs: "Expression"
    rhs: "Expression"


@dataclass
class IntegerLiteral(Expression):
    value: int


class Ast:
    # TODO: クラスにする必要ないかも
    @staticmethod
    def add(lhs: "Expression", rhs: "Expression") -> "BinaryExpression":
        return BinaryExpression(Operator.ADD, lhs, rhs)

    @staticmethod
    def integer(value: int) -> "IntegerLiteral":
        return IntegerLiteral(value)

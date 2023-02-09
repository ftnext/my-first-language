from .ast import Expression, BinaryExpression, IntegerLiteral
from .operator import Operator


class Interpreter:
    def interpret(self, expression: "Expression") -> int:
        if isinstance(expression, BinaryExpression):
            lhs = self.interpret(expression.lhs)
            rhs = self.interpret(expression.rhs)
            match expression.operator:
                case Operator.ADD: return lhs + rhs
        elif isinstance(expression, IntegerLiteral):
            return expression.value
        else:
            raise RuntimeError("not reach here")

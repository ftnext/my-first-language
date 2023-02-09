from unittest import TestCase

from calculator.ast import Ast
from calculator.interpreter import Interpreter


class InterpreterPlusTestCase(TestCase):
    def test_10_plus_20_should_work(self):
        # TODO: subTestにして書き直す（テストメソッドを分けなくてよさそう）
        interpreter = Interpreter()
        expression = Ast.add(Ast.integer(10), Ast.integer(20))

        self.assertEqual(30, interpreter.interpret(expression))

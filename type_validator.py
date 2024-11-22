from JuliaSimplificadaParser import JuliaSimplificadaParser
from collections import defaultdict

class TypeValidator:
    def __init__(self):
        self.variables = defaultdict(str)  # Almacena variables y sus tipos
        self.errors = []  # Lista de errores de validación

    def visit(self, node):
        """Visita recursivamente cada nodo del árbol y valida los tipos."""
        if isinstance(node, JuliaSimplificadaParser.AssignmentContext):
            self.visit_assignment(node)
        elif isinstance(node, JuliaSimplificadaParser.ExpressionContext):
            return self.visit_expression(node)
        elif isinstance(node, JuliaSimplificadaParser.FunctionDeclContext):
            self.visit_function_decl(node)
        elif hasattr(node, 'children'):
            # Si el nodo tiene hijos, los visita recursivamente
            for child in node.children:
                self.visit(child)

    def visit_assignment(self, node):
        """Valida una asignación."""
        var_name = node.IDENTIFIER().getText()  # Obtiene el nombre de la variable
        value_type = self.visit(node.expression())  # Valida la expresión asignada
        if node.type():
            declared_type = node.type().getText()
            if declared_type != value_type:
                self.errors.append(
                    f"Tipo incorrecto para {var_name}. Se esperaba {declared_type} pero se encontró {value_type}."
                )
            else:
                self.variables[var_name] = declared_type  # Guarda el tipo declarado
        else:
            self.variables[var_name] = value_type  # Infieren el tipo de la expresión

    def visit_expression(self, node):
        """Valida una expresión y devuelve su tipo."""
        if node.logicalOrExpression():  # Valida expresiones lógicas o aritméticas
            return self.visit(node.logicalOrExpression())
        elif node.primaryExpression():  # Para literales o identificadores
            return self.visit(node.primaryExpression())
        else:
            return "Unknown"

    def visit_primaryExpression(self, node):
        """Valida expresiones primarias (literales o identificadores)."""
        if node.IDENTIFIER():
            var_name = node.IDENTIFIER().getText()
            if var_name not in self.variables:
                self.errors.append(f"Uso de variable no declarada: {var_name}.")
                return "Unknown"
            return self.variables[var_name]
        elif node.INT():
            return "Int"
        elif node.FLOAT():
            return "Float"
        elif node.STRING():
            return "String"
        elif node.BOOL():
            return "Bool"
        else:
            return "Unknown"

    def visit_function_decl(self, node):
        """Valida declaraciones de funciones."""
        func_name = node.IDENTIFIER().getText()
        print(f"Validando función: {func_name}")
        # Implementar lógica para validar parámetros y cuerpo de la función

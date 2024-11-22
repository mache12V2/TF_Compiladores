import sys
from antlr4 import *
from JuliaSimplificadaLexer import JuliaSimplificadaLexer
from JuliaSimplificadaParser import JuliaSimplificadaParser

def procesar_codigo(codigo):
    input_stream = InputStream(codigo)
    lexer = JuliaSimplificadaLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = JuliaSimplificadaParser(token_stream)

    try:
        tree = parser.program()
        # Devolver el árbol de análisis como texto
        return tree.toStringTree(recog=parser)
    except Exception as e:
        return f"Error durante el análisis: {e}"

def main():
    if len(sys.argv) < 2:
        codigo = sys.stdin.read()
        print(procesar_codigo(codigo))
    else:
        archivo = sys.argv[1]
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                codigo = f.read()
            print(procesar_codigo(codigo))
        except FileNotFoundError:
            print(f"Error: No se pudo encontrar el archivo {archivo}")

if __name__ == "__main__":
    main()

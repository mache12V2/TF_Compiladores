import llvmlite.ir
import llvmlite.binding as llvm

# Inicializar LLVM
llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

def crear_modulo_llvm():
    # Crear un módulo LLVM
    module = llvmlite.ir.Module(name="example_module")

    # Crear un tipo de función (por ejemplo, int32 sum(int32, int32))
    function_type = llvmlite.ir.FunctionType(llvmlite.ir.IntType(32), [llvmlite.ir.IntType(32), llvmlite.ir.IntType(32)])

    # Crear la función dentro del módulo
    function = llvmlite.ir.Function(module, function_type, name="sum")

    # Crear un bloque de código (bloque de entrada)
    block = function.append_basic_block(name="entry")
    builder = llvmlite.ir.IRBuilder(block)

    # Definir los parámetros de la función
    a, b = function.args
    # Realizar la suma
    result = builder.add(a, b, name="result")
    builder.ret(result)

    # Mostrar el código LLVM IR generado
    print(str(module))



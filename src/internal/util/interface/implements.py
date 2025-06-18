import inspect
from typing import get_type_hints

def get_method_signature(obj):
    cls = obj if inspect.isclass(obj) else type(obj)
    signatures = {}
    for member_name, member in inspect.getmembers(cls, predicate=inspect.isfunction):
        if not member_name.startswith('_'):
            signatures[member_name] = (inspect.signature(member), get_type_hints(member))
    return signatures

def implements_interface(A, B):
    a_signatures = get_method_signature(A)
    b_signatures = get_method_signature(B)

    for op, (a_signature, a_type_hints) in a_signatures.items():
        if op not in b_signatures:
            raise NotImplementedError(f"operation {op} is not implemented by provided controller or middlewares")
        
        b_signature, b_type_hints = b_signatures[op]

        # Check if all parameters are present and have correct types
        for param_name, param in a_signature.parameters.items():
            if param_name not in b_signature.parameters:
                raise NotImplementedError(f"operation {op} is missing parameter {param_name}")

            # Check type hints
            a_param_type = a_type_hints.get(param_name)
            b_param_type = b_type_hints.get(param_name)
            if a_param_type is not None and a_param_type != b_param_type:
                raise NotImplementedError(f"operation {op} parameter {param_name} does not have the correct type ({a_param_type} != {b_param_type})")

        # Check for extra parameters in B that are not in A
        for param_name in b_signature.parameters:
            if param_name not in a_signature.parameters:
                raise NotImplementedError(f"operation {op} in provided controller has an extra parameter {param_name}")

        # Check return type
        if 'return' in a_type_hints and 'return' in b_type_hints and a_type_hints['return'] != b_type_hints['return']:
            raise NotImplementedError(f"operation {op} has an incorrect return type")

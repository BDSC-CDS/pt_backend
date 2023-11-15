class Resolution:
    def __init__(self, function, operation_id):
        """
        Represents the result of operation resolution

        :param function: The endpoint function
        :type function: types.FunctionType
        """
        self.function = function
        self.operation_id = operation_id


class Resolver:
    def __init__(self, controllers):
        """
        Standard resolver

        :param function_resolver: Function that resolves functions using an operationId
        :type function_resolver: types.FunctionType
        """
        self.controllers = controllers

    def resolve(self, operation):
        """
        Default operation resolver

        :type operation: connexion.operations.AbstractOperation
        """
        router_controller = operation.router_controller
        if router_controller is None:
            raise NotImplementedError("operation " + operation.operation_id + " is missing x-openapi-router-controller")

        controller = self.controllers.get(router_controller)
        if controller is None:
            raise NotImplementedError("controller " + router_controller + " does not exist in provided controllers")

        func = getattr(controller, operation.operation_id, None)
        if func is None:
            raise NotImplementedError("controller " + router_controller + " does not implement " + operation.operation_id)

        return Resolution(func, operation.operation_id)

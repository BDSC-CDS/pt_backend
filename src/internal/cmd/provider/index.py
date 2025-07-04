import src.internal.api.server_template.controllers.index_service_controller as connexion_index_controller
import src.internal.api.controllers.index_controller as internal_index_controller

index_controller = None

def provide_index_controller():
    global index_controller

    if index_controller is not None:
        return index_controller
    
    controller = internal_index_controller.IndexServiceController()
    index_controller = connexion_index_controller.IndexServiceController(controller)

    return index_controller
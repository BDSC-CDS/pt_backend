from src.pkg.config_generator.model.config_generator import ConfigGenerator

class ConfigGeneratorService:
    def __init__(self, config_generator_store):
        self.config_generator_store = config_generator_store

    def log_event(self, log: ConfigGenerator):
        self.config_generator_store.log_event(log)

    def get_logs(self,offset:int,limit:int):
        logs = self.config_generator_store.get_logs(offset,limit)
        return logs

    def get_logs_for_user(self, identifier:int,offset:int,limit:int):
        logs = self.config_generator_store.get_logs_for_user(identifier=identifier,offset=offset,limit=limit)
        return logs

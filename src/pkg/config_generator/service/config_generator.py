from src.pkg.config_generator.model.config_generator import ConfigGenerator

class ConfigGeneratorService:
    def __init__(self, config_generator_store):
        self.config_generator_store = config_generator_store

    def create_config(self, config: ConfigGenerator):
        self.config_generator_store.create_config(config)

    def get_configs(self,offset:int,limit:int):
        configs = self.config_generator_store.get_configs(offset,limit)
        return configs

    def get_configs_for_user(self, identifier:int,offset:int,limit:int):
        configs = self.config_generator_store.get_configs_for_user(identifier=identifier,offset=offset,limit=limit)
        return configs

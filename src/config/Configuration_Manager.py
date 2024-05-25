from src.utils import * 
from src.constants import * 
from src.entity import * 




# Configuraion manager

class Configuration_Manager:
    def __init__(self,config=config_path,params=params_path):
        self.config=read_yaml(config)
        self.params=read_yaml(params)

        create_directories([self.config.artifacts])

    def ingestion_config(self)->ingestion:
        config=self.config.ingestion 

        create_directories([config.root_dir])


        ingestion_configuration=ingestion(
            root_dir=config.root_dir,
            test_data=config.test_data,
            train_dat=config.train_data
        )

        return ingestion_configuration

    def trasformation_config(self)-> transformation:
        config=self.config.trasformation

        create_directories([config.root_dir])

        transformation_configuration=transformation(
            root_dir=config.root_dir,
            transformed_train_data=config.transformed_train_data,
            transformed_test_data=config.transformed_test_data,
            transformation_pickle_file=config.transformation_pickle_file
            )
        
        return transformation_configuration
    

    def model_traning_config(self)->model_training:
        config=self.config.model_training
        
        create_directories([config.root_dir])

        model_=model_training(
            root_dir=config.root_dir,
            saved_model=config.saved_model,
            saved_vector_model=config.saved_vector_model

        )

        return model_
    
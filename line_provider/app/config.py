from pydantic import BaseModel, Field
from os import environ as env


class KafkaConfig(BaseModel):

    host: str = Field(alias="KAFKA_HOST")
    port: str = Field(alias="KAFKA_PORT")
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1

    @property
    def instance(self):
        return f"{self.host}:{self.port}"


class Config(BaseModel):
    kafka_: KafkaConfig = Field(default_factory=lambda: KafkaConfig(**env))


config = Config()

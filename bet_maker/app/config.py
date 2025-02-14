from pydantic import BaseModel, Field
from os import environ as env


class PostgresConfig(BaseModel):
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT")
    login: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    database: str = Field(alias="POSTGRES_DB")

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.login}:{self.password}@{self.host}:{self.port}/{self.database}"

class KafkaConfig(BaseModel):
    host: str = Field(alias="KAFKA_HOST")
    port: str = Field(alias="KAFKA_PORT")
    topics: str = Field(alias="KAFKA_TOPICS")
    file_encoding: str = "utf-8"
    file_compression_quality: int = 1

    @property
    def instance(self):
        return f"{self.host}:{self.port}"
    
class Config(BaseModel):
    postgres_: PostgresConfig = Field(default_factory=lambda: PostgresConfig(**env))
    kafka_: KafkaConfig = Field(default_factory=lambda: KafkaConfig(**env))


config = Config()
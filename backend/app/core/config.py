from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "CompDDL API"
    api_v1_str: str = "/api"

    mysql_user: str = "root"
    mysql_password: str = "12345678"
    mysql_host: str = "localhost"
    mysql_port: int = 3306
    mysql_db: str = "compddl"

    @property
    def sqlalchemy_database_uri(self) -> str:
        return (
            f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}"
            f"@{self.mysql_host}:{self.mysql_port}/{self.mysql_db}?charset=utf8mb4"
        )

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()

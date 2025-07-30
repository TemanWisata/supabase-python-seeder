from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class KaggleConfig(BaseSettings):
    username: str | None = Field(
        default=None, description="Kaggle username", alias="KAGGLE__USERNAME"
    )
    key: SecretStr | None = Field(
        default=None, description="Kaggle API key", alias="KAGGLE__KEY"
    )
    model_config = SettingsConfigDict(
        # root/notebooks/config.py -> root/.env
        env_file=Path(__file__).parent.parent.joinpath(".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


class Config(BaseSettings):
    kaggle: KaggleConfig | None = Field(
        default=KaggleConfig(),
        description="Kaggle configuration containing username and key",
    )
    USER_STARTER_PASSWORD: SecretStr | None = Field(
        default=None,
        description="User starter password",
    )

    model_config = SettingsConfigDict(
        env_file="./.env",
        env_file_encoding="utf-8",
        env_nested_delimiter="_",
        case_sensitive=False,
        extra="ignore",
    )


CONFIG = Config()

if __name__ == "__main__":
    print(CONFIG)

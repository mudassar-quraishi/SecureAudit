from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_env: str = "development"
    app_name: str = "SecureAudit API"
    app_port: int = 8000

    database_url: str = "postgresql://secureaudit:secureaudit@localhost:5432/secureaudit"

    auth0_domain: str
    auth0_client_id: str
    auth0_client_secret: str
    auth0_audience: str
    auth0_private_key_path: str = "./private-key.pem"
    auth0_org_id: str | None = None

    github_api_base: str = "https://api.github.com"
    token_exchange_scope_read: str = "repo:read"
    token_exchange_scope_write: str = "repo:write"

    openfga_api_url: str = "http://localhost:8080"
    openfga_store_id: str
    openfga_model_id: str


settings = Settings()

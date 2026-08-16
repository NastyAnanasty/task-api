from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Secret — env only
    llm_api_key: str

    # LLM provider
    llm_base_url: str = "https://openrouter.ai/api/v1"
    llm_model: str = "deepseek/deepseek-v4-pro-0813"
    llm_temperature: float = 0.0

    # Vector store
    qdrant_url: str = "http://qdrant:6333"
    collection_name: str = "sklearn_docs"
    top_k: int = 4

    # Embeddings
    embedding_model: str = "intfloat/multilingual-e5-small"
    embedding_dim: int = 384
    normalize_embeddings: bool = True

    # agent (этой недели)
    max_iterations: int = 5
    agent_temperature: float = 0.0
    enable_web_search: bool = True
    agent_max_output_chars: int = 2000


settings = Settings()

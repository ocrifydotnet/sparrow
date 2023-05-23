from pydantic import BaseSettings


class Settings(BaseSettings):
    huggingface_key: str = "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"
    dataset_name: str = "katanaml-org/invoices-donut-data-v1"


settings = Settings()
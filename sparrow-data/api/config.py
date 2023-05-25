from pydantic import BaseSettings


class Settings(BaseSettings):
    sparrow_key: str = "2ec6602fa3fe013f3fa8859d008bd66e"
    huggingface_key: str = "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"
    dataset_name: str = "katanaml-org/invoices-donut-data-v1"
    ocr_stats_file: str = "data/ocr_stats.json"


settings = Settings()
from pydantic import BaseSettings


class Settings(BaseSettings):
    sparrow_key: str = "2ec6602fa3fe013f3fa8859d008bd66e"
    huggingface_key: str = "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"
    ocr_stats_file: str = "data/ocr_stats.json"


settings = Settings()
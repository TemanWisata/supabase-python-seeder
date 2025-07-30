"""Extracts the Indonesia Tourism Destination dataset from KaggleHub."""

from pathlib import Path
import os
import kagglehub  # type: ignore
from loguru import logger


try:
    download_path = Path(__file__).parent
    # Set the dataset download path
    os.environ["KAGGLEHUB_CACHE"] = str(download_path)

    path = kagglehub.dataset_download("aprabowo/indonesia-tourism-destination")

    logger.success("Path to dataset files: {}", path)

except Exception as e:
    logger.error("An error occurred: {}", e)
    raise

from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class LindormConfig(BaseSettings):
    """
    Lindorm configs
    """

    LINDORM_URL: Optional[str] = Field(
        description="Lindorm url",
        default=None,
    )
    LINDORM_USERNAME: Optional[str] = Field(
        description="Lindorm user",
        default=None,
    )
    LINDORM_PASSWORD: Optional[str] = Field(
        description="Lindorm password",
        default=None,
    )
    LINDORM_UGC_INDEX_NAME: Optional[str] = Field(
        description="Lindorm UGC index name. When using, all data will be store in a single index but you can search "
                    "separately",
        default=None,
    )
    LINDORM_UGC_ROUTING_FIELD: Optional[str] = Field(
        description="Lindorm UGC routing field name, used in search index to do UGC full-text search",
        default="routing_field"
    )

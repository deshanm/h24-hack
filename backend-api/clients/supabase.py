import os
from supabase import Client, create_client
from supabase.lib.client_options import ClientOptions

from cgen_api.server.config import Settings, get_settings


def get_supabase_client(settings: Settings | None = None) -> Client:
    if not settings:
        settings = get_settings()

    return create_client(
        supabase_url= os.environ.get("SUPABASE_URL"),
        supabase_key= os.environ.get("SUPABASE_KEY"),
        options=ClientOptions(
            postgrest_client_timeout=30,
        )
    )

from fastapi import Cache

cache = Cache()

@cache.on_miss()
async def cache_data(key: str, data_callable: Callable) -> Any:
    return await data_callable()

# Caching strategies can be applied to frequently accessed endpoints, reducing server load and improving response time.
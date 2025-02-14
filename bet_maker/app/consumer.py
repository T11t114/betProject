import json
from aiokafka import AIOKafkaConsumer
import brotli
from app.config import config
from app.crud import update_bet_status
from app.data_access.database import get_session

def create_consumer() -> AIOKafkaConsumer:

    return AIOKafkaConsumer(
        config.kafka_.topics,
        bootstrap_servers=config.kafka_.instance,
    )

consumer = create_consumer()

async def decompress(file_bytes: bytes) -> dict:
    decompressed_str = str(brotli.decompress(file_bytes), config.kafka_.file_encoding)
    return json.loads(decompressed_str)  


async def consume():
    while True:
        async for msg in consumer:
            value = await decompress(msg.value)
            async for session in get_session():
                await update_bet_status(session, value["event_id"], value["status"])

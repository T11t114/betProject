import json
import brotli
from app.schemas import EventState
from app.config import config
from aiokafka import AIOKafkaProducer

def create_producer() -> AIOKafkaProducer:

    return AIOKafkaProducer(
        bootstrap_servers=config.kafka_.instance,
    )

producer = create_producer()

async def compress(message: str) -> bytes:
    return brotli.compress(
        bytes(message, config.kafka_.file_encoding),
        quality=config.kafka_.file_compression_quality,
    )


async def handle_event_status(event_id: str, status: EventState):
    message = {"event_id": event_id, "status": status}
    await producer.send_and_wait("event-status", await compress(json.dumps(message)))


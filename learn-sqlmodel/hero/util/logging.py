import sys
import logging
from loguru import logger

logger.remove()
logger.add(
    sys.stdout, 
    format="<green>{time:YYYY/MM/DD HH:mm:ss}</green> <level>{level: <5} <cyan>{name}</cyan> {message}</level>",
    level="DEBUG",
)


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists.
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message.
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(
            depth=depth, exception=record.exc_info
        ).log(
            "DEBUG", record.getMessage()
        )


def configure_log_handler(*, log_level=logging.WARNING):
    logging.basicConfig(handlers=[InterceptHandler()],
                        level=logging.NOTSET, force=True)
    for target in ['sqlalchemy.engine.Engine', 'sqlalchemy.engine']:
        logging.getLogger(target).setLevel(log_level)

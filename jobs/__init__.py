from .design1 import TestDesignJob
from nautobot.apps.jobs import register_jobs


__all__ = [
    TestDesignJob,
]

register_jobs(__all__)

from dataclasses import dataclass, field, asdict
from flask import jsonify

@dataclass
class ResponseMessage:
    message: str
    status: str = field(default='error')

    def json(self):
        return jsonify(asdict(self))
        
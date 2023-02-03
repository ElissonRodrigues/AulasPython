from dataclasses import dataclass, field, asdict
from flask import jsonify

@dataclass
class ResponseMessage:
    message: str
    status: str = field(default='error')

    def json(self):
        return jsonify(asdict(self))
        
@dataclass
class ContactData:
    id_: int
    nome: str
    email: str
    telefone: str
    nascimento: str

    def json(self):
        return asdict(self)

        
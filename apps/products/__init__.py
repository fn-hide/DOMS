from flask import Blueprint

blueprint = Blueprint(
    'products_blueprint',
    __name__,
    url_prefix=''
)

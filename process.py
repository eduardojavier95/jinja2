
from jinja2 import Environment, FileSystemLoader, select_autoescape
import json

spec = ""
with open('spec.json', 'r') as f:
    spec=json.load(f)

env = Environment(
    loader=FileSystemLoader(searchpath="./"),
    autoescape=select_autoescape
)

template = env.get_template("template.txt")

print(template.render(spec))
from jinja2 import Environment, FileSystemLoader

data = [
    #{'h1': 'страница с домашним заданием'},
    #{'p': 'Домашние задание выполненно'}
    {},
]

file_loader = FileSystemLoader('hw_templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(enter=data)

print(msg)
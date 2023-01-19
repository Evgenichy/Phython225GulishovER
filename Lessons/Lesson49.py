from jinja2 import Template

# link = """B HTML-документе ссылка определяется так:
# <a href=#>Ссылка</a>"""
#
# tm = Template("{{ link | e}}")
# msg = tm.render(link=link)
#
# print(msg)

# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Смоленск'},
#     {'id': 4, 'city': 'Минск'},
#     {'id': 5, 'city': 'Ярославль'}
# ]
#
# link = """<select name='cities'>
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% elif c.city == "Москва" -%}
#     <option>{{ c['city']}}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

#################
# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новаости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contacts', 'link': 'Контакты'},
# ]
#
# link = """<ul>
#     {% for m in menu -%}
#     <li><a "{{ m['href'] }} class={{ m['link']"></a></li>
#     {% endfor -%}
# </ul>
# """
#
# tm = Template(link)
# msg = tm.render(menu=menu)
#
# print(msg)
############

# menu = [
#     {'url': '/index', 'title': 'Главная '},
#     {'url': '/news', 'title': 'О нас'},
#     {'url': '/about', 'title': 'Новости'},
#     {'url': '/shop', 'title': 'Магазин'},
#     {'url': '/contacts', 'title': 'Контакты'}
# ]
#
# text = """
#     <ul>
#     {% for m in menu -%}
#         {% if m['url'] == '/index' -%}
#             <li><a href='{{ m['url'] }}' class='active'>{{ m['title'] }}</a></li>
#         {% else %}
#             <li><a href='{{ m['url'] }}'>{{ m['title'] }}</a></li>
#         {% endif -%}
#     {% endfor -%}
#     </ul>
# """
#
# tm = Template(text)
# msg = tm.render(menu=menu)
# print(msg)
########################


# cars = [
#     {'model': 'Audi', 'price': 63450},
#     {'model': 'BMW', 'price': 75990},
#     {'model': 'Mercedes', 'price': 73400},
#     {'model': 'Lexus', 'price': 51300},
#     {'model': 'Toyota', 'price': 25500},
# ]
#
# # tpl = "Автомобиль: {{ (cs | min(attribute='price')).model }}"
# # tpl = "Автомобиль: {{ cs | random }}"
# tpl = "Автомобиль: {{ cs | replace('model', 'brand') }}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.3},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.2},
# ]
#
# tpl = """
# {% for u in user -%}
#     {% filter upper %} {{ u.name }} {% endfilter %} {% filter string %} {{u.year}} - {{u.weight}} {% endfilter %}
# {% endfor -%}
# """
#
# tm = Template(tpl)
# msg = tm.render(user=persons)
# print(msg)

# html = '''
# {%- macro input(name, value='', type='text', size20) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{value}}" size="{{ size }}">
# {%- endmacro %}
#
# <p>{{ input('username') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password') }}</p> была ошибка, пересмотреть
# '''
#
# tm = Template(html)
# msg = tm.render()
# print(msg)


# html='''
# {%macro input}
# '''

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.3},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.2},
# ]
#
# html='''
#     {%macro list_users(list_of_users) -%}
#     <ul>
#         {% for u in list_of_users -%}
#         <li>{{ u.name }} {{ caller(u) }} </li>
#         {% endfor %}
#     </ul>
#     {%- endmacro %}
#
#     {% call(user) list_users(users) %}
#         <ul>
#             <li>age: {{user.year}}</li>
#             <li>weight: {{user.weight}}</li>
#         </ul>
#     {% endcall %}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Алексей', 'year': 18, 'weight': 78.5},
    {'name': 'Никита', 'year': 28, 'weight': 82.3},
    {'name': 'Виталий', 'year': 33, 'weight': 94.2},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons)

print(msg)

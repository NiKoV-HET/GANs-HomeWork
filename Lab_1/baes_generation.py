# возможные элементы стиля
from pprint import pprint
import random

styles = {
    'прическа':[
        'нет волос',
        'длинные в пучок',
        'длинные волнистые',
        'длинные прямые',
        'короткая волнистые',
        'короткая прямые',
        'короткая курчавые'
    ],
    'цвет волос':[
        'черный',
        'блонд',
        'каштановый',
        'пастельный розовый',
        'рыжий',
        'серебристо серый',
    ],
    'аксесуар':[
        'нет очков',
        'круглые очки',
        'солнцезащитные очки',
    ],
    'одежда':[
        'худи',
        'комбинезон',
        'футболка с круглым вырезом',
        'футболка с V-вырезом',
    ],
    'цвет одежды':[
        'черный',
        'синий',
        'серый',
        'зеленый',
        'оранжевый',
        'розовый',
        'красный',
        'белый'
    ],
}
# количество элементов стиля в наблюдаемых данных
styles_count = {
    'прическа':[
        7,
        0,
        1,
        23,
        1,
        11,
        7
    ],
    'цвет волос':[
        7,
        6,
        2,
        3,
        8,
        24,
    ],
    'аксесуар':[
        11,
        22,
        17,
    ],
    'одежда':[
        7,
        18,
        19,
        6,
    ],
    'цвет одежды':[
        4,
        5,
        6,
        8,
        6,
        8,
        7,
        6
    ],
}


set_summ = set()
for style_k, style_v in styles_count.items():
    set_summ.add(sum(style_v))

if len(set_summ) > 1:
    print("Количество элементов стиля не совпадает")
    exit(0)

summ = set_summ.pop()

# Generate person usual
p = {}

for k in styles:
    p[k] = []
    for n, i_style in enumerate(styles[k]):
        p_n = styles_count[k][n] / summ
        p[k].append(p_n)
pprint(p)

new_person = {}
for feature in styles:
    p_acc = p[feature]
    acc = styles[feature]
    rand = random.choices(acc,p_acc)
    new_person[feature] = rand[0]

if new_person['прическа'] == 'нет волос':
    new_person.pop('цвет волос')
print('Generate person usual:')
pprint(new_person)
print()




# Generate person using "Additive smoothing"
p = {}

for k in styles:
    p[k] = []
    for n, i_style in enumerate(styles[k]):
        p_n = (styles_count[k][n] + 1) / (summ + len(styles_count[k]))
        p[k].append(p_n)
pprint(p)

new_person = {}
for feature in styles:
    p_acc = p[feature]
    acc = styles[feature]
    rand = random.choices(acc,p_acc)
    new_person[feature] = rand[0]

if new_person['прическа'] == 'нет волос':
    new_person.pop('цвет волос')
print('Generate person using "Additive smoothing":')
pprint(new_person)
print()




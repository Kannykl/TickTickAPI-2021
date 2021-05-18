# Приложение для взаимодействия с Tick-Tick посредством REST API

Разработка проекта ведется на **python 3.8** с использованием библиотеки **requests**, для тестирования используется библиотека **pytest 6.2.2**

------

<b>Планируется реализовать:</b>

- [x] Авторизация в приложении
- [x] Получение проектов, задач
- [x] Создание задач, проектов, тегов

##### Пример использования:

Авторизация в приложении

```
username = 'MyProfile'
password = '123456789'
API = TickAPI(username, password)
```

Добавление проекта

```
project_title = API.add_project('НазваниеПроекта', colour='синий')
```

Получение проекта по названию/цвету

```
project = API.get_project_by_title('НазваниеПроекта')
project = API.get_project_by_colour('синий')
```

Добавление задачи

```
project_id = API.get_project_by_title('НазваниеПроекта')
task = API.add_task('НазваниеЗадачи', project_id, content='МояКрутаяЗадача', tag='МойКрутойТег')
```

Добавление тега

```
tag = API.add_tag('МойКрутойТег', 'красный')
```

Получение всех тегов/тега по имени

```
tags = API.get_tags()
tag = API.get_tag_by_name('МойКрутойТег')
```

##### Запуск

*Перед запуском тестов убедитесь, что установили все зависимости*

```
pip install -r requirements.txt
pytest --cov=src tests/tests.py
```


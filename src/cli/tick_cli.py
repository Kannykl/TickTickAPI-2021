import sys
import click
sys.path.append("..")

from src.tick_tick import TickAPI


def authentication(login, password):
    with open(".tick", "w") as file:
        file.writelines([f"{login}\n", password])
    return login, password


def get_api():
    try:
        with open(".tick", "r") as file:
            username, password = file.readlines()
        api = TickAPI(username.strip(), password.strip())
    except FileNotFoundError:
        print("Вам нужно авторизироваться, воспользуйтесь опцией --login")
        api = ""
    return api


@click.command()
@click.option("--login",
              is_flag=True,
              help="авторизация в TickTick, нужно указать логин и пароль от аккаунта")
@click.option("--get_projects_id", is_flag=True)
@click.option("--get_tasks_by_project_id", is_flag=True)
@click.option("--get_completed_tasks_by_project_id", is_flag=True)
@click.option("--get_tags", is_flag=True)
@click.option("--get_tag_by_name", is_flag=True)
@click.option("--get_tasks_by_title", is_flag=True)
@click.option("--get_project_by_id", is_flag=True)
@click.option("--get_project_by_name", is_flag=True)
@click.option("--get_projects_by_colour", is_flag=True)
@click.option("--add_task", is_flag=True)
@click.option("--add_tag", is_flag=True)
@click.option("--delete_project", is_flag=True)
@click.option("--delete_task", is_flag=True)
@click.option("--delete_tag", is_flag=True)
@click.option("--empty_trash", is_flag=True)
@click.option("--add_project", is_flag=True)
@click.argument("arg1", default="")
@click.argument("arg2", default="")
@click.argument("arg3", default="")
def main(
    login,
    arg1,
    arg2,
    arg3,
    get_projects_id,
    get_tasks_by_project_id,
    get_completed_tasks_by_project_id,
    get_tags,
    get_tag_by_name,
    add_task,
    add_tag,
    delete_project,
    delete_task,
    delete_tag,
    add_project,
    empty_trash,
    get_tasks_by_title,
    get_project_by_id,
    get_project_by_name,
    get_projects_by_colour,
):
    if login:
        if all((arg1, arg2)):
            authentication(arg1, arg2)
        else:
            print('Введите логин и пароль для авторизации')
    elif get_projects_id:
        api = get_api()
        if api:
            projects_id = api.get_projects_id()
            print("ID проектов: ", projects_id)
    elif get_tasks_by_project_id:
        api = get_api()
        if api:
            tasks = api.get_tasks_by_project_id(arg1)
            print("Задания: ", tasks)
    elif get_completed_tasks_by_project_id:
        api = get_api()
        if api:
            tasks = api.get_completed_tasks_by_project_id(arg1, arg2)
            print("Завершенные задания: ", tasks)

    elif get_tags:
        api = get_api()
        if api:
            tags = api.get_tags()
            print("Теги: ", tags)
    elif get_tag_by_name:
        api = get_api()
        if api:
            tag = api.get_tag_by_name(arg1)
            print("Теги: ", tag)
    elif add_task:
        api = get_api()
        if api:
            task_name = api.add_task(arg1, arg2, arg3)
            print(f'Успешно создано задание "{task_name}"')
    elif add_tag:
        api = get_api()
        if api:
            created_tag = api.add_tag(arg1, arg2)
            print(f"Тег {created_tag} создан")
    elif delete_project:
        api = get_api()
        if api:
            deleted_project = api.delete_project(arg1)
            print(f"{deleted_project} удален")
    elif delete_task:
        api = get_api()
        if api:
            deleted_task = api.delete_task(arg1, arg2)
            print(f"{deleted_task} удалена")
    elif delete_tag:
        api = get_api()
        if api:
            deleted_tag = api.delete_tag(arg1)
            print(f"{deleted_tag} тег удален")
    elif add_project:
        api = get_api()
        if api:
            created_project = api.add_project(arg1, arg2, arg3)
            print(f"{created_project} создан")
    elif empty_trash:
        api = get_api()
        if api:
            api.empty_trash()
            print("Корзина очищена")
    elif get_tasks_by_title:
        api = get_api()
        if api:
            tasks = api.get_tasks_by_title(arg1, arg2)
            print(tasks)
    elif get_project_by_id:
        api = get_api()
        if api:
            project = api.get_project_by_id(arg1)
            print(project)
    elif get_project_by_name:
        api = get_api()
        if api:
            project = api.get_project_by_name(arg1)
            print(project)
    elif get_projects_by_colour:
        api = get_api()
        if api:
            projects = api.get_projects_by_colour(arg1)
            print(projects)


if __name__ == '__main__':
    main()

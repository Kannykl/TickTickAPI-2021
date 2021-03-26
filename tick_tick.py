import requests


class TickAPI:

    def __init__(self, username, passwd):
        self.session = requests.Session()
        self.session.headers = {
            'Content-Type': 'application/json',
            'accept': '*/*',
        }
        request = self.session.post("https://api.ticktick.com/api/v2/user/signon?wc=true", json={
            'username': f'{username}',
            'password': f'{passwd}',
        })
        if request.status_code == 200:
            token = request.json()['token']
            client_id = request.json()['userId']
            self.token = token
            self.client_id = client_id
        else:
            raise AttributeError('Неверный логин или пароль')

    def get_projects(self):
        projects = list()
        url = 'https://api.ticktick.com/api/v2/projects'
        request = self.session.get(url, cookies={'t': f'{self.token}'})
        if request.status_code == 200:
            data = request.json()
            for i in data:
                id_ = i['id']
                projects.append(id_)
            if len(projects) == 0:
                return None
        else:
            raise Exception('Не удалось получить проекты')
        return projects

    def get_tasks_of_project(self, project_id):
        tasks_list = list()
        url = 'https://api.ticktick.com/api/v2/batch/check/1'
        request = self.session.get(url, cookies={'t': f'{self.token}'})
        if request.status_code == 200:
            data = request.json()
            tasks = data['syncTaskBean']['update']
            for task in tasks:
                if task['projectId'] == project_id:
                    tasks_list.append(task)
        else:
            raise Exception('Не удалось получить задачи проекта')
        return tasks_list

    def get_completed_tasks(self, project_id):
        url = f'https://api.ticktick.com/api/v2/project/{project_id}/completed/?limit=50'
        request = self.session.get(url, cookies={'t': f'{self.token}'})
        if request.status_code == 200:
            pass
        else:
            raise BaseException('Не удалось получить завершенные задания')

    def add_task(self, name):
        url = 'https://ticktick.com/api/v2/task'
        request = self.session.post(url)
        if request.status_code == 200:
            return name
        else:
            raise BaseException('Не удалось создать задание')

<br/>
<p align="center">
  <h3 align="center">Новый сайт института мерзлотоведения demo - https://imz.goykt.ru</h3>

  <p align="center">
    Репозиторий создан как пример для новых сайтов других институтов
    <br/>
    <br/>
  </p>
</p>



## About The Project

Этот проект был создан как пример сайтов научных институтов

Зачем:

* Сообщать новости института
* Писать объявления
* Распространять публикации
* Иметь прозрачную структуру
* Хранить информацию в соответствии с правилами для научных организаций

## Ближайшие цели
- [ ] Добавить линтеры, форматеры
- [ ] Добавить автотесты
- [ ] Добавить Dockerfile и docker-compose.dev для окружения
- [ ] Добавить PostgreSQL и Redis
- [ ] Добавить регистрацию сотрудников и прикрепление их профилей к учетным записям
- [ ] Добавить CI/CD

## Built With

Сайт сделан на Python Django 

## Getting Started

Это пример как вы можете запустить проект в несколько шагов
To get a local copy up and running follow these simple example steps.

### Prerequisites

Что у вас должно быть заранее установлено

* python 3.11
* git

Протестировано на ubuntu 22.04
```sh
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install python3.11 git
```

### Installation

1. Установить python

2. Склонировать репозиторий

```sh
git clone https://github.com/x-victor/site_imz_demo
```

3. Создание виртуального окружения и активация

```sh
cd %project_folder%
python3.11 -m venv venv
. venv/bin/activate
```

4. Установка зависимостей

```sh
pip install -r requirements
```

5. Напишите .env файл в папке проекта, пример:
```sh
SECRET_KEY=super-secret-key
DEBUG=True
```

## Usage

Для первого запуска используйте следующие команды

```sh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Для доступов к админ панели по умолчанию зайдите по адресу http://127.0.0.1/admin

## Roadmap

See the [open issues](https://github.com/x-victor/imz_site_demo/issues) for a list of proposed features (and known issues).

## Contributing

Помощь - это то, что делает сообщество с открытым исходным кодом таким удивительным местом, где можно учиться, вдохновлять и творить. Мы ** высоко ценим любой ваш вклад **.
* Если у вас есть предложения по добавлению или удалению проектов, не стесняйтесь [открыть проблему](https://github.com/x-victor/imz_site_demo/issues/new ), чтобы обсудить это, или непосредственно создать запрос на извлечение после того, как вы отредактируете *README.md * файл с необходимыми изменениями.
* Пожалуйста, обязательно проверьте свою орфографию и грамматику.
* Создайте индивидуальный PR для каждого предложения.

### Creating A Pull Request

1. Создайте форк на проект
2. Создайте свою ветвь (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте свои изменения (`git commit -m 'Добавляет некоторые удивительные функции")
4. Перейдите к ветке (`git push origin feature/AmazingFeature`)
5. Откройте Pull request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/x-victor/imz_site_demo/blob/main/LICENSE.md) for more information.

## Authors

* **Павлов Виктор** - *Developer* - [Павлов Виктор](https://github.com/x-victor/) - *https://t.me/nire1*

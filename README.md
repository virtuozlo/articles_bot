# articles_bot
## Описание проекта
<p>Бот может проходить по папкам и подпапкам, пока не наткнется на текстовый файл и предложит вывести его в Telegram</p>
<p>Параллельно с этим проводится поиск фото к текущем файлам / директориям</p>
<p>Фото грузятся идентично директории text_files</p>

## Порядок установки
<p>В консоли загрузить виртуальное окружение</p>

 `$ pip install -r requirements.txt`

Получить токен бота телеграмм в [BotFather](https://t.me/BOTSplus/288).

Создать файл .env и внести необходимые переменные согласно шаблону [.env.template](\.env.template)

<p>Запустить Unittest Python</p>
```$python -m unittest```
<p>Создастся папка для хранения текстовых файлов с description и для хранения фото</p>
<p>Создать папки text_files. Поместить файл description для отправки сообщения ботом.</p>
<p>Файл не может быть пустым, так как запрещено отправлять пустые сообщения в тлг</p>
<p>Вложенность подпапок может доходить до 3-х. Название папки/файла не должно превышать 10 символов</p>

## Взаимодейтсвие с БД
В программе установлена возможность записи данных о пользователе <br>
(id_user, nickname(optional), counter(Количество раз, когда выводилась статья))

Для пользования базой данных, после её установки и настройки, необходимо в директории bot_work создать файл database.ini [Прописать в нем](\database.ini.example)
~~~
[postgresql]
host=localhost
database=database_name
user=user_name
password=password_user_name
~~~



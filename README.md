# articles_bot
## Описание проекта
Бот может проходить по папкам и подпапкам, пока не наткнется на текстовый файл и предложит вывести его в Telegram
Параллельно с этим проводится поиск фото к текущем файлам / директориям
Фото грузятся идентично директории text_files

## Порядок установки
В консоли загрузить виртуальное окружение
> $ pip install -r requirements.txt

Получить токен бота телеграмм в [BotFather](https://t.me/BOTSplus/288).

Создать файл .env и внести необходимые переменные согласно шаблону .env.template

PATH_TO_FILES - директория до бота/text_files/

PATH_TO_PHOTO - директория до бота/photo/

## Взаимодейтсвие с БД
В программе установлена возможность записи данных о пользователе <br>
(id_user, nickname(optional), counter(Количество раз, когда выводилась статья))

Для пользования базой данных, после её установки и настройки, необходимо в директории bot_work создать файл database.ini

[Прописать в нем](C:\Users\Иван\Desktop\bot_work\database.ini.example)
~~~
[postgresql]
host=localhost
database=database_name
user=user_name
password=password_user_name
~~~



Общее описание проекта
======================
>В данном проекте упор делался на масштабируемость проекта,
>Поэтому проект планируется развивать дальше,
>так же при разработке классов я старался опираться на все принципы **SOLID**.
---
В пакете ***src*** находится исходный код проекта

---

**В данном пакете есть четыре раздела:**
-
+ ***api_classes***
+ ***interact_func***
+ ***savers***
+ ***vacancy_classes***
---
Подробнее про интерактивную функцию:
---
>Данная функция не является полноценной реализаций проекта, иначе говоря, несколько пакетов
> кода писались не для неё, а скорее как удобный инструмент для программиста.
>>Данная функция служит скорее примером того, что можно сделать с помощью данных классов
> 
**Интерактивная функция называется ***main*****, состоит из нескольких функций, а именно:
+ **platform_act** - функция получения вакансий с платформы
+ **file_act** - функция получения вакансий из файла
+ **operator_act** - функция для работы с объектом - обработчиком вакансий, реализует мини-язык запросов
+ **main** - сама общая функция, запускает программу
---
Интерактивная функция в процессе:
---
В первую очередь запустится **main** и предложит ввести значения 1 или 2:
+ 1 - получение вакансий с платформы объявлений
+ 2 - получение вакансий из существующего файла с вакансиями, созданного ранее

>При вводе **1** управление будет передано функции **platform_act**,\
> при вводе **2** - **file_act**
---
Действие **platform_act**:
---
Функция запросит платформу для поиска, а именно **HH** или **SJ**
>Для работы с superjob установите пользовательскую переменную среды с именем **SJ_API_KEY**,
> в неё запишите ключ для работы с API от superjob

После ввода платформы функция попросит ввести ключевое слово для поиска - можно пропустить,
в этом случае всё будет работать

После получения ключевого слова, функция запрашивает файл для сохранения, название списка вакансий,
вызывает метод для подключения к API, получает вакансии и передаёт управление **operator_act**
---
Действие file_act:
---
В случае, если в качестве действия введено **2**, **main** передаёт управление **file_act**, 
которая запрашивает файлы для открытия и сохранения, после чего предаёт управление **operator_act**
---
Действие operator_act:
---
Функция запускает мини-язык запросов, небольшая версия терминала, в котором реализованы команды для
работы с вакансиями:
+ **выход** - завершить работу программы, сохранить изменения
+ **сорт_зп** - отсортировать вакансии по заработной плате
+ **вывод** - вывести список вакансий на данный момент
+ **фильтр_сл <ключевое слово[str]>** - фильтрация по ключевому слову
+ **фильтр_зп <зп_от[int]>-<зп_до[int]>** - фильтрация по диапазону зарплат
+ **топ <количество вакансий[int]>** - оставляет только топ вакансии по зп, количество вакансий указывает пользователь
>Каждое применение функции изменяет список вакансий, т. е. если например применить сначала "фильтр_сл SQL", а затем
> "топ 5", то в списке окажутся топ 5 вакансий c ключевым словом SQL

После завершения работы с вакансиями через "выход", изменения запишутся в указанный файл, в случае, если 
возникнет ошибка python, то вакансии запишутся без изменений

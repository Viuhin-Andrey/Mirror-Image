# Mirror Image

### Для работы необходимо:

🐍 Python (версия 3.12 и выше. Более старые версии не были протестированы) - https://www.python.org/ (небольшая инструкция)↓

⚪ Скачиваете инсталлер и сразу ставите галочку о ✅️ "Add python.exe to Path" (необходима, чтобы скачать библиотеки через cmd, также есть возможность уже после установки проставить данный путь, в самом низу инструкция)

🖥 После установки python запустите cmd

🖥 Введите команду для установки всех используемых библиотек: `pip install opencv-python numpy keyboard mss pyautogui`

✔ Далее нажмите на скрипт правой кнопкой мыши и выберите "открыть с помощью", установите приложение по умолчанию python

⚙️ Добавьте удобный способ запуска скрипта (у меня это autoHot pie menu - https://github.com/dumbeau/AutoHotPie/releases)

![ScriptView](https://github.com/user-attachments/assets/ab1468e7-e45e-4716-985a-5ee423d0877b)


### Функционал

🕹️ M - отвечает за отзеркаливание изображения

🕹️ S - сохранение по прописанному в скрипте пути (по умолчанию это: C:\Mirror_Screenshots)

🕹️ esc - закрытие программы (закрытие работает только так или через диспетчер задач)

### Проблемы, требующие фикса 🌱

Закрытие программы реализовано только через esc, если закрыть ее через правую кнопку мыши "закрыть окно", оно вновь откроется.

Сохранение изображений не работает должным образом. Не сохраняет если в пути есть кириллица. Перезаписывает изображения, после нового открытия (запись ведется с тегами original и mirrored, перезаписываются именно по названию, будьте аккуратны)

### Инструкция, если не установлен path к скриптам питона:

**1 способ (на постоянное пользование)**

Вам нужно установить путь к pip в переменные окружения, это можно сделать при установке python выбрав пункт Add Python to PATH.

Если вы уже установили, но забыли выбрать этот пункт, можно добавить путь вручную:

Панель управления -> Система -> Дополнительные параметры системы -> Переменные среды
Вы увидите 2 окошка, Переменные среды пользователя для <username> и Системные переменные, вам нужно первое, нажимаем на переменную Path -> Изменить, далее вы увидите поле Значение переменной, нажмите создать и добавьте путь к директории где находится pip (например, C:\Users\Andrew\AppData\Local\Programs\Python\Python312\Scripts, путь к директории Python может отличаться).

**2 способ (придется постоянно вводить в консоль)**

Откройте cmd и пропишите путь до директории pip

`cd C:\Users\Andrew\AppData\Local\Programs\Python\Python312\Scripts` после чего можете вводить `pip install opencv-python numpy keyboard mss pyautogui`

### Небольшая демонстрация работы на проекте:

![Untitled-1](https://github.com/user-attachments/assets/dd2a1016-cbda-47a4-a53f-d66bc63fbe84)


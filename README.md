# Автотесты для сайта [PuppyCase](https://315982.website3.me/)

## Обзор

Этот репозиторий содержит комплексный набор автоматизированных тестов для сайта [PuppyCase](https://315982.website3.me/).

Кроме того, проект использует базу данных SQLite (`customers.db`) для тестовых данных, связанных с процессом оформления заказа.

---

## Используемые технологии

- **Python 3.12**
- **Playwright**: автоматизация веб-браузеров
- **pytest**: тестовый фреймворк
- **Allure Report**: отчетность и визуализация тестов
- **SQLite3**: хранилище тестовых данных
- **Flake8**: проверка качества кода

---

## Интеграция с базой данных

Проект использует базу данных SQLite (`customers.db`) для хранения данных клиентов, используемых в тестах, связанных с оформлением заказов. 

База данных предварительно заполнена **30 тестовыми записями клиентов**.

### Структура таблицы:

```
id          INTEGER                       # Уникальный идентификатор
first_name  TEXT                          # Имя клиента
last_name   TEXT                          # Фамилия клиента
email       TEXT                          # Email клиента
address     TEXT                          # Адрес клиента
city        TEXT                          # Город проживания
country     TEXT                          # Страна проживания
state       TEXT                          # Регион/область
phone       TEXT                          # Контактный номер клиента
```

Файл `customers.db` автоматически используется фикстурой `customer_db` в соответствующих тестах (например, `test_place_order`), не требуя ручной настройки.

---

## Установка

### Требования:

Убедитесь, что у вас установлен **Python 3.12**.

### Инструкции по установке:

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/GlebRadtsevich/Diplom_PythonAQA
    cd Diplom_PythonAQA
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. Установите необходимые зависимости:
    ```bash
    pip install -r requirements.txt
    ```

---

## Запуск тестов

### Запуск всех тестов

```bash
python -m pytest

HEADLESS=true python -m pytest # Linux/macOS запуск в headless-режиме
$env:headless="true"; python -m pytest # Windows запуск в headless-режиме
```

### Генерация отчетов Allure

1. Запустите тесты и сохраните результаты:
    ```bash
    python -m pytest --alluredir allure-results
    ```
2. Сгенерируйте и откройте отчет:
    ```bash
    allure serve allure-results
    ```
---

## Интеграция с Docker

Для удобного запуска тестов в изолированных средах проект включает `docker-compose.yml` и `Dockerfile`. Эти конфигурации позволяют запускать различные группы тестов внутри контейнеров Docker.

### Запуск тестов с `docker-compose.yml`:

```bash
docker-compose up               # Запуск всех тестов в параллельном режиме
docker-compose down             # Остановка и удаление контейнеров
```

### Запуск тестов с `Dockerfile`:

```bash
docker build -t <имя образа> .      # Создание docker-образа
docker run --rm <имя образа>        # Запуск контейнера с docker-образом и его удаление после выполнения
```

### Запуск Allure-отчетов в Docker:
Если надо посмотреть отчёт Allure после тестов:

```bash
docker-compose up allure-server       # Запуск контейнера с docker-образом и его удаление после выполнения
```

Затем надо открыть браузер и зайти на http://localhost:5050

Примечание: тесты в Docker выполняются в headless-режиме.
---

## Структура проекта

``` vbnet
├── .github/                        # GitHub workflows (тесты на pull request & push в main)
├── core/                           # Базовые методы
├── data/                           # Данные для тестов
├── pages/                          # Классы Page Object Model (POM)
├── tests/                          # Тесты
├── .gitignore                      # Файл исключений Git
├── pytest.ini                      # Конфигурация Pytest
├── README.md                       # Документация проекта
├── requirements.txt                # Зависимости Python

```

---

## Автор

Автор: Gleb Radtsevich  
GitHub: [github.com/GlebRadtsevich](https://github.com/GlebRadtsevich)

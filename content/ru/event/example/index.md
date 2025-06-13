---
title: Пример доклада

event: Конференция Hugo Blox Builder
event_url: https://example.org

location: Штаб-квартира Hugo Blox Builder
address:
  street: 450 Serra Mall
  city: Стэнфорд
  region: CA
  postcode: '94305'
  country: Соединённые Штаты

summary: Пример доклада с использованием функции Markdown-слайдов Hugo Blox Builder.
abstract: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellusac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum. Sed ac faucibus dolor, scelerisque sollicitudin nisi. Cras purus urna, suscipit quis sapien eu, pulvinar tempor diam.'

# Время начала и окончания доклада.
#   Время окончания можно скрыть, добавив в начале строки `#`.
date: '2030-06-01T13:00:00Z'
date_end: '2030-06-01T15:00:00Z'
all_day: false

# Дата публикации страницы расписания (НЕ дата доклада).
publishDate: '2017-01-01T00:00:00Z'

authors:
  - admin

tags: []

# Это выделенный доклад? (true/false)
featured: false

image:
  caption: 'Фото: [**Unsplash**](https://unsplash.com/photos/bzdhc5b3Bxs)'
  focal_point: Right

#links:
#  - icon: twitter
#    icon_pack: fab
#    name: Подписаться
#    url: https://twitter.com/georgecushen
url_code: 'https://github.com'
url_pdf: ''
url_slides: 'https://slideshare.net'
url_video: 'https://youtube.com'

# Markdown-слайды (опционально).
#   Свяжите этот доклад с Markdown-слайдами.
#   Просто укажите имя файла слайдов без расширения.
#   Например, `slides = "example-slides"` указывает на `content/slides/example-slides.md`.
#   Иначе укажите `slides = ""`.
slides: ""

# Проекты (опционально).
#   Свяжите этот пост с одним или несколькими проектами.
#   Просто укажите папку или имя проекта без расширения.
#   Например, `projects = ["internal-project"]` указывает на `content/project/deep-learning/index.md`.
#   Иначе укажите `projects = []`.
projects:
  - example
---

{{% callout note %}}
Нажмите кнопку **Slides** выше, чтобы посмотреть встроенную функцию слайдов.
{{% /callout %}}

Слайды можно добавить несколькими способами:

- **Создать** слайды с помощью функции [_Slides_](https://docs.hugoblox.com/reference/content-types/) Hugo Blox Builder и связать через параметр `slides` в front matter файла доклада
- **Загрузить** готовую презентацию в папку `static/` и связать через параметр `url_slides` в front matter файла доклада
- **Встроить** слайды (например, Google Slides) или видео с презентацией на этой странице с помощью [шорткодов](https://docs.hugoblox.com/reference/markdown/).

Дополнительные детали мероприятия, включая [элементы страницы](https://docs.hugoblox.com/reference/markdown/), такие как галереи изображений, можно добавить в тело этой страницы.
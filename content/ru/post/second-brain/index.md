---
title: 🧠 Отточите мышление с помощью второго мозга
summary: Создайте личную базу знаний и делитесь знаниями с коллегами.
date: 2023-10-26
authors:
  - admin
tags:
  - Второй мозг
  - Markdown
image:
  caption: 'Источник изображения: [**Unsplash**](https://unsplash.com)'
---

Создайте личную базу знаний и делитесь своими знаниями с коллегами.

Веб-фреймворк Hugo Blox предоставляет одну из самых гибких возможностей для ведения заметок.

Создайте мощную базу знаний, работающую на основе локальной папки с простыми Markdown-файлами.

Используйте её как второй мозг — публикуйте знания на сайте для всех или храните в приватном репозитории на GitHub с защищённым паролем сайтом только для себя.

## Ментальные карты (Mindmaps)

Hugo Blox поддерживает расширение Markdown для ментальных карт.

Этот открытый формат позволяет редактировать карты в других популярных инструментах, например, Obsidian.

Просто вставьте блок кода Markdown с меткой `markmap` и при необходимости задайте высоту карты, как в примере ниже.

Ментальные карты создаются простым списком в Markdown внутри блока `markmap`, с отступами для создания вложенных уровней:

<div class="highlight">
<pre class="chroma">
<code>
```markmap {height="200px"}
- Hugo Modules
  - Hugo Blox
  - blox-plugins-netlify
  - blox-plugins-netlify-cms
  - blox-plugins-reveal
```
</code>
</pre>
</div>

отобразится как

```markmap {height="200px"}
- Hugo Modules
  - Hugo Blox
  - blox-plugins-netlify
  - blox-plugins-netlify-cms
  - blox-plugins-reveal
```

А вот более продвинутая карта с форматированием, блоками кода и математикой:

<div class="highlight">
<pre class="chroma">
<code>
```markmap
- Mindmaps
  - Ссылки
    - [Документация Hugo Blox](https://docs.hugoblox.com/)
    - [Сообщество Discord](https://discord.gg/z8wNYzb)
    - [GitHub](https://github.com/HugoBlox/hugo-blox-builder)
  - Особенности
    - Форматирование Markdown
    - **жирный** ~~зачёркнутый~~ *курсив*
    - многострочный
      текст
    - `встроенный код`
    -
      ```js
      console.log('привет');
      console.log('блок кода');
      ```
    - Математика: $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$
```
</code>
</pre>
</div>

отобразится как

```markmap
- Mindmaps
  - Ссылки
    - [Документация Hugo Blox](https://docs.hugoblox.com/)
    - [Сообщество Discord](https://discord.gg/z8wNYzb)
    - [GitHub](https://github.com/HugoBlox/hugo-blox-builder)
  - Особенности
    - Форматирование Markdown
    - **жирный** ~~зачёркнутый~~ *курсив*
    - многострочный
      текст
    - `встроенный код`
    -
      ```js
      console.log('привет');
      console.log('блок кода');
      ```
    - Математика: $x = {-b \pm \sqrt{b^2-4ac} \over 2a}$
```

## Выделение текста

<mark>Выделяйте</mark> важный текст с помощью тега `mark`:

```html
<mark>Выделенный текст</mark>
```

## Вызовы внимания (Callouts)

Используйте [callouts](https://docs.hugoblox.com/reference/markdown/#callouts) (также известные как _врезки_, _подсказки_ или _предупреждения_), чтобы привлечь внимание к заметкам, советам и предупреждениям.

Если обернуть абзац в `{{%/* callout note */%}} ... {{%/* /callout */%}}`, он отобразится как врезка:

```markdown
{{%/* callout note */%}}
Markdown-врезка полезна для отображения заметок, подсказок или определений для ваших читателей.
{{%/* /callout */%}}
```

отобразится как

{{% callout note %}}
Markdown-врезка полезна для отображения заметок, подсказок или определений для ваших читателей.
{{% /callout %}}

Или используйте тип `warning`, чтобы читатели не пропустили важные детали:

{{% callout warning %}}
Markdown-врезка полезна для отображения заметок, подсказок или определений для ваших читателей.
{{% /callout %}}

## Вам понравилась эта страница? Поделитесь ею 🙌
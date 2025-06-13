---
title: Изучайте JavaScript
summary: Легко изучайте JavaScript за 10 минут!
date: 2023-10-24
type: docs
math: false
tags:
  - JavaScript
image:
  caption: 'Встраивайте мультимедиа, такие как видео и математические формулы LaTeX'
---

[Hugo Blox Builder](https://hugoblox.com) создан для удобства технических авторов контента. Вы можете сосредоточиться на содержании, а Hugo Blox Builder, на котором построен этот шаблон, позаботится обо всем остальном.

**Встраивайте видео, подкасты, код, математические формулы LaTeX и даже проверяйте студентов!**

На этой странице вы найдете примеры типов технического контента, которые можно отобразить с помощью Hugo Blox.

## Видео

Преподавайте свой курс, делясь видео со студентами. Выберите один из следующих способов:

{{< youtube D2vj0WcvH5c >}}

**Youtube**:

    {{</* youtube w7Ft2ymGmfc */>}}

**Bilibili**:

    {{</* bilibili id="BV1WV4y1r7DF" */>}}

**Видео файл**

Видео можно добавить на страницу, поместив их в медиатеку `assets/media/` или в папку [страницы](https://gohugo.io/content-management/page-bundles/), а затем вставив с помощью шорткода _video_:

    {{</* video src="my_video.mp4" controls="yes" */>}}

## Подкаст

Вы можете добавить подкаст или музыку на страницу, поместив MP3 файл в папку страницы или медиатеку и вставив аудио на страницу с помощью шорткода _audio_:

    {{</* audio src="ambient-piano.mp3" */>}}

Попробуйте:

{{< audio src="ambient-piano.mp3" >}}

## Проверка студентов

Обеспечьте простую и интересную самопроверку, показывая решения задач с помощью шорткода `spoiler`:

```markdown
{{</* spoiler text="👉 Нажмите, чтобы увидеть решение" */>}}
Вы нашли меня!
{{</* /spoiler */>}}
```

будет отображаться как

{{< spoiler text="👉 Нажмите, чтобы увидеть решение" >}} Вы нашли меня 🎉 {{< /spoiler >}}

## Математика

Hugo Blox Builder поддерживает расширение Markdown для математических формул в $\LaTeX$. Вы можете включить эту функцию, переключив опцию `math` в файле `config/_default/params.yaml`.

Чтобы отобразить _встроенную_ или _блочную_ математику, оберните LaTeX формулы с помощью `{{</* math */>}}$...${{</* /math */>}}` или `{{</* math */>}}$$...$${{</* /math */>}}`, соответственно.

{{% callout note %}}
Мы оборачиваем LaTeX математику в шорткод Hugo Blox _math_, чтобы Hugo не обрабатывал её как Markdown.
{{% /callout %}}

Пример **блочной математики**:

```latex
{{</* math */>}}
$$
\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}
$$
{{</* /math */>}}
```

будет отображаться как

{{< math >}}
$$\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}$$
{{< /math >}}

Example **inline math** `{{</* math */>}}$\nabla F(\mathbf{x}_{n})${{</* /math */>}}` renders as {{< math >}}$\nabla F(\mathbf{x}_{n})${{< /math >}}.

Пример **встроенной математики** `{{</* math */>}}$
abla F(\mathbf{x}_{n})${{</* /math */>}}` отображается как {{< math >}}$
abla F(\mathbf{x}_{n})${{< /math >}}.

Пример **многострочной математики** с переносом строки (`\`):

```latex
{{</* math */>}}
$$f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
1-p_{0}^{*} & \text{if }k=0.\end{cases}$$
{{</* /math */>}}
```

будет отображаться как

{{< math >}}

$$
f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{if }k=1, \\
1-p_{0}^{*} & \text{if }k=0.\end{cases}
$$

{{< /math >}}

## Код

Hugo Blox Builder использует расширение Markdown Hugo для подсветки синтаксиса кода. Тему подсветки можно выбрать в файле `config/_default/params.yaml`.


    ```python
    import pandas as pd
    data = pd.read_csv("data.csv")
    data.head()
    ```

будет отображаться как

```python
import pandas as pd
data = pd.read_csv("data.csv")
data.head()
```

## Встроенные изображения

```go
{{</* icon name="python" */>}} Python
```

будет отображаться как

{{< icon name="python" >}} Python

## Эта страница была полезной? Поделитесь 🙌
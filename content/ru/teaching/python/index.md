---
title: Изучайте Python  
summary: Легко изучайте Python за 10 минут!  
date: 2023-10-24  
type: docs  
math: false  
tags:  
  - Python  
image:  
  caption: 'Встраивайте богатый контент: видео и LaTeX-математику'  
---

[Hugo Blox Builder](https://hugoblox.com) создан для того, чтобы технические авторы контента работали максимально комфортно. Вы можете сосредоточиться на содержании, а Hugo Blox Builder, на котором построен этот шаблон, позаботится обо всём остальном.

**Встраивайте видео, подкасты, код, LaTeX-математику и даже тестируйте студентов!**

На этой странице вы найдёте примеры различных типов технического контента, которые можно отобразить с помощью Hugo Blox.

## Видео

Обучайте курс, делясь видео со своими студентами. Выберите один из следующих способов:

{{< youtube D2vj0WcvH5c >}}

**YouTube**:

    {{</* youtube w7Ft2ymGmfc */>}}

**Bilibili**:

    {{</* bilibili id="BV1WV4y1r7DF" */>}}

**Видео-файл**

Видео можно добавить на страницу, разместив их в вашей медиатеке `assets/media/` или в [папке страницы](https://gohugo.io/content-management/page-bundles/), а затем встроить с помощью шорткода _video_:

    {{</* video src="my_video.mp4" controls="yes" */>}}

## Подкаст

Вы можете добавить подкаст или музыку на страницу, поместив MP3-файл в папку страницы или медиатеку и затем встроив аудио с помощью шорткода _audio_:

    {{</* audio src="ambient-piano.mp3" */>}}

Попробуйте:

{{< audio src="ambient-piano.mp3" >}}

## Тестирование студентов

Организуйте простую и увлекательную самопроверку, показывая решения заданий с помощью шорткода `spoiler`:

```markdown
{{</* spoiler text="👉 Нажмите, чтобы увидеть решение" */>}}
Вы меня нашли!
{{</* /spoiler */>}}
```

отобразится как

{{< spoiler text="👉 Нажмите, чтобы увидеть решение" >}} Вы меня нашли 🎉 {{< /spoiler >}}

## Математика

Hugo Blox Builder поддерживает расширение Markdown для $\LaTeX$-математики. Вы можете включить эту функцию, переключив опцию `math` в вашем файле `config/_default/params.yaml`.

Чтобы отобразить _встроенную_ или _блочную_ математику, оберните LaTeX формулы в `{{</* math */>}}$...${{</* /math */>}}` или `{{</* math */>}}$$...$${{</* /math */>}}` соответственно.

{{% callout note %}}  
Мы оборачиваем LaTeX-математику в шорткод Hugo Blox _math_, чтобы избежать рендеринга формул как Markdown.  
{{% /callout %}}

Пример **блочной математики**:

```latex
{{</* math */>}}
$$
\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}
$$
{{</* /math */>}}
```

отобразится как

{{< math >}}
$$\gamma_{n} = \frac{ \left | \left (\mathbf x_{n} - \mathbf x_{n-1} \right )^T \left [\nabla F (\mathbf x_{n}) - \nabla F (\mathbf x_{n-1}) \right ] \right |}{\left \|\nabla F(\mathbf{x}_{n}) - \nabla F(\mathbf{x}_{n-1}) \right \|^2}$$
{{< /math >}}

Пример **встроенной математики** `{{</* math */>}}$\nabla F(\mathbf{x}_{n})${{</* /math */>}}` отобразится как {{< math >}}$\nabla F(\mathbf{x}_{n})${{< /math >}}.

Пример **многострочной математики** с использованием переноса строк (`\\`):

```latex
{{</* math */>}}
$$f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{если }k=1, \\
1-p_{0}^{*} & \text{если }k=0.\end{cases}$$
{{</* /math */>}}
```

отобразится как

{{< math >}}

$$
f(k;p_{0}^{*}) = \begin{cases}p_{0}^{*} & \text{если }k=1, \\
1-p_{0}^{*} & \text{если }k=0.\end{cases}
$$

{{< /math >}}

## Код

Hugo Blox Builder использует расширение Markdown Hugo для подсветки синтаксиса кода. Тему для кода можно выбрать в файле `config/_default/params.yaml`.


    ```python
    import pandas as pd
    data = pd.read_csv("data.csv")
    data.head()
    ```

отобразится как

```python
import pandas as pd
data = pd.read_csv("data.csv")
data.head()
```

## Встроенные иконки

```go
{{</* icon name="python" */>}} Python
```

отобразится как

{{< icon name="python" >}} Python

## Эта страница была полезна? Поделитесь ею 🙌
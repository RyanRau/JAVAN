# Base Template

base.html contains the css & js that all other templates should use, it can be found at:

templates/base/base.html

## How to use

```
    {% extends "PATH TO base.html FROM CURRENT DIR" %}


    {% block title %} TITLE FOR PAGE {% endblock %}


    {% block head %}
        <!-- content to be inserted into head -->
    {% endblock head %}


    {% block body %}
        <!-- content to be inserted into body -->
    {% endblock body %}
```

**Note:** When importing static files into the head you must load static in order for it to work:

```
    {% load static from staticfiles %}
    <link rel="stylesheet" href="{% static 'PATH TO FILE' %}">
```
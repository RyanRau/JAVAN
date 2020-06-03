# Templating Logic
Django support basic logic within its templates. Below is a brief run down of the basics,
official documentation can be found at [Django's Documentation Site](https://docs.djangoproject.com/en/3.0/ref/templates/language/).

## The Basics

#### - IF statement

Its an if statement... if this do this...

```html
    {% if x == "some_value" %}
        <p>show this text</p>
    {% else %}
        <p>show this text instead</p>
    {% endif %}
```

Practical usages of this can found in the following files:

   - templates/materials/index.html (lines: 39 - 60)

#### - FOR loop
The FOR loop can be used to iterate over a list object which you pass along from the view. The following example
would render an unordered list consisting of the items in list.

```html
    <ul>
        {% for x in list %}
            <li>{{ x }}</li>
        {% endfor %}
    </ul>
```

If the list is an object you can scope into its values as such

```html
    <ul>
        {% for user in user_list %}
            <li>{{ user.first_name }} {{ user.last_name }}</li>
        {% endfor %}
    </ul>
```

Practical usages of this can found in the following files:

   - templates/materials/index.html (lines: 27 - 64)
   - templates/materials/includes/item_list.html
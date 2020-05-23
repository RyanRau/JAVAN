# Include Templates

Templates that can be found in the includes folder are tidbits of html that made more sense
to be abstracted out. These include the modal form, list of objects, nav bars, etc...

You can include a template in another template by using:

```html
{% include "path/to/template" %}
```

For example the index.html of the materials folder includes the navigation bar as shown
```html
{% include "../base/includes/nav.html" %}
```

## Usages

Abstracting templates can be helpful when trying to dynamically load content. For example,
when you add an item to your order in materials you can have the page dynamically update 
the list of order items rather then refreshing the page. See []() for more information.

Abstracting stuff out also makes it easier to update just a part of a page as the html is a bit
cleaner and easier to follow.


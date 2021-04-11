class htmlObject:
    def __init__(self, children=None, id=None, style=None, className=None, **kwargs):
        self.id = id
        if style is None:
            self.style = []
        elif not isinstance(style, list):
            self.style = [style]
        else:
            self.style = style

        if children is None:
            self.children = []
        elif not isinstance(children, list):
            self.children = [children]
        else:
            self.children = children

        if className is None:
            self.className = []
        elif not isinstance(className, list):
            self.className = [className]
        else:
            self.className = className

        self.additional_html_open = {}
        self.kwargs = kwargs

    def html_open(self):
        html_open = f"<{self.type} "
        if self.id is not None:
            html_open += f'id="{self.id}" '
        style = ";".join(self.style)
        html_open += f'style="{style}" '
        classes = " ".join(self.className)
        html_open += f'class="{classes}" '
        for key, val in self.additional_html_open.items():
            key = key.replace("_", "-")
            html_open += f'{key}="{val}" '
        for key, val in self.kwargs.items():
            key = key.replace("_", "-")
            html_open += f'{key}="{val}" '
        html_open += ">"
        return html_open + "\n"

    def html_close(self):
        return f"</{self.type}>"

    def html_body(self):
        html_body = ""
        for child in self.children:
            child_html = child.__str__()
            for ch_html in child_html.split("\n"):
                html_body += "\t" + ch_html + "\n"

        return html_body

    def __str__(self):
        html_open = self.html_open()
        html_close = self.html_close()
        html_body = self.html_body()

        html = html_open
        html += html_body
        html += html_close
        return html


class div(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "div"


class a(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "a"
        self.href = kwargs.get("href", None)
        if self.href is not None:
            self.additional_html_open.update({"href": self.href})


class span(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "span"


class h1(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "h1"


class h2(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "h2"


class h3(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "h3"


class img(htmlObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = "img"


class strong(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "strong"


class form(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "form"


class label(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "label"


class input(htmlObject):
    def __init__(self, children=None, **kwargs):
        if children is not None:
            raise ValueError("input cannot have children")
        super().__init__(children=children, **kwargs)
        self.type = "input"

    def html_body(self):
        return ""

    def html_close(self):
        return ""


class textarea(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "textarea"

    def html_body(self):
        if self.children in [None, [""]]:
            return ""
        else:
            return self.children[0].__str__()

    def html_open(self):
        html_open = super().html_open()
        return html_open.replace("\n", "")


class button(htmlObject):
    def __init__(self, children=None, **kwargs):
        super().__init__(children=children, **kwargs)
        self.type = "button"


def add_kwargs(kwargs_dict, **kwargs):
    for key, value in kwargs.items():
        if not isinstance(value, list):
            value = [value]
        if key in kwargs_dict:
            if not isinstance(kwargs_dict[key], list):
                kwargs_dict[key] = [kwargs_dict[key]]
            kwargs_dict[key] += value
        else:
            kwargs_dict[key] = value
    return kwargs_dict


br = "<br>\n"
hr = "<hr/>\n"

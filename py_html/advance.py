from .core import div, htmlObject


class progressBar(htmlObject):
    def __init__(self, perc, colors, add_value=False, **kwargs):
        super().__init__(**kwargs)
        self.perc = [p * 100 for p in perc]
        self.colors = colors
        if len(self.perc) != len(self.colors):
            raise ValueError("perc and colors have to have the same length")
        self.add_value = add_value
        if not "style" in kwargs.keys():
            self.style = []

    def __str__(self):
        children = [
            div(
                className="progress-bar",
                role="progressbar",
                style=";".join(self.style)
                + f"width: {perc}%;background-color: {color} ;",
                aria_valuenow=f"{perc}",
                aria_valuemin="0",
                aria_valuemax="100",
                children=[perc] if self.add_value else [],
            )
            for perc, color in zip(self.perc, self.colors)
        ]
        return div(
            className=self.className,
            children=[div(className="progress", children=children,)],
        ).__str__()


import py_html.core as html


class TestCore:
    def test_div(self):
        div = html.div("hello")
        assert str(div) == '<div style="" class="" >\n\thello\n</div>'

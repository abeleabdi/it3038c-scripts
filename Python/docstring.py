def calculate(a, b, c):
    """Calculate curve value .

    Args:
        a ([type]): [description]
        b ([type]): [description]
        c ([type]): [description]

    Returns:
        [type]: [description]
    """
    d = 100 * c - 10 * b + c
    return d

def create_app():
    """Create a Flask app .

    Returns:
        [type]: [description]
    """
    @app.route("/")
    def index():
        return jsonify(hello="world")

def sina_xml_to_url_(xml_data):
    """Convert a string of XML to a list of URLs .

    Args:
        xml_data ([type]): [description]

    Returns:
        [type]: [description]
    """
    rawurl = []
    dom = parseString(xml_data)
    for node in dom.getElementsByTagName('durl'):
        url = node.getElementsByTagName('url')[0]
        rawurl.append(url.childNodes[0].data)
    return rawurl
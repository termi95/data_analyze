from base64 import b64encode
from io import StringIO
import plotly.graph_objects as go
from db import execute_query

def test():
    names, occurrences = zip(*execute_query("SELECT Company, COUNT(*) AS occurrences FROM laptops GROUP BY Company;"))
    fig = go.Figure(
    data=[go.Bar(y=occurrences,x=names)],
    layout_title_text="A Figure Displayed with fig.show()"
    )
    encoded = get_base64_data_from_chart(fig)
    return fig.to_json()

def get_base64_data_from_chart(fig):    
    buffer = StringIO()
    fig.write_html(buffer)
    html_bytes = buffer.getvalue().encode()
    return b64encode(html_bytes).decode()
    
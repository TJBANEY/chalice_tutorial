from chalice import Chalice, BadRequestError, Response
import jinja2
import os

from os import listdir
from os.path import isfile, join

app = Chalice(app_name='chalice-helloworld')

app.debug = True

battleship_template = '''
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title></title>

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
          integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  </head>
  <body>
    <div class="container">
      <div class="row">
        <div class="col-xs-12" style="height: 200px; border: 1px solid red;">
          Woot Woot This Works
        </div>
      </div>
    </div>
  </body>
</html>
'''

def render(tpl_path, context):
    path, filename = os.path.split(tpl_path)
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(path or './')
    ).get_template(filename).render(context)

@app.route('/')
def index():

    return Response(body=battleship_template,
                    status_code=200,
                    headers={'Content-Type': 'text/html'})

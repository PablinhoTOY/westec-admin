import os
from flask.helpers import make_response
from flask import redirect, render_template, request, url_for
from app import app

import logging

# Se obliga a weasyprint a solo mostrar mensajes de error
logging.getLogger("fontTools").setLevel(logging.ERROR)
logging.getLogger("weasyprint").setLevel(logging.ERROR)


# TODO funcion para generar el pdf

# ===========================================================================
# *** Esta función crea el pdf con los datos que le son traspasados.
# ===========================================================================


def final_pdf(filename, final):
    from flask_weasyprint import HTML, render_pdf

    pdf = render_pdf(HTML(string=final), download_filename=filename)
    response = make_response(pdf)
    response.headers["Content-Type"] = "aplication/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=" + filename

    return response

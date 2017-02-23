#!/usr/bin/python

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.5 

Servidor de aplicaciones con herencia de clases
ADIOS MUNDO CRUEL
"""

import webapp


class holaApp (webapp.webApp):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        return ("200 OK", "<html><body><h1>Adios mundo cruel</h1></body></html>")

if __name__ == "__main__":
    testwebApp = holaApp("localhost", 1234)

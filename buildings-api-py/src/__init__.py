
# Export the handlers in the top level of the application
from .handlers import RootHandler
from .handlers import BuildingHandler
from .handlers import BuildingListHandler
from . import wsgi

# def main():
#     from http.server import HTTPServer
#     import sys
#     if len(sys.argv) > 1:
#         app = wsgi.app(sys.argv[1])
#     else:
#         app = wsgi.app()
#     httpd = HTTPServer(('0.0.0.0', 8000), app)
#     httpd.serve_forever()

# if __name__ == "__main__":
#     main()

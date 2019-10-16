from flask import request
from flask_graphql import GraphQLView
from .render_altair import render_altair

class AltairView(GraphQLView):
  """Renders Altair GraphQL Client for Flask"""
  schema = None
  graphql_endpoint = None
  def __init__(self, **kwargs):
    super(AltairView, self).__init__(**kwargs)
    for key, value in kwargs.items():
      if hasattr(self, key):
        setattr(self, key, value)

  def dispatch_request(self):
    return render_altair(self.graphql_endpoint)

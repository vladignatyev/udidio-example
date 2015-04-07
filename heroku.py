"""
  Heroku specific patch to make Flask properly handle HTTP headers
"""
from flask import Request

class HerokuRequest(Request):
    """
    `Request` subclass that overrides `remote_addr` with Heroku's
    HTTP_X_FORWARDED_FOR when available.
    """

    @property
    def remote_addr(self):
        """The remote address of the client."""
        fwd = self.environ.get('HTTP_X_FORWARDED_FOR', None)
        if fwd is None:
            return self.environ.get('REMOTE_ADDR')
        # sometimes x-forwarded-for contains multiple addresses,
        # actual client is first, rest are proxy
        fwd = fwd.split(',')[0]
        return fwd

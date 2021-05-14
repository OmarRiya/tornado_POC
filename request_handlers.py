from http_status_code.standard import successful_request
from queries import pool
import queries
from tornado import gen, web
import datetime
import json
import asyncio
import concurrent
import tornado




class BaseHandler(web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


class LoginHandler(BaseHandler):
    def initialize(self):
        self.session = queries.TornadoSession('postgresql://postgres:12345@localhost:5432/tornado_poc')

    def get(self):
        self.render("login.html", next=self.get_argument("next","/"), message=self.get_argument("error","") )

    async def post(self):
        user_name = self.get_argument("user_name", "")
        password = self.get_argument("password", "")
        sql = f"SELECT * FROM accounts WHERE username ='{user_name}' AND password = '{password}'"

        try:
            result = await self.session.query(sql)

        except queries.OperationalError as error:
            logging.error('Error connecting to the database: %s', error)
            raise web.HTTPError(503)

        if result:
            self.set_secure_cookie("username", user_name)
            self.write("Successfully loged in")
            result.free()
        self.render("invalid_login.html")


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('username')
        self.redirect("/login/")
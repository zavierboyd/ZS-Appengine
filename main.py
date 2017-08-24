#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
try:
    import webapp2
    from google.appengine.ext import ndb
    from google.appengine.api import users
except:
    pass
import os
import jinja2

import zscript as zs

temdir = os.path.join(os.path.dirname(__file__), 'html')
jinjaenv = jinja2.Environment(loader=jinja2.FileSystemLoader(temdir),
                              autoescape=True)


initprogram = """
;; := sets variables

a := 1
c := 1
b = (4*a*c)^0.5

;; = makes definitions which are evaluated when called
;;d2 = b^2 - 4*a*c
x1 = -b;; + d2^0.5
x2 = -b;; - d2^0.5

;; x_ = makes a next definition where when next is called it calculates itself and updates the original variable to the next one
a_ = a  + 1
c_ = c + 1

;; trace will tell the program to print out the variable progressively as it runs throught next
trace b

;; next loops over the next definitions and replaces the old variables with the new calculated ones
;; it also prints out the trace variables at each time step
next 10
"""

class Program(ndb.Model):
    username = ndb.StringProperty()
    program = ndb.TextProperty()
    replenv = ndb.TextProperty()


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **kw):
        t = jinjaenv.get_template(template)
        return t.render(kw)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


def newProgram(user):
    dbprogram = Program(username=user,
                        program=initprogram,
                        replenv=repr(zs.Env()))
    return dbprogram


class MainHandler(Handler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        query = Program.query(Program.username == nickname)
        dbprogram = query.get()
        if dbprogram is None:
            dbprogram = newProgram(nickname)
            dbprogram.put()

        self.render("repl.html")


class ProgramHandler(Handler):
    def get(self):
        user = users.get_current_user()
        nickname = user.nickname()
        query = Program.query(Program.username == nickname)
        dbprogram = query.get()

        if dbprogram is None:
            dbprogram = newProgram(user)
            dbprogram.put()
        self.render("program.html", program=dbprogram.program)

    def post(self):
        program = self.request.get('program')

        user = users.get_current_user()
        nickname = user.nickname()
        query = Program.query(Program.username == nickname)
        dbprogram = query.get()

        dbprogram.program = program
        dbprogram.put()
        self.render("program.html", program=dbprogram.program)


def runprogram(com, env):
    nenv = repr(env)
    try:
        output = zs.compilerun(com, env)
        nenv = repr(env)
        # print(nenv)
        # print('Output:', output)
        n = []
        for out in output:
            if out is not None:
                if type(out) != list:
                    n.append(str(out))
                else:
                    n.append('\n'.join(['[' + ', '.join([str(bit) for bit in row]) + ']' for row in out]))
        # print('N format', n)
        output = n
    except Exception as out:
        print(out.args[0])
        output = [out.args[0]]
    output += zs.ZWarning.currentwarnings
    zs.ZWarning.clearwarnings()
    if len(output) != 0:
        if issubclass(output[0].__class__, Exception):
            output[0] = output[0].message
        output = '\n'.join(output)
    else:
        output = ''
    # print((output))
    return output, nenv


class RunHandler(Handler):
    def get(self):
        program = self.request.get('program')
        output, nenv = runprogram(program, zs.Env())
        self.write(output)


class CommandHandler(Handler):
    def post(self):
        user = users.get_current_user()
        nickname = user.nickname()
        query = Program.query(Program.username == nickname)
        dbprogram = query.get()

        env = zs.Env(repl=True)
        zs.compilerun(dbprogram.replenv, env)

        com = str(self.request.get('com'))

        print()
        print()
        print()
        print()
        print()
        print(com)
        print()
        print()
        print()
        print()
        print()
        if com == 'env':
            nenv = repr(env)
            output = nenv
        else:
            output, nenv = runprogram(com, env)

        if dbprogram.replenv != nenv:
            dbprogram.replenv = nenv
            dbprogram.put()
        self.write(output+':=:=:'+nenv)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/program', ProgramHandler),
    ('/run', RunHandler),
    ('/eq', CommandHandler)
], debug=True)

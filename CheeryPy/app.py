import cherrypy

import json

users = [{
    "id":1,"name":"ajay","course":"Python"
}]

class CRUDAPP:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def user(self):
        return users
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def add(self):
        data = cherrypy.request.json
        users.append(data)
        return {"message":"Added Sucessfully"}
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def update(self,id):
        data = cherrypy.request.json
        for u in users:
            if u['id'] ==int(id):
                u.update(data)
                return{"message":"user Updated succesfully"}

if __name__ =="__main__":
    cherrypy.config.update({
        "server.socket_port":9090
    })
    cherrypy.quickstart(CRUDAPP())
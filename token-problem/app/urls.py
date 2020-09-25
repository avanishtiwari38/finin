from app.handlers.hello import Hello
from app.handlers.token import NewToken, AssignToken, UnassignToken, DeleteToken, RefreshToken
from app import api



api.add_resource(Hello, '/hello')
api.add_resource(NewToken, '/new-token')
api.add_resource(AssignToken, '/assign-token')
api.add_resource(UnassignToken, '/unassign-token')
api.add_resource(DeleteToken, '/delete-token')
api.add_resource(RefreshToken, '/refresh-token')






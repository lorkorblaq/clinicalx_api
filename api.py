from flask import Flask, request, jsonify, render_template, Blueprint
from flask_restful import Api
from flask_cors import CORS
from items_api import *  # Import your resources
from put_in_use_api import *
from user_api import *
from channels_api import *
from lot_exp_api import *



app = Flask(__name__)
api = Api(app)
CORS(app)

#users
api.add_resource(UserPush, "/api/user/push/")
api.add_resource(UserPut, "/api/user/put/<string:user_id>/")
api.add_resource(UserDel, "/api/user/del/<string:user_id>/")
api.add_resource(UserGetOne, "/api/user/get/<string:user_id>/")
api.add_resource(UsersGetAll, "/api/users/get/")

#items
api.add_resource(ItemsResource, "/api/items/get/")
# api.add_resource(ItemsPut, "/api/item/put/")


#put in use
api.add_resource(P_in_usePush, "/api/piu/push/<string:user_id>/")
api.add_resource(P_in_usePut, "/api/piu/put/<string:piu_id>/")
api.add_resource(P_in_useDelete, "/api/piu/delete/<string:piu_id>/")
api.add_resource(P_in_useGetOne, "/api/piu/get/<string:piu_id>/")
api.add_resource(P_in_useGetAll, "/api/piu/get/")

#channel
api.add_resource(ChannelPush, "/api/channel/push/<string:user_id>/")
api.add_resource(ChannelPut, "/api/channel/put/<string:channel_id>/")
api.add_resource(ChannelDel, "/api/channel/delete/<string:channel_id>/")
api.add_resource(ChannelGetOne, "/api/channel/get/<string:channel_id>/")
api.add_resource(ChannelGetAll, "/api/channels/get/")

#lot exp
api.add_resource(Lot_exp_Get, "/api/lotexp/get/")
api.add_resource(Lot_exp_Push, "/api/lotexp/push/<string:user_id>/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

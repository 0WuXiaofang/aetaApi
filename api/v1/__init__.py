from flask import Blueprint
from api.v1 import maplistInfo,predict_info,foundationData,stationinfo,userOp


def create_blueprint_aFang():
    bp = Blueprint('v1', __name__)
    maplistInfo.api.register(bp, url_prefix='/earthquakePredict')
    predict_info.api.register(bp, url_prefix='/earthquakePredict')
    foundationData.api.register(bp, url_prefix='/earthquakePredict')
    stationinfo.api.register(bp, url_prefix='/earthquakePredict')
    userOp.api.register(bp, url_prefix='/earthquakePredict')
    return bp

from fastapi import APIRouter, Depends
from mifaker.models.generate import MakeClassesRequest
from mifaker.services.make_classes import make_classes, make_classes_jpg, make_classes_svg

router = APIRouter()


@router.get("/classes/data")
def generate_classes_data(request: MakeClassesRequest = Depends()):
    return make_classes(request)


@router.get("/classes/image")
def generate_classes_image(request: MakeClassesRequest = Depends()):
    return make_classes_jpg(request)


@router.get("/classes/svg")
def generate_classes_image(request: MakeClassesRequest = Depends()):
    return make_classes_svg(request)

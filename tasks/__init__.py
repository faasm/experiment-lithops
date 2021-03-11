from invoke import Collection

from . import azure
from . import faasm
from . import knative

ns = Collection(
    azure,
    faasm,
    knative,
)

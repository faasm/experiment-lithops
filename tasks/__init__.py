from invoke import Collection

from . import azure
from . import knative

ns = Collection(
    azure,
    knative,
)

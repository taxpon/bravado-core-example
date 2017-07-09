# -*- coding: utf-8 -*-

import yaml
from bravado_core.spec import Spec
from bravado_core.request import IncomingRequest, unmarshal_request


class DummyRequest(IncomingRequest):

    @property
    def path(self):
        return {"id": 1}

    @property
    def query(self):
        return {}

    @property
    def form(self):
        return {}

    @property
    def headers(self):
        return {}

    @property
    def files(self):
        return {}

    def json(self):
        return {
            "id": 1,
            "title": "Merchant of Venice",
            "author": "William Shakespeare",
            "release_date": "2017-07-17"}

    pass


def main():
    with open('../spec/1/openapi.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec, config={'use_models': False})

    req = DummyRequest()
    op_books_detail_put = spec.get_op_for_request('put', '/api/v1/books/{id}')
    param = unmarshal_request(req, op_books_detail_put)
    print(param)

if __name__ == "__main__":
    main()

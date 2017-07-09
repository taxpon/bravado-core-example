# -*- coding: utf-8 -*-

import yaml
from bravado_core.spec import Spec
from bravado_core.param import Param, unmarshal_param
from bravado_core.request import IncomingRequest


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

    # Method 1
    op_books_get = spec.get_op_for_request('get', '/api/v1/books/{id}')
    _param = raw_spec['paths']['/books/{id}']['parameters'][0]
    param = Param(spec, op_books_get, _param)
    print(param)

    # Method 2
    print(op_books_get.params)

    req = DummyRequest()
    obj = unmarshal_param(op_books_get.params['id'], req)
    print(obj)

    # Method 3
    op_books_post = spec.get_op_for_request('post', '/api/v1/books')
    book = unmarshal_param(op_books_post.params['book'], req)
    print(book)

    op_books_detail_put = spec.get_op_for_request('put', '/api/v1/books/{id}')
    book = unmarshal_param(op_books_detail_put.params['book'], req)
    print(book)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

import yaml
from bravado_core.spec import Spec
from bravado_core.operation import Operation


def main():
    with open('../spec/1/openapi.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec)

    # Method 1
    path_books = raw_spec['paths']['/books']['get']
    op = Operation.from_spec(spec, "/books", "get", path_books)
    print(op)

    # Method 2
    op = spec.get_op_for_request('get', '/api/v1/books/{id}')
    print(op)


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

from datetime import date
import yaml
from bravado_core.spec import Spec
from bravado_core.marshal import marshal_schema_object


def main():
    with open('../spec/1/openapi.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec)
    book = raw_spec['definitions']['Book']

    Book = spec.definitions['Book']
    book_obj = Book(id=1, title="Merchant of Venice", author="William Shakespeare", release_date=date(2017, 7, 11))
    book_dict = marshal_schema_object(spec, book, book_obj)
    print(book_dict)

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-

import yaml
from bravado_core.spec import Spec
from bravado_core.unmarshal import unmarshal_schema_object


def main():
    with open('../spec/1/openapi.yaml', 'r') as f:
        raw_spec = yaml.load(f)
    spec = Spec.from_dict(raw_spec)
    book = raw_spec['definitions']['Book']

    book_obj = unmarshal_schema_object(
        spec, book,
        {"id": 1,
         "title": "Merchant of Venice",
         "author": "William Shakespeare",
         "release_date": "2017-07-17"
         })
    print(book_obj)

if __name__ == "__main__":
    main()

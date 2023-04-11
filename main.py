from urllib.parse import urlparse, parse_qsl


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    return dict(parse_qsl(parsed_url.query))


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https//www.domain.com/page?key1=value1&key2=value2') == {'key1': 'value1', 'key2': 'value2'}
    assert parse('') == {}
    assert parse('https://www.domain.com/?utm_source=twitter&utm_medium=tweet&utm_campaign=summer-sale')\
           == {'utm_source': 'twitter', 'utm_medium': 'tweet', 'utm_campaign': 'summer-sale'}
    assert parse('/shoes/women-shoes?type=high-heels') == {'type': 'high-heels'}
    assert parse('http://domain.com?productid=xyz') == {'productid': 'xyz'}


# def parse_cookie(query: str) -> dict:
#     parsed_url = urlparse(query)
#     return dict(parse_qsl(parsed_url.path) + parse_qsl(parsed_url.params, separator=';'))
#
#
# if __name__ == '__main__':
#     assert parse_cookie('name=Dima;') == {'name': 'Dima'}
#     assert parse_cookie('') == {}
#     assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
#     assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
#     assert parse_cookie('age=28;') == {'age': '28'}
#     assert parse_cookie('tasty_cookie=strawberry;') == {'tasty_cookie': 'strawberry'}
#     assert parse_cookie('tasty_cookie=strawberry') == {'tasty_cookie': 'strawberry'}
#     assert parse_cookie('id=a3fWa;Expires=Thu 31 Oct 2021') == {'id': 'a3fWa', 'Expires': 'Thu 31 Oct 2021'}
#     assert parse_cookie('Expires=Thu 31 Oct 2021;') == {'Expires': 'Thu 31 Oct 2021'}
#     assert parse_cookie('key1=value1;key2=value2;') == {'key1': 'value1', 'key2': 'value2'}

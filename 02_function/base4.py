# inner関数　ノンローカル変数

def outer():
    outer_value = '外側の変数'
    def inner():
        nonlocal outer_value
        outer_value = '内側の変数'
        print('inner: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))
    inner()
    print('outer: outer_value = {}, id = {}'.format(outer_value, id(outer_value)))

outer()

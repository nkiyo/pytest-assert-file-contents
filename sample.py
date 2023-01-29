import textwrap

# sudo apt install -y python3-pip
# pip3 install pytest
# python3 -m pytest sample.py
#
# 適当な関数
def my_function(s):
    return s

# fileっぽい内容を文字列定義する
#file_contents = """\
#<hoge>
#  hogehoge
#</hoge>"""

# fileを文字列として読み込む、関数に渡す
#my_function(file_contents)

# ユニットテストを実行する
def test_my_function():
    # fileっぽい内容を文字列定義する
    file_contents = textwrap.dedent("""\
    <hoge>
      hogehoge
    </hoge>""")
    print(file_contents)
    actual = my_function(file_contents)
    assert actual == file_contents

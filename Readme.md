# 概要
チャットボットやSNS、もしくはそれらのデータを用いての解析において、不適切表現のフィルタリングをするための不適切表現単語リストです。
日本語における不適切表現を収集します。  
現状不適切表現は、単語それ自体が不適切だと断定できるものを基準として人力で収集しています(例えばローションはボディーローションが存在し、不適切とは断定できないので入っていません)  

(2020/08/19 攻撃的/差別的表現リストを暫定で追加しました。)

utf-16も考えましたが、現状絵文字のたぐいの殆どがutf-8内に収まっていると考えたのでutf-8です。

# 資源

## Sexual.txt
性的な表現のリストです。内部はソートされてます。

## Sexual_with_mask.txt
make_with_masked.pyで生成された伏せ字を含むSexualな単語です。

## Sexual_with_bopo.txt
Sexual.txtのうち、似ている注音符号(ボポモフォ/bopomofo)で文字を置き換えたものです。  
Sexual.txtから make_with_bopomofo.py 及び bopomofo_map.txtから機械的に生成されています。  

## offensive.txt
攻撃的/差別的な表現のリストです。(暫定版)

-----------------------------------------------------------

# ユーティリティその他

## word_inserter.py
単語を追加するときに使っているプログラムです。

```
wort_inserter.py [filename] [-w [words1 words2...]] [-s [souce_file]]
```

です。filenameは必須で新たな単語を挿入する先のファイル名(e.g. Sexual.txt)を指定します

-w はコマンドラインに入力した単語を追加できます。スペース区切りで複数いけます。  
-s はSexual.txtと同様に改行で区切られた単語ファイルからimportするときに使います。  
**ちょっとサボったので同一ディレクトリのファイルからしか今はインポートできません。**

コードをみれば明らかな通り、-wと-sを同時に指定すると-wだけ追加されてしまいます。
万一使うことがあれば別々の追加をお願いいたします。

## make_with_masked.py
一部を伏せ字にした表現を機械的に生成しています。
2k+1(k>=0)文字目を伏せ字にしたものを機械的に生成します。この生成方法、正直精度はイマイチですが一応作ってみました。

```
make_with_masked.py [filename e.g. Sexual.txt]
```

で実行します。生成ファイルは[filename]+"_with_mask"の形です。

## make_with_bopomofo.py
似ている注音記号が存在するひらがな/カタカナ/アルファベットを注音記号に置換したものを生成します。  
make_with_masked.pyと同じく、

```
make_with_bopomofo.py [filename e.g. Sexual.txt]
```

で実行します。生成ファイルは[filename]+"_with_bopo"の形です。
  
## bopomofo_map.txt
make_with_bopomofo.pyで使用している各種文字と注音記号の対応リストです。
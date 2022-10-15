# Patient Locational Ontology-based Data (PLOD)

## 目次
- [概要](#概要)
- [提案データセット](#提案データセット)
- [COVID-19感染リスク推論オントロジー（CIRO）](#covid-19感染リスク推論オントロジーciro)
- [オントロジーに基づく個々のデータ（PLOD）](./rdf/example/)
- [PLODの使用例](./sparql/)
- [3つの密の推論実験の結果](#3つの密の推論実験の結果)

## 概要
- COVID-19の感染拡大防止に向けて，日本国政府では「[3つの密](https://www.kantei.go.jp/jp/content/000061868.pdf)」（以下，三密）や，「[5つの場面](https://corona.go.jp/prevention/pdf/infection-20201117.pdf)」を提言しています．
- これらの提言に基づき，各人の感染リスクを自動で評価できれば，追跡調査対象者の順序付けやスクリーニングといった保健所で行われている業務を大幅に効率化できると考えています．
- そこで，場所や行動に紐づくCOVID-19感染リスクを整理し，個別の行動事例における感染リスクを推論可能なオントロジー(CIRO)を開発しました．
- 本リポジトリでは，このオントロジーに基づいてナレッジグラフ化(RDF化)された疑似データ（PLOD）を，オープンデータとして提供します．
- このようなデータを使用することで，追跡調査に有用な三密リスクの推論とグラフ検索が可能なことを示しています．

## 提案データセット
- [COVID-19感染リスク推論オントロジー（CIRO）](./rdf/CIRO.owl)
- [オントロジーに基づく個々のデータ（PLOD）](./rdf/example/ciro_sample.rdf)
- [三密推論実験の再現](https://zenodo.org/record/6482275#.YmY-QfNBzS4)

## COVID-19感染リスク推論オントロジー（CIRO）

### オントロジーの仕様書
全クラス・インスタンス・プロパティの説明は下記の仕様書を御覧ください。  
[https://plod-info.github.io/PLOD/ciro.html](https://plod-info.github.io/PLOD/ciro.html)  
以下で代表的なクラス・プロパティを説明します。

### スキーマ図
黄色が新規に作成したクラス。青色が再利用したクラス。
<img src="./diagram/ontology_revise.png" alt="CIROクラス図">

## オントロジーに基づく個々のデータ（PLOD）

現在，構築したオントロジーを保健所のシステムに応用することを想定しています．そこで，システムへの導入を前に，行動調査を模した擬似的な行動シナリオの模擬データを作成し，オントロジーに基づいてナレッジグラフ化しました．例えば，下図のような行動イベントがナレッジグラフ化されています．赤矢印はCIROのOWL推論により導出されるリンクです．
<img src="./diagram/kg.png" alt="kgの例">

## PLODの使用例
PLODはRDF形式のデータで提供しているため，トリプルストアに格納することで，クエリ言語SPARQLを使用して様々な検索が可能です．  

参考資料:
- 【トリプルストアについての参考資料】[トリプルストアの導入](https://www.slideshare.net/KnowledgeGraph/lod-250078657)  （12ページから）
- 【SPARQLについての参考資料】[Wikidataを例としたSPARQLクエリの例](https://www.slideshare.net/KnowledgeGraph/linked-open-data2020-sparqlsparql)（16ページから）

### SPARQLクエリ例
以下のSPARQLクエリの一部はOWL 2 DL推論をサポートした推論エンジン（[Pellet](https://github.com/stardog-union/pellet), [HermiT](http://www.hermit-reasoner.com/)）が必要になります。

- [リスクのあるイベントまたは状況](#リスクのあるイベントまたは状況)
- [密閉している状況](#密閉している状況)
- [密接しているイベント](#密接しているイベント)
- [密集している状況](#密集している状況)
- [時間的，空間的に交差する異なる2つの行動イベントの組み合わせ](#時間的空間的に交差する異なる2つの行動イベントの組み合わせ)
- [同じ都市かつ開始・終了時間がオーバーラップするイベントの組](#同じ都市かつ開始・終了時間がオーバーラップするイベントの組)
- [Aさんが参加している密閉イベントに同席している人物を，同席回数で降順表示](#aさんが参加している密閉イベントに同席している人物を同席回数で降順表示)
- [中密閉となった場所と、その場所で行われたイベント回数を降順表示](#中密閉となった場所とその場所で行われたイベント回数を降順表示)
- [特定の期間でリスクのあるイベントとリスクの種類を取得](#特定の期間でリスクのあるイベントとリスクの種類を取得)

#### リスクのあるイベントまたは状況
```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
select ?event where { 
    ?event a plod:RiskContext ;
        a ?o .
    filter(?o = plod:Situation || ?o = schema:Event)
}
```

#### 密閉している状況
```sparql
PREFIX plod: <http://plod.info/rdf/>
select ?s where { 
    ?s a plod:ClosedSpace .
}
```

#### 密接しているイベント
```sparql
PREFIX plod: <http://plod.info/rdf/>
select ?s where { 
    ?s a plod:CloseContact .
}
```

#### 密集している状況
```sparql
PREFIX plod: <http://plod.info/rdf/>
select ?s where { 
    ?s a plod:Crowding .
}
```

#### 時間的，空間的に交差する異なる2つの行動イベントの組み合わせ
```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select distinct ?event1 ?place1 ?city1 ?event2 ?place2 ?city2 where { 
  ?event1 a schema:Event ; 
            plod:time ?time1 ;
            schema:location ?place1 .
    ?place1 plod:city ?city1 .
    ?time1  time:hasBeginning ?begin1 ; 
            time:hasEnd ?end1 .
  ?event2 a schema:Event ; 
          plod:time ?time2 ; 
    		plod:agent ?agent ;
          schema:location ?place2 .
    ?event2 schema:location ?place1 .
    ?place2 plod:city ?city1 .
  ?time2 time:hasBeginning ?begin2 ; time:hasEnd ?end2 .
    filter(xsd:dateTime(?end1) > xsd:dateTime(?begin2) 
        && xsd:dateTime(?begin1) < xsd:dateTime(?end2))
  filter(?event1 != ?event2)
}
```

#### 同じ都市かつ開始・終了時間がオーバーラップするイベントの組
```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select distinct ?event1 ?place1 ?city1 ?event2 ?place2 ?city2 where { 
  ?event1 a schema:Event ; 
            plod:time ?time1 ;
            schema:location ?place1 .
    ?place1 plod:city ?city1 .
    ?time1  time:hasBeginning ?begin1 ; 
            time:hasEnd ?end1 .
  ?event2 a schema:Event ; 
          plod:time ?time2 ; 
            plod:agent ?agent ;
          schema:location ?place2 .
    ?event2 schema:location ?place1 .
    ?place2 plod:city ?city1 .
  ?time2 time:hasBeginning ?begin2 ; time:hasEnd ?end2 .
    filter(xsd:dateTime(?end1) > xsd:dateTime(?begin2) 
        && xsd:dateTime(?begin1) < xsd:dateTime(?end2))
  filter(?event1 != ?event2)
}

```

#### Aさんが参加している密閉イベントに同席している人物を，同席回数で降順表示

```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT ?agent (count(distinct ?event) AS ?cnt)  WHERE { 
	?event plod:agent <http://plod.info/rdf/id/person_a_A> ;
        plod:agent ?agent ;
        plod:time ?time ;	
        schema:location ?place .
    filter (?agent != <http://plod.info/rdf/id/person_a_A>)
    ?situation plod:isSituationOf ?place .
    ?situation rdf:type ?sanmitsu .
    ?sanmitsu rdfs:label "中密閉"@ja .
} GROUP BY ?agent ORDER BY DESC(?cnt)
```

#### 中密閉となった場所と、その場所で行われたイベント回数を降順表示
```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX schema: <http://schema.org/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
select ?place (count(distinct ?event) AS ?cnt) where { 
    ?event schema:location ?place .
    ?situation plod:isSituationOf ?place ;
               a [ rdfs:label "中密閉"@ja] .
} group by ?place order by DESC(?cnt)
```

#### 特定の期間でリスクのあるイベントとリスクの種類を取得
```sparql
PREFIX plod: <http://plod.info/rdf/>
PREFIX time: <http://www.w3.org/2006/time#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
select ?s ?type where { 
    ?s a ?type ;
       plod:time ?time .
    ?time time:hasBeginning ?begin ;
          time:hasEnd ?end .
    filter (?begin >= "2020-12-06T19:30:00"^^xsd:dateTime)
    filter (?end >= "2020-12-06T21:30:00"^^xsd:dateTime)
    filter (?type = plod:ClosedSpace || ?type = plod:CloseContact || ?type = plod:Crowding)
}
```

## 3つの密の推論実験の結果
3つの密を更に3段階（高リスク、中リスク、低リスク(リスク無し)）に分けて，与えられた行動イベントや空間的な状況がどのリスクに該当するか,OWL 2 DL推論により判定する実験を行いました.

OWL 2 DL推論が可能な[HermiT](http://www.hermit-reasoner.com/)を内包する[Owlready2](https://owlready2.readthedocs.io/en/v0.37/)を使用した実験用スクリプトを公開しています。各のリスクパターンの疑似データ（PLOD）を自動的に作成し,CIROを用いて正しく推論できるか評価を行います.

実験の結果,CIROはこれらのリスクを正しく推論できることを確認しました.

実験スクリプトおよび結果：  
<a href="https://doi.org/10.5281/zenodo.6482275"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6482275.svg" alt="DOI"></a>

## リファレンス

- 江上周作，山本泰智，大向一輝，奥村貴史: オントロジーを用いたCOVID-19感染リスク行動の推論，第56回人工知能学会セマンティックウェブとオントロジー研究会, SIG-SWO-056-16 (2022)[[J-STAGE]](https://www.jstage.jst.go.jp/article/jsaisigtwo/2022/SWO-056/2022_16/_article/-char/ja/)

## ライセンス
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><a xmlns:cc="http://creativecommons.org/ns#" href="https://profile.idease.info/" property="cc:attributionName" rel="cc:attributionURL">江上周作</a>，山本泰智，大向一輝，奥村貴史 作『<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Patient Locational Ontology-based Data (PLOD)</span>』は<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">クリエイティブ・コモンズ 表示 4.0 国際 ライセンス</a>で提供されています。

## 謝辞
本研究は，AMEDの課題番号JP20he0622042の支援を受けた．
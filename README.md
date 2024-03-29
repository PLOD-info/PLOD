# Patient Locational Ontology-based Data (PLOD)

## 目次
- [概要](#概要)
- [提案データセット](#提案データセット)
- [COVID-19感染リスク推論オントロジー（CIRO）](#covid-19感染リスク推論オントロジーciro)
- [オントロジーに基づく個々のデータ（PLOD）](./rdf/example/)
- [PLODの使用例](./sparql/)
- [3つの密の推論実験の結果](#3つの密の推論実験の結果)
- [LODチャレンジ2022向けの説明](#lodチャレンジ2022向けの説明)

## 概要
- COVID-19の感染拡大防止に向けて，日本国政府では「[3つの密](https://www.kantei.go.jp/jp/content/000061868.pdf)」（以下，三密）や，「[5つの場面](https://corona.go.jp/prevention/pdf/infection-20201117.pdf)」を提言しています．
- これらの提言に基づき，各人の感染リスクを自動で評価できれば，追跡調査対象者の順序付けやスクリーニングといった保健所で行われている業務を大幅に効率化できると考えています．
- そこで，場所や行動に紐づくCOVID-19感染リスクを整理し，個別の行動事例における感染リスクを推論可能なオントロジー(CIRO)を開発しました．
- 本リポジトリでは，このオントロジーに基づいてナレッジグラフ化(RDF化)された疑似データ（PLOD）を，オープンデータとして提供します．
- このようなデータを使用することで，追跡調査に有用な三密リスクの推論とグラフ検索が可能なことを示しています．

## 提案データセット
- [COVID-19感染リスク推論オントロジー（CIRO）](./rdf/CIRO.owl)
- [オントロジーに基づく個々のデータ（PLOD）](./rdf/example/ciro_sample.rdf)
- [三密推論実験のスクリプトと結果](https://zenodo.org/record/6482275#.YmY-QfNBzS4)

## COVID-19感染リスク推論オントロジー（CIRO）

### オントロジーの仕様書
全クラス・インスタンス・プロパティの説明は下記の仕様書を御覧ください。  
[https://plod-info.github.io/PLOD/ciro.html](https://plod-info.github.io/PLOD/ciro.html)  
以下で代表的なクラス・プロパティを説明します。

### スキーマ図
黄色が新規に作成したクラス。青色が再利用したクラス。
<img src="./diagram/ontology_revise.png" alt="CIROクラス図">

<details>
<summary>接頭辞</summary>
<table>
    <tr>
        <td>Prefix</td>
        <td>URI</td>
    </tr>
    <tr>
        <td>:</td>
        <td>http://plod.info/rdf/</td>
    </tr>
    <tr>
        <td>time:</td>
        <td>http://www.w3.org/2006/time#</td>
    </tr>
    <tr>
        <td>schema:</td>
        <td>http://schema.org/</td>
    </tr>
    <tr>
        <td>xsd:</td>
        <td>http://www.w3.org/2001/XMLSchema#</td>
    </tr>
</table>
</details>

<details>
<summary>代表的なクラス</summary>
<table>
    <tr>
        <td>Name</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>schema:Event</td>
        <td>イベント</td>
    </tr>
    <tr>
        <td>:Situation</td>
        <td>場所の状況</td>
    </tr>
    <tr>
        <td>:Action</td>
        <td>人の行動</td>
    </tr>
    <tr>
        <td>:RiskAction</td>
        <td>リスク行動</td>
    </tr>
    <tr>
        <td>:IndirectContact</td>
        <td>間接接触行動</td>
    </tr>
    <tr>
        <td>:DropletReachableAction</td>
        <td>飛沫到達行動</td>
    </tr>
    <tr>
        <td>:Context</td>
        <td>コンテキスト。RiskContextをより抽象化したクラス。</td>
    </tr>
    <tr>
        <td>:RiskContext</td>
        <td>イベントや状況に関してリスク行動的な、またはリスク空間的なメタデータを表すクラス</td>
    </tr>
    <tr>
        <td>:SpatialRiskContext</td>
        <td>空間的な感染リスクを表す。</td>
    </tr>
    <tr>
        <td>:BeihavioralRiskContext</td>
        <td>行動的な感染リスクを表す。</td>
    </tr>
    <tr>
        <td>:Crowding</td>
        <td>密集</td>
    </tr>
    <tr>
        <td>:ClosedSpace</td>
        <td>密閉</td>
    </tr>
    <tr>
        <td>:CloseContact</td>
        <td>密接</td>
    </tr>
    <tr>
        <td>:Time</td>
        <td>時間（定性的、定量的なものを含む）</td>
    </tr>
</table>
</details>

<details>
<summary>代表的なプロパティ</summary>
<table>
    <tr>
        <td>QName</td>
        <td>Domains</td>
        <td>Ranges</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>schema:location</td>
        <td>schema:Event</td>
        <td>schema:Place</td>
        <td>イベントの場所を表す．</td>
    </tr>
    <tr>
        <td>:action</td>
        <td>schema:Event</td>
        <td>:Action</td>
        <td>イベントにおける人の行動を表す．</td>
    </tr>
    <tr>
        <td>:agent</td>
        <td>schema:Event</td>
        <td>schema:Person</td>
        <td>イベントの主体．</td>
    </tr>
    <tr>
        <td>:time</td>
        <td>schema:Event or schema:Situation</td>
        <td>:Time</td>
        <td>イベントや状況の時間を表す．</td>
    </tr>
    <tr>
        <td>:followingEvent</td>
        <td>schema:Event</td>
        <td>schema:Event</td>
        <td>次のイベントを表す．時系列的に直後のイベントを意味する．</td>
    </tr>
    <tr>
        <td>:context</td>
        <td>schema:Event</td>
        <td>:Context</td>
        <td>イベントや状況に背景的・文脈的なセマンティクスを付与する．CIROにおいては主に空間的または行動的なリスク要因を表すのに使用される．</td>
    </tr>
    <tr>
        <td>:afford</td>
        <td>schema:Place</td>
        <td>:Action</td>
        <td>場所が誘引する人の行動を表す．</td>
    </tr>
    <tr>
        <td>:isSituationOf</td>
        <td>:Situation</td>
        <td>schema:Place</td>
        <td>どの場所の状況であるか表す．</td>
    </tr>
</table>
</details>

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
3つの密を更に3段階（高リスク、中リスク、低リスク(リスク無し)）に分けて，与えられた行動イベントや空間的な状況がどのリスクに該当するか，OWL 2 DL推論により判定する実験を行いました.

OWL 2 DL推論が可能な[HermiT](http://www.hermit-reasoner.com/)を内包する[Owlready2](https://owlready2.readthedocs.io/en/v0.37/)を使用した実験用スクリプトを公開しています．各リスクパターンの疑似データ（PLOD）を自動的に作成し,CIROを用いて正しく推論できるか評価を行います.

実験の結果，CIROはこれらのリスクを正しく推論できることを確認しました.

実験スクリプトおよび結果：  
<a href="https://doi.org/10.5281/zenodo.6482275"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.6482275.svg" alt="DOI"></a>

## LODチャレンジ2022向けの説明
- Impact - 影響力
  - 提案オントロジー(CIRO)を保健所のシステムに導入し，PLODデータとして蓄積することで，濃厚接触者の追跡調査の順序付けやスクリーニングといった，保健所で行われている業務を大幅に効率化できます．
  - 新型コロナウイルス感染症の患者の実データはプライバシーの問題から一般利用が困難ですが，本データセットは実データに近い模擬データセットであるため，広く感染対策に関する研究開発に利用することができる．
- Creativity - 創造力
  - 人の行動と空間に着目して，「3つの密」や「5つの場面」といったわかりやすい感染リスク指標を用いて推論できる，他に類を見ないオントロジーです．さらに，模擬データセットをオープンデータとして公開している点も新しいです．
- Usefulness - 有用性
  - 場所や時間などの任意の項目をキーとした検索や，三密の程度の推論が可能です．
  - 感染クラスターの特定や，追跡調査の優先度が高い濃厚接触者の特定に利用できます．
- Accessibility - 機械可読性
  - オントロジー（CIRO）、模擬データ（PLOD）ともにRDF形式で提供し，可能な限りエンティティをリテラルではなくURI付きリソースとしており，機械可読性は高いと言えます．
- Openness - 開放性
  - CC BY 4.0ライセンスのオープンデータとして公開しています．
  - RDF化されており，各エンティティに一意なURIが付与されていますが，参照解決は今後の課題としています．
- Linkability - つながる可能
  - 多くのLODで使用されているschema.orgの語彙を再利用しており，間接的に多くのデータセットとつながることができます．特に，人の行動やイベントに関するデータセットとつながる可能性が高いと考えます．
  - [Simple Event Model](https://semanticweb.cs.vu.nl/2009/11/sem/)を参考にしたイベント中心モデルであり，他のデータセットとの連携や拡張性に優れています．
  - 今後の疫学的調査結果を踏まえて三密ルールを調整可能であり，ひいては新型コロナウイルス以外の感染症にも適用できる可能性があります．
- Sustainability − 持続可能性
  - 独自サーバではなくGitHub repositoryで管理しており，持続可能性は高いです．
  - 現在，北海道庁との連携の議論が進んでおり，継続的な開発と社会実装が見込まれます．

## リファレンス
- Shusaku Egami, Yasunori Yamamoto, Ikki Ohmukai, Takashi Okumura: CIRO: COVID-19 Infection Risk Ontology, PLOS ONE, 18(3):e0282291, pp.1-18 (2023) [[Open Access](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282291)]
- 江上周作，山本泰智，大向一輝，奥村貴史: オントロジーを用いたCOVID-19感染リスク行動の推論，第56回人工知能学会セマンティックウェブとオントロジー研究会, SIG-SWO-056-16 (2022) [[Open Access]](https://doi.org/10.11517/jsaisigtwo.2022.SWO-056_16)

## ライセンス
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br /><a xmlns:cc="http://creativecommons.org/ns#" href="https://profile.idease.info/" property="cc:attributionName" rel="cc:attributionURL">江上周作</a>，山本泰智，大向一輝，奥村貴史 作『<span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">Patient Locational Ontology-based Data (PLOD)</span>』は<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">クリエイティブ・コモンズ 表示 4.0 国際 ライセンス</a>で提供されています。

## 謝辞
本研究は，AMEDの課題番号JP20he0622042の支援を受けた．また，神崎正英氏，坂根昌一氏，伊藤真和吏氏，野本昌子氏には，本研究を進める上で様々なご助力を頂いた．ここに深く感謝の意を表する．

# stemming-service
Microservice for turning documents into lists of words. Currently supports Chinese, English, and Spanish.

## Use instructions
1. Install the requirements with `pip install -r requirements.txt`
2. Set an environmental variable to tell flask what to run with `export FLASK_APP=StemmingService.py`
3. Start flask with `flask run`

There is only one api call supported right now, a POST to `<server_address>/v1/<language>/document`. Include the text you want stemmed in a `text` field in your json body.
Eg:
```
POST to http://localhost:5000/v1/chinese/document
{
	"text": "春节将近，由于三聚氰胺事件，牛奶厂没钱支付工钱，为回家过年，个性憨厚的工人牛耿（王宝强饰）向厂长逼要薪水，但厂长只给工人几张欠据让他们自己去讨，于是牛耿踏上了前往长沙的路。李成功（徐峥饰）是一玩具集团老板，为人非常高傲跋扈，这次新春打算回长沙过年，而且情人还要求他回家与老婆离婚。后来牛耿和李成功两人在石家庄机场相遇并开始了一段互相勉励，改变心路的旅程，他们乘坐了各种交通工具奔波在回家的路上，包括飞机、火车、大巴（两次）、轮渡、面包车和拖拉机，遇到了不少囧事。但是两人还是在荒郊野外度过了大年三十，回首这一路的艰辛，与他们路途中遇到人或事，对两人人生有了很大触动。最终，两人从敌对到成为朋友，牛耿的真诚也改变李成功冷漠的性格，唤起李成功对真情的回归。"
}
```
Response:
```
{"status":"OK","message":"","words":["一段","度过","触动","高傲","机场","交通工具","性格","两人","勉励","很大","还","轮渡","工人","包括","冷漠","厂","跋扈","成功","打算","欠据","囧","真情","但","石家庄","或","这次","三聚氰胺","大巴","只","这","最终","与","改变","新春","有","真诚","奔波","的","遇到","玩具","给","对","是","去","火车","讨","中","相遇","飞机","荒郊野外","钱","一路","由于","回","老板","集团","离婚","逼要","人","春节","让","在","面包车","将近","从","并","和","踏上","还是","了","自己","没","李","于是","各种","到","乘坐","过年","也","开始","路上","厂长","旅程","大年三十","朋友","事件","路途","牛耿","向","工钱","牛奶","为","拖拉机","憨厚","两次","薪水","强饰","支付","长沙","前往","徐峥饰","但是","回家","互相","情人","敌对","回首","个性","要求","唤起","事","路","老婆","非常","心路","后来","回归","人生","不少","艰辛","他们","几张","王宝","成为","一","他","而且"]}
```

Built on Flask, jieba, and Spacy.

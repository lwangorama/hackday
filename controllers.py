import tornado.web
from elasticsearch import Elasticsearch


class MainHandler(tornado.web.RequestHandler):

    es = Elasticsearch()

    def get(self):
        query = self.get_argument("q", "")
        current_page = int(self.get_argument("p", 0))

        res = self.search(query, current_page)

        items = None
        total = 0
        if res is not None:
            total = res["hits"]["total"]
            items = []
            for hit in res["hits"]["hits"]:
                items.append(hit["_source"])

        self.render("main.html", query=query, current_page=current_page, total=total, items=items)

    def search(self, query, current_page):
        if not query:
            return None
        bd = {"query": {"match": {"_all": query}}}
        # bd = {"query": {"match_all": {}}}
        start_from = max(0, current_page - 1) * 10
        res = self.es.search(index="product", body=bd, params={"from": start_from})
        return res
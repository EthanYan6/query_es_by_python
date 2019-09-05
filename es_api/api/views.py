from django.shortcuts import render
from es_api.settings import ES_HOST
from elasticsearch import Elasticsearch
from django.http import JsonResponse

# Create your views here.
client = Elasticsearch(hosts=ES_HOST, http_auth=("admin","admin"))

def matchall(request, index):
    query_json = {
        "query": {"match_all": {}}
    }
    query1 = client.search(index=str(index), body=query_json)
    total = query1['hits']['total']  # es查询出的结果总量
    # 小数据量查询
    if int(total) < 10000:
        query = client.search(index=str(index), body=query_json, size=int(total))
        results = query['hits']['hits']
        source = []
        for res in results:
            source.append(res['_source'])
        return JsonResponse(source, safe=False, json_dumps_params={'ensure_ascii': False})
    # 大数据量查询
    else:
        query = client.search(index=str(index), body=query_json, scroll='5m', size=100)
        results = query['hits']['hits']  # es查询出的结果第一页
        total = query['hits']['total']  # es查询出的结果总量
        scroll_id = query['_scroll_id']  # 游标用于输出es查询出的所有结果
        source = []
        for i in range(0, int(total / 100) + 1):
            # scroll参数必须指定否则会报错
            query_scroll = client.scroll(scroll_id=scroll_id, scroll='5m')['hits']['hits']
            results += query_scroll
        for res in results:
            source.append(res['_source'])
        return JsonResponse(source, safe=False, json_dumps_params={'ensure_ascii':False})